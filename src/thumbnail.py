"""Editorial collage thumbnail for Human Curriculum (1280x720).

Layout: show masthead + tagline, coral episode tag, big navy serif title with a coral
brush stroke, a subtitle with one coral italic word, a stack of books naming the
episode's real sources, a coral coffee cup with a handwritten note, and the character
cut out over a sky-and-window panel with handwritten keywords and a torn pink note.

Optional fields in episodes.json (all fall back to sensible defaults):
  thumb_title    main title (default: title before ": ")
  thumb_sub      subtitle   (default: title after ": ", or the text in parentheses)
  thumb_accent   word in the subtitle drawn in coral italics (default: longest word)
  thumb_notes    list of 3-4 short handwritten keywords
  thumb_cup      short handwritten line on the cup (default: "Learn what AI can't.")
  thumb_note     line on the torn pink note (default: "Grow your EQ")
  thumb_character  "SENA" or "DANIEL" (default: SENA)
Per-episode pose: put an illustration at episodes/epNN_art.png (light background) to use it
instead of the default character art.
"""
import math
import os
import random
import re

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageOps

import render as R

S = 1.5  # draw at 1920x1080, save at 1280x720
W, H = 1920, 1080
CREAM = (246, 239, 226)
PINK = (236, 168, 160)
SKY_TOP = (196, 214, 232)
SKY_BOT = (236, 226, 214)


def _split_title(ep):
    title = ep.get("title", "")
    main = ep.get("thumb_title")
    sub = ep.get("thumb_sub")
    if main is None:
        if ": " in title:
            main, rest = title.split(": ", 1)
            sub = rest if sub is None else sub
        else:
            m = re.match(r"^(.*?)\s*\((.*)\)\s*$", title)
            if m:
                main, sub0 = m.group(1), m.group(2)
                sub = sub0[:1].upper() + sub0[1:] if sub is None else sub
            else:
                main = title
    return main.strip(), (sub or "").strip()


def _books(ep):
    out = []
    for s in ep.get("sources", []):
        m = re.match(r"^(.*?)\s*\((\d{4})[^)]*\)", s)
        if m:
            name, year = m.group(1).strip(), m.group(2)
        else:
            name, year = s.split(",")[0].strip(), ""
        name = re.sub(r"\s+et al\.?$", " et al.", name)
        if len(name) > 26:
            name = name.split(",")[0].split(" & ")[0] + " et al."
        if name and all(name != b[0] for b in out):
            out.append((name, year))
    return out[:3]


def _notes(ep):
    if ep.get("thumb_notes"):
        return ep["thumb_notes"][:4]
    generic = {"eq", "emotional intelligence", "career", "leadership", "people manager", "audiobook",
               "english learning", "management", "ai", "future of work"}
    return [t[:1].upper() + t[1:] for t in ep.get("tags", []) if t.lower() not in generic][:4]


def _cutout(name, path=None):
    """Character art with its light background made transparent (flood fill from the edges)."""
    base = name.lower()
    path = path or next((os.path.join(R.CHAR_DIR, f) for f in (f"{base}.png", f"{base}.jpg")
                         if os.path.exists(os.path.join(R.CHAR_DIR, f))), None)
    if not path:
        return None
    img = Image.open(path).convert("RGB")
    w, h = img.size
    gray = img.convert("L")
    light = gray.point(lambda v: 255 if v > 232 else 0)
    # pad so the fill can travel all the way around the figure
    pad = Image.new("L", (w + 2, h + 2), 255)
    pad.paste(light, (1, 1))
    ImageDraw.floodfill(pad, (0, 0), 128)
    bg = pad.crop((1, 1, w + 1, h + 1)).point(lambda v: 255 if v == 128 else 0)
    # enclosed patches of the exact paper-white background (e.g. inside a suitcase handle);
    # cream clothing is slightly warmer, so it stays. Opening removes tiny highlights.
    r, g, b = img.split()
    near = ImageChops.multiply(ImageChops.multiply(r.point(lambda v: 255 if v >= 251 else 0),
                                                   g.point(lambda v: 255 if v >= 248 else 0)),
                               b.point(lambda v: 255 if v >= 243 else 0))
    near = near.filter(ImageFilter.MinFilter(9)).filter(ImageFilter.MaxFilter(9))
    bg = ImageChops.lighter(bg, near)
    alpha = ImageChops.invert(bg).filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.GaussianBlur(1.2))
    out = img.convert("RGBA")
    out.putalpha(alpha)
    return out.crop(out.getbbox())


