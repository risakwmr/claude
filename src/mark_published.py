"""Record an uploaded episode in published.json so it is not uploaded twice."""
import json
import os
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(ROOT, "published.json")
data = json.load(open(path)) if os.path.exists(path) else {}
data[sys.argv[1]] = {"video_id": sys.argv[2], "uploaded_at": datetime.now(timezone.utc).isoformat(timespec="seconds")}
json.dump(data, open(path, "w"), indent=2)
