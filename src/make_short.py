"""Build a vertical YouTube Short (1080x1920, under a minute) from a few lines of an episode.

Usage:
  python src/make_short.py 14              # real voices (GitHub Actions)
  python src/make_short.py 14 --fake-tts   # placeholder tones, for checking the visuals
  python src/make_short.py 14 --frame 3    # only save one still frame (line 3 of the clip) as a PNG

What goes into the Short comes from episodes/epNN.short.json (epNNN for 100+):

{
  "lines": [44, 47],                       # 1-based line range in the episode script (inclusive)
  "hook": "AI apologizes all the time. So why can't it do this?",   # big text at the top, from the first frame
  "title": "Why saying sorry works for you, not for AI",            # YouTube title (optional, default: the hook)
  "tag": "WHY CAN'T AI DO THIS?",          # small label above the hook (optional)
  "board": {"type": "keyword", "text": "...", "icon": "Robot"}      # center card (optional)
}

Without that file, the Short is cut automatically from the episode's "Why can't AI do this?" part
(every episode has one), so new episodes get a Short with no extra work.
The center card follows the episode's visual cues when it has them, otherwise it shows "board" or the cover.
Clips are kept under MAX_SECONDS: lines at the end are dropped if the voices run long.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys

import numpy as np
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_episode as me  # noqa: E402
import render as r  # noqa: E402
import scenes  # noqa: E402

ROOT = me.ROOT
W, H = 1080, 1920
FPS = 12
RATE = "+0%"          # natural native speed
GAP = 0.22
LEAD, TAIL = 0.35, 1.4
MAX_SECONDS = 58.0
TARGET_WORDS = 140    # rough size of an automatic clip before voicing

HOOK_TOP, HOOK_SPACE = 280, 330     # hook text block (centered vertically in this space)
BOARD_BOX = (100, 640, 980, 1250)   # center card area
BAR = (40, 1268, 1040, 1508)        # caption bar
BUST_FLOOR = 2010                    # busts stand behind the bar; their lower half runs off the bottom
BUST_X = {"SENA": 300, "DANIEL": 780}
NEXT_PART = re.compile(r"\bstor(y|ies)\b|failure|confession|mistake of mine|hold that thought", re.I)
AI_QUESTION = re.compile(r"why can.?t ai|why is this (a skill|something) ai can.?t|ai can.?t do (this|that) for", re.I)


def short_path(num):
    name = f"ep{num:02d}.short.json" if num < 100 else f"ep{num:03d}.short.json"
    return os.path.join(ROOT, "episodes", name)


def auto_range(lines):
    """The 'Why can't AI do this?' part: from the question, about TARGET_WORDS words."""
    start = next((i for i, (_, t) in enumerate(lines) if i > 5 and AI_QUESTION.search(t)), None)
    if start is None:  # no AI question: take the middle of the episode
        start = len(lines) // 2
    words, end = 0, start
    while end < len(lines) and (words < TARGET_WORDS or end - start < 3):
        if end - start >= 2 and NEXT_PART.search(lines[end][1]):  # Daniel's story etc. starts: stop here
            break
        words += len(lines[end][1].split())
        end += 1
        if words > TARGET_WORDS * 1.25:
            break
    return start, end  # python slice


def load_spec(num, ep, lines):
    spec = {}
    p = short_path(num)
    if os.path.exists(p):
        spec = json.load(open(p, encoding="utf-8"))
    if spec.get("lines"):
        a, b = spec["lines"]
        start, end = a - 1, b
    else:
        start, end = auto_range(lines)
    spec.setdefault("hook", f"Why can't AI do this? {ep['short_title']}")
    spec.setdefault("title", spec["hook"])
    spec.setdefault("tag", "LEARN WHAT AI CAN'T DO")
    spec["start"], spec["end"] = start, end
    return spec


def default_poses(spk_active):
    return {"SENA": "default" if spk_active == "SENA" else "listen",
            "DANIEL": "explain" if spk_active == "DANIEL" else "listen"}


def clip_states(num, ep, lines, spec):
    """Poses and center card for each line of the clip."""
    start, end = spec["start"], spec["end"]
    visual = scenes.has_visuals(num)
    states = scenes.line_states(num, lines, ep)[0] if visual else None
    out = []
    for i in range(start, end):
        spk = lines[i][0]
        if states:
            st = dict(states[i])
            board = st["board"]
            if spec.get("board"):
                board = spec["board"]
            elif board.get("type") in ("none", "repeat", "question", "challenge") or not board:
                board = {"type": "cover"}
            poses = {"SENA": st["sena"], "DANIEL": st["daniel"]}
        else:
            board = spec.get("board") or {"type": "cover"}
            poses = default_poses(spk)
        out.append({"sena": poses["SENA"], "daniel": poses["DANIEL"], "board": board})
    return out


