"""Upload a finished episode to YouTube and set its thumbnail.

Needs the GitHub secrets CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN as environment variables.

PUBLISH_AT decides how the video goes up:
  empty                   private, only you can see it
  now                     public right away
  2026-10-08T03:00:00Z    private now, goes public by itself at that time (UTC)
"""
import json
import os
import sys
import time
from datetime import datetime, timedelta, timezone

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def youtube():
    creds = Credentials(
        token=None,
        refresh_token=os.environ["REFRESH_TOKEN"],
        client_id=os.environ["CLIENT_ID"],
        client_secret=os.environ["CLIENT_SECRET"],
        token_uri="https://oauth2.googleapis.com/token",
    )
    creds.refresh(Request())
    return build("youtube", "v3", credentials=creds, cache_discovery=False)


def sync_published():
    """Add uploaded episodes missing from published.json (e.g. when a run's git push failed).

    Reads the channel's uploads list (a few quota units) and matches episode numbers in titles."""
    import re
    path = os.path.join(ROOT, "published.json")
    pub = json.load(open(path)) if os.path.exists(path) else {}
    known = {v["video_id"] for v in pub.values()}
    shorts_path = os.path.join(ROOT, "shorts.json")
    if os.path.exists(shorts_path):  # Shorts are tracked separately
        known |= {v["video_id"] for v in json.load(open(shorts_path)).values()}
    yt = youtube()
    me = yt.channels().list(part="contentDetails,snippet", mine=True).execute()["items"][0]
    note_status("channel", f"{me['snippet']['title']} ({me['id']})")
    uploads = me["contentDetails"]["relatedPlaylists"]["uploads"]
    ids, token = [], None
    while True:
        r = yt.playlistItems().list(part="contentDetails", playlistId=uploads, maxResults=50,
                                    pageToken=token).execute()
        ids += [i["contentDetails"]["videoId"] for i in r.get("items", [])]
        token = r.get("nextPageToken")
        if not token:
            break
    new = [v for v in ids if v not in known]
    added = 0
    for i in range(0, len(new), 50):
        for item in yt.videos().list(part="snippet,status", id=",".join(new[i:i + 50])).execute().get("items", []):
            title = item["snippet"]["title"]
            if "#shorts" in title.lower():
                continue
            m = re.match(r"^EP\s*(\d+)\s*\|", title) or re.search(r"\bEP\s*(\d+)\s*$", title)
            if not m or str(int(m.group(1))) in pub:
                continue
            st = item["status"]
            when = st.get("publishAt") or item["snippet"]["publishedAt"]
            pub[str(int(m.group(1)))] = {"video_id": item["id"], "uploaded_at": item["snippet"]["publishedAt"],
                                         "publish_at": when.replace(".000Z", "Z")}
            print(f"  recorded EP {int(m.group(1)):02d}: {item['id']} (public at {when})", flush=True)
            added += 1
    pub = dict(sorted(pub.items(), key=lambda kv: int(kv[0])))
    json.dump(pub, open(path, "w"), indent=2)
    print(f"  published.json in sync ({added} added)", flush=True)


def video_title(meta, ep, num):
    """The episode title first; the show name and episode number at the end."""
    title = f"{ep['title']} | {meta['show']} EP{num:02d}"
    if len(title) > 100:
        title = f"{ep['title'][:90]} | EP{num:02d}"
    return title


PLAYLIST_FILE = os.path.join(ROOT, "playlist.json")


def playlist_id(yt, meta):
    """The show's playlist (all episodes in order), created on first use."""
    if os.path.exists(PLAYLIST_FILE):
        return json.load(open(PLAYLIST_FILE))["id"]
    body = {
        "snippet": {
            "title": f"{meta['show']} | All Episodes in Order",
            "description": f"Every episode of {meta['show']}, from episode 1. Listen in order and grow with Sena, "
                           "one episode at a time.",
            "defaultLanguage": "en",
        },
        "status": {"privacyStatus": "public"},
    }
    pid = yt.playlists().insert(part="snippet,status", body=body).execute()["id"]
    json.dump({"id": pid}, open(PLAYLIST_FILE, "w"), indent=2)
    print(f"  created playlist https://www.youtube.com/playlist?list={pid}", flush=True)
    return pid


