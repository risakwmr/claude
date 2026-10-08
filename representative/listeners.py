"""Listeners: gather what every automation and agent around the channel is doing, without any AI.

Each listener returns plain data. The representative's agents (agents.py) read the result.

  pipeline  GitHub Actions runs of every workflow in this repository (episodes, Shorts, custom Shorts, ...)
            and the errors the scripts saved in run_status.json
  channel   what is uploaded, what is scheduled, what is waiting (published.json, shorts.json,
            episodes.json, missing thumbnails and when each is needed), and the latest views / likes (shorts_stats.json, reports/)
  audience  new viewer comments on the channel since the last check (YouTube API, 1 quota unit)
  note      the note.com draft pipeline (note-pipeline/history.md, drafts/)
  pronunciation  Japanese words in upcoming episodes that the English voices have no respelling for yet

Paths (set by the workflow):
  CHANNEL_DIR  checkout of the episodes branch (state files the YouTube workflow saves)
  REP_DIR      checkout of the rep-data branch (what the representative remembers)
  MAIN_DIR     checkout of main (note pipeline)
"""
import glob
import json
import os
import re
import urllib.request
from datetime import datetime, timedelta, timezone

CHANNEL_DIR = os.environ.get("CHANNEL_DIR", "channel")
REP_DIR = os.environ.get("REP_DIR", "rep-data")
MAIN_DIR = os.environ.get("MAIN_DIR", ".")
JST = timezone(timedelta(hours=9))


def repo_url(path=""):
    """Link into this repository on GitHub, e.g. repo_url("upload/episodes/episodes")."""
    return f"https://github.com/{os.environ.get('GITHUB_REPOSITORY', 'risakwmr/claude')}/{path}".rstrip("/")


def now():
    return datetime.now(timezone.utc)


