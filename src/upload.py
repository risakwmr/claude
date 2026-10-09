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
                record_short_by_title(item)
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


def record_short_by_title(item):
    """A Short on the channel that shorts.json doesn't know: find which episode/kind it is by its title."""
    import shorts
    import make_short
    import make_episode
    data = shorts.load_shorts()
    if any(v["video_id"] == item["id"] for v in data.values()):
        return
    title = item["snippet"]["title"]
    meta = json.load(open(os.path.join(ROOT, "episodes", "episodes.json"), encoding="utf-8"))
    for ep in meta["episodes"]:
        n = ep["number"]
        try:
            _, _, lines = make_episode.load_episode(n)
            specs = make_short.specs(n, ep, lines)
        except Exception:
            continue
        for kind, spec in specs.items():
            if short_title(spec["title"]) == title and shorts.key(n, kind) not in data:
                st = item["status"]
                when = (st.get("publishAt") or item["snippet"]["publishedAt"]).replace(".000Z", "Z")
                shorts.record(n, kind, item["id"], when)
                print(f"  recorded Short {n}-{kind}: {item['id']}", flush=True)
                return


def video_title(meta, ep, num):
    """The viewer's problem first, in plain words (yt_title); "Business English Podcast" and the episode number at the end.

    "Business English" is what the audience (people who work in English) searches for, and what the episodes are.

    Popular channels put the topic in the first ~40 characters (mobile and search cut titles at about 70)."""
    main = ep.get("yt_title") or ep["title"]
    title = f"{main} | Business English Podcast EP{num:02d}"
    if len(title) > 100:
        title = f"{main[:88]} | EP{num:02d}"
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
    # The first two lines are all most viewers see before "more": a relatable question, then the promise.
    hook = ep.get("hook_ja") or ep.get("summary_ja", "")
    points = ep.get("points_ja") or []
    phrases = speaking_phrases(ep)
    nxt = next_title_ja(meta, num)
    pid = json.load(open(PLAYLIST_FILE))["id"] if os.path.exists(PLAYLIST_FILE) else None
    lines = [hook, ""]
    if points:
        lines += ["📌 この回でわかること", *[f"・{p}" for p in points], ""]
    if phrases:
        lines += ["🗣 今日の英語フレーズ（声に出してみよう）"]
        for en, ja in phrases:
            lines += [en, f"→ {ja}" if ja else ""]
        lines += [""]
    lines += ["✅ 今日のチャレンジ", ep.get("practice_ja", ""), ""]
    if chapters:
        lines += ["⏱ 目次", chapters.strip(), ""]
    if nxt:
        lines += [f"▶ 次回 EP{num + 1:02d}「{nxt}」"]
    if pid:
        lines += [f"📚 全話を順番に聴く → https://www.youtube.com/playlist?list={pid}"]
    if nxt or pid:
        lines += [""]
    lines += [
        "📖 紹介した研究",
        *[f"- {x}" for x in ep["sources"]],
        "",
        "――",
        f"{meta['show']}｜AIにできない人間の力（EQ）を、英語で。",
        "東京で働くセナが、シアトルのメンター・ダニエルと一緒に、毎日少しずつ成長していく英語オーディオブックです。"
        "字幕（CC）で日本語訳を表示できます。",
        "※セナとダニエルは架空の人物で、声はAIです。",
        "イラスト：Fluent Emoji by Microsoft（MIT License）",
        "",
        "#英語学習 #EQ #キャリア",
    ]
    return {"ja": {"title": title, "description": "\n".join(lines)[:4900]}}