def playlist_videos(yt, pid):
    ids, token = [], None
    while True:
        r = yt.playlistItems().list(part="contentDetails", playlistId=pid, maxResults=50, pageToken=token).execute()
        ids += [i["contentDetails"]["videoId"] for i in r.get("items", [])]
        token = r.get("nextPageToken")
        if not token:
            return ids


def add_to_playlist(yt, meta, vid, position=None):
    try:
        pid = playlist_id(yt, meta)
        try:
            present = playlist_videos(yt, pid)
        except HttpError as e:
            if e.resp.status != 404:  # a brand-new playlist can take a moment to appear
                raise
            time.sleep(5)
            present = []
        if vid in present:
            return
        snippet = {"playlistId": pid, "resourceId": {"kind": "youtube#video", "videoId": vid}}
        if position is not None:
            snippet["position"] = min(position, len(present))
        yt.playlistItems().insert(part="snippet", body={"snippet": snippet}).execute()
        print("  added to playlist", flush=True)
    except HttpError as e:
        print(f"  WARNING: not added to playlist ({e.resp.status}) {str(e)[:200]}", flush=True)
        note_status(f"playlist:{vid}", f"{e.resp.status} {str(e)[:400]}")


def organize(nums):
    """Update titles and descriptions of uploaded episodes and add them to the playlist, in this order."""
    meta = json.load(open(os.path.join(ROOT, "episodes", "episodes.json"), encoding="utf-8"))
    pub = json.load(open(os.path.join(ROOT, "published.json")))
    yt = youtube()
    for n in nums:
        ep = next(e for e in meta["episodes"] if e["number"] == n)
        vid = pub[str(n)]["video_id"]
        snip = yt.videos().list(part="snippet", id=vid).execute()["items"][0]["snippet"]
        chapters = existing_chapters(snip.get("description"))
        new = {k: snip[k] for k in ("categoryId", "tags", "defaultLanguage", "defaultAudioLanguage") if k in snip}
        new["title"] = video_title(meta, ep, n)
        new["description"] = description(meta, ep, chapters)
        new.setdefault("categoryId", "27")
        new.setdefault("defaultLanguage", "en")
        body = {"id": vid, "snippet": new}
        loc = localizations(meta, ep, n, chapters)
        if loc:
            body["localizations"] = loc
        yt.videos().update(part="snippet,localizations" if loc else "snippet", body=body).execute()
        print(f"  EP {n:02d}: {new['title']}", flush=True)
        note_status(f"organize:{n}", "ok")
        add_to_playlist(yt, meta, vid, position=n - 1)


def localizations(meta, ep, num, chapters=None):
    """Japanese title and description, shown to viewers whose YouTube language is Japanese."""
    if not ep.get("title_ja"):
        return None
    title = f"{ep['title_ja']} | {meta['show']} EP{num:02d}"
    if len(title) > 100:
        title = f"{ep['title_ja'][:90]} | EP{num:02d}"
    lines = [
        ep.get("summary_ja", ""),
        "",
        *([chapters.strip(), ""] if chapters else []),
        f"今日のチャレンジ：{ep.get('practice_ja', '')}",
        "",
        "この回で紹介した研究：",
        *[f"- {x}" for x in ep["sources"]],
        "",
        f"{meta['show']} は、AIにはできない人間の力とEQを、英語で学ぶオーディオブックです。"
        "東京のアソシエイト・セナが、シアトルのピープルマネージャー・ダニエルから学びます。"
        "字幕（CC）で日本語訳を表示できます。英語のリスニングとスピーキングの練習にもどうぞ。",
        "",
        "セナとダニエルは架空の人物で、声はAIで作っています。",
        "イラスト：Fluent Emoji by Microsoft（MIT License）",
        "",
        "#英語学習 #英語リスニング #EQ #キャリア #HumanCurriculum",
    ]
    return {"ja": {"title": title, "description": "\n".join(lines)[:4900]}}


