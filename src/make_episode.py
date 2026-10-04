"""Build one episode: script -> voices -> subtitles -> talking video + thumbnail.

Usage:
  python src/make_episode.py 1              # real voices (needs internet, for GitHub Actions)
  python src/make_episode.py 1 --fake-tts   # placeholder tones, for testing the visuals
  python src/make_episode.py 1 --lines 12   # only the first 12 lines (quick test)
  python src/make_episode.py 1 --audio-only # voices + subtitle files only, no video (for adding captions later)

Speaking speed: new episodes use RATE / GAP below. An episode can keep its own settings with
"voice_rate" and "turn_gap" in episodes.json (episodes 1-13 were made at -4% with 0.35 s gaps, 14-15 at 0.25 s gaps,
so their caption timings stay in sync).
Japanese captions: if episodes/epNN.ja.txt exists (one line per script line, "SENA: ..."), an
epNN.ja.srt is written next to the video and uploaded as YouTube captions.
"""
import argparse
import asyncio
import json
import os
import re
import shutil
import subprocess
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render import draw_frame, draw_scene_frame, draw_thumbnail  # noqa: E402
import scenes  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SR = 24000
FPS = 12
RATE = "+0%"      # speaking rate for new episodes (natural native speed)
GAP = 0.12        # silence between turns (s) for new episodes: native conversation pace
LEAD, TAIL = 0.8, 1.6

VOICES = {  # change here to swap voices
    "SENA": os.environ.get("SENA_VOICE") or "en-US-AvaNeural",
    "DANIEL": os.environ.get("DANIEL_VOICE") or "en-US-AndrewNeural",
}
FALLBACK = {"SENA": "en-US-JennyNeural", "DANIEL": "en-US-GuyNeural"}


def load_episode(num):
    meta = json.load(open(os.path.join(ROOT, "episodes", "episodes.json"), encoding="utf-8"))
    ep = next(e for e in meta["episodes"] if e["number"] == num)
    lines = []
    for raw in open(os.path.join(ROOT, "episodes", ep["script"]), encoding="utf-8"):
        m = re.match(r"^\s*(SENA|DANIEL)\s*:\s*(.+?)\s*$", raw)
        if m:
            lines.append((m.group(1), m.group(2)))
    return meta, ep, lines


def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def decode(path):
    out = subprocess.run(["ffmpeg", "-v", "quiet", "-i", path, "-f", "s16le", "-ac", "1", "-ar", str(SR), "-"],
                         check=True, capture_output=True).stdout
    return np.frombuffer(out, dtype=np.int16).astype(np.float32) / 32768.0


# ---------- voices ----------

async def tts_line(text, voice, path, rate=RATE):
    import edge_tts
    words = []
    try:
        comm = edge_tts.Communicate(text, voice, rate=rate, boundary="WordBoundary")
    except TypeError:  # older edge-tts without the boundary option
        comm = edge_tts.Communicate(text, voice, rate=rate)
    with open(path, "wb") as f:
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                words.append((chunk["offset"] / 1e7, (chunk["offset"] + chunk["duration"]) / 1e7, chunk["text"]))
    return words


def synth(speaker, text, path, rate=RATE):
    """Always the character's own voice: retry patiently instead of switching to another voice mid-video.

    The fallback voice is used only if NO_VOICE_FALLBACK is not set and the main voice failed 8 times."""
    import time
    voices = [VOICES[speaker]] + ([] if os.environ.get("NO_VOICE_FALLBACK") else [FALLBACK[speaker]])
    for vi, voice in enumerate(voices):
        for attempt in range(8 if vi == 0 else 3):
            try:
                words = asyncio.run(tts_line(text, voice, path, rate))
                if os.path.getsize(path) > 1000:
                    if vi:
                        print(f"  WARNING: {speaker} used the fallback voice {voice} for: {text[:50]}", flush=True)
                    return words
            except Exception as e:  # network hiccups: wait and retry
                print(f"  tts retry ({voice}): {e}", flush=True)
            time.sleep(min(30, 2 ** attempt))
    raise RuntimeError(f"Text-to-speech failed for: {text[:60]}")