# ---------- drawing ----------

def base(spec, ep_title):
    img = r.paper(W, H, seed=17).convert("RGBA")
    for box, color, seed, a in (((520, -50, 640, 260), r.BLUE, 1, 110), ((-60, 120, 520, 120), r.CORAL, 2, 120),
                                ((-80, 1700, 700, 260), r.BLUE, 3, 70), ((620, 1800, 520, 120), r.CORAL, 4, 100)):
        s = r.brush(box[2:], color, seed, alpha=a)
        img.alpha_composite(s, (box[0], box[1]))
    d = ImageDraw.Draw(img)
    r.spaced(d, (W / 2, 92), "THE", r.sans(20, "SemiBold"), r.NAVY, spacing=6, anchor_center=True)
    d.text((W / 2, 116), "Human Curriculum", font=r.serif(52, "Bold"), fill=r.NAVY, anchor="ma")
    # tag
    tf = r.sans(24, "SemiBold")
    tag = spec["tag"].upper()
    tw = r.spaced_width(tag, tf, 4)
    x0 = (W - tw - 40) / 2
    d.rounded_rectangle((x0, 196, x0 + tw + 40, 242), radius=8, fill=r.CORAL)
    r.spaced(d, (x0 + 20, 205), tag, tf, (255, 255, 255), spacing=4)
    # hook
    f, lines, size = r._fit_font(d, spec["hook"], lambda s: r.serif(s, "Bold"), W - 140, 3, 84, 52)
    block = int(size * 1.14) * len(lines)
    y = HOOK_TOP + max(0, (HOOK_SPACE - block) // 2)
    for k, line in enumerate(lines):
        if k == len(lines) - 1:
            lw = int(d.textlength(line, font=f)) + 40
            hl = r.brush((lw, int(size * 0.5)), r.CORAL, seed=41, alpha=140, roughness=0.15)
            img.alpha_composite(hl, (int((W - lw) / 2), int(y + size * 0.62)))
            d = ImageDraw.Draw(img)
        d.text((W / 2, y), line, font=f, fill=r.NAVY, anchor="ma")
        y += int(size * 1.14)
    return img


def board_card(num, board):
    key = json.dumps(board, sort_keys=True)
    card = r.board_image(num, key)
    if card is None:
        return None
    bw, bh = BOARD_BOX[2] - BOARD_BOX[0], BOARD_BOX[3] - BOARD_BOX[1]
    s = min(bw / card.width, bh / card.height)
    return card.resize((int(card.width * s), int(card.height * s)), Image.LANCZOS)


def bust(name, pose, active):
    img = r.full_pose(name, pose) if active else r.faded(name, pose)
    return img.resize((int(img.width * 1.08), int(img.height * 1.08)), Image.LANCZOS)


def draw(num, spec, ep_title, speaker, level, subtitle, sena, daniel, board_key, base_cache={}):
    k = (num, spec["hook"])
    if k not in base_cache:
        base_cache.clear()
        base_cache[k] = base(spec, ep_title)
    img = base_cache[k].copy()
    card = board_card(num, json.loads(board_key))
    if card is not None:
        cx, cy = (BOARD_BOX[0] + BOARD_BOX[2]) // 2, (BOARD_BOX[1] + BOARD_BOX[3]) // 2
        img.alpha_composite(card, (cx - card.width // 2, cy - card.height // 2))
    for name, pose in (("SENA", sena), ("DANIEL", daniel)):
        active = name == speaker
        fig = bust(name, pose, active)
        bob = -6 if (active and level >= 2) else 0
        img.alpha_composite(fig, (BUST_X[name] - fig.width // 2, BUST_FLOOR - fig.height + bob))
    # caption bar on top of the busts
    bx0, by0, bx1, by1 = BAR
    bar = r.paper(bx1 - bx0, by1 - by0, seed=9).convert("RGBA")
    ImageDraw.Draw(bar).rectangle((0, 0, bx1 - bx0 - 1, by1 - by0 - 1), outline=(214, 204, 186), width=2)
    sh = Image.new("RGBA", (bx1 - bx0 + 40, by1 - by0 + 40), (0, 0, 0, 0))
    sh.paste((60, 50, 40, 70), (20, 14, bx1 - bx0 + 20, by1 - by0 + 20))
    from PIL import ImageFilter
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(10)), (bx0 - 20, by0 - 20))
    img.alpha_composite(bar, (bx0, by0))
    d = ImageDraw.Draw(img)
    p = r.PEOPLE[speaker]
    d.rounded_rectangle((bx0 + 36, by0 - 26, bx0 + 216, by0 + 22), radius=8, fill=p["accent"])
    d.text((bx0 + 126, by0 - 2), p["first"], font=r.serif(32, "SemiBold", italic=True), fill=(255, 255, 255), anchor="mm")
    if subtitle:
        f, lines, size = r._fit_font(d, subtitle, lambda s: r.sans(s, "Bold"), bx1 - bx0 - 70, 3, 58, 40)
        cy = (by0 + by1) / 2 + 6
        step = int(size * 1.22)
        for i, line in enumerate(lines):
            d.text((W / 2, cy + (i - (len(lines) - 1) / 2) * step), line, font=f, fill=r.NAVY, anchor="mm")
    return img.convert("RGB")


def end_card(num, spec, ep):
    """Last moment: point to the full episode."""
    img = base(spec, ep["title"]).copy()
    d = ImageDraw.Draw(img)
    card = board_card(num, {"type": "cover"})
    if card is not None:
        img.alpha_composite(card, (W // 2 - card.width // 2, 700))
        d = ImageDraw.Draw(img)
    y = 700 + (card.height if card is not None else 300) + 40
    d.text((W / 2, y), "Full episode on the channel", font=r.hand(64), fill=r.CORAL, anchor="ma")
    f, lines, size = r._fit_font(d, ep["title"], lambda s: r.serif(s, "SemiBold"), W - 160, 2, 54, 36)
    y += 96
    for line in lines:
        d.text((W / 2, y), line, font=f, fill=r.NAVY, anchor="ma")
        y += int(size * 1.2)
    return img.convert("RGB")


# ---------- build ----------

def build(num, fake=False, out_dir=None, frame=None):
    meta, ep, lines = me.load_episode(num)
    spec = load_spec(num, ep, lines)
    states = clip_states(num, ep, lines, spec)
    clip = lines[spec["start"]:spec["end"]]
    icons = set()
    for st in states:
        b = st["board"]
        for key in ("icon", "icons"):
            v = b.get(key)
            icons |= {v} if isinstance(v, str) else set(v or [])
    if icons:
        try:
            import fetch_icons
            fetch_icons.fetch(icons)
        except Exception as e:  # illustrations are a nice-to-have
            print(f"  illustrations skipped: {e}", flush=True)
    out_dir = out_dir or os.path.join(ROOT, "output", f"ep{num:02d}")
    os.makedirs(out_dir, exist_ok=True)
    print(f"EP {num:02d} short: lines {spec['start'] + 1}-{spec['end']} | {spec['hook']}", flush=True)

    if frame is not None:
        i = max(0, min(frame - 1, len(clip) - 1))
        st = states[i]
        sub = me.chunk_text(clip[i][1])[0]
        path = os.path.join(out_dir, f"ep{num:02d}_short_frame{i + 1}.png")
        draw(num, spec, ep["title"], clip[i][0], 2, sub, st["sena"], st["daniel"],
             json.dumps(st["board"], sort_keys=True)).save(path)
        end_card(num, spec, ep).save(os.path.join(out_dir, f"ep{num:02d}_short_end.png"))
        print(f"  frame: {path}", flush=True)
        return {"frame": path}

    work = os.path.join(out_dir, "short_work")
    shutil.rmtree(work, ignore_errors=True)
    os.makedirs(work)
    voiced = []
    for i, (spk, text) in enumerate(clip):
        if fake:
            a, words = me.fake_audio(text, spk), []
        else:
            mp3 = os.path.join(work, f"line{i:03d}.mp3")
            words = me.synth(spk, text, mp3, RATE)
            a = me.decode(mp3)
        voiced.append((spk, text, a, words))
    # keep it under a minute: drop lines from the end (never end on a question)
    def length(v):
        return LEAD + sum(len(a) / me.SR + GAP for _, _, a, _ in v) + TAIL
    while len(voiced) > 2 and (length(voiced) > MAX_SECONDS or voiced[-1][1].rstrip().endswith("?")):
        voiced.pop()
    if length(voiced) > MAX_SECONDS:
        print(f"  WARNING: clip is {length(voiced):.0f}s, over {MAX_SECONDS:.0f}s; YouTube still takes Shorts up to 3 minutes",
              flush=True)
    states = states[:len(voiced)]

    audio = [np.zeros(int(LEAD * me.SR), np.float32)]
    t = LEAD
    segments, subs = [], []
    for spk, text, a, words in voiced:
        dur = len(a) / me.SR
        segments.append((t, t + dur, spk))
        for s, e, c in me.time_chunks(me.chunk_text(text, max_words=7, max_chars=42), words, dur):
            subs.append((t + s, t + e, spk, c))
        audio += [a, np.zeros(int(GAP * me.SR), np.float32)]
        t += dur + GAP
    speech_end = t
    audio.append(np.zeros(int(TAIL * me.SR), np.float32))
    pcm = np.concatenate(audio)
    total = len(pcm) / me.SR
    wav = os.path.join(work, "audio.wav")
    import wave
    with wave.open(wav, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(me.SR)
        w.writeframes((np.clip(pcm, -1, 1) * 32767).astype(np.int16).tobytes())

    n_frames = int(np.ceil(total * FPS))
    hop = me.SR // FPS
    rms = np.array([np.sqrt(np.mean(pcm[i * hop:(i + 1) * hop] ** 2) + 1e-12) for i in range(n_frames)])
    keys, seg_i, sub_i, last = [], 0, 0, voiced[0][0]
    for fi in range(n_frames):
        tt = fi / FPS
        if tt >= speech_end + 0.2:
            keys.append(("END",))
            continue
        while seg_i < len(segments) - 1 and tt >= segments[seg_i][1] + GAP / 2:
            seg_i += 1
        s0, s1, spk = segments[seg_i]
        talking = s0 <= tt < s1
        if talking:
            last = spk
        while sub_i < len(subs) - 1 and tt >= subs[sub_i][1]:
            sub_i += 1
        st_sub = subs[sub_i]
        subtitle = st_sub[3] if st_sub[0] <= tt < st_sub[1] else ""
        level = 0
        if talking:
            rr = rms[fi]
            level = 3 if rr > 0.12 else 2 if rr > 0.05 else 1 if rr > 0.015 else 0
        st = states[seg_i]
        keys.append((last, level, subtitle, st["sena"], st["daniel"], json.dumps(st["board"], sort_keys=True)))

    frames_dir = os.path.join(work, "frames")
    os.makedirs(frames_dir)
    cache, listing = {}, []
    run_key, run_len = keys[0], 0
    for k in keys + [None]:
        if k == run_key:
            run_len += 1
            continue
        if run_key not in cache:
            p = os.path.join(frames_dir, f"f{len(cache):05d}.png")
            im = end_card(num, spec, ep) if run_key == ("END",) else draw(num, spec, ep["title"], *run_key)
            im.save(p, compress_level=1)
            cache[run_key] = p
        listing.append((cache[run_key], run_len / FPS))
        run_key, run_len = k, 1
    lst = os.path.join(work, "frames.txt")
    with open(lst, "w") as f:
        for p, dd in listing:
            f.write(f"file '{p}'\nduration {dd:.4f}\n")
        f.write(f"file '{listing[-1][0]}'\n")
    mp4 = os.path.join(out_dir, f"ep{num:02d}_short.mp4")
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-i", wav,
                    "-vf", f"fps={FPS * 2},format=yuv420p", "-c:v", "libx264", "-preset", "medium",
                    "-tune", "stillimage", "-crf", "20", "-c:a", "aac", "-b:a", "160k", "-ar", "48000",
                    "-shortest", "-movflags", "+faststart", mp4],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    shutil.rmtree(work, ignore_errors=True)
    info = {"video": mp4, "title": spec["title"], "hook": spec["hook"], "duration": round(total, 1),
            "lines": [spec["start"] + 1, spec["start"] + len(voiced)]}
    json.dump(info, open(os.path.join(out_dir, f"ep{num:02d}_short.json"), "w"), indent=2, ensure_ascii=False)
    print(f"  {len(cache)} unique frames, {total:.1f}s -> {mp4}", flush=True)
    return info


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("episode", type=int)
    ap.add_argument("--fake-tts", action="store_true")
    ap.add_argument("--out")
    ap.add_argument("--frame", type=int)
    a = ap.parse_args()
    print(json.dumps(build(a.episode, a.fake_tts, a.out, a.frame), indent=2, ensure_ascii=False))
