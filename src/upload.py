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


def description(meta, ep):
    lines = [
        ep["summary"],
        "",
        f"This week's practice: {ep['practice']}",
        "",
        "Research mentioned in this episode:",
        *[f"- {s}" for s in ep["sources"]],
        "",
        f"{meta['show']} is an audiobook about the human skills AI can't do for you, and about growing your EQ. "
        "Sena, an Associate in Tokyo, learns from her mentor Daniel, a People Manager in Seattle.",
        "",
        "Sena and Daniel are fictional characters. Their voices are AI-generated.",
        "",
        "#EQ #EmotionalIntelligence #Leadership #CareerGrowth #HumanCurriculum",
    ]
    return "\n".join(lines)[:4900]


def _send(yt, body, video):
    media = MediaFileUpload(video, mimetype="video/mp4", chunksize=8 * 1024 * 1024, resumable=True)
    req = yt.videos().insert(part="snippet,status", body=body, media_body=media)
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
    title = f"EP {num:02d} | {ep['title']} | {meta['show']}"
    if len(title) > 100:
        title = f"EP {num:02d} | {ep['title']}"[:100]
    yt = youtube()
    body = {
        "snippet": {
            "title": title,
            "description": description(meta, ep),
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
    ja_srt = os.path.join(os.path.dirname(video), f"ep{num:02d}.ja.srt")
    if os.path.exists(ja_srt):
        add_japanese_captions(yt, vid, ja_srt)
    return vid


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
        return True
    except HttpError as e:
        print(f"  WARNING: Japanese captions not added ({e.resp.status}). If this is 403, create a new "
              "refresh token that includes the https://www.googleapis.com/auth/youtube.force-ssl scope. "
              f"{str(e)[:300]}", flush=True)
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
    if sys.argv[1] == "captions":
        captions([int(n) for n in sys.argv[2:]])
        sys.exit(0)
    if sys.argv[1] == "publish":
        publish_now([int(n) for n in sys.argv[2:]])
        sys.exit(0)
    if sys.argv[1] == "thumb":
        for n in sys.argv[2:]:
            update_thumbnail(int(n))
        sys.exit(0)
    n = int(sys.argv[1])
    d = os.path.join(ROOT, "output", f"ep{n:02d}")
    print(upload(n, os.path.join(d, f"ep{n:02d}.mp4"), os.path.join(d, f"ep{n:02d}_thumbnail.jpg")))
