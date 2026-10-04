"""Visual cues for an episode: character poses, the center board and section names.

An episode uses the visual layout when episodes/epNN.visual.json exists (epNNN for 100+):

{
  "cues": [
    {"line": 1,  "section": "Last time", "sena": "happy", "daniel": "default", "board": {"type": "cover"}},
    {"line": 13, "section": "Today",     "sena": "worried", "board": {"type": "keyword", "text": "10 seconds of silence", "icon": "Zipper-mouth face"}},
    {"line": 25, "section": "Research",  "daniel": "read", "board": {"type": "study", "who": "Edmondson (1999)",
                  "stat": "51 teams", "text": "Safety → learning → performance", "note": "One company · correlational", "icon": "Factory"}}
  ]
}

- "line" is the 1-based line number in the script. A cue applies from that line until the next cue changes the same thing.
- "sena" / "daniel": a pose name from assets/characters/full/ (see POSES below).
- "section": short chapter name. It shows on screen and becomes a YouTube chapter.
- "board" types: cover, keyword, study, compare, list, story, question, challenge, none.
  keyword:   text, sub (optional), icon or icons (optional, up to 3)
  study:     who, stat (big number or short fact), text, note (caveat), icon
  compare:   left {title, items[]}, right {title, items[]}   (e.g. Japan / US)
  list:      title, items[] (up to 4)
  story:     title, text, icon        (Daniel's story)
  question:  text                     (the listener's 40-second question)
  challenge: text (headline), sub (one line)
  cover:     the episode thumbnail
- Speaking Lab "repeat" boards are automatic: a DANIEL line that is only a quoted sentence, followed by SENA
  repeating it, shows the sentence big and then adds a short silent "Your turn" pause with a countdown.
- Icons are free illustrations (Fluent Emoji 3D, MIT). Names: assets/icons/INDEX.txt.
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SENA_POSES = ["default", "happy", "energy", "listen", "coffee", "calm", "cheer", "surprised", "confused", "study", "idea",
              "shrug", "thumbsup", "delighted", "shock", "cheek", "work", "sip", "chin", "curious", "phone", "think",
              "laughcry", "down", "wave", "cool", "shy", "oh", "moved", "worried", "relief", "tired", "point", "write",
              "drink", "lunch", "giggle", "dreamy", "peace", "bun"]
DANIEL_POSES = ["default", "listen", "happy", "think", "surprised", "laugh", "stretch", "point", "explain", "dreamy",
                "chin", "notice", "open", "offer", "casual", "idea", "smile", "sheepish", "chuckle", "thanks", "coffee",
                "work", "mugpoint", "pet", "wave", "puzzled", "grin", "dog"]


def visual_path(num):
    name = f"ep{num:02d}.visual.json" if num < 100 else f"ep{num:03d}.visual.json"
    return os.path.join(ROOT, "episodes", name)


def has_visuals(num):
    return os.path.exists(visual_path(num))


def load_cues(num):
    p = visual_path(num)
    if not os.path.exists(p):
        return []
    data = json.load(open(p, encoding="utf-8"))
    return sorted(data.get("cues", []), key=lambda c: c["line"])


def _strip_quotes(s):
    s = s.strip()
    if len(s) > 2 and s[0] in "\"“" and s[-1] in "\"”":
        return s[1:-1].strip()
    return None


def _norm(s):
    return re.sub(r"[^a-z0-9 ]", "", s.lower()).split()


def line_states(num, lines, ep=None):
    """One state dict per script line, plus a list of practice pauses {line_index: seconds_factor}.

    state = {"sena": pose, "daniel": pose, "section": str, "board": dict or None}
    """
    cues = load_cues(num)
    by_line = {}
    for c in cues:
        by_line.setdefault(c["line"] - 1, []).append(c)
    state = {"sena": "default", "daniel": "default", "section": "", "board": {"type": "cover"}}
    states, repeats = [], set()
    in_lab = False
    for i, (spk, text) in enumerate(lines):
        for c in by_line.get(i, []):
            for k in ("sena", "daniel", "section"):
                if k in c:
                    state[k] = c[k]
            if "board" in c:
                state["board"] = c["board"]
        s = dict(state)
        if "speaking lab" in text.lower():
            in_lab = True
        # automatic repeat boards inside the Speaking Lab
        q = _strip_quotes(text) if spk == "DANIEL" else None
        if q and i + 1 < len(lines) and lines[i + 1][0] == "SENA" and _norm(lines[i + 1][1]) == _norm(q):
            s["board"] = {"type": "repeat", "text": q}
            s["section"] = s["section"] or "Speaking Lab"
        elif spk == "SENA" and i > 0 and states and states[-1]["board"].get("type") == "repeat" \
                and _norm(text) == _norm(states[-1]["board"]["text"]):
            s["board"] = dict(states[-1]["board"])
            repeats.add(i)
        elif in_lab and states and states[-1]["board"].get("type") == "repeat" and not any(
                "board" in c for c in by_line.get(i, [])):
            s["board"] = state["board"] = {"type": "none"}
        if "today's challenge" in text.lower() and not any("board" in c for c in by_line.get(i, [])) and ep:
            s["board"] = state["board"] = {"type": "challenge", "text": ep.get("thumb_cup") or "Today's challenge",
                                           "sub": ep.get("practice", "")}
            s["section"] = state["section"] = "Today's challenge"
        states.append(s)
    return states, repeats