def fake_audio(text, speaker):
    """Speech-like placeholder: syllable-rate amplitude bursts."""
    dur = max(0.8, len(text.split()) / 2.6)
    t = np.arange(int(dur * SR)) / SR
    f0 = 210 if speaker == "SENA" else 120
    env = (np.sin(2 * np.pi * 4.2 * t) > -0.2).astype(np.float32)
    env *= (np.sin(2 * np.pi * 0.7 * t + 1) > -0.85)
    return 0.25 * np.sin(2 * np.pi * f0 * t) * env


# ---------- subtitles ----------

def chunk_text(text, max_words=9, max_chars=58):
    tokens = text.split()
    chunks, cur = [], []
    for i, tok in enumerate(tokens):
        cur.append(tok)
        joined = " ".join(cur)
        end_punct = re.search(r"[.?!:;]\"?$", tok)
        soft = re.search(r",\"?$", tok) and len(cur) >= 5
        if end_punct or soft or len(cur) >= max_words or len(joined) >= max_chars:
            chunks.append(cur)
            cur = []
    if cur:
        if chunks and len(cur) <= 2 and len(" ".join(chunks[-1] + cur)) <= max_chars + 10:
            chunks[-1] += cur
        else:
            chunks.append(cur)
    return [" ".join(c) for c in chunks]


def time_chunks(chunks, words, dur):
    """Return [(start, end, text)] relative to the line start."""
    n_tok = [len(c.split()) for c in chunks]
    if words and len(words) >= sum(n_tok) * 0.8:
        out, wi = [], 0
        for c, n in zip(chunks, n_tok):
            s = words[min(wi, len(words) - 1)][0]
            wi = min(wi + n, len(words))
            e = words[wi - 1][1]
            out.append([s, e, c])
        # stretch to cover gaps
        for i in range(len(out) - 1):
            out[i][1] = out[i + 1][0]
        out[0][0], out[-1][1] = 0.0, dur
        return [tuple(x) for x in out]
    total = sum(len(c) for c in chunks)
    out, t = [], 0.0
    for c in chunks:
        d = dur * len(c) / total
        out.append((t, t + d, c))
        t += d
    return out


def load_japanese(ep, n_lines):
    """Japanese translation lines (one per script line), or None."""
    path = os.path.join(ROOT, "episodes", ep["script"].replace(".txt", ".ja.txt"))
    if not os.path.exists(path):
        return None
    ja = []
    for raw in open(path, encoding="utf-8"):
        m = re.match(r"^\s*(SENA|DANIEL)\s*:\s*(.+?)\s*$", raw)
        if m:
            ja.append(m.group(2))
    if len(ja) < n_lines:
        print(f"  WARNING: {os.path.basename(path)} has {len(ja)} lines, script has {n_lines}; "
              "Japanese captions skipped", flush=True)
        return None
    return ja[:n_lines]


def split_japanese(text, max_chars=34):
    """Split a Japanese line into caption-sized pieces at sentence ends, then commas."""
    parts = [p for p in re.split(r"(?<=[。！？!?])", text) if p.strip()]
    out = []
    for p in parts:
        while len(p) > max_chars:
            cut = max((p.rfind(c, 0, max_chars) for c in "、，,"), default=-1)
            cut = cut + 1 if cut >= 8 else max_chars
            out.append(p[:cut])
            p = p[cut:]
        if p.strip():
            out.append(p)
    return [p.strip() for p in out] or [text]


def write_japanese_srt(path, segments, ja):
    k = 0
    with open(path, "w", encoding="utf-8") as f:
        for (s0, s1, spk), text in zip(segments, ja):
            pieces = split_japanese(text)
            total = sum(len(p) for p in pieces)
            t = s0
            for p in pieces:
                d = (s1 - s0) * len(p) / total
                k += 1
                name = "セナ" if spk == "SENA" else "ダニエル"
                f.write(f"{k}\n{srt_time(t)} --> {srt_time(t + d)}\n{name}: {p}\n\n")
                t += d


