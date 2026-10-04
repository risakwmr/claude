"""Frame and thumbnail drawing for Human Curriculum videos.

Style: cream paper, navy serif titles, coral and blue brush strokes,
handwritten notes, and illustrated character cards (your own artwork).

Character art goes in assets/characters/:
  sena.png, daniel.png              (required: one illustration each)
  sena_talk.png, daniel_talk.png    (optional: mouth open, used while talking)
A ready-made thumbnail for an episode can be placed at episodes/epNN_thumbnail.png (or .jpg);
it is used as-is instead of a generated one.
"""
import json
import math
import os
import random
from functools import lru_cache

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_DIR = os.path.join(ROOT, "assets", "fonts")
CHAR_DIR = os.path.join(ROOT, "assets", "characters")

W, H = 1920, 1080
PAPER = (247, 241, 230)
NAVY = (20, 36, 72)
CORAL = (238, 120, 104)
BLUE = (58, 104, 168)
INK = (44, 52, 70)

PEOPLE = {
    "SENA": {"first": "Sena", "role": "Associate · Tokyo", "accent": CORAL, "cx": 600, "tilt": -2.5},
    "DANIEL": {"first": "Daniel", "role": "People Manager · Seattle", "accent": BLUE, "cx": 1320, "tilt": 2.5},
}


# ---------- fonts ----------

@lru_cache(maxsize=None)
def serif(size, weight="Bold", italic=False):
    f = ImageFont.truetype(os.path.join(FONT_DIR, "Lora-Italic-Variable.ttf" if italic else "Lora-Variable.ttf"), size)
    try:
        f.set_variation_by_name(f"{weight} Italic" if italic and weight != "Regular" else ("Italic" if italic else weight))
    except Exception:
        pass
    return f


@lru_cache(maxsize=None)
def sans(size, weight="SemiBold"):
    return ImageFont.truetype(os.path.join(FONT_DIR, f"Inter-{weight}.otf"), size)


@lru_cache(maxsize=None)
def hand(size):
    return ImageFont.truetype(os.path.join(FONT_DIR, "texgyrechorus-mediumitalic.otf"), size)


def spaced(draw, xy, text, fnt, fill, spacing=4, anchor_center=False):
    widths = [draw.textlength(c, font=fnt) for c in text]
    total = sum(widths) + spacing * (len(text) - 1)
    x, y = xy
    if anchor_center:
        x -= total / 2
    for c, w in zip(text, widths):
        draw.text((x, y), c, font=fnt, fill=fill)
        x += w + spacing
    return total


def spaced_width(text, fnt, spacing=4):
    d = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    return sum(d.textlength(c, font=fnt) for c in text) + spacing * (len(text) - 1)


def wrap(draw, text, fnt, max_w, max_lines=None):
    lines, cur = [], ""
    for w in text.split():
        test = (cur + " " + w).strip()
        if draw.textlength(test, font=fnt) <= max_w or not cur:
            cur = test
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines[:max_lines] if max_lines else lines


# ---------- textures ----------

