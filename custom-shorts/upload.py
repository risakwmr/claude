"""Upload one hand-made Short from custom-shorts/ to YouTube.

Usage: python custom-shorts/upload.py NAME VISIBILITY SLOT_HOUR_JST
  NAME           custom-shorts/NAME.mp4 and custom-shorts/NAME.json (title, description, tags)
  VISIBILITY     schedule (private now, public at the next SLOT_HOUR_JST), public, or private
  SLOT_HOUR_JST  8, 18 or 22 (same slots as the automatic Shorts: US evening / Asia afternoon / US morning)

Needs CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN (same GitHub secrets as the episode uploads).
Records the result in custom-shorts/uploaded.json so the same file is not uploaded twice.
"""
import json
import os
import sys
import time
from datetime import datetime, timedelta, timezone

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

HERE = os.path.dirname(os.path.abspath(__file__))
JST = timezone(timedelta(hours=9))


def next_slot(hour, now=None):
    now = now or datetime.now(timezone.utc)
    earliest = (now + timedelta(minutes=30)).astimezone(JST)
    slot = earliest.replace(hour=hour, minute=0, second=0, microsecond=0)
    if slot < earliest:
        slot += timedelta(days=1)
    return slot


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


def send(yt, body, video):
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


def main():
    name, visibility, hour = sys.argv[1], sys.argv[2], int(sys.argv[3])
    video = os.path.join(HERE, f"{name}.mp4")
    meta = json.load(open(os.path.join(HERE, f"{name}.json"), encoding="utf-8"))
    log_path = os.path.join(HERE, "uploaded.json")
    log = json.load(open(log_path)) if os.path.exists(log_path) else {}
    if name in log:
        sys.exit(f"{name} was already uploaded: https://youtube.com/shorts/{log[name]['video_id']}")

    body = {
        "snippet": {
            "title": meta["title"][:100],
            "description": meta["description"][:4900],
            "tags": meta.get("tags", []),
            "categoryId": "27",  # Education
            "defaultLanguage": "en",
            "defaultAudioLanguage": "en",
        },
        "status": {
            "privacyStatus": "public" if visibility == "public" else "private",
            "selfDeclaredMadeForKids": False,
            "containsSyntheticMedia": True,  # same as the episodes (AI voices / generated art)
        },
    }
    when = ""
    if visibility == "schedule":
        slot = next_slot(hour)
        body["status"]["publishAt"] = slot.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        when = f"{slot:%Y-%m-%d %H:%M} JST"
        print(f"  goes public at {when}", flush=True)

    yt = youtube()
    try:
        resp = send(yt, body, video)
    except HttpError as e:
        if e.resp.status == 400 and "containsSyntheticMedia" in str(e):
            body["status"].pop("containsSyntheticMedia")
            resp = send(yt, body, video)
        else:
            raise
    vid = resp["id"]
    log[name] = {"video_id": vid, "visibility": visibility, "publish_at": when,
                 "uploaded_at": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    json.dump(log, open(log_path, "w"), indent=2)
    print(f"https://youtube.com/shorts/{vid}  (publish: {when or visibility})")


if __name__ == "__main__":
    main()
