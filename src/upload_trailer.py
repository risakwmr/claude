"""Upload the finished "Start here" trailer (made outside this repo) as PRIVATE, with its thumbnail.

Files: episodes/trailer/final/trailer.mp4 and trailer_thumbnail.jpg
Review it in YouTube Studio, set the end screen, then make it public.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_trailer as mt  # noqa: E402
import upload as up  # noqa: E402
from googleapiclient.http import MediaFileUpload  # noqa: E402

FINAL = os.path.join(mt.DIR, "final")

if __name__ == "__main__":
    video = os.path.join(FINAL, "trailer.mp4")
    thumb = os.path.join(FINAL, "trailer_thumbnail.jpg")
    try:
        vid = mt.upload({"video": video})
    except Exception as e:
        detail = str(e)[:500]
        up.note_status("trailer", f"ERROR {type(e).__name__}: {detail}")
        print(f"Trailer upload failed: {detail}", flush=True)
        sys.exit(75 if "uploadLimitExceeded" in detail else 1)
    yt = up.youtube()
    try:
        yt.thumbnails().set(videoId=vid, media_body=MediaFileUpload(thumb, mimetype="image/jpeg")).execute()
        print("thumbnail set", flush=True)
    except Exception as e:
        print(f"WARNING: thumbnail not set ({str(e)[:200]}); set it in YouTube Studio", flush=True)
    print(f"https://youtu.be/{vid}", flush=True)
