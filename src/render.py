"""Frame and thumbnail drawing for Human Curriculum videos.

Style: cream paper, navy serif titles, coral and blue brush strokes,
handwritten notes, and illustrated character cards (your own artwork).

Character art goes in assets/characters/:
  sena.png, daniel.png              (required: one illustration each)
  sena_talk.png, daniel_talk.png    (optional: mouth open, used while talking)
A ready-made thumbnail for an episode can be placed at episodes/epNN_thumbnail.png (or .jpg);
it is used as-is instead of a generated one.
"""
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
