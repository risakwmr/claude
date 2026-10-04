"""Build the "Start here" channel trailer: how Sena found Daniel and Human Curriculum began.

Script:  episodes/trailer/trailer.txt (+ trailer.ja.txt for Japanese captions)
Visuals: episodes/trailer/trailer.visual.json (same cue format as episodes, see src/scenes.py)

python src/make_trailer.py               real voices (GitHub Actions)
python src/make_trailer.py --fake-tts    placeholder tones, for checking the visuals
python src/make_trailer.py --upload      also upload to YouTube as PRIVATE (review it, then make it public
                                         and set it as the channel trailer in YouTube Studio)

It reuses the episode renderer, with a "START HERE" tag instead of an episode number. The last board shows
the Episode 1 cover.
"""
import argparse
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_episode as me  # noqa: E402
import render as r  # noqa: E402
import scenes  # noqa: E402
from PIL import ImageDraw  # noqa: E402

ROOT = me.ROOT
DIR = os.path.join(ROOT, "episodes", "trailer")
TITLE = "How Sena Found Her Mentor"
YT_TITLE = "Start Here: How Sena Found Her Mentor | Human Curriculum English Podcast"
COVER_EP = 1  # the cover board shows this episode's thumbnail


def load_trailer(_num):
    meta = json.load(open(os.path.join(ROOT, "episodes", "episodes.json"), encoding="utf-8"))
    ep = {"number": COVER_EP, "script": "trailer/trailer.txt", "title": TITLE, "short_title": TITLE}
    lines = []
    for raw in open(os.path.join(DIR, "trailer.txt"), encoding="utf-8"):
        m = re.match(r"^\s*(SENA|DANIEL)\s*:\s*(.+?)\s*$", raw)
        if m:
            lines.append((m.group(1), m.group(2)))
    return meta, ep, lines


def trailer_base(ep_num, ep_title):
    """The episode frame header, with START HERE in place of the episode number."""
    img = r.paper(r.W, r.H).convert("RGBA")
    for box, color, seed, a in (((1180, -40, 820, 300), r.BLUE, 1, 120), ((1380, 170, 600, 120), r.CORAL, 2, 150),
                                ((-80, 860, 760, 260), r.BLUE, 3, 70), ((-60, 1000, 640, 90), r.CORAL, 4, 110)):
        img.alpha_composite(r.brush(box[2:], color, seed, alpha=a), (box[0], box[1]))
    d = ImageDraw.Draw(img)
    r.spaced(d, (82, 52), "THE", r.sans(22, "SemiBold"), r.NAVY, spacing=6)
    d.text((78, 76), "Human Curriculum", font=r.serif(56, "Bold"), fill=r.NAVY)
    tag = "START HERE"
    tf = r.sans(24, "SemiBold")
    tw = r.spaced_width(tag, tf, 5)
    x1 = r.W - 90
    d.rectangle((x1 - tw - 44, 58, x1, 104), fill=r.CORAL)
    r.spaced(d, (x1 - tw - 22, 66), tag, tf, (255, 255, 255), spacing=5)
    d.text((x1, 124), TITLE, font=r.serif(34, "SemiBold"), fill=r.NAVY, anchor="ra")
    d.text((x1, 180), "Tokyo → Seattle", font=r.hand(40), fill=r.NAVY, anchor="ra")
    return img


def build(fake=False, out_dir=None):
    os.environ["NO_VOICE_FALLBACK"] = "1"  # the trailer must sound exactly like the episodes
    me.load_episode = load_trailer
    scenes.visual_path = lambda num: os.path.join(DIR, "trailer.visual.json")
    r.scene_base = trailer_base
    out_dir = out_dir or os.path.join(ROOT, "output", "trailer")
    try:  # free illustrations used by the cues
        import fetch_icons
        names = set()
        for c in scenes.load_cues(0):
            board = c.get("board") or {}
            names |= {board["icon"]} if board.get("icon") else set()
            names |= set(board.get("icons") or [])
        fetch_icons.fetch(names)
    except Exception as e:
        print(f"  illustrations skipped: {e}", flush=True)
    res = me.build(COVER_EP, fake=fake, out_dir=out_dir)
    # name the files after the trailer (the renderer names them after the cover episode)
    final = {}
    for key in ("video", "srt", "ja_srt"):
        p = res.get(key)
        if p and os.path.exists(p):
            new = os.path.join(out_dir, os.path.basename(p).replace(f"ep{COVER_EP:02d}", "trailer"))
            shutil.move(p, new)
            final[key] = new
    final["duration"] = res["duration"]
    print(json.dumps(final, indent=2), flush=True)
    return final


def upload(files):
    import upload as up
    from googleapiclient.http import MediaFileUpload
    yt = up.youtube()
    body = {
        "snippet": {
            "title": YT_TITLE,
            "description": "\n".join([
                "If AI can do your job, what's left for you?",
                "Sena, an Associate in Tokyo, wants to lead people in the US. So she finds a mentor in Seattle. "
                "This is how Human Curriculum began.",
                "",
                "▶ Start with Episode 1, and grow with Sena, one episode at a time.",
                "",
                "Human Curriculum | Learn what AI can't do, in natural English. Real situations, real research, and "
                "one challenge you can try at work today.",
                "Sena and Daniel are fictional characters. Their voices are AI-generated.",
                "",
                "#EnglishPodcast #EQ #CareerGrowth",
            ]),
            "tags": ["English podcast", "EQ", "career", "leadership", "people manager", "English learning", "audiobook"],
            "categoryId": "27",
            "defaultLanguage": "en",
            "defaultAudioLanguage": "en",
        },
        "status": {"privacyStatus": "private", "selfDeclaredMadeForKids": False, "containsSyntheticMedia": True},
    }
    resp = up._send(yt, body, files["video"])
    vid = resp["id"]
    if files.get("ja_srt"):
        up.add_japanese_captions(yt, vid, files["ja_srt"])
    json.dump({"video_id": vid, "privacy": "private"}, open(os.path.join(ROOT, "trailer.json"), "w"), indent=2)
    up.note_status("trailer", f"ok {vid} (private)")
    print(f"Trailer uploaded as private: https://youtu.be/{vid}", flush=True)
    return vid


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--fake-tts", action="store_true")
    ap.add_argument("--out")
    ap.add_argument("--upload", action="store_true")
    a = ap.parse_args()
    files = build(a.fake_tts, a.out)
    if a.upload:
        try:
            upload(files)
        except Exception as e:  # keep the reason (saved with run_status.json); the video is still in output/trailer
            import upload as up
            detail = str(e)[:500]
            up.note_status("trailer", f"ERROR {type(e).__name__}: {detail}")
            print(f"Trailer upload failed: {detail}", flush=True)
            sys.exit(75 if "uploadLimitExceeded" in detail else 1)