def speaking_phrases(ep):
    """Speaking Lab repeat sentences (a DANIEL line that is only a quote, then SENA saying it) with their Japanese."""
    import re
    if ep.get("phrases"):  # chosen by hand (episodes before the Speaking Lab)
        return [tuple(p) for p in ep["phrases"]][:3]
    path = os.path.join(ROOT, "episodes", ep["script"])
    ja_path = path[:-4] + ".ja.txt"
    if not os.path.exists(path):
        return []
    split = lambda f: [l.split(": ", 1) for l in open(f, encoding="utf-8").read().splitlines() if ": " in l]
    en = split(path)
    ja = split(ja_path) if os.path.exists(ja_path) else []
    norm = lambda s: re.sub(r"[^a-z0-9 ]", "", s.lower()).split()
    out = []
    for i, (spk, text) in enumerate(en[:-1]):
        t = text.strip()
        if spk == "DANIEL" and len(t) > 2 and t[0] in "\"“" and t[-1] in "\"”" \
                and en[i + 1][0] == "SENA" and norm(en[i + 1][1]) == norm(t[1:-1]):
            j = ja[i][1].strip().strip("「」『』\"") if len(ja) == len(en) else ""
            out.append((t[1:-1].strip(), j))
    return out[:3]


def next_title_ja(meta, num):
    nxt = next((e for e in meta["episodes"] if e["number"] == num + 1), None)
    if nxt:
        return nxt.get("title_ja") or nxt["title"]
    import re
    plan = os.path.join(ROOT, "episodes", "plan.md")
    for line in open(plan, encoding="utf-8") if os.path.exists(plan) else []:
        m = re.match(rf"^{num + 1} (.+?) \|", line)
        if m:
            return m.group(1).strip()
    return None


def existing_chapters(text):
    import re
    lines = [l for l in (text or "").splitlines() if re.match(r"^\d+:\d\d \S", l)]
    return "\n".join(lines) if len(lines) >= 3 else None


def read_chapters(video, num):
    p = os.path.join(os.path.dirname(video), f"ep{num:02d}.chapters.txt")
    return open(p, encoding="utf-8").read() if os.path.exists(p) else None


def next_title_en(meta, num):
    nxt = next((e for e in meta["episodes"] if e["number"] == num + 1), None)
    if nxt:
        return nxt.get("yt_title") or nxt["title"]
    import re
    plan = os.path.join(ROOT, "episodes", "plan.md")
    for line in open(plan, encoding="utf-8") if os.path.exists(plan) else []:
        m = re.match(rf"^{num + 1} (.+?) \|", line)
        if m:
            return m.group(1).strip()
    return None


