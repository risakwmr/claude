"""Build one episode: script -> voices -> subtitles -> talking video + thumbnail.

Usage:
  python src/make_episode.py 1              # real voices (needs internet, for GitHub Actions)
  python src/make_episode.py 1 --fake-tts   # placeholder tones, for testing the visuals
  python src/make_episode.py 1 --lines 12   # only the first 12 lines (quick test)
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
from render import draw_frame, draw_thumbnail  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SR = 24000
FPS = 12
GAP = 0.35        # silence between turns (s)
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

async def tts_line(text, voice, path):
    import edge_tts
    words = []
    try:
        comm = edge_tts.Communicate(text, voice, rate="-4%", boundary="WordBoundary")
    except TypeError:  # older edge-tts without the boundary option
        comm = edge_tts.Communicate(text, voice, rate="-4%")
    with open(path, "wb") as f:
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                words.append((chunk["offset"] / 1e7, (chunk["offset"] + chunk["duration"]) / 1e7, chunk["text"]))
    return words


def synth(speaker, text, path):
    for voice in (VOICES[speaker], FALLBACK[speaker]):
        for attempt in range(3):
            try:
                words = asyncio.run(tts_line(text, voice, path))
                if os.path.getsize(path) > 1000:
                    return words
            except Exception as e:  # network hiccups: retry, then fall back
                print(f"  tts retry ({voice}): {e}", flush=True)
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


def srt_time(s):
    h, m = int(s // 3600), int(s % 3600 // 60)
    return f"{h:02d}:{m:02d}:{int(s % 60):02d},{int(round((s % 1) * 1000)) % 1000:03d}"


# ---------- main ----------

def build(num, fake=False, limit=None, out_dir=None):
    meta, ep, lines = load_episode(num)
    if limit:
        lines = lines[:limit]
    out_dir = out_dir or os.path.join(ROOT, "output", f"ep{num:02d}")
    work = os.path.join(out_dir, "work")
    shutil.rmtree(work, ignore_errors=True)
    os.makedirs(work, exist_ok=True)

    print(f"EP {num:02d}: {len(lines)} lines", flush=True)
    audio = [np.zeros(int(LEAD * SR), np.float32)]
    t = LEAD
    segments, subs = [], []  # segments: (start, end, speaker)
    for i, (spk, text) in enumerate(lines):
        if fake:
            a, words = fake_audio(text, spk), []
        else:
            mp3 = os.path.join(work, f"line{i:03d}.mp3")
            words = synth(spk, text, mp3)
            a = decode(mp3)
        dur = len(a) / SR
        segments.append((t, t + dur, spk))
        for s, e, c in time_chunks(chunk_text(text), words, dur):
            subs.append((t + s, t + e, spk, c))
        audio += [a, np.zeros(int(GAP * SR), np.float32)]
        t += dur + GAP
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

    # timeline -> unique frames
    n_frames = int(np.ceil(total * FPS))
    hop = SR // FPS
    rms = np.array([np.sqrt(np.mean(pcm[i * hop:(i + 1) * hop] ** 2) + 1e-12) for i in range(n_frames)])
    seg_i = sub_i = 0
    last_speaker = lines[0][0]
    keys = []
    for fi in range(n_frames):
        tt = fi / FPS
        while seg_i < len(segments) - 1 and tt >= segments[seg_i][1] + GAP / 2:
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
    return {"video": mp4, "thumbnail": thumb, "srt": srt, "duration": total}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("episode", type=int)
    ap.add_argument("--fake-tts", action="store_true")
    ap.add_argument("--lines", type=int)
    ap.add_argument("--out")
    a = ap.parse_args()
    print(json.dumps(build(a.episode, a.fake_tts, a.lines, a.out), indent=2))