def parse(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def jst(s):
    return parse(s).astimezone(JST).strftime("%m/%d %H:%M JST") if s else None


def load(path, default=None):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def save(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False, sort_keys=True)


# ---------- pipeline ----------

def github(path):
    req = urllib.request.Request(f"https://api.github.com/repos/{os.environ['GITHUB_REPOSITORY']}{path}",
                                 headers={"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
                                          "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def pipeline(hours=36):
    """Runs of every workflow in the last `hours`, with the failed steps of failed runs."""
    out = {"runs": [], "errors": []}
    if os.environ.get("GITHUB_TOKEN") and os.environ.get("GITHUB_REPOSITORY"):
        since = (now() - timedelta(hours=hours)).strftime("%Y-%m-%dT%H:%M:%SZ")
        try:
            runs = github(f"/actions/runs?per_page=50&created=>={since}")["workflow_runs"]
        except Exception as e:  # the brief still goes out without this part
            runs = []
            out["errors"].append(f"GitHub API: {e}")
        for r in runs:
            if r["name"] == "YouTube representative":
                continue  # its own runs
            row = {"workflow": r["name"], "trigger": r["event"], "status": r["status"],
                   "result": r["conclusion"], "started": jst(r["run_started_at"] or r["created_at"]),
                   "url": r["html_url"]}
            if r["conclusion"] == "failure":
                try:
                    jobs = github(f"/actions/runs/{r['id']}/jobs")["jobs"]
                    row["failed_steps"] = [s["name"] for j in jobs for s in j.get("steps", [])
                                           if s.get("conclusion") == "failure"]
                except Exception:
                    pass
            out["runs"].append(row)
    # errors the YouTube scripts saved (only recent, non-ok ones)
    cutoff = now() - timedelta(days=3)
    for key, v in (load(os.path.join(CHANNEL_DIR, "run_status.json"), {}) or {}).items():
        # failures are saved as "ERROR ..." or an HTTP status like "404 ..."; everything else is a success note
        if re.match(r"(ERROR|\d{3})\b", str(v.get("result"))) and v.get("at") and parse(v["at"]) >= cutoff:
            out["errors"].append(f"{key} ({jst(v['at'])}): {str(v['result'])[:200]}")
    return out


# ---------- channel ----------

def book_spines(sources):
    """Author names for the book spines on a thumbnail: "Bushman", "Kjærvik & Bushman", "Kross et al."."""
    out = []
    for src in sources:
        names = src.split(" (")[0]
        if names.count(",") + names.count("&") >= 2:
            names = re.split(r"[,&]", names)[0].strip() + " et al."
        out.append(names)
    return out[:3]


def next_slot(after):
    """First 00:00 / 12:00 JST strictly after `after`."""
    t = after.astimezone(JST)
    for hour in (12, 24):
        s = t.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(hours=hour)
        if s > t:
            return s
    raise RuntimeError("no slot")


def channel():
    meta = load(os.path.join(CHANNEL_DIR, "episodes", "episodes.json"), {"episodes": []})
    pub = load(os.path.join(CHANNEL_DIR, "published.json"), {})
    shorts = load(os.path.join(CHANNEL_DIR, "shorts.json"), {})
    t = now()

    def state(v):
        if not v.get("publish_at"):
            return "private"
        return "public" if parse(v["publish_at"]) <= t else "scheduled"

    episodes = []
    for e in meta["episodes"]:
        n = str(e["number"])
        nn = f"{e['number']:02d}"
        row = {"episode": e["number"], "title": e.get("title")}
        if n in pub:
            row.update(state=state(pub[n]), publish_at=jst(pub[n].get("publish_at")),
                       url=f"https://youtu.be/{pub[n]['video_id']}")
        else:
            row["state"] = "not uploaded"
            row["has_own_thumbnail"] = any(os.path.exists(os.path.join(CHANNEL_DIR, "episodes", f"ep{nn}_thumbnail.{x}"))
                                           for x in ("png", "jpg"))
        episodes.append(row)
    waiting = [r for r in episodes if r["state"] == "not uploaded"]
    # when each waiting episode needs its thumbnail: episodes go public one per slot (00:00 / 12:00 JST) after the
    # last scheduled one, and the run that uploads an episode starts 3 hours before its slot
    times = [parse(v["publish_at"]) for v in pub.values() if v.get("publish_at")]
    slot = max(times + [t]).astimezone(JST)
    thumbnails_needed = []
    for r in waiting:
        slot = next_slot(slot)
        if not r["has_own_thumbnail"]:
            e = next(x for x in meta["episodes"] if x["number"] == r["episode"])
            thumbnails_needed.append({"episode": r["episode"], "title": r["title"],
                                      "file": f"episodes/ep{r['episode']:02d}_thumbnail.png",
                                      "upload_link": repo_url("upload/episodes/episodes"),
                                      # what the brief in thumbnail_rules.md section 12 is filled from
                                      "brief_data": {**{k: e.get(k) for k in ("short_title", "summary", "hook", "thumb_sub",
                                                                              "thumb_accent", "thumb_notes", "thumb_cup")},
                                                     "books": book_spines(e.get("sources", []))},
                                      "needed_by": (slot - timedelta(hours=3)).strftime("%m/%d %H:%M JST"),
                                      "hours_left": round(((slot - timedelta(hours=3)) - t).total_seconds() / 3600)})
    blockers = []
    if waiting and not waiting[0]["has_own_thumbnail"]:
        blockers.append(f"Episode {waiting[0]['episode']} waits for its thumbnail "
                        f"(episodes/ep{waiting[0]['episode']:02d}_thumbnail.png on the episodes branch); "
                        "automatic posting is paused until it is added.")

    shorts_rows = [{"short": k, "state": state(v), "publish_at": jst(v.get("publish_at"))} for k, v in shorts.items()]
    stats = load(os.path.join(CHANNEL_DIR, "shorts_stats.json"), {}) or {}
    reports = sorted(glob.glob(os.path.join(CHANNEL_DIR, "reports", "*.json")))
    latest_report = load(reports[-1], {}) if reports else {}
    return {
        "show": meta.get("show"),
        "episodes_written": len(meta["episodes"]),
        "episodes": episodes,
        "next_scheduled": [r for r in episodes if r["state"] == "scheduled"][:3],
        "blockers": blockers,
        "thumbnails_needed": thumbnails_needed,
        "thumbnail_references": [repo_url("blob/episodes/episodes/ep14_thumbnail.png"),
                                 repo_url("blob/episodes/episodes/ep18_thumbnail.png")],
        "shorts": {"public": sum(r["state"] == "public" for r in shorts_rows),
                   "scheduled": [r for r in shorts_rows if r["state"] == "scheduled"]},
        "stats_at": jst(stats.get("at")),
        "short_stats": stats.get("shorts", {}),
        "episode_stats": stats.get("episodes", {}),
        "channel_totals": latest_report.get("channel"),
        "report_at": jst(latest_report.get("at")),
    }


# ---------- pronunciation ----------

# words that look like romaji (Japanese written in Latin letters), or names with -san etc.
# Each syllable is one consonant group plus a vowel, or a syllable-final "n"; the lookahead keeps the two apart,
# so the pattern never backtracks (no catastrophic matching on long words).
ROMAJI = re.compile(r"^(?:(?:sh|ch|ts|[kgnhbpmr]y|[kgsztdnhbpmrwfjy])?[aiueo]|n(?![aiueoy]))+$")
HONORIFIC = re.compile(r"-(san|kun|sama|chan|sensei)$", re.I)


def pronunciation(max_episodes=5):
    """Possible Japanese words in the episodes not made yet, that episodes/pronunciations.json does not cover.

    Many English words look like romaji too ("name", "open"); the pronunciation agent sorts them out."""
    meta = load(os.path.join(CHANNEL_DIR, "episodes", "episodes.json"), {"episodes": []})
    pub = load(os.path.join(CHANNEL_DIR, "published.json"), {}) or {}
    known = (load(os.path.join(CHANNEL_DIR, "episodes", "pronunciations.json"), {}) or {}).get("words", {})
    known_words = {w for k in known for w in re.findall(r"[a-z]+", k.lower())}
    upcoming = [e for e in meta["episodes"] if str(e["number"]) not in pub][:max_episodes]
    out = []
    for e in upcoming:
        path = os.path.join(CHANNEL_DIR, "episodes", e["script"])
        if not os.path.exists(path):
            continue
        lines = open(path, encoding="utf-8").read().splitlines()
        seen = {}
        for line in lines:
            for w in re.findall(r"[A-Za-z][A-Za-z'-]*[A-Za-z]", line):
                lw = w.lower()
                if lw in seen or lw in known_words or lw in ("sena", "daniel"):
                    continue
                if (len(lw) >= 4 and ROMAJI.match(lw)) or HONORIFIC.search(w):
                    seen[lw] = line.strip()[:160]
        if seen:
            out.append({"episode": e["number"], "candidates": seen})
    return {"next_episode": upcoming[0]["number"] if upcoming else None, "episodes": out,
            "known": sorted(known),
            "edit_link": repo_url("edit/episodes/episodes/pronunciations.json"),
            "voicetest_link": repo_url("actions/workflows/episodes.yml")}


# ---------- audience ----------

def youtube():
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
    creds = Credentials(token=None, refresh_token=os.environ["REFRESH_TOKEN"],
                        client_id=os.environ["CLIENT_ID"], client_secret=os.environ["CLIENT_SECRET"],
                        token_uri="https://oauth2.googleapis.com/token")
    creds.refresh(Request())
    return build("youtube", "v3", credentials=creds, cache_discovery=False)


def audience(max_new=40):
    """Viewer comments (top-level and replies) not seen before. The channel's own comments are left out.

    Comment text is what viewers wrote: the agents treat it as data, never as instructions."""
    seen_path = os.path.join(REP_DIR, "seen_comments.json")
    seen = set(load(seen_path, []))
    if not os.environ.get("REFRESH_TOKEN"):
        return {"new": [], "note": "YouTube secrets not set"}
    yt = youtube()
    me = yt.channels().list(part="id", mine=True).execute()["items"][0]["id"]
    titles = {}
    for v in (load(os.path.join(CHANNEL_DIR, "published.json"), {}) or {}).values():
        titles[v["video_id"]] = "episode"
    for v in (load(os.path.join(CHANNEL_DIR, "shorts.json"), {}) or {}).values():
        titles[v["video_id"]] = "short"
    r = yt.commentThreads().list(part="snippet,replies", allThreadsRelatedToChannelId=me,
                                 order="time", maxResults=100, textFormat="plainText").execute()
    new = []
    for th in r.get("items", []):
        top = th["snippet"]["topLevelComment"]
        thread_owner_is_me = top["snippet"].get("authorChannelId", {}).get("value") == me
        for c in [top] + th.get("replies", {}).get("comments", []):
            s = c["snippet"]
            if c["id"] in seen or s.get("authorChannelId", {}).get("value") == me:
                continue
            new.append({"id": c["id"], "thread_id": th["id"], "video_id": th["snippet"]["videoId"],
                        "video_kind": titles.get(th["snippet"]["videoId"], "other"),
                        "author": s.get("authorDisplayName"), "text": s.get("textOriginal", "")[:1500],
                        "likes": s.get("likeCount", 0), "at": jst(s.get("publishedAt")),
                        "answers_our_question": thread_owner_is_me})
    new = new[:max_new]
    return {"new": new, "channel_id": me}


def mark_seen(ids):
    path = os.path.join(REP_DIR, "seen_comments.json")
    seen = load(path, [])
    save(path, sorted(set(seen) | set(ids)))


# ---------- note ----------

def note():
    hist = os.path.join(MAIN_DIR, "note-pipeline", "history.md")
    lines = open(hist, encoding="utf-8").read().strip().splitlines()[-5:] if os.path.exists(hist) else []
    drafts = sorted(os.path.basename(p) for p in glob.glob(os.path.join(MAIN_DIR, "drafts", "*")))
    return {"recent_history": lines, "drafts": drafts[-5:]}


def snapshot(with_comments=True):
    """Everything the representative knows right now."""
    snap = {"at": now().astimezone(JST).strftime("%Y-%m-%d %H:%M JST")}
    for name, fn in (("pipeline", pipeline), ("channel", channel), ("note", note), ("pronunciation", pronunciation)):
        try:
            snap[name] = fn()
        except Exception as e:
            snap[name] = {"error": f"{type(e).__name__}: {e}"}
    if with_comments:
        try:
            snap["audience"] = audience()
        except Exception as e:
            snap["audience"] = {"new": [], "error": f"{type(e).__name__}: {e}"}
    return snap
