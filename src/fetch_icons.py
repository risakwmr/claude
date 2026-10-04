"""Download the free illustrations an episode's visual cues use.

Illustrations: Microsoft Fluent Emoji, 3D style (MIT License), https://github.com/microsoft/fluentui-emoji
Valid names are listed in assets/icons/INDEX.txt (e.g. "Light bulb", "Handshake", "Tokyo tower").

python src/fetch_icons.py 14 15     downloads what episodes 14 and 15 need into assets/icons/
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICON_DIR = os.path.join(ROOT, "assets", "icons")
REPO = "https://github.com/microsoft/fluentui-emoji"


def slug(name):
    return name.strip().lower().replace(" ", "_").replace("/", "_")


def icon_path(name):
    return os.path.join(ICON_DIR, slug(name) + ".png")


def names_in(num):
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from scenes import load_cues
    out = set()
    for cue in load_cues(num):
        board = cue.get("board") or {}
        for key in ("icon", "icons"):
            v = board.get(key)
            if isinstance(v, str):
                out.add(v)
            elif isinstance(v, list):
                out.update(v)
    return out


def index():
    path = os.path.join(ICON_DIR, "INDEX.txt")
    return {line.strip().lower(): line.strip() for line in open(path, encoding="utf-8") if line.strip()}


def fetch(names):
    idx = index()
    want = {}
    for n in names:
        real = idx.get(n.strip().lower())
        if not real:
            print(f"  WARNING: no illustration called {n!r} (see assets/icons/INDEX.txt)", flush=True)
            continue
        if not os.path.exists(icon_path(n)):
            want[n] = real
    if not want:
        return
    tmp = tempfile.mkdtemp()
    run = lambda *a: subprocess.run(a, cwd=tmp, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    run("git", "clone", "--depth", "1", "--filter=blob:none", "--sparse", REPO, "fe")
    subprocess.run(["git", "sparse-checkout", "set", "--no-cone"] + [p for r in want.values()
                                                            for p in (f"/assets/{r}/3D/", f"/assets/{r}/Default/3D/")],
                   cwd=os.path.join(tmp, "fe"), check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    os.makedirs(ICON_DIR, exist_ok=True)
    for n, real in want.items():
        d = os.path.join(tmp, "fe", "assets", real, "3D")
        pngs = [f for f in os.listdir(d) if f.endswith(".png")] if os.path.isdir(d) else []
        if not pngs:  # skin-tone variants keep the default one in a subfolder
            alt = os.path.join(tmp, "fe", "assets", real, "Default", "3D")
            d = alt
            pngs = [f for f in os.listdir(d) if f.endswith(".png")] if os.path.isdir(d) else []
        if pngs:
            shutil.copy(os.path.join(d, pngs[0]), icon_path(n))
            print(f"  illustration: {real}", flush=True)
        else:
            print(f"  WARNING: could not download {real!r}", flush=True)
    shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    names = set()
    for a in sys.argv[1:]:
        names |= names_in(int(a))
    fetch(names)
