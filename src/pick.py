"""Pick which episodes to build: an explicit number, or the next unpublished ones."""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

arg = sys.argv[1] if len(sys.argv) > 1 else "next"
count = int(sys.argv[2]) if len(sys.argv) > 2 else 2
meta = json.load(open(os.path.join(ROOT, "episodes", "episodes.json"), encoding="utf-8"))
pub_path = os.path.join(ROOT, "published.json")
published = json.load(open(pub_path)) if os.path.exists(pub_path) else {}

if arg.strip().lower() in ("", "next"):
    todo = [e["number"] for e in sorted(meta["episodes"], key=lambda e: e["number"])
            if str(e["number"]) not in published][:count]
else:
    todo = [int(x) for x in arg.replace(" ", "").split(",") if x]
print(" ".join(map(str, todo)))