def _torn(size, color, seed, alpha=255):
    w, h = size
    rng = random.Random(seed)
    pts = []
    step = 14
    for x in range(0, w + 1, step):
        pts.append((x, rng.uniform(0, 10)))
    for y in range(0, h + 1, step):
        pts.append((w - rng.uniform(0, 10), y))
    for x in range(w, -1, -step):
        pts.append((x, h - rng.uniform(0, 10)))
    for y in range(h, -1, -step):
        pts.append((rng.uniform(0, 10), y))
    m = Image.new("L", size, 0)
    ImageDraw.Draw(m).polygon(pts, fill=alpha)
    tex = R.paper(w, h, seed=seed).convert("RGB")
    tint = Image.blend(tex, Image.new("RGB", size, color), 0.82)
    out = tint.convert("RGBA")
    out.putalpha(m)
    return out


def _shadow(layer, off=(10, 14), blur=14, strength=0.35):
    sh = Image.new("RGBA", (layer.width + 80, layer.height + 80), (0, 0, 0, 0))
    a = layer.getchannel("A").point(lambda v: int(v * strength))
    sh.paste((60, 45, 35, 255), (40 + off[0], 40 + off[1]), a)
    sh = sh.filter(ImageFilter.GaussianBlur(blur))
    sh.alpha_composite(layer, (40, 40))
    return sh


def _paste(img, layer, xy, rot=0, shadow=True):
    if rot:
        layer = layer.rotate(rot, resample=Image.BICUBIC, expand=True)
    if shadow:
        layer = _shadow(layer)
        xy = (xy[0] - 40, xy[1] - 40)
    img.alpha_composite(layer, (int(xy[0]), int(xy[1])))


def _window_panel(w, h, seed):
    rng = random.Random(seed)
    p = Image.new("RGB", (w, h))
    d = ImageDraw.Draw(p)
    for y in range(h):
        t = y / h
        d.line((0, y, w, y), fill=tuple(int(a + (b - a) * t) for a, b in zip(SKY_TOP, SKY_BOT)))
    # distant skyline
    x = 0
    base = int(h * 0.80)
    while x < w:
        bw = rng.randint(24, 70)
        bh = rng.randint(30, 170)
        d.rectangle((x, base - bh, x + bw, h), fill=(170, 182, 200))
        x += bw + rng.randint(0, 10)
    d.rectangle((0, base, w, h), fill=(214, 204, 192))
    # a plane
    px, py = int(w * 0.70), int(h * 0.16)
    plane = [(0, 0), (90, -6), (110, -2), (90, 4), (0, 6)]
    d.polygon([(px + a, py + b) for a, b in plane], fill=(92, 110, 140))
    d.polygon([(px + 40, py), (70 + px, py - 34), (82 + px, py - 34), (64 + px, py)], fill=(92, 110, 140))
    d.polygon([(px + 40, py + 2), (66 + px, py + 30), (78 + px, py + 30), (62 + px, py + 2)], fill=(92, 110, 140))
    d.polygon([(px + 4, py), (px - 8, py - 22), (px + 4, py - 22), (px + 18, py)], fill=(92, 110, 140))
    # window mullions
    for fx in (int(w * 0.30), int(w * 0.66)):
        d.rectangle((fx, 0, fx + 16, h), fill=(232, 228, 222))
    d.rectangle((0, int(h * 0.42), w, int(h * 0.42) + 12), fill=(232, 228, 222))
    p = p.filter(ImageFilter.GaussianBlur(1.6))
    return Image.blend(p, R.paper(w, h, seed=seed).convert("RGB"), 0.25).convert("RGBA")


