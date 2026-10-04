"""Anime version of the Start here trailer: the 8 illustrated cuts timed to the trailer voices.

Inputs
  episodes/trailer/anime/cutN.png   still image for each cut (16:9)
  episodes/trailer/anime/cutN.mp4   optional: an image-to-video clip for that cut (used instead of the still)
  audio: output/trailer/trailer.mp4 (made by src/make_trailer.py) or --audio FILE, with its .srt next to it

Each still gets a slow camera move (push-in or drift) and cuts cross-fade. Clips are trimmed or slowed to fit.
English captions are drawn at the bottom; the last seconds show the show title.

python src/make_anime_trailer.py --audio output/trailer/trailer.mp4 --out output/trailer/trailer_anime.mp4
"""
import argparse
import os
import re
import subprocess
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render as r  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT, "episodes", "trailer", "anime")
W, H, FPS = 1920, 1080, 24
FADE = 0.6
# which script lines (1-based) each cut covers, and its camera move: (zoom from, zoom to, x drift, y drift)
CUTS = [((1, 2), (1.00, 1.10, 0.00, 0.00)),
        ((3, 4), (1.08, 1.02, -0.03, 0.00)),
        ((5, 6), (1.02, 1.10, 0.02, 0.02)),
        ((7, 8), (1.00, 1.08, 0.03, 0.00)),
        ((9, 10), (1.06, 1.00, -0.02, 0.00)),
        ((11, 11), (1.00, 1.12, -0.04, 0.03)),
        ((12, 15), (1.00, 1.06, 0.00, 0.00)),
        ((16, 18), (1.10, 1.00, 0.00, 0.02))]


def srt(path):
    segs = []
    for b in open(path, encoding="utf-8").read().strip().split("\n\n"):
        lines = b.split("\n")
        a, c = lines[1].split(" --> ")
        t = lambda s: int(s[:2]) * 3600 + int(s[3:5]) * 60 + float(s[6:].replace(",", "."))
        spk, _, text = " ".join(lines[2:]).partition(": ")
        segs.append((t(a), t(c), spk, text))
    return segs


def line_starts(segs, script):
    lines = [l.split(": ", 1)[1] for l in open(script, encoding="utf-8") if ": " in l]
    starts, i = [], 0
    for body in lines:
        while i < len(segs) and not body.startswith(segs[i][3][:12]):
            i += 1
        starts.append(segs[min(i, len(segs) - 1)][0])
    return starts