@lru_cache(maxsize=None)
def paper(w, h, seed=7):
    rng = random.Random(seed)
    img = Image.new("RGB", (w, h), PAPER)
    noise = Image.effect_noise((w // 2, h // 2), 18).resize((w, h)).filter(ImageFilter.GaussianBlur(1.2))
    img = Image.blend(img, Image.merge("RGB", [noise] * 3).point(lambda v: 200 + v // 5), 0.08)
    # faint fibres
    d = ImageDraw.Draw(img)
    for _ in range(260):
        x, y = rng.randrange(w), rng.randrange(h)
        d.line((x, y, x + rng.randint(-30, 30), y + rng.randint(-6, 6)), fill=(232, 224, 210), width=1)
    return img


def brush(size, color, seed, alpha=200, roughness=0.35):
    """A dry-brush stroke filling roughly the given box."""
    w, h = size
    rng = random.Random(seed)
    layer = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(layer)
    for i in range(max(6, int(h / 2.2))):
        y = rng.uniform(0.08 * h, 0.92 * h)
        x0 = rng.uniform(0, 0.08 * w)
        x1 = w - rng.uniform(0, 0.12 * w)
        d.line((x0, y, x1, y + rng.uniform(-h * 0.04, h * 0.04)), fill=rng.randint(170, 255),
               width=max(3, int(h * rng.uniform(0.04, 0.12))))
    layer = layer.filter(ImageFilter.GaussianBlur(2.5))
    grain = Image.effect_noise((w, h), 50).filter(ImageFilter.GaussianBlur(0.8)).point(
        lambda v: 255 if v > 255 * roughness * 0.45 else 0)
    mask = Image.composite(layer, Image.new("L", (w, h), 0), grain).point(lambda v: min(255, int(v * alpha / 255)))
    out = Image.new("RGBA", (w, h), color + (0,))
    out.putalpha(mask)
    return out


# ---------- characters ----------

def _placeholder(name):
    p = PEOPLE[name]
    img = Image.new("RGB", (600, 600), PAPER)
    img.paste(paper(600, 600, seed=3))
    wash = brush((520, 420), p["accent"], seed=11 if name == "SENA" else 23, alpha=110)
    img.paste(wash, (40, 90), wash)
    d = ImageDraw.Draw(img)
    d.text((300, 270), p["first"], font=hand(96), fill=NAVY, anchor="mm")
    d.text((300, 360), "illustration goes here", font=sans(26, "Regular"), fill=INK, anchor="mm")
    return img


# Sena sits on the left and looks right; Daniel sits on the right, so his art (looking right) is mirrored.
FACE_LEFT = {"DANIEL"}


@lru_cache(maxsize=None)
def portrait(name, talking=False):
    base = name.lower()
    for fn in ([f"{base}_talk.png", f"{base}_talk.jpg"] if talking else []) + [f"{base}.png", f"{base}.jpg"]:
        path = os.path.join(CHAR_DIR, fn)
        if os.path.exists(path):
            img = Image.open(path).convert("RGB")
            w, h = img.size
            if h > w * 1.15:  # full-body illustration: keep head and upper body
                side = int(w * 0.72)
                top = int(h * 0.01)
                left = (w - side) // 2
                img = img.crop((left, top, left + side, top + side))
            if name in FACE_LEFT:  # turn the art so the two characters face each other
                img = ImageOps.mirror(img)
            return ImageOps.fit(img, (600, 600), Image.LANCZOS, centering=(0.5, 0.35))
    return _placeholder(name)


@lru_cache(maxsize=None)
def card(name, active, talking):
    """Polaroid-style card with the character illustration, rotated slightly."""
    p = PEOPLE[name]
    img = portrait(name, talking and active)
    if not active:
        img = ImageEnhance.Color(img).enhance(0.45)
        img = Image.blend(img, Image.new("RGB", img.size, PAPER), 0.32)
    pad, bottom = 22, 120
    c = Image.new("RGBA", (600 + pad * 2, 600 + pad + bottom), (255, 253, 248, 255))
    c.paste(img, (pad, pad))
    d = ImageDraw.Draw(c)
    d.text((pad + 8, 600 + pad + 18), p["first"], font=hand(66), fill=NAVY if active else (120, 128, 146))
    d.text((pad + 12, 600 + pad + 88), p["role"], font=sans(24, "Medium") if os.path.exists(os.path.join(FONT_DIR, "Inter-Medium.otf")) else sans(24, "Regular"),
           fill=INK if active else (150, 156, 170))
    if active:  # a strip of washi tape
        tape = brush((200, 54), p["accent"], seed=5, alpha=210, roughness=0.15)
        c.alpha_composite(tape, ((c.width - 200) // 2, -6 + 0))
    scale = 0.74 if active else 0.66
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    c = c.rotate(p["tilt"], resample=Image.BICUBIC, expand=True)
    # soft shadow
    sh = Image.new("RGBA", (c.width + 60, c.height + 60), (0, 0, 0, 0))
    a = c.getchannel("A").point(lambda v: int(v * 0.35))
    sh.paste((60, 50, 40, 255), (30, 40), a)
    sh = sh.filter(ImageFilter.GaussianBlur(14))
    sh.alpha_composite(c, (30, 30))
    return sh


# ---------- frame ----------

@lru_cache(maxsize=4)
def base_frame(ep_num, ep_title):
    img = paper(W, H).convert("RGBA")
    for box, color, seed, a in (((1180, -40, 820, 300), BLUE, 1, 120), ((1380, 170, 600, 120), CORAL, 2, 150),
                                ((-80, 860, 760, 260), BLUE, 3, 70), ((-60, 1000, 640, 90), CORAL, 4, 110)):
        s = brush(box[2:], color, seed, alpha=a)
        img.alpha_composite(s, (box[0], box[1]))
    d = ImageDraw.Draw(img)
    spaced(d, (82, 52), "THE", sans(22, "SemiBold"), NAVY, spacing=6)
    d.text((78, 76), "Human Curriculum", font=serif(56, "Bold"), fill=NAVY)
    d.line((640, 66, 640, 140), fill=(190, 182, 168), width=2)
    for i, t in enumerate(("SCIENCE ×", "EQ ×", "GLOBAL CAREER")):
        spaced(d, (664, 66 + i * 26), t, sans(18, "Medium") if os.path.exists(os.path.join(FONT_DIR, "Inter-Medium.otf")) else sans(18, "Regular"), INK, spacing=3)
    # episode tag + title, right side
    tag = f"EPISODE {ep_num:02d}"
    tf = sans(24, "SemiBold")
    tw = spaced_width(tag, tf, 5)
    x1 = W - 90
    d.rectangle((x1 - tw - 44, 58, x1, 104), fill=CORAL)
    spaced(d, (x1 - tw - 22, 66), tag, tf, (255, 255, 255), spacing=5)
    lines = wrap(d, ep_title, serif(34, "SemiBold"), 980, max_lines=2)
    for i, line in enumerate(lines):
        d.text((x1, 124 + i * 44), line, font=serif(34, "SemiBold"), fill=NAVY, anchor="ra")
    # handwritten route note
    d.text((x1, 124 + len(lines) * 44 + 12), "Tokyo → Seattle", font=hand(40), fill=NAVY, anchor="ra")
    return img


def draw_frame(ep_num, ep_title, speaker, level, subtitle):
    """speaker: 'SENA'/'DANIEL'. level: 0-3 voice loudness. subtitle: str or ''."""
    img = base_frame(ep_num, ep_title).copy()
    for name, p in PEOPLE.items():
        active = name == speaker
        c = card(name, active, level >= 2)
        bob = -6 if (active and level >= 2) else 0
        img.alpha_composite(c, (int(p["cx"] - c.width / 2), int(560 - c.height / 2) + bob))
        if active:  # little sound bars next to the name
            d = ImageDraw.Draw(img)
            bx = int(p["cx"] + c.width / 2 - 140)
            by = int(560 + c.height / 2 - 62)
            heights = [(level + k) % 4 for k in (0, 2, 1, 3, 2)]
            for k, hgt in enumerate(heights):
                hh = 10 + hgt * 9 if level else 8
                d.rounded_rectangle((bx + k * 14, by - hh, bx + k * 14 + 8, by), radius=4, fill=p["accent"])

    if subtitle:
        d = ImageDraw.Draw(img)
        f = sans(46, "SemiBold")
        lines = wrap(d, subtitle, f, 1440, max_lines=2)
        box_h = 54 + 60 * len(lines)
        y0 = H - 34 - box_h
        strip = paper(1600, box_h, seed=9).convert("RGBA")
        sd = ImageDraw.Draw(strip)
        sd.rectangle((0, 0, 1599, box_h - 1), outline=(214, 204, 186), width=2)
        shadow = Image.new("RGBA", (1640, box_h + 40), (0, 0, 0, 0))
        shadow.paste((60, 50, 40, 70), (20, 26, 1620, box_h + 26))
        shadow = shadow.filter(ImageFilter.GaussianBlur(10))
        img.alpha_composite(shadow, (140, y0 - 14))
        img.alpha_composite(strip, (160, y0))
        d = ImageDraw.Draw(img)
        p = PEOPLE[speaker]
        d.rounded_rectangle((190, y0 - 26, 370, y0 + 22), radius=8, fill=p["accent"])
        d.text((280, y0 - 3), p["first"], font=serif(32, "SemiBold", italic=True), fill=(255, 255, 255), anchor="mm")
        for i, line in enumerate(lines):
            d.text((W / 2, y0 + 56 + i * 60), line, font=f, fill=NAVY, anchor="mm")
    return img.convert("RGB")


# ---------- thumbnail ----------

def draw_thumbnail(ep_num, short_title, path):
    for ext in ("png", "jpg", "jpeg"):
        custom = os.path.join(ROOT, "episodes", f"ep{ep_num:02d}_thumbnail.{ext}")
        if os.path.exists(custom):
            im = ImageOps.fit(Image.open(custom).convert("RGB"), (1280, 720), Image.LANCZOS)
            im.save(path, quality=90)
            return path
    if isinstance(short_title, dict):  # full episode entry: use the editorial collage layout
        import thumbnail
        return thumbnail.draw(ep_num, short_title, path)
    TW, TH = 1280, 720
    img = paper(TW, TH, seed=12).convert("RGBA")
    s = brush((620, 520), BLUE, seed=31, alpha=90)
    img.alpha_composite(s, (680, 120))
    for name, (x, y, rot) in (("DANIEL", (930, 170, 4), ), ("SENA", (700, 230, -4), )):
        im = portrait(name).resize((380, 380), Image.LANCZOS)
        c = Image.new("RGBA", (404, 470), (255, 253, 248, 255))
        c.paste(im, (12, 12))
        ImageDraw.Draw(c).text((22, 404), PEOPLE[name]["first"], font=hand(48), fill=NAVY)
        c = c.rotate(rot, resample=Image.BICUBIC, expand=True)
        img.alpha_composite(c, (x, y))
    d = ImageDraw.Draw(img)
    spaced(d, (58, 44), "THE", sans(18), NAVY, spacing=5)
    d.text((54, 64), "Human Curriculum", font=serif(44), fill=NAVY)
    tag = f"EPISODE {ep_num:02d}"
    tw = spaced_width(tag, sans(26), 5)
    d.rectangle((58, 150, 58 + tw + 40, 198), fill=CORAL)
    spaced(d, (78, 158), tag, sans(26), (255, 255, 255), spacing=5)
    tf = serif(76, "Bold")
    lines = wrap(d, short_title, tf, 640, max_lines=3)
    y = 228
    for i, line in enumerate(lines):
        if i == len(lines) - 1:
            hl = brush((int(d.textlength(line, font=tf)) + 30, 40), CORAL, seed=41, alpha=150, roughness=0.15)
            img.alpha_composite(hl, (50, y + 52))
            d = ImageDraw.Draw(img)
        d.text((58, y), line, font=tf, fill=NAVY)
        y += 88
    d.text((60, min(y + 20, TH - 90)), "Learn what AI can't.", font=hand(54), fill=CORAL)
    img.convert("RGB").save(path, quality=92)
    return path


# ---------- visual layout (episodes with epNN.visual.json) ----------

FULL_DIR = os.path.join(CHAR_DIR, "full")
ICON_DIR = os.path.join(ROOT, "assets", "icons")
# Art faces right by default. Sena stands on the left and Daniel on the right, so they face each other:
SENA_FLIP = {"idea", "shy", "work", "calm", "fun"}       # Sena poses whose art looks left
DANIEL_KEEP = {"relax"}                                   # Daniel poses already looking left
STAGE = {"SENA": (40, 500), "DANIEL": (1380, 500)}        # x and box width; feet stand at FLOOR
FLOOR = 905
BOARD = (560, 238, 1360, 830)                             # center board box


@lru_cache(maxsize=None)
def full_pose(name, pose):
    who = name.lower()
    path = os.path.join(FULL_DIR, f"{who}_{pose}.png")
    if not os.path.exists(path):
        path = os.path.join(FULL_DIR, f"{who}_default.png")
    img = Image.open(path).convert("RGBA")
    flip = (name == "SENA" and pose in SENA_FLIP) or (name == "DANIEL" and pose not in DANIEL_KEEP)
    if flip:
        img = ImageOps.mirror(img)
    x, bw = STAGE[name]
    max_h = 580
    s = min(bw / img.width, max_h / img.height)
    return img.resize((int(img.width * s), int(img.height * s)), Image.LANCZOS)


@lru_cache(maxsize=None)
def faded(name, pose):
    img = full_pose(name, pose)
    rgb = Image.blend(img.convert("RGB"), Image.new("RGB", img.size, PAPER), 0.28)
    out = rgb.convert("RGBA")
    out.putalpha(img.getchannel("A"))
    return out


@lru_cache(maxsize=None)
def icon(name, size):
    import fetch_icons
    p = fetch_icons.icon_path(name)
    if not os.path.exists(p):
        return None
    im = Image.open(p).convert("RGBA")
    im.thumbnail((size, size), Image.LANCZOS)
    return im


def _fit_font(draw, text, make, max_w, max_lines, start, stop=28, step=4):
    size = start
    while size > stop:
        f = make(size)
        lines = wrap(draw, text, f, max_w)
        if len(lines) <= max_lines:
            return f, lines, size
        size -= step
    f = make(stop)
    return f, wrap(draw, text, f, max_w, max_lines=max_lines), stop


def _label(d, xy, text, color):
    f = sans(22, "SemiBold")
    w = spaced_width(text, f, 4)
    x, y = xy
    d.rounded_rectangle((x, y, x + w + 34, y + 40), radius=8, fill=color)
    spaced(d, (x + 17, y + 7), text, f, (255, 255, 255), spacing=4)
    return w + 34


@lru_cache(maxsize=64)
def board_image(num, board_key):
    """The center card for one board. board_key is a json string of the board dict (+ countdown)."""
    b = json.loads(board_key)
    kind = b.get("type", "none")
    bw, bh = BOARD[2] - BOARD[0], BOARD[3] - BOARD[1]
    if kind == "none":
        return None
    if kind == "cover":
        for ext in ("png", "jpg"):
            p = os.path.join(ROOT, "episodes", f"ep{num:02d}_thumbnail.{ext}")
            if os.path.exists(p):
                im = ImageOps.fit(Image.open(p).convert("RGB"), (bw - 40, int((bw - 40) * 9 / 16)), Image.LANCZOS)
                c = Image.new("RGBA", (im.width + 28, im.height + 28), (255, 253, 248, 255))
                c.paste(im, (14, 14))
                tape = brush((180, 46), CORAL, seed=5, alpha=200, roughness=0.15)
                c.alpha_composite(tape, ((c.width - 180) // 2, -4))
                return c.rotate(-1.2, resample=Image.BICUBIC, expand=True)
        return None
    full_h = bh * 2  # draw on a tall sheet, then shrink to fit if the content runs long
    card_img = Image.new("RGBA", (bw, full_h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card_img)
    pad = 48
    inner = bw - pad * 2
    accent = BLUE if kind in ("study", "compare", "list") else CORAL
    bottom = [0]

    def icons_row(names, size, y):
        ims = [icon(n, size) for n in names]
        ims = [i for i in ims if i is not None]
        if not ims:
            return 0
        total = sum(i.width for i in ims) + 30 * (len(ims) - 1)
        x = (bw - total) // 2
        for i in ims:
            card_img.alpha_composite(i, (x, y + (size - i.height) // 2))
            x += i.width + 30
        return size

    icons = b.get("icons") or ([b["icon"]] if b.get("icon") else [])
    y = 66
    if kind == "keyword":
        h = icons_row(icons[:3], 170 if len(icons) <= 1 else 140, y)
        y += h + (26 if h else 40)
        f, lines, size = _fit_font(d, b.get("text", ""), lambda s: serif(s, "Bold"), inner, 3, 96)
        for line in lines:
            d.text((bw / 2, y), line, font=f, fill=NAVY, anchor="ma")
            y += int(size * 1.15)
        if b.get("sub"):
            fs, sl, ss = _fit_font(d, b["sub"], hand, inner, 2, 54, 34)
            y += 10
            for line in sl:
                d.text((bw / 2, y), line, font=fs, fill=CORAL, anchor="ma")
                y += int(ss * 1.1)
    elif kind == "study":
        _label(d, (pad, 44), "RESEARCH", BLUE)
        d = ImageDraw.Draw(card_img)
        if icons:
            ic = icon(icons[0], 130)
            if ic:
                card_img.alpha_composite(ic, (bw - pad - ic.width, 36))
                d = ImageDraw.Draw(card_img)
        y = 112
        fw, wl, ws = _fit_font(d, b.get("who", ""), lambda s: serif(s, "SemiBold"), inner - 140, 2, 42, 28)
        for line in wl:
            d.text((pad, y), line, font=fw, fill=NAVY)
            y += int(ws * 1.2)
        y += 18
        if b.get("stat"):
            ft, tl, ts = _fit_font(d, b["stat"], lambda s: serif(s, "Bold"), inner, 1, 110, 56)
            for line in tl:
                d.text((pad, y), line, font=ft, fill=CORAL)
                y += int(ts * 1.08)
            y += 12
        fx, xl, xs = _fit_font(d, b.get("text", ""), lambda s: sans(s, "SemiBold"), inner, 3, 44, 28)
        for line in xl:
            d.text((pad, y), line, font=fx, fill=INK)
            y += int(xs * 1.3)
        if b.get("note"):
            y += 14
            fn, nl, ns = _fit_font(d, b["note"], lambda s: serif(s, "Regular", italic=True), inner, 2, 30, 24)
            for line in nl:
                d.text((pad, y), line, font=fn, fill=(120, 116, 108))
                y += int(ns * 1.3)
    elif kind in ("compare", "list"):
        if kind == "compare":
            cols = [b.get("left", {}), b.get("right", {})]
            cw = (inner - 40) // 2
            for k, col in enumerate(cols):
                x = pad + k * (cw + 40)
                _label(d, (x, 44), col.get("title", "").upper(), CORAL if k == 0 else BLUE)
                d = ImageDraw.Draw(card_img)
                yy = 120
                for item in col.get("items", [])[:4]:
                    fi, il, isz = _fit_font(d, item, lambda s: sans(s, "SemiBold"), cw - 30, 3, 38, 26)
                    d.ellipse((x, yy + isz * 0.35, x + 12, yy + isz * 0.35 + 12), fill=CORAL if k == 0 else BLUE)
                    for line in il:
                        d.text((x + 28, yy), line, font=fi, fill=NAVY)
                        yy += int(isz * 1.25)
                    yy += 22
                bottom[0] = max(bottom[0], yy)
            d.line((bw // 2, 110, bw // 2, max(bh, bottom[0]) - 50), fill=(214, 204, 186), width=2)
        else:
            f, lines, size = _fit_font(d, b.get("title", ""), lambda s: serif(s, "Bold"), inner, 2, 58, 36)
            for line in lines:
                d.text((pad, y - 10), line, font=f, fill=NAVY)
                y += int(size * 1.15)
            y += 20
            for k, item in enumerate(b.get("items", [])[:4]):
                d.ellipse((pad, y, pad + 52, y + 52), fill=BLUE)
                d.text((pad + 26, y + 26), str(k + 1), font=sans(30, "SemiBold"), fill=(255, 255, 255), anchor="mm")
                fi, il, isz = _fit_font(d, item, lambda s: sans(s, "SemiBold"), inner - 80, 2, 40, 28)
                yy = y + 6
                for line in il:
                    d.text((pad + 76, yy), line, font=fi, fill=NAVY)
                    yy += int(isz * 1.25)
                y = max(y + 74, yy + 18)
    elif kind == "story":
        _label(d, (pad, 44), "DANIEL'S STORY", BLUE)
        d = ImageDraw.Draw(card_img)
        y = 120
        h = icons_row(icons[:2], 150, y)
        y += h + 24
        f, lines, size = _fit_font(d, b.get("title", ""), lambda s: serif(s, "Bold"), inner, 2, 72, 40)
        for line in lines:
            d.text((bw / 2, y), line, font=f, fill=NAVY, anchor="ma")
            y += int(size * 1.15)
        if b.get("text"):
            fs, sl, ss = _fit_font(d, b["text"], hand, inner, 2, 52, 34)
            y += 8
            for line in sl:
                d.text((bw / 2, y), line, font=fs, fill=CORAL, anchor="ma")
                y += int(ss * 1.1)
    elif kind in ("repeat", "question"):
        countdown = b.get("countdown")
        if kind == "repeat":
            _label(d, (pad, 44), "YOUR TURN · SAY IT OUT LOUD" if countdown is not None else "SPEAKING LAB · REPEAT",
                   CORAL)
        else:
            _label(d, (pad, 44), "YOUR TURN · 40 SECONDS", CORAL)
        d = ImageDraw.Draw(card_img)
        f, lines, size = _fit_font(d, b.get("text", ""), lambda s: serif(s, "Bold"), inner, 4, 76, 40)
        total = len(lines) * int(size * 1.2)
        y = max(120, (bh - total) // 2 - (40 if countdown is not None else 0))
        for line in lines:
            d.text((bw / 2, y), line, font=f, fill=NAVY, anchor="ma")
            y += int(size * 1.2)
        if countdown is not None:
            cx, cy, r = bw // 2, bh - 92, 46
            d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=CORAL, width=6)
            d.text((cx, cy), str(countdown), font=sans(44, "SemiBold"), fill=CORAL, anchor="mm")
        elif kind == "question":
            d.text((bw / 2, bh - 90), "Pause and answer out loud", font=hand(46), fill=CORAL, anchor="ma")
    elif kind == "challenge":
        _label(d, (pad, 44), "TODAY'S CHALLENGE", CORAL)
        d = ImageDraw.Draw(card_img)
        y = 130
        h = icons_row(icons[:1], 140, y)
        y += h + (20 if h else 10)
        f, lines, size = _fit_font(d, b.get("text", ""), lambda s: serif(s, "Bold"), inner, 2, 80, 44)
        for line in lines:
            d.text((bw / 2, y), line, font=f, fill=NAVY, anchor="ma")
            y += int(size * 1.15)
        if b.get("sub"):
            y += 16
            fs, sl, ss = _fit_font(d, b["sub"], lambda s: sans(s, "Regular"), inner, 4, 34, 26)
            for line in sl:
                d.text((bw / 2, y), line, font=fs, fill=INK, anchor="ma")
                y += int(ss * 1.35)
    used = max(y, bottom[0]) + 40
    content = card_img.crop((0, 0, bw, max(used, bh)))
    if used > bh:  # shrink everything to fit the board
        k = bh / used
        content = content.resize((int(bw * k), bh), Image.LANCZOS)
    final = paper(bw, bh, seed=21).convert("RGBA")
    final.alpha_composite(content, ((bw - content.width) // 2, 0))
    ImageDraw.Draw(final).rectangle((0, 0, bw - 1, bh - 1), outline=(220, 210, 192), width=2)
    tape = brush((200, 48), accent, seed=8, alpha=190, roughness=0.15)
    final.alpha_composite(tape, ((bw - 200) // 2, -10))
    card_img = final
    # soft shadow around the card
    sh = Image.new("RGBA", (bw + 60, bh + 60), (0, 0, 0, 0))
    sh.paste((60, 50, 40, 60), (30, 38, bw + 30, bh + 38))
    sh = sh.filter(ImageFilter.GaussianBlur(12))
    sh.alpha_composite(card_img, (30, 30))
    return sh


@lru_cache(maxsize=4)
def scene_base(ep_num, ep_title):
    return base_frame(ep_num, ep_title)


def draw_scene_frame(ep_num, ep_title, speaker, level, subtitle, sena_pose, daniel_pose, section, board_key):
    img = scene_base(ep_num, ep_title).copy()
    d = ImageDraw.Draw(img)
    if section:
        _label(d, (82, 168), section.upper(), NAVY)
    board = board_image(ep_num, board_key)
    if board is not None:
        bx = (BOARD[0] + BOARD[2]) // 2 - board.width // 2
        by = (BOARD[1] + BOARD[3]) // 2 - board.height // 2
        img.alpha_composite(board, (bx, by))
    for name, pose in (("SENA", sena_pose), ("DANIEL", daniel_pose)):
        active = name == speaker
        fig = full_pose(name, pose) if active else faded(name, pose)
        x, bw = STAGE[name]
        bob = -6 if (active and level >= 2) else 0
        img.alpha_composite(fig, (x + (bw - fig.width) // 2, FLOOR - fig.height + bob))
    d = ImageDraw.Draw(img)
    if subtitle:
        f = sans(44, "SemiBold")
        lines = wrap(d, subtitle, f, 1440, max_lines=2)
        box_h = 50 + 58 * len(lines)
        y0 = H - 30 - box_h
        strip = paper(1600, box_h, seed=9).convert("RGBA")
        sd = ImageDraw.Draw(strip)
        sd.rectangle((0, 0, 1599, box_h - 1), outline=(214, 204, 186), width=2)
        img.alpha_composite(strip, (160, y0))
        d = ImageDraw.Draw(img)
        p = PEOPLE[speaker]
        d.rounded_rectangle((190, y0 - 24, 360, y0 + 20), radius=8, fill=p["accent"])
        d.text((275, y0 - 2), p["first"], font=serif(30, "SemiBold", italic=True), fill=(255, 255, 255), anchor="mm")
        for i, line in enumerate(lines):
            d.text((W / 2, y0 + 52 + i * 58), line, font=f, fill=NAVY, anchor="mm")
    return img.convert("RGB")
