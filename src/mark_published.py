"""Record an uploaded episode in published.json so it is not uploaded twice."""
import json
import os
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(ROOT, "published.json")
data = json.load(open(path)) if os.path.exists(path) else {}
now = datetime.now(timezone.utc)
entry = {"video_id": sys.argv[2], "uploaded_at": now.isoformat(timespec="seconds")}
when = sys.argv[3].strip() if len(sys.argv) > 3 else ""
if when == "now":
    entry["publish_at"] = now.strftime("%Y-%m-%dT%H:%M:%SZ")
elif when:
    entry["publish_at"] = when
data[sys.argv[1]] = entry
json.dump(data, open(path, "w"), indent=2)
