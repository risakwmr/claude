"""Weekly numbers for the channel: views, likes and comments of every episode and Short, plus watch time,
retention, traffic sources and countries when the YouTube Analytics permission is there.

python src/report.py         saves reports/YYYY-MM-DD.json and prints a short Markdown summary

- Always works (YouTube Data API, a few quota units): subscribers, and views / likes / comments per video.
  "This week" numbers are the change since the previous saved report.
- Needs the refresh token to include the scope https://www.googleapis.com/auth/yt-analytics.readonly and the
  "YouTube Analytics API" turned on in the Google Cloud project: watch time, average % viewed, subscribers gained,
  traffic sources, countries and devices for the last 7 days. Without it the report says so and skips that part.
  YouTube Analytics data runs about 2–3 days behind.
"""
import json
import os
import sys
from datetime import date, datetime, timedelta, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORT_DIR = os.path.join(ROOT, "reports")


def credentials():
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    creds = Credentials(token=None, refresh_token=os.environ["REFRESH_TOKEN"], client_id=os.environ["CLIENT_ID"],
                        client_secret=os.environ["CLIENT_SECRET"], token_uri="https://oauth2.googleapis.com/token")
    creds.refresh(Request())
    return creds


def load(path):
    return json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {}


def previous_report(today):
    """The newest earlier report at least 5 days old (else the newest earlier one), for week-over-week numbers."""
    if not os.path.isdir(REPORT_DIR):
        return None
    names = sorted(f for f in os.listdir(REPORT_DIR) if f.endswith(".json") and f[:10] < today.isoformat())
    if not names:
        return None
    old = [f for f in names if date.fromisoformat(f[:10]) <= today - timedelta(days=5)]
    return load(os.path.join(REPORT_DIR, (old or names)[-1]))


def video_stats(yt):
    pub = load(os.path.join(ROOT, "published.json"))
    shorts = load(os.path.join(ROOT, "shorts.json"))
    meta = load(os.path.join(ROOT, "episodes", "episodes.json"))
    titles = {str(e["number"]): e["title"] for e in meta.get("episodes", [])}
    keys = {}
    for k, v in pub.items():
        keys[v["video_id"]] = ("episode", k)
    for k, v in shorts.items():
        keys[v["video_id"]] = ("short", k)
    rows = []
    ids = list(keys)
    for i in range(0, len(ids), 50):
        r = yt.videos().list(part="statistics,snippet,status,contentDetails", id=",".join(ids[i:i + 50])).execute()
        for item in r.get("items", []):
            kind, k = keys[item["id"]]
            st = item.get("statistics", {})
            status = item["status"]
            rows.append({
                "kind": kind, "key": k, "video_id": item["id"],
                "title": item["snippet"]["title"], "episode_title": titles.get(k.split("-")[0], ""),
                "public": status.get("privacyStatus") == "public",
                "published": status.get("publishAt") or item["snippet"].get("publishedAt"),
                "duration": item.get("contentDetails", {}).get("duration"),
                "views": int(st.get("viewCount", 0)), "likes": int(st.get("likeCount", 0)),
                "comments": int(st.get("commentCount", 0)),
            })
    return rows


