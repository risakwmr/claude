"""Instagram Reels for @learnwhataicant, made from the YouTube Shorts (Buffer free plan).

The Reel is the same 1080x1920 mp4 that src/make_short.py renders for YouTube (voice + burned-in captions).
GitHub Actions (.github/workflows/reels.yml on main) renders it and attaches it to the public release "reels",
together with a small JSON sidecar that already holds the Instagram caption. Buffer then fetches the mp4 from the
stable public release URL.

Order: Shorts already on YouTube (shorts.json, not deleted, publish_at passed), by episode, and inside an
episode culture > highlight > lab > ai > story (culture Shorts do ~2x the others).

In GitHub Actions (repo checkout of the episodes branch):
  python src/reels.py todo N HAVE_FILE      next N keys ("1-highlight") whose mp4 is not in the release yet
  python src/reels.py meta N KIND OUT_DIR   write the caption sidecar epNN_short_KIND.reel.json

Anywhere (Hark's daily run; needs only Python 3 stdlib, the Buffer key on api.buffer.com, and the GitHub
connector for writing reels.json):
  curl -sL https://raw.githubusercontent.com/risakwmr/claude/episodes/src/reels.py | python3 - post            # draft
  curl -sL https://raw.githubusercontent.com/risakwmr/claude/episodes/src/reels.py | python3 - post --schedule # 20:00 JST
  ... post --key 1-highlight --draft          a specific Short as a draft
  ... channels                                print Buffer organizations / channels
Drafts and scheduled posts are both recorded in reels.json (episodes branch) so a Short is never posted twice.
"""
import base64
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

OWNER, REPO, BRANCH, TAG = "risakwmr", "claude", "episodes", "reels"
JST = timezone(timedelta(hours=9))
KIND_ORDER = ["culture", "highlight", "lab", "ai", "story"]
POST_HOUR_JST = int(os.environ.get("REELS_HOUR_JST", "20"))
BUFFER = "https://api.buffer.com"
IG_HANDLE = "learnwhataicant"

LINE = {
    "culture": "Same problem at work. Japan and the US handle it very differently.",
    "highlight": "The one moment from this episode that changes how you see work.",
    "lab": "Phrases that work at work. Save this for your next meeting.",
    "ai": "AI can draft the words. It can't do this part for you.",
    "story": "A real mistake at work, and the human skill it taught.",
}
BASE_TAGS = ["#softskills", "#emotionalintelligence", "#workplace", "#careeradvice"]
KIND_TAGS = {
    "culture": ["#japanvsusa", "#workculture", "#crossculturalcommunication", "#japan"],
    "highlight": ["#futureofwork", "#worklife", "#leadership"],
    "lab": ["#communicationskills", "#workplacecommunication", "#leadership"],
    "ai": ["#aiandwork", "#futureofwork", "#humanskills"],
    "story": ["#careerlessons", "#worklife", "#humanskills"],
}


def stem(num, kind):
    return f"ep{int(num):02d}_short_{kind}"


def sort_key(k):
    n, kind = k.split("-", 1)
    return int(n), KIND_ORDER.index(kind) if kind in KIND_ORDER else 9


