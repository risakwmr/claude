"""Choose when the next episode goes public on YouTube.

Episodes go public one at a time, in order, at 00:00 and 12:00 Japan time. Each new
episode takes the first slot after the last one already scheduled in published.json.

python src/slot.py          prints a UTC time like 2026-10-08T03:00:00Z,
                            "wait" when the next slot is more than 6 hours away (queue is full),
                            or "now" when this run is too late for its slot.
python src/slot.py --force  always prints the next free slot time.
"""
import json
import os
import sys
from datetime import datetime, timedelta, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JST = timezone(timedelta(hours=9))
SLOTS_JST = (0, 12)  # hours of the day in Japan time
LEAD = timedelta(hours=6)  # scheduled runs start about 3 hours before a slot


def fmt(t):
    return t.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def first_slot(t):
    """First 00:00 / 12:00 JST at or after t."""
    t = t.astimezone(JST)
    for day in range(2):
        for hour in SLOTS_JST:
            slot = (t + timedelta(days=day)).replace(hour=hour, minute=0, second=0, microsecond=0)
            if slot >= t:
                return slot
    raise RuntimeError("no slot found")


def load_published():
    path = os.path.join(ROOT, "published.json")
    return json.load(open(path)) if os.path.exists(path) else {}


def last_scheduled(published, skip=()):
    times = [parse(v["publish_at"]) for k, v in published.items()
             if v.get("publish_at") and k not in skip]
    return max(times) if times else None


def next_free(now, published, skip=()):
    """(slot, from_queue): the next free slot, and whether it follows an already scheduled episode."""
    earliest = now + timedelta(minutes=15)
    last = last_scheduled(published, skip)
    if last and last + timedelta(hours=11) > earliest:
        return first_slot(last + timedelta(hours=11)), True
    return first_slot(earliest), False


def decide(now=None, published=None, force=False):
    now = now or datetime.now(timezone.utc)
    published = load_published() if published is None else published
    slot, from_queue = next_free(now, published)
    if force or slot - now <= LEAD:
        return fmt(slot)
    return "wait" if from_queue else "now"


if __name__ == "__main__":
    print(decide(force="--force" in sys.argv))
