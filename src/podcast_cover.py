"""Square cover for the show's playlist (YouTube needs a 1:1 playlist image before it can be marked as a podcast).

python src/podcast_cover.py      writes assets/podcast_cover.jpg (2048 x 2048)
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageOps

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render import CORAL, INK, NAVY, PAPER, ROOT, sans, serif, spaced  # noqa: E402

S = 2048
OUT = os.path.join(ROOT, "assets", "podcast_cover.jpg")


def card(path, w, h, tilt):
    """The character on a white card with a soft shadow, slightly tilted (collage style)."""
    art = Image.open(path).convert("RGB")
    bg = art.getpixel((5, 5))
    art = ImageOps.pad(art, (w - 60, h - 60), color=bg, centering=(0.5, 0.5))
    c = Image.new("RGBA", (w, h), bg + (255,))
    c.paste(art, (30, 30))
    pad = 60
    shadow = Image.new("RGBA", (w + pad * 2, h + pad * 2), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rectangle((pad + 14, pad + 22, pad + w + 14, pad + h + 22), fill=(20, 36, 72, 70))
    shadow = shadow.filter(ImageFilter.GaussianBlur(22))
    shadow.paste(c, (pad, pad), c)
    return shadow.rotate(tilt, resample=Image.BICUBIC, expand=True)


def main():
    im = Image.new("RGB", (S, S), PAPER)
    d = ImageDraw.Draw(im)
    # brush-like accents
    d.rectangle((0, 0, S, 26), fill=CORAL)
    d.rectangle((0, S - 26, S, S), fill=NAVY)

    label = "ENGLISH PODCAST"
    f = sans(64, "Bold")
    spaced(d, (S // 2, 150), label, f, CORAL, spacing=12, anchor_center=True)
    for i, word in enumerate(["Human", "Curriculum"]):
        ft = serif(250, "Bold")
        w = d.textlength(word, font=ft)
        d.text(((S - w) / 2, 230 + i * 260), word, font=ft, fill=NAVY)
    sub = "Learn what AI can't do"
    fs = serif(104, "Medium", italic=True)
    d.text(((S - d.textlength(sub, font=fs)) / 2, 790), sub, font=fs, fill=CORAL)
    line = "EQ  ·  careers  ·  natural English"
    fl = sans(56, "Medium")
    d.text(((S - d.textlength(line, font=fl)) / 2, 935), line, font=fl, fill=INK)

    chars = os.path.join(ROOT, "assets", "characters")
    left = card(os.path.join(chars, "sena.png"), 720, 780, 4)
    right = card(os.path.join(chars, "daniel.png"), 720, 780, -4)
    im.paste(left, (170, 1010), left)
    im.paste(right, (S - 170 - right.width, 1010), right)
    fn = sans(54, "SemiBold")
    for x, name in ((170 + left.width // 2, "Sena · Tokyo"), (S - 170 - right.width // 2, "Daniel · Seattle")):
        w = d.textlength(name, font=fn)
        d.rounded_rectangle((x - w / 2 - 34, 1850, x + w / 2 + 34, 1930), 40, fill=NAVY)
        d.text((x - w / 2, 1861), name, font=fn, fill=(255, 255, 255))
    im.save(OUT, quality=92)
    print(OUT)


if __name__ == "__main__":
    main()