def parse(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def eligible(shorts, now=None):
    now = now or datetime.now(timezone.utc)
    out = []
    for k, v in shorts.items():
        if "-" not in k or v.get("deleted") or not v.get("video_id"):
            continue
        if v.get("publish_at") and parse(v["publish_at"]) > now:
            continue
        out.append(k)
    return sorted(out, key=sort_key)


# ---------- GitHub Actions side ----------

def caption(num, kind, title, hook, ep_title, ep_url):
    hook = (hook or title or "").strip()
    title = (title or "").strip()
    parts = [hook]
    if title and title.lower() != hook.lower():
        parts.append(title)
    parts.append(LINE.get(kind, ""))
    full = f"Full episode: Human Curriculum EP{int(num):02d}"
    if ep_title:
        full += f" \u201c{ep_title}\u201d"
    parts.append(full + " (link in bio)" + (f"\n{ep_url}" if ep_url else ""))
    parts.append("Follow for the work skills AI can't do.")
    tags = BASE_TAGS + KIND_TAGS.get(kind, [])
    return "\n\n".join(p for p in parts if p) + "\n\n" + " ".join(tags)


def cmd_todo(n, have_file):
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    shorts = json.load(open(os.path.join(root, "shorts.json")))
    reels = json.load(open(os.path.join(root, "reels.json"))) if os.path.exists(os.path.join(root, "reels.json")) else {}
    have = set(open(have_file).read().split()) if have_file and os.path.exists(have_file) else set()
    todo = [k for k in eligible(shorts) if k not in reels and f"{stem(*k.split('-', 1))}.mp4" not in have]
    print(" ".join(todo[: int(n)]))


def cmd_meta(num, kind, out_dir):
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import make_episode as me
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    meta, ep, lines = me.load_episode(int(num))
    info_path = os.path.join(out_dir, f"{stem(num, kind)}.json")
    info = json.load(open(info_path)) if os.path.exists(info_path) else {}
    pub = json.load(open(os.path.join(root, "published.json")))
    ep_vid = (pub.get(str(int(num))) or {}).get("video_id")
    ep_url = f"https://youtu.be/{ep_vid}" if ep_vid else ""
    shorts = json.load(open(os.path.join(root, "shorts.json")))
    side = {
        "key": f"{int(num)}-{kind}", "episode": int(num), "kind": kind,
        "title": info.get("title"), "hook": info.get("hook"), "duration": info.get("duration"),
        "episode_title": ep.get("title"), "episode_url": ep_url,
        "short_url": f"https://youtube.com/shorts/{(shorts.get(f'{int(num)}-{kind}') or {}).get('video_id', '')}",
        "caption": caption(num, kind, info.get("title"), info.get("hook"), ep.get("title"), ep_url),
    }
    path = os.path.join(out_dir, f"{stem(num, kind)}.reel.json")
    json.dump(side, open(path, "w"), indent=2, ensure_ascii=False)
    print(path)


# ---------- Hark side ----------

def http_json(url, data=None, headers=None):
    req = urllib.request.Request(url, data=data, headers=headers or {})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())


def gql(query, variables=None):
    body = json.dumps({"query": query, "variables": variables or {}}).encode()
    hdr = {"Content-Type": "application/json"}
    key = os.environ.get("BUFFER_API_KEY")
    if key:
        hdr["Authorization"] = f"Bearer {key}"   # proxy may also inject it on api.buffer.com
    res = http_json(BUFFER, body, hdr)
    if res.get("errors"):
        raise SystemExit("Buffer error: " + json.dumps(res["errors"])[:400])
    return res["data"]


def find_channel():
    if os.environ.get("BUFFER_CHANNEL_ID"):
        return os.environ["BUFFER_CHANNEL_ID"]
    orgs = gql("query { account { organizations { id name } } }")["account"]["organizations"]
    for o in orgs:
        chs = gql("query($o: OrganizationId!) { channels(input: {organizationId: $o}) { id name service } }",
                  {"o": o["id"]})["channels"]
        for c in chs:
            if c["service"] == "instagram" and IG_HANDLE in (c.get("name") or "").lower():
                return c["id"]
        for c in chs:
            if c["service"] == "instagram":
                return c["id"]
    raise SystemExit("No Instagram channel in Buffer")


def gh_file(path):
    """(json, sha) of a file on the episodes branch, unauthenticated public read (no CDN cache)."""
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{path}?ref={BRANCH}"
    try:
        d = http_json(url, headers={"Accept": "application/vnd.github+json"})
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return {}, None
        raise
    return json.loads(base64.b64decode(d["content"]).decode() or "{}"), d["sha"]


