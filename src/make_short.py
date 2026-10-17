"""Build vertical YouTube Shorts (1080x1920) from parts of an episode.

Usage:
  python src/make_short.py 14                  # every kind of Short for episode 14 (real voices, GitHub Actions)
  python src/make_short.py 14 --kind story     # one kind only
  python src/make_short.py 14 --fake-tts       # placeholder tones, for checking the visuals
  python src/make_short.py 14 --kind lab --frame 3   # only save one still frame (line 3 of the clip) as a PNG
  python src/make_short.py 14 --list           # print the kinds this episode has
  python src/make_short.py 1 --kind highlight --ig   # Instagram Reel variant -> output/ep01/ep01_reel_highlight.mp4

Instagram variant (--ig): same clip, voices and timing, but laid out for the Reels UI: a big hook at the top
(spec "ig_hook", falling back to "hook"), large burned-in subtitles in the middle so it reads on mute, bigger
characters at the bottom, no episode thumbnail. All text stays inside the IG safe zone (clear of the top 220 px,
bottom 420 px and right 150 px where Instagram draws its UI). Audio: stereo AAC 44.1 kHz 160k, -14 LUFS;
video: H.264 High, yuv420p, 30 fps, faststart.

Kinds of Short (one episode gives up to four):
  ai       "Why can't AI do this?"  (every episode)
  story    Daniel's failure story
  culture  Japan vs the US
  highlight the most striking moment of the episode, marked by the writer in epNN.short.json (no automatic cut)
  lab      Phrases that work at work: 2-3 natural phrases from the dialogue, each shown big and said once,
           then a short silent "your turn" countdown. From EP32 the episode has no Speaking Lab, so the writer
           specifies it in epNN.short.json ("phrases", below). EP12-31 still cut it from the Speaking Lab automatically.

What goes into each Short comes from episodes/epNN.short.json (epNNN for 100+):

{
  "shorts": [
    {"kind": "ai",      "lines": [44, 47], "hook": "AI apologizes all the time. So why can't it do this?",
     "title": "When AI says sorry, it costs nothing. That's the point."},
    {"kind": "story",   "lines": [49, 57], "hook": "...", "board": {"type": "story", "title": "...", "icon": "Door"}},
    {"kind": "culture", "lines": [62, 68], "hook": "...", "board": {"type": "compare", "left": {...}, "right": {...}}}
  ]
}

- Explicit "lab" Short (EP32 on; no Speaking Lab in the script):
    {"kind": "lab", "lines": [40, 44],
     "phrases": ["Can I push back on that a little?", "Here's what I'm seeing.", "What would make this a yes?"],
     "hook": "3 phrases that make pushback sound like teamwork", "title": "How to push back without sounding difficult",
     "tag": "PHRASES THAT WORK AT WORK"}
  "lines" is the stretch of dialogue where the phrases come up naturally (played as is, each phrase card shows
  while the line that contains it is spoken). Then each phrase (2-3, short, taken from those lines) is said once
  by "voice" (DANIEL by default, or SENA), shown big, followed by the silent "your turn" countdown.
  If the dialogue runs past max_seconds, dialogue lines are dropped from the end; the phrase drill is always kept.
- "lines": 1-based line range in the episode script (inclusive). "hook": big text at the top from the first frame.
  "ig_hook": optional punchier hook for the Instagram Reel (--ig); words in CAPS are drawn in yellow.
  "title": YouTube title (default: the hook). "tag": small label (default per kind). "board": center card (optional).
  "max_seconds": length limit (default per kind); lines at the end are dropped if the voices run long.
- An old single-Short file ({"lines": ..., "hook": ...}) counts as the "ai" Short.
- Any kind missing from the file is cut automatically when the episode has that part, so new episodes get
  their Shorts with no extra work.
- The center card follows the episode's visual cues when it has them, otherwise "board", otherwise the cover.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys

import numpy as np
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_episode as me  # noqa: E402
import render as r  # noqa: E402
import scenes  # noqa: E402

ROOT = me.ROOT
W, H = 1080, 1920
FPS = 12
RATE = "+0%"          # natural native speed
GAP = 0.1   # native back-and-forth: almost no pause between turns
LEAD, TAIL = 0.2, 0.5   # short tail and no end card, so the Short loops straight back to the hook

KINDS = ["ai", "highlight", "story", "culture", "lab"]
TAGS = {"ai": "WHY CAN'T AI DO THIS?", "highlight": "DID YOU KNOW?", "story": "DANIEL'S STORY", "culture": "JAPAN VS THE US",
        "lab": "PHRASES THAT WORK AT WORK"}
LAB_CARD_LABEL = "PHRASE THAT WORKS"   # label on a phrase card (render.py board "repeat"; the countdown label stays)
MAX_SECONDS = {"ai": 55.0, "highlight": 50.0, "story": 58.0, "culture": 60.0, "lab": 58.0}  # popular Shorts run ~30-45 s
TARGET_WORDS = {"ai": 140, "story": 230, "culture": 190}   # rough size of an automatic clip before voicing

HOOK_TOP, HOOK_SPACE = 280, 330     # hook text block (centered vertically in this space)
BOARD_BOX = (100, 640, 980, 1250)   # center card area
BAR = (40, 1268, 1040, 1508)        # caption bar
BUST_FLOOR = 2010                    # busts stand behind the bar; their lower half runs off the bottom
BUST_X = {"SENA": 300, "DANIEL": 780}
BUST_SCALE = {"SENA": 0.88, "DANIEL": 1.08}   # Sena's pose art is drawn larger, so she is scaled down to match Daniel
STORY_ASK = re.compile(r"failure story|one of your stories|a story for me|your story|mistake of mine|"
                       r"tell you about a mistake|a confession|promised you a story", re.I)
CULTURE = re.compile(r"cultur(e|al) (question|point|difference)|connects to (japan|culture)|about japan|"
                     r"topic in japan|harder in japan|version of this problem|in japan, we", re.I)
NEXT_PART = re.compile(r"\bstor(y|ies)\b|failure|confession|mistake of mine|hold that thought|"
                       r"which eq skill|eq domain|speaking lab|today's challenge|cultur(e|al) (question|point)|"
                       r"about japan", re.I)
AI_QUESTION = re.compile(r"why can.?t ai|why is this (a skill|something) ai can.?t|ai can.?t do (this|that) for", re.I)
LAB_TOPIC = re.compile(r"(?:three|3) (?:sentences|phrases) (?:for|to) ([^.]+)\.", re.I)


def short_path(num):
    name = f"ep{num:02d}.short.json" if num < 100 else f"ep{num:03d}.short.json"
    return os.path.join(ROOT, "episodes", name)


def grow(lines, start, target, min_lines=3):
    """From start, take lines up to about `target` words, stopping before the next part of the episode."""
    words, end = 0, start
    while end < len(lines) and (words < target or end - start < min_lines):
        if end - start >= 2 and NEXT_PART.search(lines[end][1]):
            break
        words += len(lines[end][1].split())
        end += 1
        if words > target * 1.25:
            break
    return end


def auto_range(lines, kind="ai"):
    """(start, end) python slice for an automatic Short of this kind, or None if the episode has no such part."""
    if kind == "ai":
        start = next((i for i, (_, t) in enumerate(lines) if i > 5 and AI_QUESTION.search(t)), None)
        if start is None:
            return None
        return start, grow(lines, start, TARGET_WORDS["ai"])
    if kind == "story":
        start = next((i for i, (_, t) in enumerate(lines) if i > 20 and STORY_ASK.search(t)), None)
        if start is None:
            return None
        # skip a one-line "Now, my failure story." / "Can I ask for one of your stories?" when the story follows
        if len(lines[start][1].split()) < 25 and start + 1 < len(lines):
            nxt = start + 1
            if len(lines[nxt][1].split()) < 8 and nxt + 1 < len(lines):  # "I was waiting for it."
                nxt += 1
            start = nxt
        words, end = 0, start
        while end < len(lines) and words < TARGET_WORDS["story"]:
            if end - start >= 3 and CULTURE.search(lines[end][1]):
                break
            words += len(lines[end][1].split())
            end += 1
        return start, end
    if kind == "culture":
        start = next((i for i, (_, t) in enumerate(lines) if i > 20 and CULTURE.search(t)), None)
        if start is None:
            return None
        return start, grow(lines, start, TARGET_WORDS["culture"])
    if kind == "highlight":  # the most striking moment, chosen by the script writer in epNN.short.json
        return None
    if kind == "lab":
        states, repeats = scenes.line_states(0, lines)
        reps = sorted(repeats)
        if not reps:
            return None
        start = reps[0] - 1  # Daniel's first quoted sentence
        end = reps[0] + 1
        for k in reps[1:]:
            if k - 1 <= end:  # keep consecutive repeat pairs together
                end = k + 1
            else:
                break
        return start, end
    raise ValueError(kind)


def lab_topic(lines, start):
    for i in range(max(0, start - 3), start):
        m = LAB_TOPIC.search(lines[i][1])
        if m:
            return m.group(1).strip()
    return None


def lab_phrases(spec):
    """The explicit phrases of a lab Short (list of str), or [] for the old auto-detected Speaking Lab."""
    if spec.get("kind") != "lab":
        return []
    ph = spec.get("phrases") or []
    if isinstance(ph, str):
        ph = [ph]
    return [str(p).strip().strip("\"“”") for p in ph if str(p).strip()][:3]


def _norm_text(s):
    return " ".join(re.sub(r"[^a-z0-9' ]", " ", s.lower().replace("’", "'")).split())


def phrase_line(phrase, lines, start, end):
    """Index of the first dialogue line in [start, end) that contains the phrase (punctuation/case ignored), or None."""
    target = _norm_text(phrase)
    for i in range(start, end):
        if target and target in _norm_text(lines[i][1]):
            return i
    return None


def specs(num, ep, lines):
    """All Shorts this episode has, as a dict kind -> spec."""
    data = {}
    p = short_path(num)
    if os.path.exists(p):
        data = json.load(open(p, encoding="utf-8"))
    items = data.get("shorts") if "shorts" in data else ([dict(data, kind="ai")] if data else [])
    by_kind = {it.get("kind", "ai"): dict(it) for it in items}
    out = {}
    for kind in KINDS:
        spec = by_kind.get(kind)
        if spec is None:
            rng = auto_range(lines, kind)
            if rng is None:
                continue
            spec = {"auto": True}
            start, end = rng
        elif spec.get("skip"):
            continue
        elif spec.get("lines"):
            a, b = spec["lines"]
            start, end = a - 1, b
        else:
            rng = auto_range(lines, kind)
            if rng is None:
                continue
            start, end = rng
        topic = ep["short_title"]
        phrases = lab_phrases(dict(spec, kind=kind))
        defaults = {
            "ai": f"Why can't AI do this? {topic}",
            "highlight": topic,
            "story": f"A manager's mistake: {topic}",
            "culture": f"Japan vs the US: {topic}",
            "lab": (f"{len(phrases)} phrases that work at work: {topic}" if phrases else
                    f"Say it out loud: 3 phrases for {lab_topic(lines, start) or topic.lower()}"),
        }
        spec["kind"] = kind
        spec.setdefault("hook", defaults[kind])
        spec.setdefault("title", spec["hook"])
        spec.setdefault("tag", TAGS[kind])
        spec.setdefault("max_seconds", MAX_SECONDS[kind])
        spec["start"], spec["end"] = start, end
        if phrases:
            spec["phrases"] = phrases
            spec.setdefault("voice", "DANIEL")
            if spec["voice"] not in ("DANIEL", "SENA"):
                spec["voice"] = "DANIEL"
            for ph in phrases:
                if phrase_line(ph, lines, start, end) is None:
                    print(f"  WARNING: EP {num:02d} lab phrase not found in lines {start + 1}-{end}: {ph!r}",
                          file=sys.stderr, flush=True)
        out[kind] = spec
    return out


def load_spec(num, ep, lines, kind="ai"):
    return specs(num, ep, lines)[kind]


def default_poses(spk_active):
    return {"SENA": "default" if spk_active == "SENA" else "listen",
            "DANIEL": "explain" if spk_active == "DANIEL" else "listen"}


def clip_lines(lines, spec):
    """(speaker, text) of every line in the clip: the dialogue, then for an explicit lab Short one line per phrase."""
    clip = list(lines[spec["start"]:spec["end"]])
    clip += [(spec.get("voice", "DANIEL"), p) for p in spec.get("phrases") or []]
    return clip


def clip_states(num, ep, lines, spec):
    """Poses and center card for each line of the clip, and which lines get a "your turn" pause."""
    if spec.get("phrases"):
        return lab_clip_states(num, ep, lines, spec)
    start, end = spec["start"], spec["end"]
    visual = scenes.has_visuals(num)
    states, repeats = scenes.line_states(num, lines, ep)
    out = []
    for i in range(start, end):
        spk = lines[i][0]
        st = states[i]
        board = st["board"]
        if board.get("type") == "repeat":
            pass  # Speaking Lab sentence, shown big
        elif spec.get("board"):
            board = spec["board"]
        elif not visual or board.get("type") in ("none", "question", "challenge") or not board:
            board = {"type": "cover"}
        if visual:
            poses = {"SENA": st["sena"], "DANIEL": st["daniel"]}
        else:
            poses = default_poses(spk)
        out.append({"sena": poses["SENA"], "daniel": poses["DANIEL"], "board": board})
    pauses = {i - start for i in repeats if start <= i < end}
    return out, pauses


def lab_clip_states(num, ep, lines, spec):
    """Explicit lab Short: dialogue lines as usual (a phrase card shows on the line that contains it),
    then one drill line per phrase, shown big, each followed by a "your turn" pause."""
    start, end = spec["start"], spec["end"]
    visual = scenes.has_visuals(num)
    states, _ = scenes.line_states(num, lines, ep)
    found = {}
    for ph in spec["phrases"]:
        k = phrase_line(ph, lines, start, end)
        if k is not None and k not in found:
            found[k] = ph
    label = spec.get("card_label", LAB_CARD_LABEL)
    out = []
    for i in range(start, end):
        spk = lines[i][0]
        st = states[i]
        if i in found:
            board = {"type": "repeat", "text": found[i], "label": label}
        elif spec.get("board"):
            board = spec["board"]
        elif not visual or st["board"].get("type") in ("none", "question", "challenge", "repeat") or not st["board"]:
            board = {"type": "cover"}
        else:
            board = st["board"]
        poses = {"SENA": st["sena"], "DANIEL": st["daniel"]} if visual else default_poses(spk)
        out.append({"sena": poses["SENA"], "daniel": poses["DANIEL"], "board": board})
    voice = spec.get("voice", "DANIEL")
    n = end - start
    for ph in spec["phrases"]:
        poses = default_poses(voice)
        if voice == "SENA":
            poses["SENA"] = "point" if "point" in scenes.SENA_POSES else "default"
        out.append({"sena": poses["SENA"], "daniel": poses["DANIEL"],
                    "board": {"type": "repeat", "text": ph, "label": label}})
    pauses = set(range(n, n + len(spec["phrases"])))
    return out, pauses


# ---------- drawing ----------

def base(spec, ep_title):
    img = r.paper(W, H, seed=17).convert("RGBA")
    for box, color, seed, a in (((520, -50, 640, 260), r.BLUE, 1, 110), ((-60, 120, 520, 120), r.CORAL, 2, 120),
                                ((-80, 1700, 700, 260), r.BLUE, 3, 70), ((620, 1800, 520, 120), r.CORAL, 4, 100)):
        s = r.brush(box[2:], color, seed, alpha=a)
        img.alpha_composite(s, (box[0], box[1]))
    d = ImageDraw.Draw(img)
    r.spaced(d, (W / 2, 92), "THE", r.sans(20, "SemiBold"), r.NAVY, spacing=6, anchor_center=True)
    d.text((W / 2, 116), "Human Curriculum", font=r.serif(52, "Bold"), fill=r.NAVY, anchor="ma")
    # tag
    tf = r.sans(24, "SemiBold")
    tag = spec["tag"].upper()
    tw = r.spaced_width(tag, tf, 4)
    x0 = (W - tw - 40) / 2
    d.rounded_rectangle((x0, 196, x0 + tw + 40, 242), radius=8, fill=r.CORAL)
    r.spaced(d, (x0 + 20, 205), tag, tf, (255, 255, 255), spacing=4)
    # hook: big, heavy and high-contrast (like popular Shorts), on a navy band so it reads at a glance
    band_top, band_h = 262, 360
    d.rectangle((0, band_top, W, band_top + band_h), fill=r.NAVY)
    f, lines, size = r._fit_font(d, spec["hook"], lambda s: r.sans(s, "ExtraBold"), W - 90, 3, 96, 56)
    step = int(size * 1.16)
    y = band_top + max(16, (band_h - step * len(lines)) // 2)
    for k, line in enumerate(lines):
        fill = (255, 255, 255) if k < len(lines) - 1 or len(lines) == 1 else (255, 214, 102)
        if len(lines) == 1:
            fill = (255, 214, 102)
        d.text((W / 2, y), line, font=f, fill=fill, anchor="ma", stroke_width=6, stroke_fill=r.CORAL)
        y += step
    return img


def board_card(num, board):
    key = json.dumps(board, sort_keys=True)
    card = r.board_image(num, key)
    if card is None:
        return None
    bw, bh = BOARD_BOX[2] - BOARD_BOX[0], BOARD_BOX[3] - BOARD_BOX[1]
    s = min(bw / card.width, bh / card.height)
    return card.resize((int(card.width * s), int(card.height * s)), Image.LANCZOS)


def bust(name, pose, active, face=None):
    img = r.full_pose(name, pose, face) if active else r.faded(name, pose, face)
    k = BUST_SCALE[name]
    return img.resize((int(img.width * k), int(img.height * k)), Image.LANCZOS)


def draw(num, spec, ep_title, speaker, level, subtitle, sena, daniel, board_key, sena_face=None, daniel_face=None,
         base_cache={}):
    k = (num, spec["hook"])
    if k not in base_cache:
        base_cache.clear()
        base_cache[k] = base(spec, ep_title)
    img = base_cache[k].copy()
    card = board_card(num, json.loads(board_key))
    if card is not None:
        cx, cy = (BOARD_BOX[0] + BOARD_BOX[2]) // 2, (BOARD_BOX[1] + BOARD_BOX[3]) // 2
        img.alpha_composite(card, (cx - card.width // 2, cy - card.height // 2))
    for name, pose in (("SENA", sena), ("DANIEL", daniel)):
        active = name == speaker
        fig = bust(name, pose, active, sena_face if name == "SENA" else daniel_face)
        bob = -6 if (active and level >= 2) else 0
        img.alpha_composite(fig, (BUST_X[name] - fig.width // 2, BUST_FLOOR - fig.height + bob))
    # caption bar on top of the busts
    bx0, by0, bx1, by1 = BAR
    bar = r.paper(bx1 - bx0, by1 - by0, seed=9).convert("RGBA")
    ImageDraw.Draw(bar).rectangle((0, 0, bx1 - bx0 - 1, by1 - by0 - 1), outline=(214, 204, 186), width=2)
    sh = Image.new("RGBA", (bx1 - bx0 + 40, by1 - by0 + 40), (0, 0, 0, 0))
    sh.paste((60, 50, 40, 70), (20, 14, bx1 - bx0 + 20, by1 - by0 + 20))
    from PIL import ImageFilter
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(10)), (bx0 - 20, by0 - 20))
    img.alpha_composite(bar, (bx0, by0))
    d = ImageDraw.Draw(img)
    p = r.PEOPLE[speaker]
    d.rounded_rectangle((bx0 + 36, by0 - 26, bx0 + 216, by0 + 22), radius=8, fill=p["accent"])
    d.text((bx0 + 126, by0 - 2), p["first"], font=r.serif(32, "SemiBold", italic=True), fill=(255, 255, 255), anchor="mm")
    if subtitle:
        f, lines, size = r._fit_font(d, subtitle, lambda s: r.sans(s, "ExtraBold"), bx1 - bx0 - 70, 2, 84, 52)
        cy = (by0 + by1) / 2 + 6
        step = int(size * 1.22)
        for i, line in enumerate(lines):
            d.text((W / 2, cy + (i - (len(lines) - 1) / 2) * step), line, font=f, fill=r.NAVY, anchor="mm")
    return img.convert("RGB")


def end_card(num, spec, ep):
    """Last moment: point to the full episode."""
    img = base(spec, ep["title"]).copy()
    d = ImageDraw.Draw(img)
    card = board_card(num, {"type": "cover"})
    if card is not None:
        img.alpha_composite(card, (W // 2 - card.width // 2, 700))
        d = ImageDraw.Draw(img)
    y = 700 + (card.height if card is not None else 300) + 40
    d.text((W / 2, y), "Full episode on the channel", font=r.hand(64), fill=r.CORAL, anchor="ma")
    f, lines, size = r._fit_font(d, ep.get("yt_title") or ep["title"], lambda s: r.serif(s, "SemiBold"), W - 160, 2, 54, 36)
    y += 96
    for line in lines:
        d.text((W / 2, y), line, font=f, fill=r.NAVY, anchor="ma")
        y += int(size * 1.2)
    return img.convert("RGB")


# ---------- Instagram Reel layout (--ig) ----------

IG_SAFE_TOP, IG_SAFE_BOTTOM, IG_SAFE_RIGHT = 220, 420, 150   # Instagram UI overlays (Reels header, caption, buttons)
IG_TEXT_W = W - 2 * IG_SAFE_RIGHT                            # 780: text centered, clear of the right-side buttons
IG_BAND = (IG_SAFE_TOP + 10, 700)                            # navy hook band (top, bottom)
IG_SUB_BOX = (100, 730, W - 100, 1080)                        # subtitle card
IG_BUST_FLOOR = 1930
IG_BUST_X = {"SENA": 290, "DANIEL": 800}
# Rendered figure heights (px, feet/bottom on IG_BUST_FLOOR). Sena is drawn smaller than Daniel (owner feedback,
# EP01 Reel: "Sena is too big"), so Daniel's head sits clearly higher; both scale from their art's actual height.
IG_DANIEL_H = 720                                            # ~1.6x the Shorts size
IG_SENA_RATIO = 0.86                                         # Sena's height as a share of Daniel's
IG_BUST_H = {"SENA": int(IG_DANIEL_H * IG_SENA_RATIO), "DANIEL": IG_DANIEL_H}
YELLOW = (255, 214, 102)


def _wrap_words(d, words, font, max_w):
    lines, cur = [], []
    for w in words:
        trial = cur + [w]
        if cur and d.textlength(" ".join(trial), font=font) > max_w:
            lines.append(cur)
            cur = [w]
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines


def _fit_words(d, text, make, max_w, max_lines, start, stop, step=4, max_h=None, lead=1.12):
    words = text.split()
    size = start
    while True:
        f = make(size)
        lines = _wrap_words(d, words, f, max_w)
        fits_h = max_h is None or int(size * lead) * len(lines) <= max_h
        if (len(lines) <= max_lines and fits_h and all(d.textlength(" ".join(l), font=f) <= max_w for l in lines)) \
                or size <= stop:
            return f, lines, size
        size -= step


def _is_caps(word):
    core = re.sub(r"[^A-Za-z]", "", word)
    return len(core) >= 3 and core.isupper()   # "WORSE" yes, "AI" no


def ig_base(spec):
    img = r.paper(W, H, seed=17).convert("RGBA")
    for box, color, seed, a in (((-80, 1180, 760, 300), r.BLUE, 3, 70), ((560, 1300, 600, 160), r.CORAL, 4, 90),
                                ((640, 1080, 520, 120), r.BLUE, 5, 50)):
        img.alpha_composite(r.brush(box[2:], color, seed, alpha=a), (box[0], box[1]))
    d = ImageDraw.Draw(img)
    # small brand above the safe zone (decoration only; fine if the Reels header covers it)
    r.spaced(d, (W / 2, 118), "THE HUMAN CURRICULUM", r.sans(24, "SemiBold"), r.NAVY, spacing=6, anchor_center=True)
    top, bot = IG_BAND
    d.rectangle((0, top, W, bot), fill=r.NAVY)
    # tag chip
    tf = r.sans(26, "Bold")
    tag = spec["tag"].upper()
    tw = r.spaced_width(tag, tf, 4)
    x0 = (W - tw - 44) / 2
    d.rounded_rectangle((x0, top + 26, x0 + tw + 44, top + 76), radius=10, fill=r.CORAL)
    r.spaced(d, (x0 + 22, top + 36), tag, tf, (255, 255, 255), spacing=4)
    # hook: as big as fits in 3 lines, CAPS words in yellow
    hook = spec["hook"]
    area_top, area_h = top + 100, bot - top - 128
    f, lines, size = _fit_words(d, hook, lambda s: r.sans(s, "ExtraBold"), IG_TEXT_W, 3, 140, 60, max_h=area_h)
    step = int(size * 1.12)
    y = area_top + max(0, (area_h - step * len(lines)) // 2) + int(size * 0.05)
    any_caps = any(_is_caps(w) for w in hook.split())
    space = d.textlength(" ", font=f)
    for k, words in enumerate(lines):
        lw = d.textlength(" ".join(words), font=f)
        x = (W - lw) / 2
        for w in words:
            if any_caps:
                fill = YELLOW if _is_caps(w) else (255, 255, 255)
            else:
                fill = YELLOW if k == len(lines) - 1 else (255, 255, 255)
            d.text((x, y), w, font=f, fill=fill, stroke_width=5, stroke_fill=r.CORAL)
            x += d.textlength(w, font=f) + space
        y += step
    return img


def draw_ig(num, spec, ep_title, speaker, level, subtitle, sena, daniel, board_key, sena_face=None, daniel_face=None,
            base_cache={}):
    k = ("ig", num, spec["hook"])
    if k not in base_cache:
        base_cache.clear()
        base_cache[k] = ig_base(spec)
    img = base_cache[k].copy()
    for name, pose in (("SENA", sena), ("DANIEL", daniel)):
        active = name == speaker
        fig = r.full_pose(name, pose, sena_face if name == "SENA" else daniel_face) if active else \
            r.faded(name, pose, sena_face if name == "SENA" else daniel_face)
        s = IG_BUST_H[name] / fig.height
        fig = fig.resize((int(fig.width * s), int(fig.height * s)), Image.LANCZOS)
        bob = -8 if (active and level >= 2) else 0
        # keep the drawn figure (its opaque pixels) fully inside the frame width
        bb = fig.getchannel("A").point(lambda v: 255 if v > 24 else 0).getbbox() or (0, 0, fig.width, fig.height)
        x = IG_BUST_X[name] - fig.width // 2
        x = max(-bb[0] + 8, min(x, W - 8 - bb[2]))
        img.alpha_composite(fig, (x, IG_BUST_FLOOR - fig.height + bob))
    # subtitle card in the middle (the main reading surface when muted)
    from PIL import ImageFilter
    x0, y0, x1, y1 = IG_SUB_BOX
    sh = Image.new("RGBA", (x1 - x0 + 60, y1 - y0 + 60), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((30, 38, x1 - x0 + 30, y1 - y0 + 38), radius=36, fill=(60, 50, 40, 70))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(12)), (x0 - 30, y0 - 30))
    d = ImageDraw.Draw(img)
    p = r.PEOPLE[speaker]
    d.rounded_rectangle((x0, y0, x1, y1), radius=36, fill=(255, 255, 255), outline=p["accent"], width=6)
    cw = d.textlength(p["first"], font=r.serif(36, "SemiBold", italic=True)) + 56
    d.rounded_rectangle((x0 + 44, y0 - 30, x0 + 44 + cw, y0 + 30), radius=12, fill=p["accent"])
    d.text((x0 + 44 + cw / 2, y0), p["first"], font=r.serif(36, "SemiBold", italic=True), fill=(255, 255, 255),
           anchor="mm")
    if subtitle:
        f, lines, size = _fit_words(d, subtitle, lambda s: r.sans(s, "ExtraBold"), IG_TEXT_W - 40, 3, 104, 56,
                                    max_h=y1 - y0 - 40, lead=1.18)
        step = int(size * 1.18)
        cy = (y0 + y1) / 2 + 8
        for i, words in enumerate(lines):
            d.text((W / 2, cy + (i - (len(lines) - 1) / 2) * step), " ".join(words), font=f, fill=r.NAVY, anchor="mm")
    return img.convert("RGB")


def encode_ig(lst, wav, mp4):
    """Instagram-safe encode: stereo AAC 44.1 kHz at -14 LUFS (two-pass loudnorm), H.264 High yuv420p 30 fps."""
    up = "aresample=44100,pan=stereo|c0=c0|c1=c0"   # upmix BEFORE measuring: a mono->stereo copy reads +3 LU louder
    m = subprocess.run(["ffmpeg", "-hide_banner", "-i", wav, "-af", up + ",loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json",
                        "-f", "null", "-"], capture_output=True, text=True)
    meas = json.loads(m.stderr[m.stderr.rindex("{"):m.stderr.rindex("}") + 1])
    af = (up + ",loudnorm=I=-14:TP=-1.5:LRA=11:linear=true"
          f":measured_I={meas['input_i']}:measured_TP={meas['input_tp']}:measured_LRA={meas['input_lra']}"
          f":measured_thresh={meas['input_thresh']}:offset={meas['target_offset']},aresample=44100")
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-i", wav,
                    "-vf", "fps=30,format=yuv420p", "-r", "30", "-c:v", "libx264", "-profile:v", "high",
                    "-level", "4.1", "-preset", "medium", "-tune", "stillimage", "-crf", "20",
                    "-af", af, "-c:a", "aac", "-b:a", "160k", "-ar", "44100", "-ac", "2",
                    "-shortest", "-movflags", "+faststart", mp4],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


# ---------- build ----------

def build(num, kind="ai", fake=False, out_dir=None, frame=None, ig=False):
    meta, ep, lines = me.load_episode(num)
    all_specs = specs(num, ep, lines)
    if kind not in all_specs:
        print(f"EP {num:02d}: no {kind} Short in this episode, skipped", flush=True)
        return None
    spec = all_specs[kind]
    if ig:  # Instagram Reel: optional punchier hook, own layout and file name
        spec = dict(spec, hook=spec.get("ig_hook") or spec["hook"])
    paint = draw_ig if ig else draw
    states, pauses = clip_states(num, ep, lines, spec)
    clip = clip_lines(lines, spec)
    icons = set()
    for st in states:
        b = st["board"]
        for key in ("icon", "icons"):
            v = b.get(key)
            icons |= {v} if isinstance(v, str) else set(v or [])
    if icons:
        try:
            import fetch_icons
            fetch_icons.fetch(icons)
        except Exception as e:  # illustrations are a nice-to-have
            print(f"  illustrations skipped: {e}", flush=True)
    out_dir = out_dir or os.path.join(ROOT, "output", f"ep{num:02d}")
    os.makedirs(out_dir, exist_ok=True)
    stem = f"ep{num:02d}_{'reel' if ig else 'short'}_{kind}"
    print(f"EP {num:02d} {kind} {'reel (IG)' if ig else 'short'}: lines {spec['start'] + 1}-{spec['end']} | {spec['hook']}", flush=True)

    if frame is not None:
        i = max(0, min(frame - 1, len(clip) - 1))
        st = states[i]
        sub = me.chunk_text(scenes._strip_quotes(clip[i][1]) or clip[i][1], max_words=4, max_chars=26)[0]
        path = os.path.join(out_dir, f"{stem}_frame{i + 1}.png")
        paint(num, spec, ep["title"], clip[i][0], 2, sub, st["sena"], st["daniel"],
              json.dumps(st["board"], sort_keys=True)).save(path)
        if not ig:
            end_card(num, spec, ep).save(os.path.join(out_dir, f"{stem}_end.png"))
        print(f"  frame: {path}", flush=True)
        return {"frame": path}

    work = os.path.join(out_dir, f"{stem}_work")
    shutil.rmtree(work, ignore_errors=True)
    os.makedirs(work)
    voiced = []
    for i, (spk, text) in enumerate(clip):
        if fake:
            a, words = me.fake_audio(text, spk), []
        else:
            mp3 = os.path.join(work, f"line{i:03d}.mp3")
            words = me.synth(spk, text, mp3, RATE)
            a = me.decode(mp3)
        voiced.append((spk, text, a, words))

    def pause_len(i, a):
        return max(2.5, len(a) / me.SR + 1.0) if i in pauses else 0.0

    def length(v):
        return LEAD + sum(len(a) / me.SR + GAP + pause_len(i, a) for i, (_, _, a, _) in enumerate(v)) + TAIL
    limit = float(spec["max_seconds"])
    n_drill = len(spec.get("phrases") or [])
    if n_drill:
        # explicit lab: keep every phrase drill line; drop dialogue lines from the end of the dialogue to fit
        n_dia = len(voiced) - n_drill
        pauses = {n_dia + j for j in range(n_drill)}
        while n_dia > 1 and length(voiced) > limit:
            n_dia -= 1
            del voiced[n_dia]
            del states[n_dia]
            pauses = {n_dia + j for j in range(n_drill)}
    else:
        # drop lines from the end to fit (never end on a question)
        while len(voiced) > 2 and (length(voiced) > limit or voiced[-1][1].rstrip().endswith("?")):
            voiced.pop()
    if length(voiced) > limit:
        print(f"  WARNING: clip is {length(voiced):.0f}s, over {limit:.0f}s", flush=True)
    states = states[:len(voiced)]

    audio = [np.zeros(int(LEAD * me.SR), np.float32)]
    t = LEAD
    segments, subs, waits = [], [], []  # waits: (start, end, line index) silent "your turn" time
    for i, (spk, text, a, words) in enumerate(voiced):
        dur = len(a) / me.SR
        segments.append((t, t + dur, spk))
        shown = scenes._strip_quotes(text) or text  # Speaking Lab sentences are quoted in the script
        for s0, e0, c in me.time_chunks(me.chunk_text(shown, max_words=4, max_chars=26), words, dur):
            subs.append((t + s0, t + e0, spk, c))
        audio += [a, np.zeros(int(GAP * me.SR), np.float32)]
        t += dur + GAP
        pl = pause_len(i, a)
        if pl:
            audio.append(np.zeros(int(pl * me.SR), np.float32))
            waits.append((t, t + pl, i))
            t += pl
    speech_end = t
    audio.append(np.zeros(int(TAIL * me.SR), np.float32))
    pcm = np.concatenate(audio)
    total = len(pcm) / me.SR
    wav = os.path.join(work, "audio.wav")
    import wave
    with wave.open(wav, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(me.SR)
        w.writeframes((np.clip(pcm, -1, 1) * 32767).astype(np.int16).tobytes())

    n_frames = int(np.ceil(total * FPS))
    hop = me.SR // FPS
    rms = np.array([np.sqrt(np.mean(pcm[i * hop:(i + 1) * hop] ** 2) + 1e-12) for i in range(n_frames)])
    keys, seg_i, sub_i, last = [], 0, 0, voiced[0][0]
    blinks = r.blink_times(total, num * 10 + KINDS.index(kind))
    for fi in range(n_frames):
        tt = fi / FPS
        if tt >= speech_end:  # hold the last picture; the loop restarts at the hook
            tt = speech_end - 0.01
        while seg_i < len(segments) - 1 and tt >= segments[seg_i][1] + GAP / 2 and \
                not any(w0 - GAP <= tt < w1 and wi == seg_i for w0, w1, wi in waits):
            seg_i += 1
        s0, s1, spk = segments[seg_i]
        talking = s0 <= tt < s1
        if talking:
            last = spk
        while sub_i < len(subs) - 1 and tt >= subs[sub_i][1]:
            sub_i += 1
        st_sub = subs[sub_i]
        subtitle = st_sub[3] if st_sub[0] <= tt < st_sub[1] else ""
        level = 0
        if talking:
            rr = rms[fi]
            level = 3 if rr > 0.12 else 2 if rr > 0.05 else 1 if rr > 0.015 else 0
        board = dict(states[seg_i]["board"])
        for w0, w1, wi in waits:
            if w0 <= tt < w1:
                board["countdown"] = max(1, int(np.ceil(w1 - tt)))
                subtitle = "Your turn. Say it out loud."
                break
        st = states[seg_i]
        tn = spk if talking else None
        keys.append((last, level, subtitle, st["sena"], st["daniel"], json.dumps(board, sort_keys=True),
                     r.face_for("SENA", tt, fi, tn, level, blinks), r.face_for("DANIEL", tt, fi, tn, level, blinks)))

    frames_dir = os.path.join(work, "frames")
    os.makedirs(frames_dir)
    cache, listing = {}, []
    run_key, run_len = keys[0], 0
    for k in keys + [None]:
        if k == run_key:
            run_len += 1
            continue
        if run_key not in cache:
            p = os.path.join(frames_dir, f"f{len(cache):05d}.png")
            im = end_card(num, spec, ep) if run_key == ("END",) else paint(num, spec, ep["title"], *run_key)
            im.save(p, compress_level=1)
            cache[run_key] = p
        listing.append((cache[run_key], run_len / FPS))
        run_key, run_len = k, 1
    lst = os.path.join(work, "frames.txt")
    with open(lst, "w") as f:
        for p, dd in listing:
            f.write(f"file '{p}'\nduration {dd:.4f}\n")
        f.write(f"file '{listing[-1][0]}'\n")
    mp4 = os.path.join(out_dir, f"{stem}.mp4")
    if ig:
        encode_ig(lst, wav, mp4)
    else:
        subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-i", wav,
                        "-vf", f"fps={FPS * 2},format=yuv420p", "-c:v", "libx264", "-preset", "medium",
                        "-tune", "stillimage", "-crf", "20", "-c:a", "aac", "-b:a", "160k", "-ar", "48000",
                        "-shortest", "-movflags", "+faststart", mp4],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    shutil.rmtree(work, ignore_errors=True)
    info = {"video": mp4, "kind": kind, "variant": "ig" if ig else "short", "title": spec["title"], "hook": spec["hook"], "duration": round(total, 1),
            "lines": [spec["start"] + 1, spec["start"] + len(voiced) - n_drill]}
    if n_drill:
        info["phrases"] = spec["phrases"]
    json.dump(info, open(os.path.join(out_dir, f"{stem}.json"), "w"), indent=2, ensure_ascii=False)
    print(f"  {len(cache)} unique frames, {total:.1f}s -> {mp4}", flush=True)
    return info


def kinds_of(num):
    meta, ep, lines = me.load_episode(num)
    return list(specs(num, ep, lines))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("episode", type=int)
    ap.add_argument("--kind", default="all", help="ai, story, culture, lab, or all")
    ap.add_argument("--fake-tts", action="store_true")
    ap.add_argument("--out")
    ap.add_argument("--frame", type=int)
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--ig", action="store_true", help="Instagram Reel variant (epNN_reel_KIND.mp4)")
    a = ap.parse_args()
    if a.list:
        print(" ".join(kinds_of(a.episode)))
        sys.exit(0)
    kinds = kinds_of(a.episode) if a.kind == "all" else [a.kind]
    results = [build(a.episode, k, a.fake_tts, a.out, a.frame, a.ig) for k in kinds]
    print(json.dumps([x for x in results if x], indent=2, ensure_ascii=False))