def analytics(creds, start, end):
    """Last-7-days numbers from the YouTube Analytics API, or {"available": False, "error": ...}."""
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    out = {"available": True, "start": start.isoformat(), "end": end.isoformat()}
    try:
        ya = build("youtubeAnalytics", "v2", credentials=creds, cache_discovery=False)

        def q(**kw):
            r = ya.reports().query(ids="channel==MINE", startDate=start.isoformat(), endDate=end.isoformat(),
                                   **kw).execute()
            cols = [h["name"] for h in r.get("columnHeaders", [])]
            return [dict(zip(cols, row)) for row in r.get("rows", []) or []]

        out["totals"] = q(metrics="views,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,"
                                  "likes,comments,shares,subscribersGained,subscribersLost")
        out["daily"] = q(dimensions="day", metrics="views,estimatedMinutesWatched,subscribersGained", sort="day")
        out["by_video"] = q(dimensions="video", metrics="views,estimatedMinutesWatched,averageViewDuration,"
                                                        "averageViewPercentage,likes,subscribersGained",
                            sort="-views", maxResults=50)
        out["traffic"] = q(dimensions="insightTrafficSourceType", metrics="views,estimatedMinutesWatched",
                           sort="-views")
        out["countries"] = q(dimensions="country", metrics="views,estimatedMinutesWatched", sort="-views",
                             maxResults=10)
        out["devices"] = q(dimensions="deviceType", metrics="views", sort="-views")
        out["subscribed"] = q(dimensions="subscribedStatus", metrics="views,averageViewPercentage")
    except HttpError as e:
        try:
            msg = json.loads(e.content.decode())["error"]["message"]
        except Exception:
            msg = str(e)
        return {"available": False, "error": f"{e.resp.status} {msg[:400]}"}
    except Exception as e:  # e.g. missing scope reported while refreshing
        return {"available": False, "error": str(e)[:300]}
    return out


def main():
    from googleapiclient.discovery import build
    creds = credentials()
    yt = build("youtube", "v3", credentials=creds, cache_discovery=False)
    today = datetime.now(timezone.utc).date()
    ch = yt.channels().list(part="statistics,snippet", mine=True).execute()["items"][0]
    rows = video_stats(yt)
    prev = previous_report(today)
    if prev:
        before = {r["video_id"]: r for r in prev.get("videos", [])}
        for r in rows:
            b = before.get(r["video_id"])
            r["views_since_last"] = r["views"] - (b["views"] if b else 0)
            r["likes_since_last"] = r["likes"] - (b["likes"] if b else 0)
    end = today - timedelta(days=1)
    report = {
        "at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "previous_report_at": prev.get("at") if prev else None,
        "channel": {"title": ch["snippet"]["title"],
                    "subscribers": int(ch["statistics"].get("subscriberCount", 0)),
                    "views": int(ch["statistics"].get("viewCount", 0)),
                    "videos": int(ch["statistics"].get("videoCount", 0)),
                    "subscribers_before": prev["channel"]["subscribers"] if prev else None,
                    "views_before": prev["channel"]["views"] if prev else None},
        "videos": sorted(rows, key=lambda r: -r["views"]),
        "analytics": analytics(creds, end - timedelta(days=6), end),
    }
    os.makedirs(REPORT_DIR, exist_ok=True)
    path = os.path.join(REPORT_DIR, f"{today.isoformat()}.json")
    json.dump(report, open(path, "w", encoding="utf-8"), indent=2, ensure_ascii=False)

    c = report["channel"]
    print(f"## Channel report {today.isoformat()}\n")
    print(f"Subscribers: {c['subscribers']}" + (f" ({c['subscribers'] - c['subscribers_before']:+d})"
                                                 if c["subscribers_before"] is not None else ""))
    print(f"Total views: {c['views']}" + (f" ({c['views'] - c['views_before']:+d})"
                                          if c["views_before"] is not None else "") + "\n")
    print("| Video | Kind | Views | Likes | Comments |\n| --- | --- | --- | --- | --- |")
    for r in report["videos"][:20]:
        print(f"| {r['key']} | {r['kind']} | {r['views']} | {r['likes']} | {r['comments']} |")
    a = report["analytics"]
    print("\nAnalytics: " + ("last 7 days saved" if a.get("available") else f"not available ({a.get('error')})"))
    print(f"\nSaved {os.path.relpath(path, ROOT)}")


def note_error(e):
    """Run logs can't be read from outside, so the error goes to run_status.json (saved by the workflow)."""
    path = os.path.join(ROOT, "run_status.json")
    data = load(path)
    data["report"] = {"at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                      "result": f"ERROR {type(e).__name__}: {str(e)[:400]}"}
    json.dump(data, open(path, "w"), indent=2, ensure_ascii=False)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        note_error(e)
        raise