def existing_chapters(text):
    import re
    lines = [l for l in (text or "").splitlines() if re.match(r"^\d+:\d\d \S", l)]
    return "\n".join(lines) if len(lines) >= 3 else None


def read_chapters(video, num):
    p = os.path.join(os.path.dirname(video), f"ep{num:02d}.chapters.txt")
    return open(p, encoding="utf-8").read() if os.path.exists(p) else None


def description(meta, ep, chapters=None):
    lines = [
        ep["summary"],
        "",
        *([chapters.strip(), ""] if chapters else []),
        f"Practice: {ep['practice']}",
        "",
        "Research mentioned in this episode:",
        *[f"- {s}" for s in ep["sources"]],
        "",
        f"{meta['show']} is an audiobook about the human skills AI can't do for you, and about growing your EQ. "
        "Sena, an Associate in Tokyo, learns from her mentor Daniel, a People Manager in Seattle.",
        "",
        "Sena and Daniel are fictional characters. Their voices are AI-generated.",
        "Illustrations: Fluent Emoji by Microsoft (MIT License).",
        "",
        "#EQ #EmotionalIntelligence #Leadership #CareerGrowth #HumanCurriculum",
    ]
    return "\n".join(lines)[:4900]


def _send(yt, body, video):
    media = MediaFileUpload(video, mimetype="video/mp4", chunksize=8 * 1024 * 1024, resumable=True)
    part = "snippet,status,localizations" if body.get("localizations") else "snippet,status"
    req = yt.videos().insert(part=part, body=body, media_body=media)
    resp, tries = None, 0
    while resp is None:
        try:
            status, resp = req.next_chunk()
            if status:
                print(f"  uploaded {int(status.progress() * 100)}%", flush=True)
        except HttpError as e:
            if e.resp.status in (500, 502, 503, 504) and tries < 5:
                tries += 1
                time.sleep(2 ** tries)
                continue
            raise
    return resp


def upload(num, video, thumbnail, publish_at=None):
    publish_at = (publish_at if publish_at is not None else os.environ.get("PUBLISH_AT", "")).strip()
    meta = json.load(open(os.path.join(ROOT, "episodes", "episodes.json"), encoding="utf-8"))
    ep = next(e for e in meta["episodes"] if e["number"] == num)
    title = video_title(meta, ep, num)
    yt = youtube()
    chapters = read_chapters(video, num)
    body = {
        "snippet": {
            "title": title,
            "description": description(meta, ep, chapters),
            "tags": ep.get("tags", []),
            "categoryId": "27",  # Education
            "defaultLanguage": "en",
            "defaultAudioLanguage": "en",
        },
        "status": {
            "privacyStatus": "public" if publish_at == "now" else "private",
            "selfDeclaredMadeForKids": False,
            "containsSyntheticMedia": True,
        },
    }
    loc = localizations(meta, ep, num, chapters)
    if loc:
        body["localizations"] = loc
    if publish_at and publish_at != "now":
        body["status"]["publishAt"] = publish_at
        print(f"  goes public at {publish_at} (UTC)", flush=True)
    try:
        resp = _send(yt, body, video)
    except HttpError as e:
        if e.resp.status == 400 and "containsSyntheticMedia" in str(e):
            body["status"].pop("containsSyntheticMedia")
            resp = _send(yt, body, video)
        elif e.resp.status == 400 and "invalidPublishAt" in str(e):
            body["status"].pop("publishAt")
            body["status"]["privacyStatus"] = "public"
            print("  schedule time rejected, publishing now", flush=True)
            resp = _send(yt, body, video)
        else:
            raise
    vid = resp["id"]
    print(f"  video id: {vid}", flush=True)
    try:
        yt.thumbnails().set(videoId=vid, media_body=MediaFileUpload(thumbnail, mimetype="image/jpeg")).execute()
        print("  thumbnail set", flush=True)
    except HttpError as e:
        print("  WARNING: thumbnail not set. Verify the channel's phone number at youtube.com/verify, "
              f"then set it in YouTube Studio. ({e.resp.status})", flush=True)
    add_to_playlist(yt, meta, vid)
    ja_srt = os.path.join(os.path.dirname(video), f"ep{num:02d}.ja.srt")
    if os.path.exists(ja_srt):
        add_japanese_captions(yt, vid, ja_srt)
    return vid