def frames_from_clip(path, n):
    """Decode a clip to n frames (stretched or trimmed to fit)."""
    out = subprocess.run(["ffmpeg", "-v", "quiet", "-i", path, "-vf", f"scale={W}:{H}:force_original_aspect_ratio=increase,"
                          f"crop={W}:{H},fps={FPS}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                         check=True, capture_output=True).stdout
    arr = np.frombuffer(out, np.uint8).reshape(-1, H, W, 3)
    idx = np.linspace(0, len(arr) - 1, n).astype(int)
    return [Image.fromarray(arr[i]) for i in idx]


def camera(img, k, move):
    z0, z1, dx, dy = move
    e = k * k * (3 - 2 * k)  # ease in-out
    z = z0 + (z1 - z0) * e
    cw, ch = img.width / z, img.height / z
    cx = img.width / 2 + dx * img.width * (e - 0.5)
    cy = img.height / 2 + dy * img.height * (e - 0.5)
    cx = min(max(cx, cw / 2), img.width - cw / 2)
    cy = min(max(cy, ch / 2), img.height - ch / 2)
    box = (cx - cw / 2, cy - ch / 2, cx + cw / 2, cy + ch / 2)
    return img.resize((W, H), Image.BICUBIC, box=box)


def caption(img, text):
    if not text:
        return img
    d = ImageDraw.Draw(img, "RGBA")
    f, lines, size = r._fit_font(d, text, lambda s: r.sans(s, "Bold"), W - 400, 2, 50, 36)
    step = int(size * 1.25)
    h = step * len(lines) + 40
    y0 = H - 70 - h
    d.rounded_rectangle((180, y0, W - 180, y0 + h), radius=18, fill=(15, 22, 40, 150))
    for i, line in enumerate(lines):
        d.text((W / 2, y0 + 20 + i * step + step / 2), line, font=f, fill=(255, 255, 255), anchor="mm")
    return img


def title_card(img, alpha):
    over = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(over)
    d.rectangle((0, 0, W, H), fill=(10, 16, 32, int(120 * alpha)))
    a = int(255 * alpha)
    r.spaced(d, (W / 2, 330), "THE", r.sans(40, "SemiBold"), (255, 255, 255, a), spacing=10, anchor_center=True)
    d.text((W / 2, 380), "Human Curriculum", font=r.serif(140, "Bold"), fill=(255, 255, 255, a), anchor="ma")
    d.text((W / 2, 560), "Learn what AI can't do, in natural English", font=r.hand(72), fill=(255, 214, 160, a), anchor="ma")
    d.text((W / 2, 700), "Start with Episode 1", font=r.sans(52, "SemiBold"), fill=(255, 255, 255, a), anchor="ma")
    out = img.convert("RGBA")
    out.alpha_composite(over)
    return out.convert("RGB")


def build(audio, out, captions=True):
    base = os.path.splitext(audio)[0]
    segs = srt(base + ".srt")
    starts = line_starts(segs, os.path.join(ROOT, "episodes", "trailer", "trailer.txt"))
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", audio],
                               capture_output=True, text=True).stdout)
    bounds = []
    for k, ((a, b), _) in enumerate(CUTS):
        s = 0.0 if k == 0 else starts[a - 1] - 0.25
        e = starts[b] - 0.25 if b < len(starts) else dur
        bounds.append((s, e))
    total = int(dur * FPS)
    sources = []
    for k, ((_, _), move) in enumerate(CUTS):
        s, e = bounds[k]
        n = int((e - s + FADE) * FPS) + 2
        clip = os.path.join(DIR, f"cut{k + 1}.mp4")
        if os.path.exists(clip):
            sources.append(("clip", frames_from_clip(clip, n), move))
        else:
            img = Image.open(os.path.join(DIR, f"cut{k + 1}.png")).convert("RGB")
            sc = max(W / img.width, H / img.height) * 1.04  # a little room for drift
            img = img.resize((int(img.width * sc), int(img.height * sc)), Image.LANCZOS)
            sources.append(("still", img, move))
    p = subprocess.Popen(["ffmpeg", "-v", "quiet", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                          "-r", str(FPS), "-i", "-", "-i", audio, "-map", "0:v", "-map", "1:a", "-c:v", "libx264",
                          "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
                          "-shortest", "-movflags", "+faststart", out], stdin=subprocess.PIPE)

    def frame_of(k, t):
        s, e = bounds[k]
        kind, src, move = sources[k]
        span = e - s + FADE
        x = min(1.0, max(0.0, (t - s) / span))
        if kind == "clip":
            return src[min(len(src) - 1, int((t - s) * FPS))].copy()
        return camera(src, x, move)

    for i in range(total):
        t = i / FPS
        k = next((j for j, (s, e) in enumerate(bounds) if s <= t < e), len(bounds) - 1)
        img = frame_of(k, t)
        # cross-fade into the next cut
        if k + 1 < len(bounds) and t > bounds[k][1] - FADE:
            a = (t - (bounds[k][1] - FADE)) / FADE
            img = Image.blend(img, frame_of(k + 1, t), min(1.0, a))
        cap = next((txt for s0, s1, _, txt in segs if s0 <= t < s1), "")
        tail = dur - t
        if tail < 4.5:
            img = title_card(img, min(1.0, (4.5 - tail) / 1.0))
        elif captions:
            img = caption(img, cap)
        p.stdin.write(img.tobytes())
    p.stdin.close()
    p.wait()
    print(out, flush=True)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--audio", default=os.path.join(ROOT, "output", "trailer", "trailer.mp4"))
    ap.add_argument("--out", default=os.path.join(ROOT, "output", "trailer", "trailer_anime.mp4"))
    ap.add_argument("--no-captions", action="store_true")
    a = ap.parse_args()
    build(a.audio, a.out, not a.no_captions)
