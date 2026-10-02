"""Draw only the thumbnail for one or more episodes: python src/make_thumbnail.py 1 2"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render import draw_thumbnail  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
meta = json.load(open(os.path.join(ROOT, "episodes", "episodes.json"), encoding="utf-8"))
for n in map(int, sys.argv[1:]):
    ep = next(e for e in meta["episodes"] if e["number"] == n)
    out = os.path.join(ROOT, "output", f"ep{n:02d}")
    os.makedirs(out, exist_ok=True)
    print(draw_thumbnail(n, ep, os.path.join(out, f"ep{n:02d}_thumbnail.jpg")))