def _book(w, h, name, year, color, seed):
    b = _torn((w, h), color, seed)
    b = Image.new("RGBA", (w, h), color + (255,))
    b = Image.blend(b, R.paper(w, h, seed=seed).convert("RGBA"), 0.25)
    d = ImageDraw.Draw(b)
    d.rectangle((0, 0, w, 6), fill=(210, 200, 186))
    d.rectangle((0, h - 6, w, h), fill=(210, 200, 186))
    d.line((w - 70, 10, w - 70, h - 10), fill=(205, 194, 178), width=2)
    fs = 34
    while R.sans(fs, "Bold").getlength(name) > w - 120 and fs > 20:
        fs -= 1
    d.text((26, h * 0.20), name, font=R.sans(fs, "Bold"), fill=R.INK)
    if year:
        d.text((28, h * 0.60), f"({year})", font=R.sans(24, "Regular"), fill=(96, 100, 112))
    return b


def _cup(text):
    w, h = 230, 300
    c = Image.new("RGBA", (w, h + 40), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    body = [(18, 40), (w - 18, 40), (w - 40, h + 36), (40, h + 36)]
    d.polygon(body, fill=(234, 140, 128))
    d.rounded_rectangle((6, 14, w - 6, 48), 10, fill=(34, 34, 40))
    d.rounded_rectangle((26, 0, w - 26, 22), 8, fill=(48, 48, 56))
    tex = R.brush((w - 60, 200), (255, 236, 230), seed=8, alpha=60)
    c.alpha_composite(tex, (30, 90))
    d = ImageDraw.Draw(c)
    words = text.split()
    lines, cur = [], ""
    for wd in words:
        t = (cur + " " + wd).strip()
        if R.hand(46).getlength(t) <= w - 80 or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = wd
    lines.append(cur)
    y = 120
    for ln in lines[:4]:
        d.text((w / 2, y), ln, font=R.hand(46), fill=(60, 30, 34), anchor="mm")
        y += 46
    return c


def _fit_font(text, max_w, start, minimum, italic=False):
    size = start
    while size > minimum and R.serif(size, "Bold", italic).getlength(text) > max_w:
        size -= 2
    return R.serif(size, "Bold", italic)


def draw(ep_num, ep, path):
    main, sub = _split_title(ep)
    img = R.paper(W, H, seed=40 + ep_num).convert("RGBA")
    rng = random.Random(ep_num)

    # right side: window panel on torn paper
    panel = _window_panel(1060, 900, seed=60 + ep_num)
    m = _torn(panel.size, (255, 255, 255), seed=5 + ep_num).getchannel("A")
    panel.putalpha(m)
    _paste(img, panel, (900, 40), rot=1.2)

    # character
    who = ep.get("thumb_character", "SENA").upper()
    # a new pose for this episode: episodes/epNN_art.png (or .jpg), any illustration on a light background
    art = next((os.path.join(R.ROOT, "episodes", f"ep{ep_num:02d}_art.{x}") for x in ("png", "jpg", "jpeg")
                if os.path.exists(os.path.join(R.ROOT, "episodes", f"ep{ep_num:02d}_art.{x}"))), None)
    fig = _cutout(who, art)
    if fig is not None:
        fh = 1030
        fig = fig.resize((int(fig.width * fh / fig.height), fh), Image.LANCZOS)
        _paste(img, fig, (1180, 120), shadow=True)

    d = ImageDraw.Draw(img)
    # handwritten keywords with a brace
    notes = _notes(ep)
    size = 50
    while size > 32 and max((R.hand(size).getlength(n) + i * 8 for i, n in enumerate(notes)), default=0) > 290:
        size -= 2
    nf = R.hand(size)
    nx, ny = 1610, 240
    for i, n in enumerate(notes):
        d.text((nx + i * 8, ny + i * int(size * 1.25)), n, font=nf, fill=R.NAVY)
    if notes:
        bx = nx - 26
        d.arc((bx - 20, ny + 6, bx + 20, ny + len(notes) * int(size * 1.25) - 6), 100, 260, fill=R.NAVY, width=3)

    # torn pink note
    note = _torn((260, 300), PINK, seed=70 + ep_num)
    nd = ImageDraw.Draw(note)
    words = ep.get("thumb_note", "Grow your EQ").split()
    y = 70
    for wd in words[:4]:
        nd.text((130, y), wd, font=R.hand(64), fill=(70, 30, 36), anchor="mm")
        y += 68
    _paste(img, note, (1650, 640), rot=-7)

    # masthead
    d = ImageDraw.Draw(img)
    mf = R.serif(54, "Medium")
    for i, t in enumerate(("The", "Human", "Curriculum")):
        d.text((66, 40 + i * 52), t, font=mf, fill=R.NAVY)
    d.line((380, 52, 380, 186), fill=R.NAVY, width=2)
    for i, t in enumerate(("SCIENCE ×", "EMOTIONAL INTELLIGENCE ×", "REAL-WORLD SKILLS")):
        R.spaced(d, (404, 62 + i * 38), t, R.sans(20, "Medium"), R.NAVY, spacing=3)

    # episode tag
    tag = f"EPISODE {ep_num:02d}"
    tf = R.sans(40, "Medium")
    tw = R.spaced_width(tag, tf, 7)
    d.rectangle((66, 240, 66 + tw + 56, 314), fill=R.CORAL)
    R.spaced(d, (94, 252), tag, tf, (255, 255, 255), spacing=7)

    # main title
    words = main.split()
    lines = [main]
    big = _fit_font(main, 1000, 200, 120)
    if big.getlength(main) > 1000 and len(words) > 1:
        best = None
        for k in range(1, len(words)):
            a, b = " ".join(words[:k]), " ".join(words[k:])
            score = max(len(a), len(b))
            if best is None or score < best[0]:
                best = (score, [a, b])
        lines = best[1]
        big = _fit_font(max(lines, key=len), 1000, 128, 90)
    y = 340
    lh = int(big.size * 1.02)
    for i, ln in enumerate(lines):
        if i == len(lines) - 1:
            lw = int(big.getlength(ln))
            hl = R.brush((min(lw + 70, 1100), int(lh * 0.5)), R.CORAL, seed=41 + ep_num, alpha=170, roughness=0.12)
            img.alpha_composite(hl, (50, int(y + lh * 0.42)))
            d = ImageDraw.Draw(img)
        d.text((60, y), ln, font=big, fill=R.NAVY)
        y += lh

    # subtitle with one coral italic word
    if sub:
        accent = ep.get("thumb_accent") or max(re.findall(r"[\w'’-]+", sub), key=len)
        sf = _fit_font(sub, 900, 92 if len(lines) == 1 else 76, 50)
        sfi = R.serif(sf.size, "Bold", italic=True)
        x = 64
        y += 8
        for part in re.split(r"(\s+)", sub):
            if not part:
                continue
            core = part.strip("\"'“”‘’.,()")
            if part.isspace():
                x += sf.getlength(" ")
                continue
            if core == accent:
                d.text((x, y), part, font=sfi, fill=R.CORAL)
                x += sfi.getlength(part)
            else:
                d.text((x, y), part, font=sf, fill=R.NAVY)
                x += sf.getlength(part)
        y += int(sf.size * 1.2)

    # book stack (bottom left) with the episode's real sources
    books = _books(ep)
    colors = [(250, 247, 240), (240, 233, 220), (246, 241, 232)]
    by = H - 24
    for i, (name, year) in enumerate(reversed(books)):
        bw = 560 - i * 30
        b = _book(bw, 100, name, year, colors[i % 3], seed=90 + i)
        by -= 96
        _paste(img, b, (-10 + rng.randint(0, 30), by), rot=rng.uniform(-2.2, 2.2))

    # cup
    cup = _cup(ep.get("thumb_cup", "Learn what AI can't."))
    _paste(img, cup, (620, H - 360), rot=-3)

    img.convert("RGB").resize((1280, 720), Image.LANCZOS).save(path, quality=92)
    return path