def srt_time(s):
    h, m = int(s // 3600), int(s % 3600 // 60)
    return f"{h:02d}:{m:02d}:{int(s % 60):02d},{int(round((s % 1) * 1000)) % 1000:03d}"


# ---------- main ----------

def build(num, fake=False, limit=None, out_dir=None, audio_only=False):
    meta, ep, lines = load_episode(num)
    if limit:
        lines = lines[:limit]
    rate = ep.get("voice_rate", RATE)
    gap = float(ep.get("turn_gap", GAP))
    out_dir = out_dir or os.path.join(ROOT, "output", f"ep{num:02d}")
    work = os.path.join(out_dir, "work")
    shutil.rmtree(work, ignore_errors=True)
    os.makedirs(work, exist_ok=True)

    print(f"EP {num:02d}: {len(lines)} lines", flush=True)
    visual = scenes.has_visuals(num)
    states, repeats = scenes.line_states(num, lines, ep) if visual else ([], set())
    audio = [np.zeros(int(LEAD * SR), np.float32)]
    t = LEAD
    segments, subs = [], []  # segments: (start, end, speaker)
    pauses = []  # (start, end, line index): silent "your turn" practice time after a Speaking Lab repeat
    for i, (spk, text) in enumerate(lines):
        if fake:
            a, words = fake_audio(text, spk), []
        else:
            mp3 = os.path.join(work, f"line{i:03d}.mp3")
            words = synth(spk, text, mp3, rate)
            a = decode(mp3)
        dur = len(a) / SR
        segments.append((t, t + dur, spk))
        for s, e, c in time_chunks(chunk_text(text), words, dur):
            subs.append((t + s, t + e, spk, c))
        audio += [a, np.zeros(int(gap * SR), np.float32)]
        t += dur + gap
        if i in repeats:
            pause = max(2.5, dur + 1.0)
            audio.append(np.zeros(int(pause * SR), np.float32))
            pauses.append((t, t + pause, i))
            t += pause
        if (i + 1) % 20 == 0:
            print(f"  voiced {i + 1}/{len(lines)}", flush=True)
    audio.append(np.zeros(int(TAIL * SR), np.float32))
    pcm = np.concatenate(audio)
    total = len(pcm) / SR

    wav = os.path.join(work, "audio.wav")
    import wave
    with wave.open(wav, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((np.clip(pcm, -1, 1) * 32767).astype(np.int16).tobytes())

    # subtitles file (also handy to upload as captions later)
    srt = os.path.join(out_dir, f"ep{num:02d}.srt")
    with open(srt, "w", encoding="utf-8") as f:
        for k, (s, e, spk, c) in enumerate(subs, 1):
            f.write(f"{k}\n{srt_time(s)} --> {srt_time(e)}\n{spk.title()}: {c}\n\n")

    chapters = None
    if visual:
        chapters = os.path.join(out_dir, f"ep{num:02d}.chapters.txt")
        marks = []
        for (s0, _, _), st in zip(segments, states):
            name = st.get("section") or ""
            if name and (not marks or marks[-1][1] != name):
                marks.append([s0, name])
        if marks:
            marks[0][0] = 0.0
        kept = []
        for k, (s0, name) in enumerate(marks):
            nxt = marks[k + 1][0] if k + 1 < len(marks) else total
            if kept and nxt - s0 < 10:
                continue
            kept.append((s0, name))
        with open(chapters, "w", encoding="utf-8") as f:
            for s0, name in kept:
                f.write(f"{int(s0 // 60)}:{int(s0 % 60):02d} {name}\n")
        if len(kept) < 3:
            os.remove(chapters)
            chapters = None

    ja = load_japanese(ep, len(lines))
    ja_srt = None
    if ja:
        ja_srt = os.path.join(out_dir, f"ep{num:02d}.ja.srt")
        write_japanese_srt(ja_srt, segments, ja)
        print(f"  Japanese captions: {ja_srt}", flush=True)
    if audio_only:
        shutil.rmtree(work, ignore_errors=True)
        print(f"  {total / 60:.1f} min (audio only)", flush=True)
        return {"srt": srt, "ja_srt": ja_srt, "chapters": chapters, "duration": total}

    # timeline -> unique frames
    n_frames = int(np.ceil(total * FPS))
    hop = SR // FPS
    rms = np.array([np.sqrt(np.mean(pcm[i * hop:(i + 1) * hop] ** 2) + 1e-12) for i in range(n_frames)])
    seg_i = sub_i = 0
    last_speaker = lines[0][0]
    keys = []
    for fi in range(n_frames):
        tt = fi / FPS
        while seg_i < len(segments) - 1 and tt >= segments[seg_i][1] + gap / 2:
            seg_i += 1
        s0, s1, spk = segments[seg_i]
        talking = s0 <= tt < s1
        if talking:
            last_speaker = spk
        while sub_i < len(subs) - 1 and tt >= subs[sub_i][1]:
            sub_i += 1
        st = subs[sub_i]
        subtitle = st[3] if st[0] <= tt < st[1] else ""
        level = 0
        if talking:
            r = rms[fi]
            level = 3 if r > 0.12 else 2 if r > 0.05 else 1 if r > 0.015 else 0
        if visual:
            st, count = states[seg_i], None
            for p0, p1, li in pauses:
                if p0 - gap <= tt < p1:
                    st = states[li]
                    if tt >= p0:
                        count = max(1, int(np.ceil(p1 - tt)))
                        subtitle = ""
                    break
            board = dict(st["board"])
            if count is not None:
                board["countdown"] = count
            keys.append((last_speaker, level, subtitle, st["sena"], st["daniel"], st["section"],
                         json.dumps(board, sort_keys=True)))
        else:
            keys.append((last_speaker, level, subtitle))

    frames_dir = os.path.join(work, "frames")
    os.makedirs(frames_dir)
    cache, listing = {}, []
    title = ep["title"]
    run_key, run_len = keys[0], 0
    for k in keys + [None]:
        if k == run_key:
            run_len += 1
            continue
        if run_key not in cache:
            p = os.path.join(frames_dir, f"f{len(cache):05d}.png")
            if visual:
                draw_scene_frame(num, title, *run_key).save(p, compress_level=1)
            else:
                spk, level, sub = run_key
                draw_frame(num, title, spk, level, sub).save(p, compress_level=1)
            cache[run_key] = p
        listing.append((cache[run_key], run_len / FPS))
        run_key, run_len = k, 1
    print(f"  {len(cache)} unique frames, {len(listing)} cuts, {total / 60:.1f} min", flush=True)

    lst = os.path.join(work, "frames.txt")
    with open(lst, "w") as f:
        for p, d in listing:
            f.write(f"file '{p}'\nduration {d:.4f}\n")
        f.write(f"file '{listing[-1][0]}'\n")

    mp4 = os.path.join(out_dir, f"ep{num:02d}.mp4")
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-i", wav,
         "-vf", f"fps={FPS * 2},format=yuv420p", "-c:v", "libx264", "-preset", "medium", "-tune", "stillimage",
         "-crf", "21", "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-shortest", "-movflags", "+faststart", mp4])

    thumb = draw_thumbnail(num, ep, os.path.join(out_dir, f"ep{num:02d}_thumbnail.jpg"))
    shutil.rmtree(work, ignore_errors=True)
    print(f"  done: {mp4}", flush=True)
    return {"video": mp4, "thumbnail": thumb, "srt": srt, "ja_srt": ja_srt, "chapters": chapters, "duration": total}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("episode", type=int)
    ap.add_argument("--fake-tts", action="store_true")
    ap.add_argument("--lines", type=int)
    ap.add_argument("--out")
    ap.add_argument("--audio-only", action="store_true")
    a = ap.parse_args()
    print(json.dumps(build(a.episode, a.fake_tts, a.lines, a.out, a.audio_only), indent=2))