def description(meta, ep, chapters=None):
    """English description. The first two lines are all most viewers see before "more":
    a relatable situation, then what they'll learn (with the words people search for)."""
    num = ep["number"]
    hook = ep.get("hook") or ep["summary"]
    points = ep.get("points") or []
    phrases = speaking_phrases(ep)
    nxt = next_title_en(meta, num)
    pid = json.load(open(PLAYLIST_FILE))["id"] if os.path.exists(PLAYLIST_FILE) else None
    lines = [hook, ""]
    if points:
        lines += ["📌 In this episode", *[f"• {p}" for p in points], ""]
    if phrases:
        lines += ["🗣 Say it out loud: today's English phrases", *[f"• {en}" for en, _ in phrases], ""]
    lines += ["✅ Try it today", ep["practice"], ""]
    if chapters:
        lines += ["⏱ Chapters", chapters.strip(), ""]
    if nxt:
        lines += [f"▶ Next: EP{num + 1:02d} \"{nxt}\""]
    if pid:
        lines += [f"📚 All episodes in order → https://www.youtube.com/playlist?list={pid}"]
    if nxt or pid:
        lines += [""]
    lines += [
        "📖 Research mentioned in this episode",
        *[f"- {x}" for x in ep["sources"]],
        "",
        "――",
        f"{meta['show']} | Learn what AI can't do, in natural English.",
        "An English audio drama for people who work in global teams, or want to. Sena, an Associate in Tokyo, "
        "learns from her mentor Daniel, a People Manager in Seattle. Natural-speed English with captions, "
        "real research, and one challenge you can try at work today.",
        "Sena and Daniel are fictional characters. Their voices are AI-generated.",
        "Illustrations: Fluent Emoji by Microsoft (MIT License).",
        "",
        "#BusinessEnglish #EnglishListening #EnglishPodcast",
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
    for lang, name, suffix in CAPTION_TRACKS:
        srt = os.path.join(os.path.dirname(video), f"ep{num:02d}{suffix}")
        if os.path.exists(srt):
            try:
                add_captions(yt, vid, srt, lang, name)
            except QuotaExceeded:
                break
    return vid


def short_title(spec_title):
    title = f"{spec_title} #shorts"
    return title if len(title) <= 100 else f"{spec_title[:90].rstrip()}… #shorts"


def short_description(meta, ep, episode_vid):
    lines = [
        f"Full episode → https://youtu.be/{episode_vid}" if episode_vid else "Full episode on the channel.",
        "",
        f"From \"{ep.get('yt_title') or ep['title']}\", an episode of {meta['show']}: an English audiobook about the human skills "
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


def upload_short(num, kind="ai", publish_at=None):
    """Upload output/epNN/epNN_short_KIND.mp4 as a Short, link the full episode, and record it in shorts.json."""
    try:
        return _upload_short(num, kind, publish_at)
    except Exception as e:  # keep the reason in run_status.json, which every run saves
        detail = f"{e.resp.status} {str(e)[:600]}" if isinstance(e, HttpError) else f"{type(e).__name__}: {str(e)[:600]}"
        note_status(f"short:{num}-{kind}", f"ERROR {detail}")
        print(f"  ERROR uploading Short EP {num} {kind}: {detail}", flush=True)
        raise


def _upload_short(num, kind="ai", publish_at=None):
    import shorts
    publish_at = (publish_at if publish_at is not None else os.environ.get("PUBLISH_AT", "")).strip()
    meta = json.load(open(os.path.join(ROOT, "episodes", "episodes.json"), encoding="utf-8"))
    ep = next(e for e in meta["episodes"] if e["number"] == num)
    d = os.path.join(ROOT, "output", f"ep{num:02d}")
    info = json.load(open(os.path.join(d, f"ep{num:02d}_short_{kind}.json"), encoding="utf-8"))
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
    shorts.record(num, kind, vid, publish_at)
    note_status(f"short:{num}-{kind}", f"ok {vid}")
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
            and parse(v["publish_at"]) <= now and k.split("-")[0] in pub]
    if not todo:
        return
    yt = youtube()
    for k in todo:
        n = k.split("-")[0]
        ep = next(e for e in meta["episodes"] if e["number"] == int(n))
        try:
            yt.commentThreads().insert(part="snippet", body={"snippet": {
                "videoId": data[k]["video_id"],
                "topLevelComment": {"snippet": {
                    "textOriginal": f"Full episode: \"{ep.get('yt_title') or ep['title']}\" → https://youtu.be/{pub[n]['video_id']}"}},
            }}).execute()
            data[k]["commented"] = True
            print(f"  Short {k}: link comment added", flush=True)
        except HttpError as e:
            print(f"  Short {k}: link comment skipped ({e.resp.status})", flush=True)
            note_status(f"short-comment:{k}", f"{e.resp.status} {str(e)[:300]}")
            if e.resp.status == 403:  # comments turned off or not allowed: don't keep trying
                data[k]["commented"] = "skipped"
    shorts.save_shorts(data)


COMMENTS_FILE = os.path.join(ROOT, "comments.json")


def episode_question(ep):
    """The listener's 40-second question: from the Speaking Lab ("In forty seconds, answer this. ...?"),
    or the "question" field in episodes.json for episodes without one."""
    import re
    if ep.get("question"):
        return ep["question"]
    path = os.path.join(ROOT, "episodes", ep["script"])
    if not os.path.exists(path):
        return None
    for line in open(path, encoding="utf-8"):
        if line.startswith("DANIEL:") and re.search(r"(forty|40) seconds", line, re.I):
            text = re.split(r"answer this[.:]\s*", line, flags=re.I)[-1]
            qs = re.findall(r"[^.?!]*\?", text)
            if qs:
                return " ".join(q.strip() for q in qs)
    return None


def episode_comments():
    """Once an episode is public, post its "Your turn" question as a comment, so viewers answer below
    (pin it in YouTube Studio if you like). Each run catches up on episodes that went public. 50 quota units each."""
    from slot import parse
    pub = json.load(open(os.path.join(ROOT, "published.json")))
    meta = json.load(open(os.path.join(ROOT, "episodes", "episodes.json"), encoding="utf-8"))
    eps = {str(e["number"]): e for e in meta["episodes"]}
    done = json.load(open(COMMENTS_FILE)) if os.path.exists(COMMENTS_FILE) else {}
    now = datetime.now(timezone.utc)
    todo = [n for n, v in sorted(pub.items(), key=lambda kv: int(kv[0]))
            if n not in done and n in eps and v.get("publish_at") and parse(v["publish_at"]) <= now]
    if not todo:
        return
    yt = youtube()
    for n in todo:
        q = episode_question(eps[n])
        if not q:
            done[n] = "no question"
            continue
        text = (f"🗣 Your turn (40 seconds): {q}\n\n"
                "Pause, say your answer out loud, then write it here. Any level of English is welcome. 💬")
        try:
            r = yt.commentThreads().insert(part="snippet", body={"snippet": {
                "videoId": pub[n]["video_id"], "topLevelComment": {"snippet": {"textOriginal": text}}}}).execute()
            done[n] = r["id"]
            print(f"  EP {int(n):02d}: question comment added", flush=True)
        except HttpError as e:
            print(f"  EP {int(n):02d}: question comment skipped ({e.resp.status})", flush=True)
            note_status(f"episode-comment:{n}", f"{e.resp.status} {str(e)[:300]}")
            if "quotaExceeded" in str(e):
                break
            if e.resp.status == 403:  # comments turned off: don't keep trying
                done[n] = "skipped"
    json.dump(done, open(COMMENTS_FILE, "w"), indent=2, sort_keys=True)


def channel_setup():
    """Channel page: description (English, plus Japanese for viewers whose YouTube language is Japanese) and
    keywords from episodes/channel.json, and the show playlist marked as a podcast (with a square cover,
    assets/podcast_cover.jpg). The channel trailer is left as it is (set it in YouTube Studio)."""
    spec = json.load(open(os.path.join(ROOT, "episodes", "channel.json"), encoding="utf-8"))
    meta = json.load(open(os.path.join(ROOT, "episodes", "episodes.json"), encoding="utf-8"))
    yt = youtube()
    ch = yt.channels().list(part="snippet,brandingSettings,localizations", mine=True).execute()["items"][0]
    bs = ch.get("brandingSettings", {})  # send everything back: fields left out would be cleared
    c = bs.setdefault("channel", {})
    c["description"] = spec["description_en"][:1000]
    c["keywords"] = spec["keywords"]
    c["defaultLanguage"] = "en"
    steps = [
        ("channel-description", lambda: yt.channels().update(
            part="brandingSettings", body={"id": ch["id"], "brandingSettings": bs}).execute()),
    ]
    loc = ch.get("localizations", {})
    loc["ja"] = {"title": spec.get("title_ja") or ch["snippet"]["title"], "description": spec["description_ja"][:1000]}
    steps.append(("channel-ja", lambda: yt.channels().update(
        part="localizations", body={"id": ch["id"], "localizations": loc}).execute()))

    def podcast():
        pid = playlist_id(yt, meta)
        cover = os.path.join(ROOT, "assets", "podcast_cover.jpg")
        imgs = yt.playlistImages().list(part="snippet", parent=pid).execute().get("items", [])
        if not imgs:
            yt.playlistImages().insert(part="snippet", body={"snippet": {"playlistId": pid, "type": "hero"}},
                                       media_body=MediaFileUpload(cover, mimetype="image/jpeg")).execute()
            print("  playlist cover added", flush=True)
        pl = yt.playlists().list(part="snippet,status", id=pid).execute()["items"][0]
        snip = {k: pl["snippet"][k] for k in ("title", "defaultLanguage") if k in pl["snippet"]}
        snip["description"] = spec.get("playlist_description") or pl["snippet"].get("description", "")
        status = {"privacyStatus": pl["status"].get("privacyStatus", "public"), "podcastStatus": "enabled"}
        yt.playlists().update(part="snippet,status", body={"id": pid, "snippet": snip, "status": status}).execute()

    steps.append(("podcast", podcast))
    for key, fn in steps:
        try:
            fn()
            print(f"  {key}: ok", flush=True)
            note_status(key, "ok")
        except HttpError as e:
            print(f"  {key}: skipped ({e.resp.status}) {str(e)[:300]}", flush=True)
            note_status(key, f"{e.resp.status} {str(e)[:400]}")


def short_stats():
    """Views, likes and comments of every uploaded Short, saved to shorts_stats.json and summed up by kind.

    Retention ("viewed vs swiped away", average % viewed) is only in YouTube Studio's analytics."""
    import shorts
    data = shorts.load_shorts()
    yt = youtube()
    ids = {v["video_id"]: k for k, v in data.items()}
    rows = {}
    keys = list(ids)
    for i in range(0, len(keys), 50):
        r = yt.videos().list(part="statistics,snippet,status", id=",".join(keys[i:i + 50])).execute()
        for item in r.get("items", []):
            k = ids[item["id"]]
            st = item.get("statistics", {})
            rows[k] = {"video_id": item["id"], "title": item["snippet"]["title"],
                       "public": item["status"].get("privacyStatus") == "public",
                       "publish_at": data[k].get("publish_at"),
                       "views": int(st.get("viewCount", 0)), "likes": int(st.get("likeCount", 0)),
                       "comments": int(st.get("commentCount", 0))}
    # full episodes too, so title and description changes can be compared over time (git history keeps each run's numbers)
    pub = json.load(open(os.path.join(ROOT, "published.json")))
    eps = {v["video_id"]: k for k, v in pub.items()}
    ep_rows = {}
    ekeys = list(eps)
    for i in range(0, len(ekeys), 50):
        r = yt.videos().list(part="statistics,snippet", id=",".join(ekeys[i:i + 50])).execute()
        for item in r.get("items", []):
            st = item.get("statistics", {})
            ep_rows[eps[item["id"]]] = {"video_id": item["id"], "title": item["snippet"]["title"],
                                        "views": int(st.get("viewCount", 0)), "likes": int(st.get("likeCount", 0)),
                                        "comments": int(st.get("commentCount", 0))}
    ep_rows = dict(sorted(ep_rows.items(), key=lambda kv: int(kv[0])))
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    json.dump({"at": now, "shorts": rows, "episodes": ep_rows}, open(os.path.join(ROOT, "shorts_stats.json"), "w"),
              indent=2, ensure_ascii=False)
    by_kind = {}
    for k, row in rows.items():
        if row["public"]:
            kind = k.split("-", 1)[1]
            b = by_kind.setdefault(kind, [0, 0, 0])
            b[0] += 1
            b[1] += row["views"]
            b[2] += row["likes"]
    print(f"Shorts stats at {now}", flush=True)
    print("| Kind | Shorts | Views | Views per Short | Likes |\n| --- | --- | --- | --- | --- |")
    for kind, (n, v, l) in sorted(by_kind.items(), key=lambda kv: -kv[1][1] / kv[1][0]):
        print(f"| {kind} | {n} | {v} | {v / n:.1f} | {l} |")
    print("\n| Short | Views | Likes | Title |\n| --- | --- | --- | --- |")
    for k, row in sorted(rows.items(), key=lambda kv: -kv[1]["views"]):
        print(f"| {k} | {row['views']} | {row['likes']} | {row['title']} |")
    print("\n| Episode | Views | Likes | Title |\n| --- | --- | --- | --- |")
    for k, row in ep_rows.items():
        print(f"| {k} | {row['views']} | {row['likes']} | {row['title']} |")


STATUS_FILE = os.path.join(ROOT, "run_status.json")


def note_status(key, value):
    """Keep the last result of each action in run_status.json (saved with published.json)."""
    data = json.load(open(STATUS_FILE)) if os.path.exists(STATUS_FILE) else {}
    data[key] = {"at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "result": value}
    json.dump(data, open(STATUS_FILE, "w"), indent=2, ensure_ascii=False)


CAPTIONS_FILE = os.path.join(ROOT, "captions.json")
# language, track name, file suffix next to the video (epNN.ja.srt / epNN.srt)
CAPTION_TRACKS = (("ja", "日本語", ".ja.srt"), ("en", "English", ".srt"))


def caption_state():
    """{video_id: {"ja": "ok", "en": "ok"}}: which caption tracks are already up (captions.json).

    Seeded from run_status.json, where earlier runs recorded Japanese tracks as captions:<video_id> = ok."""
    data = json.load(open(CAPTIONS_FILE)) if os.path.exists(CAPTIONS_FILE) else {}
    if os.path.exists(STATUS_FILE):
        for k, v in json.load(open(STATUS_FILE)).items():
            if k.startswith("captions:") and v.get("result") == "ok":
                data.setdefault(k.split(":", 1)[1], {}).setdefault("ja", "ok")
    return data


def mark_caption(vid, lang):
    data = caption_state()
    data.setdefault(vid, {})[lang] = "ok"
    json.dump(data, open(CAPTIONS_FILE, "w"), indent=2, sort_keys=True)


class QuotaExceeded(Exception):
    pass


def add_captions(yt, vid, srt, lang="ja", name="日本語"):
    """Upload (or replace) one caption track. Needs the youtube.force-ssl scope. About 450 quota units."""
    label = "Japanese" if lang == "ja" else "English" if lang == "en" else lang
    try:
        old = yt.captions().list(part="snippet", videoId=vid).execute().get("items", [])
        for c in old:
            if c["snippet"].get("language") == lang and c["snippet"].get("trackKind") != "asr":
                yt.captions().delete(id=c["id"]).execute()
        yt.captions().insert(
            part="snippet",
            body={"snippet": {"videoId": vid, "language": lang, "name": name, "isDraft": False}},
            media_body=MediaFileUpload(srt, mimetype="application/octet-stream"),
        ).execute()
        print(f"  {label} captions added", flush=True)
        note_status(f"captions:{vid}" if lang == "ja" else f"captions-{lang}:{vid}", "ok")
        mark_caption(vid, lang)
        return True
    except HttpError as e:
        print(f"  WARNING: {label} captions not added ({e.resp.status}). If this is 403 insufficient scopes, create "
              "a new refresh token that includes https://www.googleapis.com/auth/youtube.force-ssl. "
              f"{str(e)[:300]}", flush=True)
        note_status(f"captions:{vid}" if lang == "ja" else f"captions-{lang}:{vid}", f"{e.resp.status} {str(e)[:400]}")
        if "quotaExceeded" in str(e):
            raise QuotaExceeded()
        return False


def add_japanese_captions(yt, vid, srt):
    return add_captions(yt, vid, srt, "ja", "日本語")


def missing_captions(nums=None):
    """(episode, lang) caption tracks not up yet, Japanese first (all episodes), then English, oldest first."""
    pub = json.load(open(os.path.join(ROOT, "published.json")))
    meta = json.load(open(os.path.join(ROOT, "episodes", "episodes.json"), encoding="utf-8"))
    eps = {e["number"]: e for e in meta["episodes"]}
    state = caption_state()
    nums = sorted(int(n) for n in (nums or pub) if str(n) in pub and int(n) in eps)
    out = []
    for lang, _, _ in CAPTION_TRACKS:
        for n in nums:
            if lang == "ja" and not os.path.exists(os.path.join(ROOT, "episodes", eps[n]["script"][:-4] + ".ja.txt")):
                continue
            if state.get(pub[str(n)]["video_id"], {}).get(lang) != "ok":
                out.append((n, lang))
    return out


def caption_todo(max_tracks):
    """Episode numbers that hold the next MAX_TRACKS missing caption tracks (to build their .srt files first)."""
    seen = []
    for n, _ in missing_captions()[:max_tracks]:
        if n not in seen:
            seen.append(n)
    print(" ".join(str(n) for n in seen))


def captions(nums, max_tracks=None):
    """Add the missing Japanese and English caption tracks to uploaded episodes
    (run make_episode.py N --audio-only first). At most CAPTION_MAX tracks per run (default 8, ~450 quota each);
    Japanese tracks go first. Stops quietly when the day's quota runs out; the rest go up in a later run."""
    max_tracks = max_tracks or int(os.environ.get("CAPTION_MAX") or 8)
    pub = json.load(open(os.path.join(ROOT, "published.json")))
    todo = missing_captions(nums)[:max_tracks]
    if not todo:
        print("  all caption tracks are up", flush=True)
        return
    yt = youtube()
    failed = 0
    for n, lang in todo:
        suffix = next(s for l, _, s in CAPTION_TRACKS if l == lang)
        name = next(nm for l, nm, _ in CAPTION_TRACKS if l == lang)
        srt = os.path.join(ROOT, "output", f"ep{n:02d}", f"ep{n:02d}{suffix}")
        if not os.path.exists(srt):
            print(f"  EP {n:02d} {lang}: no .srt (run make_episode.py {n} --audio-only first), skipped", flush=True)
            continue
        print(f"  EP {n:02d} ({lang}):", flush=True)
        try:
            if not add_captions(yt, pub[str(n)]["video_id"], srt, lang, name):
                failed += 1
        except QuotaExceeded:
            print("  YouTube's daily quota is used up; the remaining captions go up in a later run", flush=True)
            break
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
    if sys.argv[1] == "captions":  # captions [N ...]: missing tracks of these episodes (all when none given)
        captions([int(n) for n in sys.argv[2:]] or None)
        sys.exit(0)
    if sys.argv[1] == "caption-todo":  # caption-todo MAX_TRACKS: episodes to build .srt files for
        caption_todo(int(sys.argv[2]) if len(sys.argv) > 2 else 4)
        sys.exit(0)
    if sys.argv[1] == "publish":
        publish_now([int(n) for n in sys.argv[2:]])
        sys.exit(0)
    if sys.argv[1] == "short-stats":
        short_stats()
        sys.exit(0)
    if sys.argv[1] == "short-comments":
        comment_links()
        sys.exit(0)
    if sys.argv[1] == "channel":
        channel_setup()
        sys.exit(0)
    if sys.argv[1] == "episode-comments":
        episode_comments()
        sys.exit(0)
    if sys.argv[1] == "short":  # short EPISODE [KIND]
        try:
            print(upload_short(int(sys.argv[2]), sys.argv[3] if len(sys.argv) > 3 else "ai"))
        except HttpError as e:
            if "uploadLimitExceeded" in str(e):  # the channel's daily upload limit: try again in a later run
                sys.exit(75)
            raise
        sys.exit(0)
    if sys.argv[1] == "thumb":
        for n in sys.argv[2:]:
            update_thumbnail(int(n))
        sys.exit(0)
    n = int(sys.argv[1])
    d = os.path.join(ROOT, "output", f"ep{n:02d}")
    print(upload(n, os.path.join(d, f"ep{n:02d}.mp4"), os.path.join(d, f"ep{n:02d}_thumbnail.jpg")))
