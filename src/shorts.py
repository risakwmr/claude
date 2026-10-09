"""Which Shorts go up next, and when they go public.

Each episode gives up to five Shorts (see src/make_short.py): ai, highlight, story, culture, lab.
Its highlight and ai Shorts go public at the same moment as the episode (00:00 / 12:00 JST).
The rest, and Shorts of older episodes, go up one per scheduled run at 08:00 or 18:00 JST
(SHORT_SLOTS_JST), about 2 a day, so a day stays near 8 uploads, under YouTube's daily upload limit.
The order mixes kinds and episodes, so the same episode doesn't fill a whole day, and a Short is only made
for an episode that is public by the time the Short goes public, so its "Full episode" link works.
shorts.json keeps track of what has been uploaded (keys like "14-story").

python src/shorts.py plan                         Shorts to queue in this scheduled run: lines "EPISODE KIND WHEN"
python src/shorts.py manual 14 all schedule       by hand: episode(s) or next, kind or all, schedule/public/private
python src/shorts.py record N KIND VIDEO_ID [PUBLISH_AT]
"""
import json
import os
import sys
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slot import JST, fmt, parse  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHORTS_FILE = os.path.join(ROOT, "shorts.json")
LEAD = timedelta(hours=12)  # scheduled runs come at 09:00 and 21:00 JST
# spreads an episode's Shorts over a few days. "ai" ("AI can X, not Y") Shorts drew the fewest views in the first
# week (Oct 2026), so they come last; first-person stories, studies and practical phrases did best.
OFFSET = {"ai": 7, "highlight": 1, "story": 2, "culture": 4, "lab": 3}
KIND_ORDER = list(OFFSET)


def slots_jst():
    raw = os.environ.get("SHORT_SLOTS_JST") or "8,18"
    hours = sorted({int(h) % 24 for h in raw.replace(" ", "").split(",") if h.strip()})
    return hours or [8, 18]


def load(path):
    return json.load(open(path)) if os.path.exists(path) else {}


def key(num, kind):
    return f"{int(num)}-{kind}"


def load_shorts():
    data = load(SHORTS_FILE)
    return {(k if "-" in k else key(k, "ai")): v for k, v in data.items()}  # old files: "14" = the ai Short


def save_shorts(data):
    def order(k):
        n, kind = k.split("-", 1)
        return int(n), KIND_ORDER.index(kind) if kind in KIND_ORDER else 9
    json.dump(dict(sorted(data.items(), key=lambda kv: order(kv[0]))), open(SHORTS_FILE, "w"), indent=2)


def first_slot(t):
    t = t.astimezone(JST)
    for day in range(3):
        for hour in slots_jst():
            s = (t + timedelta(days=day)).replace(hour=hour, minute=0, second=0, microsecond=0)
            if s >= t:
                return s
    raise RuntimeError("no slot found")


def scheduled_times(data):
    return [parse(v["publish_at"]) for v in data.values() if v.get("publish_at")]


def next_free(now, times):
    earliest = now + timedelta(minutes=15)
    last = max(times) if times else None
    if last and last + timedelta(hours=1) > earliest:
        return first_slot(last + timedelta(hours=1)), True
    return first_slot(earliest), False


def kinds_of(num):
    import make_short
    return make_short.kinds_of(num)


def candidates(by_time, data, published, skip=()):
    """Shorts not uploaded yet whose episode is public by `by_time`, best first."""
    out = []
    for k in published:
        at = published[k].get("publish_at")
        if not at or parse(at) > by_time + timedelta(minutes=1):
            continue
        for kind in kinds_of(int(k)):
            if key(k, kind) in data or key(k, kind) in skip:
                continue
            out.append((int(k) + OFFSET.get(kind, 8), int(k), KIND_ORDER.index(kind), kind))
    out.sort()
    return [(n, kind) for _, n, _, kind in out]


COMPANIONS = ["highlight", "story"]  # these go public together with their episode (first two the episode has)
BACKLOG_PER_RUN = 1                 # older Shorts per scheduled run (runs come twice a day -> 2 a day)


def companions_of(num):
    kinds = kinds_of(num)
    pick = [k for k in COMPANIONS if k in kinds]
    pick += [k for k in KIND_ORDER if k in kinds and k not in pick]
    return pick[:len(COMPANIONS)]


def plan(now=None):
    """[(episode, kind, when)] for this scheduled run.

    1. Companions: an episode that goes public within LEAD (or went public in the last hour) gets its
       highlight and ai Shorts scheduled for the same moment, so the Shorts and the episode come out together.
    2. Backlog: one older Short per run, at the next 08:00 / 18:00 JST slot (SHORT_SLOTS_JST)."""
    now = now or datetime.now(timezone.utc)
    data = load_shorts()
    published = load(os.path.join(ROOT, "published.json"))
    chosen, used = [], set()
    for k, v in sorted(published.items(), key=lambda kv: int(kv[0])):
        at = v.get("publish_at")
        if not at:
            continue
        t = parse(at)
        if not (now - timedelta(hours=1) <= t <= now + LEAD):
            continue
        for kind in companions_of(int(k)):
            if key(k, kind) in data:
                continue
            chosen.append((int(k), kind, fmt(t) if t > now + timedelta(minutes=15) else "now"))
            used.add(key(k, kind))
    taken = {fmt(t) for t in scheduled_times(data)} | {w for _, _, w in chosen}
    for _ in range(BACKLOG_PER_RUN):
        slot = first_slot(now + timedelta(minutes=15))
        while fmt(slot) in taken:
            slot = first_slot(slot + timedelta(minutes=1))
        if slot - now > LEAD:
            break
        picks = candidates(slot, data, published, used)
        if not picks:
            break
        n, kind = picks[0]
        chosen.append((n, kind, fmt(slot)))
        used.add(key(n, kind))
        taken.add(fmt(slot))
    return chosen


def manual(episodes, kind, visibility, now=None):
    now = now or datetime.now(timezone.utc)
    data = load_shorts()
    published = load(os.path.join(ROOT, "published.json"))
    times = scheduled_times(data)
    if episodes.strip().lower() in ("", "next"):
        slot = next_free(now, times)[0] if visibility == "schedule" else now
        picks = [p for p in candidates(slot, data, published) if kind in ("all", p[1])][:1]
    else:
        nums = [int(x) for x in episodes.replace(" ", "").split(",") if x]
        picks = [(n, k) for n in nums for k in kinds_of(n) if kind in ("all", k)]
    out = []
    for n, k in picks:
        if visibility == "schedule":
            slot = next_free(now, times)[0]
            times.append(slot)
            out.append((n, k, fmt(slot)))
        else:
            out.append((n, k, "now" if visibility == "public" else ""))
    return out


def record(num, kind, vid, when=""):
    data = load_shorts()
    now = datetime.now(timezone.utc)
    entry = {"video_id": vid, "uploaded_at": now.isoformat(timespec="seconds")}
    if when == "now":
        entry["publish_at"] = fmt(now)
    elif when:
        entry["publish_at"] = when
    data[key(num, kind)] = entry
    save_shorts(data)


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "plan":
        for n, k, w in plan():
            print(n, k, w)
    elif cmd == "manual":
        for n, k, w in manual(sys.argv[2], sys.argv[3], sys.argv[4]):
            print(n, k, w)
    elif cmd == "record":
        record(int(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5].strip() if len(sys.argv) > 5 else "")
    else:
        sys.exit(f"unknown command {cmd}")
