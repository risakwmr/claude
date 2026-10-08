"""The YouTube representative: one place to hear from, and talk to, every automation around the channel.

python representative/main.py brief          listen to everything, run the agents, write today's brief
python representative/main.py ask            answer the question in $QUESTION
python representative/main.py command        run the /reply, /skip or /edit command in $QUESTION
python representative/main.py listen         no AI: save what the listeners heard (snapshot.json, pending_comments.json)
                                             for the Claude Code routine that reads it on the owner's Claude plan

Output for the GitHub issue goes to $OUT (default out.md).
"""
import os
import re
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import listeners as L  # noqa: E402

INBOX = os.path.join(L.REP_DIR, "inbox.json")
REPORTS = os.path.join(L.REP_DIR, "last_reports.json")
NUMBERS = os.path.join(L.REP_DIR, "last_numbers.json")
SENT = os.path.join(L.REP_DIR, "sent_replies.json")
PRON = os.path.join(L.REP_DIR, "pronunciation.json")
SNAPSHOT = os.path.join(L.REP_DIR, "snapshot.json")
PENDING = os.path.join(L.REP_DIR, "pending_comments.json")
THUMBS = os.path.join(L.REP_DIR, "thumbnails.json")
BRIEFS = os.path.join(L.REP_DIR, "briefs")
OUT = os.environ.get("OUT", "out.md")


def write_out(text):
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(text.strip() + "\n")
    print(text)


def load_inbox():
    return L.load(INBOX, {"next": 1, "items": {}})


def numbers(snap):
    ch = snap.get("channel") or {}
    return {"at": ch.get("stats_at"), "channel": ch.get("channel_totals"),
            "shorts": {k: [v.get("views"), v.get("likes")] for k, v in (ch.get("short_stats") or {}).items()},
            "episodes": {k: [v.get("views"), v.get("likes")] for k, v in (ch.get("episode_stats") or {}).items()}}


def brief():
    import agents
    snap = L.snapshot(with_comments=True)
    reports = agents.specialists(snap, L.load(NUMBERS, {}))

    # new reply drafts go to the inbox; they are posted only after the owner approves them
    inbox = load_inbox()
    new_drafts = 0
    comments = {c["id"]: c for c in (snap.get("audience") or {}).get("new", [])}
    for d in (reports.get("audience") or {}).get("comments", []):
        c = comments.get(d["id"])
        if not c or not d["reply"].strip() or d["category"] == "spam":
            continue
        rid = f"c{inbox['next']}"
        inbox["next"] += 1
        new_drafts += 1
        inbox["items"][rid] = {"comment_id": c["id"], "thread_id": c["thread_id"], "video_id": c["video_id"],
                               "author": c["author"], "comment": c["text"][:300], "category": d["category"],
                               "needs_owner": d["needs_owner"], "reply": d["reply"]}
    L.save(INBOX, inbox)
    L.mark_seen(comments)

    text = agents.brief(snap, reports, inbox["items"])
    day = datetime.now(L.JST).strftime("%Y-%m-%d")
    os.makedirs(BRIEFS, exist_ok=True)
    with open(os.path.join(BRIEFS, f"{day}.md"), "w", encoding="utf-8") as f:
        f.write(text)
    L.save(REPORTS, {"at": snap["at"], "reports": reports})
    L.save(NUMBERS, numbers(snap))
    if os.environ.get("REP_NOTIFY") != "always" and not needs_owner(snap, reports, new_drafts,
                                                                         pronunciation_news(snap, reports) + thumbnail_news(snap)):
        # nothing for the owner to do: keep the brief on the rep-data branch, post nothing
        print(f"Nothing needs you today; brief saved to briefs/{day}.md\n\n{text}")
        return
    write_out(f"## 📮 {day} のブリーフ\n\n{text}")


def pronunciation_news(snap, reports):
    """Japanese words worth a notification: found for the first time, or (once more) when their episode is next in line."""
    done = L.load(PRON, {})
    nxt = (snap.get("pronunciation") or {}).get("next_episode")
    news = []
    for w in (reports.get("pronunciation") or {}).get("words", []):
        key = w["word"].lower()
        seen = done.get(key)
        if not seen:
            done[key] = {"episode": w["episode"], "next_reported": w["episode"] == nxt}
            news.append(w["word"])
        elif w["episode"] == nxt and not seen.get("next_reported"):
            seen["next_reported"] = True
            news.append(w["word"])
    L.save(PRON, done)
    return news


def thumbnail_news(snap):
    """Episodes whose thumbnail is missing, worth a notification: found for the first time, or (once more)
    when less than a day is left before the run that uploads the episode."""
    done = L.load(THUMBS, {})
    news = []
    for t in (snap.get("channel") or {}).get("thumbnails_needed", []):
        key = str(t["episode"])
        seen = done.setdefault(key, {})
        urgent = t["hours_left"] <= 24
        if not seen.get("reported") or (urgent and not seen.get("urgent_reported")):
            news.append(f"thumbnail {key}")
        seen["reported"] = True
        seen["urgent_reported"] = seen.get("urgent_reported") or urgent
    L.save(THUMBS, done)
    return news


