"""Cut the animation pose sheets into transparent frames.

assets/characters/sheets/<who>_<mouth>_eyes_<eyes>.png  ->  assets/characters/anim/<who>_<NN>_<mouth>_<eyes>.png
  who: sena (6x4 grid) or daniel (6x5 grid); mouth: quiet / talk; eyes: open / closed.
Every variant of the same cell gets the same crop box, so frames can be swapped for lip sync and blinks.

python tools/cut_sheets.py
"""
import glob
import os
import re

import numpy as np
from PIL import Image
from scipy import ndimage

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHEETS = os.path.join(ROOT, "assets", "characters", "sheets")
OUT = os.path.join(ROOT, "assets", "characters", "anim")
GRID = {"sena": (6, 4), "daniel": (6, 5)}


def ink(a, bg):
    return np.abs(a.astype(int) - bg).sum(2) > 40


def cuts(profile, n, length, search=45):
    """Grid lines near k*length/n where the ink profile is lowest."""
    out = [0]
    for k in range(1, n):
        c = int(k * length / n)
        lo, hi = max(1, c - search), min(length - 1, c + search)
        out.append(lo + int(np.argmin(profile[lo:hi])))
    return out + [length]


def alpha_for(cell, bg):
    """Background = near-background pixels connected to the cell border."""
    near = np.abs(cell.astype(int) - bg).sum(2) < 30
    lab, _ = ndimage.label(near)
    border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    bgmask = np.isin(lab, list(border))
    alpha = np.where(bgmask, 0, 255).astype(np.uint8)
    return np.asarray(Image.fromarray(alpha).filter(__import__("PIL.ImageFilter").ImageFilter.MinFilter(3)))


def main():
    os.makedirs(OUT, exist_ok=True)
    for who, (cols, rows) in GRID.items():
        files = sorted(glob.glob(os.path.join(SHEETS, f"{who}_*_eyes_*.png")))
        if not files:
            continue
        imgs = {re.sub(rf"^{who}_", "", os.path.basename(f)[:-4]).replace("_eyes_", "_"):
                np.asarray(Image.open(f).convert("RGB")) for f in files}
        ref = imgs.get("quiet_open", next(iter(imgs.values())))
        bg = ref[5, 5].astype(int)
        m = sum(ink(a, bg).astype(int) for a in imgs.values())
        h, w = m.shape
        xs, ys = cuts(m.sum(0), cols, w), cuts(m.sum(1), rows, h)
        n = 0
        for r in range(rows):
            for c in range(cols):
                n += 1
                box = (xs[c], ys[r], xs[c + 1], ys[r + 1])
                masks = {}
                for name, a in imgs.items():
                    cell = a[box[1]:box[3], box[0]:box[2]]
                    masks[name] = alpha_for(cell, bg)
                union = np.maximum.reduce(list(masks.values()))
                yy, xx = np.nonzero(union)
                if not len(yy):
                    continue
                t, b, left, right = yy.min(), yy.max() + 1, xx.min(), xx.max() + 1
                for name, a in imgs.items():
                    cell = a[box[1]:box[3], box[0]:box[2]]
                    rgba = np.dstack([cell, masks[name]])[t:b, left:right]
                    Image.fromarray(rgba, "RGBA").save(os.path.join(OUT, f"{who}_{n:02d}_{name}.png"))
        print(who, n, "cells:", ", ".join(sorted(imgs)))


if __name__ == "__main__":
    main()