def short_title(spec_title):
    title = f"{spec_title} #shorts"
    return title if len(title) <= 100 else f"{spec_title[:90].rstrip()}… #shorts"


def short_description(meta, ep, episode_vid):
    lines = [
        f"Full episode → https://youtu.be/{episode_vid}" if episode_vid else "Full episode on the channel.",
        "",
        f"From \"{ep['title']}\", an episode of {meta['show']}: an English audiobook about the human skills "
        "AI can't do for you. Sena, an Associate in Tokyo, learns from her mentor Daniel, a People Manager in Seattle.",
        "",
        f"Try it today: {ep['practice']}",
        "",
        "Listen in natural-speed English and grow your EQ and your career at the same time.",
        "Sena and Daniel are fictional characters. Their voices are AI-generated.",
        "",
        "#shorts #EQ #EmotionalIntelligence #CareerGrowth #LearnEnglish #SoftSkills #HumanCurriculum",
    ]
    return "\n".join(lines)[:4900]


def upload_short(num, publish_at=None):
    """Upload output/epNN/epNN_short.mp4 as a Short, link the full episode, and record it in shorts.json."""
    import shorts
    publish_at = (publish_at if publish_at is not None else os.environ.get("PUBLISH_AT", "")).strip()
    meta = json.load(open(os.path.join(ROOT, "episodes", "episodes.json"), encoding="utf-8"))
    ep = next(e for e in meta["episodes"] if e["number"] == num)
    d = os.path.join(ROOT, "output", f"ep{num:02d}")
    info = json.load(open(os.path.join(d, f"ep{num:02d}_short.json"), encoding="utf-8"))
    pub = json.load(open(os.path.join(ROOT, "published.json")))
    episode_vid = pub.get(str(num), {}).get("video_id")
    yt = youtube()
    body = {
        "snippet": {
            "title": short_title(info["title"]),
            "description": short_description(meta, ep, episode_vid),
            "tags": ["shorts"] + ep.get("tags", []),
            "categoryId": "27",
            "defaultLanguage": "en",
            "defaultAudioLanguage": "en",
        },
        "status": {
            "privacyStatus": "public" if publish_at == "now" else "private",
            "selfDeclaredMadeForKids": False,
            "containsSyntheticMedia": True,
        },
    }
    loc = localizations(meta, ep, num, chapters)
    if loc:
        body["localizations"] = loc
    if publish_at and publish_at != "now":
        body["status"]["publishAt"] = publish_at
        print(f"  Short goes public at {publish_at} (UTC)", flush=True)
    try:
        resp = _send(yt, body, info["video"])
    except HttpError as e:
        if e.resp.status == 400 and "containsSyntheticMedia" in str(e):
            body["status"].pop("containsSyntheticMedia")
            resp = _send(yt, body, info["video"])
        elif e.resp.status == 400 and "invalidPublishAt" in str(e):
            body["status"].pop("publishAt")
            body["status"]["privacyStatus"] = "public"
            publish_at = "now"
            resp = _send(yt, body, info["video"])
        else:
            raise
    vid = resp["id"]
    shorts.record(num, vid, publish_at)
    note_status(f"short:{num}", f"ok {vid}")
    print(f"  Short id: {vid}", flush=True)
    return vid