def needs_owner(snap, reports, new_drafts, news=()):
    """True when the owner has something to do: a problem, a blocker, a failed agent, new replies to approve,
    Japanese words to listen to, or thumbnails to make."""
    ops = reports.get("ops") or {}
    return bool(
        new_drafts
        or news
        or (snap.get("channel") or {}).get("blockers")
        or any("error" in (r or {}) for r in reports.values())
        or ops.get("health") != "all good"
        or any(i.get("owner_action", "").strip() for i in ops.get("items", [])))


def listen():
    """Listen without any AI call. New viewer comments wait in pending_comments.json until a reader
    (the Claude Code routine) drafts replies into inbox.json and empties it."""
    snap = L.snapshot(with_comments=True)
    pending = L.load(PENDING, {})
    for c in (snap.get("audience") or {}).get("new", []):
        pending[c["id"]] = c
    L.save(PENDING, pending)
    L.mark_seen(pending)
    L.save(SNAPSHOT, snap)
    print(f"Snapshot saved ({snap['at']}); {len(pending)} viewer comment(s) waiting for reply drafts")


def ask():
    import agents
    question = os.environ.get("QUESTION", "").strip()
    snap = L.snapshot(with_comments=False)  # comments come in with the daily brief
    last = L.load(REPORTS, {})
    recent = sorted(os.listdir(BRIEFS))[-2:] if os.path.isdir(BRIEFS) else []
    briefs = "\n\n".join(open(os.path.join(BRIEFS, b), encoding="utf-8").read() for b in recent)
    text = agents.answer(question, snap, last, load_inbox()["items"], briefs)
    write_out(text)


def post_reply(yt, item, text):
    r = yt.comments().insert(part="snippet", body={"snippet": {
        "parentId": item["thread_id"], "textOriginal": text}}).execute()
    return r["id"]


def command():
    """/reply all | /reply c1 c3 | /skip c2 | /edit c4 new reply text"""
    q = os.environ.get("QUESTION", "").strip()
    inbox = load_inbox()
    items = inbox["items"]
    m = re.match(r"/(reply|skip|edit)\b\s*(.*)", q, re.S)
    if not m:
        return write_out("コマンドが読めなかったよ。`/reply all`、`/reply c1 c3`、`/skip c2`、`/edit c4 新しい返信` のどれかで書いてね。")
    cmd, rest = m.group(1), m.group(2).strip()
    lines = []
    if cmd == "edit":
        rid, _, text = rest.partition(" ")
        if rid not in items or not text.strip():
            return write_out(f"`{rid}` が見つからないか、返信の文が空だったよ。")
        targets = {rid: text.strip()}
    else:
        ids = list(items) if rest.lower() in ("all", "") else re.findall(r"c\d+", rest)
        if cmd == "reply" and rest.lower() in ("all", ""):
            # "all" leaves out the drafts the audience agent flagged for the owner
            ids = [i for i in ids if not items[i]["needs_owner"]]
        targets = {i: items[i]["reply"] for i in ids if i in items}
        lines += [f"- `{i}`: 見つからなかった（もう送信済みかも）" for i in re.findall(r"c\d+", rest) if i not in items]
    if cmd == "skip":
        for i in targets:
            items.pop(i)
        if targets:
            lines.append(f"🗑 {len(targets)}件の下書きを消したよ: " + ", ".join(f"`{i}`" for i in targets))
    else:
        yt = L.youtube()
        sent = L.load(SENT, {})
        for i, text in targets.items():
            try:
                cid = post_reply(yt, items[i], text)
                sent[i] = {**items.pop(i), "reply": text, "reply_id": cid,
                           "at": datetime.now(L.JST).strftime("%Y-%m-%d %H:%M JST")}
                lines.append(f"✅ `{i}` に返信したよ → https://youtu.be/{sent[i]['video_id']}")
            except Exception as e:
                lines.append(f"⚠️ `{i}` は送れなかった: {str(e)[:200]}")
                if "quotaExceeded" in str(e):
                    lines.append("YouTubeの1日の上限に達したみたい。残りは明日 `/reply` してね。")
                    break
        L.save(SENT, sent)
        flagged = [i for i, v in items.items() if v["needs_owner"]]
        if flagged:
            lines.append("あなたの判断が必要な下書きは残してあるよ: " + ", ".join(f"`{i}`" for i in flagged))
    L.save(INBOX, inbox)
    write_out("\n".join(lines) or "送る下書きはなかったよ。")


if __name__ == "__main__":
    {"brief": brief, "ask": ask, "command": command, "listen": listen}[sys.argv[1]]()
