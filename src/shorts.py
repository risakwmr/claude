"""Which episode gets the next Short, and when it goes public.

Shorts go public one at a time, in episode order, at 08:00 and 18:00 Japan time
(08:00 JST = early evening in the US, 18:00 JST = afternoon in India and Southeast Asia, midday in Europe).
Change the times with the repository variable SHORT_SLOTS_JST, e.g. "8" or "8,18" or "7,12,18".
A Short is only made for an episode that is already public (or goes public before the Short),
so its "Full episode" link works. shorts.json keeps track of what has been uploaded.

python src/shorts.py slot           next publish time (UTC), "wait" if the next slot is far away, or "now"
python src/shorts.py slot --force   always the next free slot
python src/shorts.py pick next      the next episode that needs a Short ("" when none is ready)
python src/shorts.py pick 3,4       these episodes
python src/shorts.py record N VIDEO_ID [PUBLISH_AT]
"""
import json
import os
import sys
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slot import JST, fmt, parse  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHORTS_FILE = os.path.join(ROOT, "shorts.json")
LEAD = timedelta(hours=12)  # scheduled runs come at 09:00 and 21:00 JST, 9-11 hours before a slot


def slots_jst():
    raw = os.environ.get("SHORT_SLOTS_JST") or "8,18"
    hours = sorted({int(h) % 24 for h in raw.replace(" ", "").split(",") if h})
    return hours or [8, 18]


def load(path):
    return json.load(open(path)) if os.path.exists(path) else {}


def load_shorts():
    return load(SHORTS_FILE)


def first_slot(t):
    t = t.astimezone(JST)
    for day in range(3):
        for hour in slots_jst():
            s = (t + timedelta(days=day)).replace(hour=hour, minute=0, second=0, microsecond=0)
            if s >= t:
                return s
    raise RuntimeError("no slot found")


def next_free(now, shorts):
    earliest = now + timedelta(minutes=15)
    times = [parse(v["publish_at"]) for v in shorts.values() if v.get("publish_at")]
    last = max(times) if times else None
    if last and last + timedelta(hours=1) > earliest:
        return first_slot(last + timedelta(hours=1)), True
    return first_slot(earliest), False


def decide(now=None, force=False):
    now = now or datetime.now(timezone.utc)
    data = load_shorts()
    slot, from_queue = next_free(now, data)
    if force or slot - now <= LEAD:
        return fmt(slot)
    times = [parse(v["publish_at"]) for v in data.values() if v.get("publish_at")]
    recent = times and max(times) > now - timedelta(hours=12)
    return "wait" if from_queue or recent else "now"


def pick(arg, when=None):
    """Episodes that get a Short: explicit numbers, or the next one whose episode is public by `when`."""
    if arg.strip().lower() not in ("", "next"):
        return [int(x) for x in arg.replace(" ", "").split(",") if x]
    published = load(os.path.join(ROOT, "published.json"))
    shorts = load_shorts()
    limit = parse(when) if when and when not in ("now", "wait") else datetime.now(timezone.utc)
    for k in sorted(published, key=int):
        if k in shorts:
            continue
        at = published[k].get("publish_at")
        if at and parse(at) <= limit + timedelta(minutes=1):
            return [int(k)]
    return []


def record(num, vid, when=""):
    shorts = load_shorts()
    now = datetime.now(timezone.utc)
    entry = {"video_id": vid, "uploaded_at": now.isoformat(timespec="seconds")}
    if when == "now":
        entry["publish_at"] = fmt(now)
    elif when:
        entry["publish_at"] = when
    shorts[str(num)] = entry
    shorts = dict(sorted(shorts.items(), key=lambda kv: int(kv[0])))
    json.dump(shorts, open(SHORTS_FILE, "w"), indent=2)


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "slot":
        print(decide(force="--force" in sys.argv))
    elif cmd == "pick":
        print(" ".join(map(str, pick(sys.argv[2] if len(sys.argv) > 2 else "next",
                                     sys.argv[3] if len(sys.argv) > 3 else None))))
    elif cmd == "record":
        record(int(sys.argv[2]), sys.argv[3], sys.argv[4].strip() if len(sys.argv) > 4 else "")
    else:
        sys.exit(f"unknown command {cmd}")