def comment_links():
    """Once a Short is public, leave a comment with the full-episode link (pin it in YouTube Studio if you like).

    Comments can't be added while a Short is still private, so each run catches up on the ones that went public."""
    import shorts
    from slot import parse
    data = shorts.load_shorts()
    pub = json.load(open(os.path.join(ROOT, "published.json")))
    meta = json.load(open(os.path.join(ROOT, "episodes", "episodes.json"), encoding="utf-8"))
    now = datetime.now(timezone.utc)
    todo = [k for k, v in data.items() if not v.get("commented") and v.get("publish_at")
            and parse(v["publish_at"]) <= now and k in pub]
    if not todo:
        return
    yt = youtube()
    for k in todo:
        ep = next(e for e in meta["episodes"] if e["number"] == int(k))
        try:
            yt.commentThreads().insert(part="snippet", body={"snippet": {
                "videoId": data[k]["video_id"],
                "topLevelComment": {"snippet": {
                    "textOriginal": f"Full episode: \"{ep['title']}\" → https://youtu.be/{pub[k]['video_id']}"}},
            }}).execute()
            data[k]["commented"] = True
            print(f"  Short for EP {int(k):02d}: link comment added", flush=True)
        except HttpError as e:
            print(f"  Short for EP {int(k):02d}: link comment skipped ({e.resp.status})", flush=True)
            note_status(f"short-comment:{k}", f"{e.resp.status} {str(e)[:300]}")
            if e.resp.status == 403:  # comments turned off or not allowed: don't keep trying
                data[k]["commented"] = "skipped"
    json.dump(data, open(shorts.SHORTS_FILE, "w"), indent=2)


STATUS_FILE = os.path.join(ROOT, "run_status.json")


