"""Upload a finished episode to YouTube and set its thumbnail.

Needs the GitHub secrets CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN as environment variables.

VISIBILITY decides how the video goes up:
  private  (default) only you can see it
  public   public right away
  schedule private now, goes public by itself at the next 00:00 or 12:00 Japan time
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


JST = timezone(timedelta(hours=9))
SLOTS_JST = (0, 12)  # publish times, hour of day in Japan time


def next_slot(now=None):
    """Next 00:00 / 12:00 JST at least 15 minutes from now, or None if the run is late."""
    now = now or datetime.now(timezone.utc)
    earliest = (now + timedelta(minutes=15)).astimezone(JST)
    for day in range(2):
        for hour in SLOTS_JST:
            slot = (earliest + timedelta(days=day)).replace(hour=hour, minute=0, second=0, microsecond=0)
            if slot >= earliest:
                # Scheduled runs start about 3 hours before a slot. A gap of more than
                # 6 hours means this run missed its slot, so publish right away instead.
                return slot if slot - now <= timedelta(hours=6) else None
    return None


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


def upload(num, video, thumbnail, visibility=None):
    visibility = visibility or os.environ.get("VISIBILITY") or "private"
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
            "privacyStatus": "public" if visibility == "public" else "private",
            "selfDeclaredMadeForKids": False,
            "containsSyntheticMedia": True,
        },
    }
    if visibility == "schedule":
        slot = next_slot()
        if slot:
            body["status"]["publishAt"] = slot.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            print(f"  goes public at {slot:%Y-%m-%d %H:%M} JST", flush=True)
        else:
            body["status"]["privacyStatus"] = "public"
            print("  run is late for its slot, publishing now", flush=True)
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
    return vid


def update_thumbnail(num):
    """Replace the thumbnail of an already uploaded episode."""
    pub = json.load(open(os.path.join(ROOT, "published.json")))
    vid = pub[str(num)]["video_id"]
    thumb = os.path.join(ROOT, "output", f"ep{num:02d}", f"ep{num:02d}_thumbnail.jpg")
    youtube().thumbnails().set(videoId=vid, media_body=MediaFileUpload(thumb, mimetype="image/jpeg")).execute()
    print(f"  thumbnail updated for EP {num:02d} ({vid})", flush=True)
    return vid


if __name__ == "__main__":
    if sys.argv[1] == "thumb":
        for n in sys.argv[2:]:
            update_thumbnail(int(n))
        sys.exit(0)
    n = int(sys.argv[1])
    d = os.path.join(ROOT, "output", f"ep{n:02d}")
    print(upload(n, os.path.join(d, f"ep{n:02d}.mp4"), os.path.join(d, f"ep{n:02d}_thumbnail.jpg")))
