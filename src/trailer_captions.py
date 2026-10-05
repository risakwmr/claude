"""Time the trailer's captions to its actual audio (faster-whisper word times matched to the script),
then upload English and Japanese caption tracks. Run with action trailer_captions."""
import difflib, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import upload as up

ROOT = up.ROOT
TD = os.path.join(ROOT, "episodes", "trailer")
VIDEO = os.path.join(TD, "final", "trailer.mp4")
vid = json.load(open(os.path.join(ROOT, "trailer.json")))["video_id"]


def lines(path):
    out = []
    for l in open(path, encoding="utf-8"):
        l = l.strip()
        if l:
            who, _, text = l.partition(":")
            out.append((who.strip().title(), text.strip()))
    return out


en, ja = lines(os.path.join(TD, "trailer.txt")), lines(os.path.join(TD, "trailer.ja.txt"))
assert len(en) == len(ja), (len(en), len(ja))

from faster_whisper import WhisperModel
model = WhisperModel("small", compute_type="int8")
import subprocess
import numpy as np
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", VIDEO, "-vn", "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
                     check=True, capture_output=True).stdout
audio = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
segs, _ = model.transcribe(audio, language="en", word_timestamps=True, vad_filter=False)
heard = [(re.sub(r"[^a-z0-9']", "", w.word.lower()), w.start, w.end) for s in segs for w in s.words]
heard = [h for h in heard if h[0]]
duration = heard[-1][2]

want, owner = [], []
for i, (_, t) in enumerate(en):
    for w in t.split():
        w = re.sub(r"[^a-z0-9']", "", w.lower())
        if w:
            want.append(w)
            owner.append(i)

sm = difflib.SequenceMatcher(None, [h[0] for h in heard], want, autojunk=False)
start, end = [None] * len(en), [None] * len(en)
for a, b, n in sm.get_matching_blocks():
    for k in range(n):
        li = owner[b + k]
        s, e = heard[a + k][1], heard[a + k][2]
        start[li] = s if start[li] is None else min(start[li], s)
        end[li] = e if end[li] is None else max(end[li], e)
print(f"matched lines: {sum(s is not None for s in start)}/{len(en)}; words {sm.ratio():.2f}", flush=True)

# fill lines that matched nothing by squeezing them between their neighbours
for i in range(len(en)):
    if start[i] is None:
        p = max([end[j] for j in range(i) if end[j] is not None] or [0.0])
        nxt = min([start[j] for j in range(i + 1, len(en)) if start[j] is not None] or [duration])
        gaps = [j for j in range(i, len(en)) if start[j] is None and (j == i or all(start[k] is None for k in range(i, j)))]
        share = (nxt - p) / max(len(gaps), 1)
        start[i], end[i] = p, p + share * 0.95
# a line runs until just before the next one starts (never overlaps)
for i in range(len(en) - 1):
    end[i] = min(end[i] + 0.3, start[i + 1] - 0.05)
end[-1] += 0.3


def ts(t):
    t = max(t, 0)
    return f"{int(t // 3600):02d}:{int(t % 3600 // 60):02d}:{int(t % 60):02d},{int(round((t % 1) * 1000)):03d}".replace(",1000", ",999")


def srt(items, path):
    cues, n = [], 1
    for i, (who, text) in enumerate(items):
        parts = [p for p in re.split(r"(?<=[。.!?！？])\s*", text) if p]
        # merge tiny pieces so every cue has some text to read
        merged = []
        for p in parts:
            if merged and len(p) < 8:
                merged[-1] += (" " if text[0].isascii() else "") + p
            else:
                merged.append(p)
        total = sum(len(p) for p in merged) or 1
        t = start[i]
        for k, p in enumerate(merged):
            d = (end[i] - start[i]) * len(p) / total
            label = f"{who}: " if k == 0 else ""
            cues.append(f"{n}\n{ts(t)} --> {ts(t + d)}\n{label}{p}\n")
            n += 1
            t += d
    open(path, "w", encoding="utf-8").write("\n".join(cues))


out_ja, out_en = os.path.join(TD, "final", "trailer.ja.srt"), os.path.join(TD, "final", "trailer.en.srt")
srt(ja, out_ja)
srt(en, out_en)
print(open(out_ja, encoding="utf-8").read()[:1200], flush=True)

yt = up.youtube()
up.add_japanese_captions(yt, vid, out_ja)
up.add_captions(yt, vid, out_en, "en", "English")
print(f"https://youtu.be/{vid}", flush=True)