def note_status(key, value):
    """Keep the last result of each action in run_status.json (saved with published.json)."""
    data = json.load(open(STATUS_FILE)) if os.path.exists(STATUS_FILE) else {}
    data[key] = {"at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "result": value}
    json.dump(data, open(STATUS_FILE, "w"), indent=2, ensure_ascii=False)


def add_japanese_captions(yt, vid, srt):
    """Upload (or replace) the Japanese caption track. Needs the youtube.force-ssl scope."""
    try:
        old = yt.captions().list(part="snippet", videoId=vid).execute().get("items", [])
        for c in old:
            if c["snippet"].get("language") == "ja" and c["snippet"].get("trackKind") != "asr":
                yt.captions().delete(id=c["id"]).execute()
        yt.captions().insert(
            part="snippet",
            body={"snippet": {"videoId": vid, "language": "ja", "name": "日本語", "isDraft": False}},
            media_body=MediaFileUpload(srt, mimetype="application/octet-stream"),
        ).execute()
        print("  Japanese captions added", flush=True)
        note_status(f"captions:{vid}", "ok")
        return True
    except HttpError as e:
        print(f"  WARNING: Japanese captions not added ({e.resp.status}). If this is 403, create a new "
              "refresh token that includes the https://www.googleapis.com/auth/youtube.force-ssl scope. "
              f"{str(e)[:300]}", flush=True)
        note_status(f"captions:{vid}", f"{e.resp.status} {str(e)[:400]}")
        return False


def captions(nums):
    """Add Japanese captions to already uploaded episodes (run make_episode.py N --audio-only first)."""
    pub = json.load(open(os.path.join(ROOT, "published.json")))
    yt = youtube()
    failed = 0
    for n in nums:
        srt = os.path.join(ROOT, "output", f"ep{n:02d}", f"ep{n:02d}.ja.srt")
        if not os.path.exists(srt):
            print(f"  EP {n:02d}: no Japanese translation yet, skipped", flush=True)
            continue
        print(f"  EP {n:02d}:", flush=True)
        if not add_japanese_captions(yt, pub[str(n)]["video_id"], srt):
            failed += 1
    if failed:
        sys.exit(1)


def reschedule(nums):
    """Give already uploaded private episodes publish times, one per free slot, in this order."""
    from slot import fmt, next_free

    pub = json.load(open(os.path.join(ROOT, "published.json")))
    keys = [str(n) for n in nums]
    slot, _ = next_free(datetime.now(timezone.utc), pub, skip=keys)
    yt = youtube()
    for k in keys:
        vid = pub[k]["video_id"]
        status = yt.videos().list(part="status", id=vid).execute()["items"][0]["status"]
        if status.get("privacyStatus") == "public":
            print(f"  EP {int(k):02d} is already public, skipped", flush=True)
            continue
        new = {key: status[key] for key in ("embeddable", "license", "publicStatsViewable",
                                            "selfDeclaredMadeForKids", "containsSyntheticMedia") if key in status}
        new.update(privacyStatus="private", publishAt=fmt(slot))
        yt.videos().update(part="status", body={"id": vid, "status": new}).execute()
        pub[k]["publish_at"] = fmt(slot)
        print(f"  EP {int(k):02d} goes public at {slot:%m/%d %H:%M} JST", flush=True)
        slot += timedelta(hours=12)
    json.dump(pub, open(os.path.join(ROOT, "published.json"), "w"), indent=2)


def publish_now(nums):
    """Make already uploaded episodes public right away (also cancels their scheduled time)."""
    pub = json.load(open(os.path.join(ROOT, "published.json")))
    yt = youtube()
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    for n in nums:
        k = str(n)
        vid = pub[k]["video_id"]
        status = yt.videos().list(part="status", id=vid).execute()["items"][0]["status"]
        if status.get("privacyStatus") == "public":
            print(f"  EP {n:02d} is already public, skipped", flush=True)
        else:
            new = {key: status[key] for key in ("embeddable", "license", "publicStatsViewable",
                                                "selfDeclaredMadeForKids", "containsSyntheticMedia") if key in status}
            new["privacyStatus"] = "public"
            yt.videos().update(part="status", body={"id": vid, "status": new}).execute()
            print(f"  EP {n:02d} is now public: https://youtu.be/{vid}", flush=True)
        pub[k]["publish_at"] = min(pub[k].get("publish_at") or now, now)
    json.dump(pub, open(os.path.join(ROOT, "published.json"), "w"), indent=2)


def update_thumbnail(num):
    """Replace the thumbnail of an already uploaded episode."""
    pub = json.load(open(os.path.join(ROOT, "published.json")))
    vid = pub[str(num)]["video_id"]
    thumb = os.path.join(ROOT, "output", f"ep{num:02d}", f"ep{num:02d}_thumbnail.jpg")
    youtube().thumbnails().set(videoId=vid, media_body=MediaFileUpload(thumb, mimetype="image/jpeg")).execute()
    print(f"  thumbnail updated for EP {num:02d} ({vid})", flush=True)
    return vid


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    if sys.argv[1] == "reschedule":
        reschedule([int(n) for n in sys.argv[2:]])
        sys.exit(0)
    if sys.argv[1] == "sync":
        sync_published()
        sys.exit(0)
    if sys.argv[1] == "organize":
        organize([int(n) for n in sys.argv[2:]])
        sys.exit(0)
    if sys.argv[1] == "captions":
        captions([int(n) for n in sys.argv[2:]])
        sys.exit(0)
    if sys.argv[1] == "publish":
        publish_now([int(n) for n in sys.argv[2:]])
        sys.exit(0)
    if sys.argv[1] == "short-comments":
        comment_links()
        sys.exit(0)
    if sys.argv[1] == "short":
        for n in sys.argv[2:]:
            print(upload_short(int(n)))
        sys.exit(0)
    if sys.argv[1] == "thumb":
        for n in sys.argv[2:]:
            update_thumbnail(int(n))
        sys.exit(0)
    n = int(sys.argv[1])
    d = os.path.join(ROOT, "output", f"ep{n:02d}")
    print(upload(n, os.path.join(d, f"ep{n:02d}.mp4"), os.path.join(d, f"ep{n:02d}_thumbnail.jpg")))