def gh_put(path, obj, sha, message):
    content = base64.b64encode((json.dumps(obj, indent=2, ensure_ascii=False) + "\n").encode()).decode()
    args = ["apicall", "github", "contents_put", f"owner={OWNER}", f"repo={REPO}", f"path={path}",
            f"message={message}", f"content={content}", f"branch={BRANCH}"] + ([f"sha={sha}"] if sha else [])
    r = subprocess.run(args, capture_output=True, text=True)
    if r.returncode != 0 or '"commit"' not in r.stdout:
        print("WARNING: reels.json not saved: " + (r.stderr or r.stdout)[:300])


def release_assets():
    d = http_json(f"https://api.github.com/repos/{OWNER}/{REPO}/releases/tags/{TAG}",
                  headers={"Accept": "application/vnd.github+json"})
    return {a["name"]: a["browser_download_url"] for a in d.get("assets", [])}


def next_slot():
    now = datetime.now(JST)
    t = now.replace(hour=POST_HOUR_JST, minute=0, second=0, microsecond=0)
    if t < now + timedelta(minutes=30):
        t += timedelta(days=1)
    return t


def cmd_post(argv):
    schedule = "--schedule" in argv
    key = argv[argv.index("--key") + 1] if "--key" in argv else None
    reels, sha = gh_file("reels.json")
    assets = release_assets()
    if key is None:
        shorts, _ = gh_file("shorts.json")
        for k in eligible(shorts):
            s = stem(*k.split("-", 1))
            if k not in reels and f"{s}.mp4" in assets and f"{s}.reel.json" in assets:
                key = k
                break
        if key is None:
            print("NOTHING: no rendered Short left to post (run the reels workflow)")
            return
    elif key in reels and "--force" not in argv:
        print(f"SKIP {key}: already in reels.json ({reels[key].get('status')})")
        return
    s = stem(*key.split("-", 1))
    if f"{s}.mp4" not in assets:
        raise SystemExit(f"{s}.mp4 is not in release '{TAG}' yet")
    video_url = assets[f"{s}.mp4"]
    side = http_json(assets[f"{s}.reel.json"]) if f"{s}.reel.json" in assets else {}
    text = side.get("caption") or key
    inp = {
        "text": text, "channelId": find_channel(), "schedulingType": "automatic",
        "assets": [{"video": {"url": video_url, "metadata": {"thumbnailOffset": 1000}}}],
        "metadata": {"instagram": {"type": "reel", "shouldShareToFeed": True}},
    }
    if schedule:
        due = next_slot()
        inp.update(mode="customScheduled", dueAt=due.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z"))
    else:
        inp.update(mode="addToQueue", saveToDraft=True)
    q = ("mutation($i: CreatePostInput!) { createPost(input: $i) { "
         "... on PostActionSuccess { post { id status dueAt } } ... on MutationError { message } } }")
    res = gql(q, {"i": inp})["createPost"]
    if "post" not in res:
        raise SystemExit(f"FAILED {key}: {res.get('message')}")
    post = res["post"]
    reels[key] = {"buffer_post_id": post["id"], "status": "scheduled" if schedule else "draft",
                  "due_at": post.get("dueAt"), "video_url": video_url,
                  "created_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
    reels = dict(sorted(reels.items(), key=lambda kv: sort_key(kv[0])))
    gh_put("reels.json", reels, sha, f"Reels: {key} {reels[key]['status']}")
    print(f"OK {key} {reels[key]['status']} {post.get('dueAt') or ''} post={post['id']}")


def cmd_channels():
    orgs = gql("query { account { organizations { id name } } }")["account"]["organizations"]
    for o in orgs:
        chs = gql("query($o: OrganizationId!) { channels(input: {organizationId: $o}) { id name service isQueuePaused } }",
                  {"o": o["id"]})["channels"]
        print(json.dumps({"organization": o, "channels": chs}, ensure_ascii=False))


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        print(__doc__)
    elif a[0] == "todo":
        cmd_todo(a[1], a[2] if len(a) > 2 else None)
    elif a[0] == "meta":
        cmd_meta(a[1], a[2], a[3])
    elif a[0] == "post":
        cmd_post(a[1:])
    elif a[0] == "channels":
        cmd_channels()
    else:
        print(__doc__)
