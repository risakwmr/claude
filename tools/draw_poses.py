"""Draw Sena and Daniel in expressive, simplified (chibi-ish) poses as SVG, then render PNGs.

Run:  python tools/draw_poses.py           -> assets/characters/poses/<name>.png
Needs Python Playwright with Chromium (only for rendering; the PNGs are committed).
"""
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "characters", "poses")

INK = "#1d1b1e"
SKIN, SKIN_SH = "#fde3d3", "#f2c4ae"
BLUSH = "#f6a8a0"
LW = 7  # outline width

SENA = dict(hair="#6a4636", hair_hi="#8a5e48", top="#ec9a92", top_sh="#d97f78", cuff="#e3887f",
            pants="#f4ecdf", pants_sh="#e2d6c4", shoe="#f7f5f0", shoe_sh="#7d8794")
DANIEL = dict(hair="#7a5232", hair_hi="#9b6d45", top="#b9d3ee", top_sh="#9dbbe0", cuff="#a9c6e8",
              pants="#1f3d74", pants_sh="#16305d", shoe="#f7f5f0", shoe_sh="#7d8794", belt="#7a5232")


# ---------- small helpers ----------

def rot(p, c, deg):
    a = math.radians(deg)
    x, y = p[0] - c[0], p[1] - c[1]
    return (c[0] + x * math.cos(a) - y * math.sin(a), c[1] + x * math.sin(a) + y * math.cos(a))


def tube(points, color, width, cap="round"):
    """A limb: thick colored stroke over a slightly thicker ink stroke."""
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in points)
    return (f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{width + 2 * LW}" '
            f'stroke-linecap="{cap}" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" '
            f'stroke-linecap="{cap}" stroke-linejoin="round"/>')


def hand(p, r=25):
    return (f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="{r}" fill="{SKIN}" stroke="{INK}" stroke-width="{LW - 1}"/>')


def cuff(p, q, color, width):
    """A short ribbed cuff just before the hand, along the forearm direction."""
    dx, dy = p[0] - q[0], p[1] - q[1]
    n = math.hypot(dx, dy) or 1
    a = (p[0] - dx / n * 30, p[1] - dy / n * 30)
    return tube([a, (p[0] - dx / n * 6, p[1] - dy / n * 6)], color, width + 6, cap="butt")


# ---------- props ----------

def prop(name, p, ch):
    x, y = p
    if name == "coffee":
        return (f'<g transform="translate({x - 26},{y - 70})">'
                f'<path d="M4,18 L52,18 L46,96 L10,96 Z" fill="#fff" stroke="{INK}" stroke-width="{LW - 1}" stroke-linejoin="round"/>'
                f'<path d="M8,46 L48,46 L46,70 L10,70 Z" fill="#b07d5b" stroke="{INK}" stroke-width="4"/>'
                f'<rect x="-2" y="4" width="60" height="18" rx="6" fill="#2b2a2e" stroke="{INK}" stroke-width="4"/></g>')
    if name == "mug":
        return (f'<g transform="translate({x - 34},{y - 40})">'
                f'<path d="M62,22 q26,4 18,30 q-6,16 -20,12" fill="none" stroke="{INK}" stroke-width="16"/>'
                f'<path d="M62,22 q26,4 18,30 q-6,16 -20,12" fill="none" stroke="#25427a" stroke-width="6"/>'
                f'<rect x="0" y="0" width="68" height="80" rx="10" fill="#25427a" stroke="{INK}" stroke-width="{LW - 1}"/></g>')
    if name == "pen":
        return (f'<g transform="translate({x},{y}) rotate(-35)">'
                f'<rect x="-6" y="-70" width="12" height="80" rx="5" fill="#2b2a2e" stroke="{INK}" stroke-width="3"/>'
                f'<path d="M-6,10 L0,26 L6,10 Z" fill="#d9b25a" stroke="{INK}" stroke-width="3"/></g>')
    if name == "notebook":
        return (f'<g transform="translate({x - 90},{y - 70}) rotate(-8 90 70)">'
                f'<rect x="0" y="0" width="180" height="130" rx="8" fill="#fffaf2" stroke="{INK}" stroke-width="{LW - 1}"/>'
                f'<line x1="90" y1="4" x2="90" y2="126" stroke="{INK}" stroke-width="4"/>'
                + "".join(f'<line x1="14" y1="{28 + i * 22}" x2="78" y2="{28 + i * 22}" stroke="#c9bfae" stroke-width="3"/>'
                          f'<line x1="102" y1="{28 + i * 22}" x2="166" y2="{28 + i * 22}" stroke="#c9bfae" stroke-width="3"/>'
                          for i in range(4)) + '</g>')
    if name == "phone":
        return (f'<g transform="translate({x - 30},{y - 80}) rotate(-10 30 50)">'
                f'<rect x="0" y="0" width="60" height="104" rx="12" fill="#2b2a2e" stroke="{INK}" stroke-width="{LW - 1}"/>'
                f'<rect x="7" y="9" width="46" height="80" rx="6" fill="#bfe0f5"/></g>')
    if name == "suitcase":
        return (f'<g transform="translate({x - 70},{y})">'
                f'<rect x="58" y="-110" width="10" height="120" fill="#2b2a2e" stroke="{INK}" stroke-width="4"/>'
                f'<rect x="20" y="-118" width="90" height="16" rx="6" fill="#2b2a2e" stroke="{INK}" stroke-width="4"/>'
                f'<rect x="0" y="0" width="130" height="200" rx="16" fill="#e59a90" stroke="{INK}" stroke-width="{LW}"/>'
                + "".join(f'<line x1="{26 + i * 26}" y1="18" x2="{26 + i * 26}" y2="182" stroke="#c8776e" stroke-width="5"/>' for i in range(4))
                + f'<circle cx="22" cy="214" r="12" fill="#2b2a2e"/><circle cx="108" cy="214" r="12" fill="#2b2a2e"/></g>')
    if name == "badge":
        return (f'<path d="M{x - 24},{y - 150} L{x},{y - 20} L{x + 24},{y - 150}" fill="none" stroke="#25427a" stroke-width="7"/>'
                f'<rect x="{x - 22}" y="{y - 24}" width="44" height="58" rx="5" fill="#fff" stroke="{INK}" stroke-width="5"/>')
    if name == "dog":  # a golden retriever sitting, wearing a navy bandana
        g, gs = "#e9b97a", "#d29a5a"
        return (f'<g transform="translate({x - 110},{y - 230})">'
                f'<path d="M60,230 C30,160 50,100 110,90 C170,90 190,160 170,230 Z" fill="{g}" stroke="{INK}" stroke-width="{LW}"/>'
                f'<path d="M150,215 q60,-10 60,-60" fill="none" stroke="{INK}" stroke-width="30" stroke-linecap="round"/>'
                f'<path d="M150,215 q60,-10 60,-60" fill="none" stroke="{g}" stroke-width="18" stroke-linecap="round"/>'
                f'<path d="M222,150 q12,-8 20,-24 M228,170 q16,-4 26,-16" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'
                f'<circle cx="110" cy="70" r="62" fill="{g}" stroke="{INK}" stroke-width="{LW}"/>'
                f'<path d="M52,40 C20,60 24,120 50,128 C66,110 62,70 60,46 Z" fill="{gs}" stroke="{INK}" stroke-width="5"/>'
                f'<path d="M168,40 C200,60 196,120 170,128 C154,110 158,70 160,46 Z" fill="{gs}" stroke="{INK}" stroke-width="5"/>'
                f'<ellipse cx="110" cy="96" rx="34" ry="24" fill="#f6dcb6" stroke="{INK}" stroke-width="4"/>'
                f'<ellipse cx="110" cy="84" rx="12" ry="8" fill="{INK}"/>'
                f'<path d="M100,104 q10,22 20,0" fill="#f08a8a" stroke="{INK}" stroke-width="4"/>'
                f'<circle cx="86" cy="62" r="7" fill="{INK}"/><circle cx="134" cy="62" r="7" fill="{INK}"/>'
                f'<path d="M66,128 L154,128 L110,170 Z" fill="#25427a" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>'
                f'<ellipse cx="80" cy="232" rx="24" ry="12" fill="{g}" stroke="{INK}" stroke-width="5"/>'
                f'<ellipse cx="140" cy="232" rx="24" ry="12" fill="{g}" stroke="{INK}" stroke-width="5"/></g>')
    return ""


def fx(name, x, y, s=1.0):
    """Expressive effects: motion lines, sparkles, idea bulb, heart, sweat drop, notes."""
    if name == "sparkle":
        def star(cx, cy, r):
            return (f'<path d="M{cx},{cy - r} Q{cx + r * .18},{cy - r * .18} {cx + r},{cy} Q{cx + r * .18},{cy + r * .18} '
                    f'{cx},{cy + r} Q{cx - r * .18},{cy + r * .18} {cx - r},{cy} Q{cx - r * .18},{cy - r * .18} {cx},{cy - r} Z" '
                    f'fill="#ffd36a" stroke="{INK}" stroke-width="4"/>')
        return star(x, y, 30 * s) + star(x + 50 * s, y + 46 * s, 18 * s) + star(x - 36 * s, y + 56 * s, 13 * s)
    if name == "bulb":
        return (f'<g transform="translate({x},{y}) scale({s})">'
                + "".join(f'<line x1="{math.cos(math.radians(a)) * 62:.0f}" y1="{math.sin(math.radians(a)) * 62:.0f}" '
                          f'x2="{math.cos(math.radians(a)) * 86:.0f}" y2="{math.sin(math.radians(a)) * 86:.0f}" '
                          f'stroke="#f2b632" stroke-width="7" stroke-linecap="round"/>' for a in range(-180, 1, 36))
                + f'<circle cx="0" cy="0" r="46" fill="#ffe28a" stroke="{INK}" stroke-width="6"/>'
                f'<rect x="-20" y="40" width="40" height="28" rx="6" fill="#c9c3b8" stroke="{INK}" stroke-width="5"/></g>')
    if name == "heart":
        return (f'<path transform="translate({x},{y}) scale({s})" d="M0,18 C-30,-8 -52,22 0,58 C52,22 30,-8 0,18 Z" '
                f'fill="#f08a8a" stroke="{INK}" stroke-width="5"/>')
    if name == "sweat":
        return (f'<path transform="translate({x},{y}) scale({s})" d="M0,0 C14,22 20,34 10,44 C0,52 -14,44 -10,30 C-8,20 -4,12 0,0 Z" '
                f'fill="#a9d6f5" stroke="{INK}" stroke-width="4"/>')
    if name == "motion":
        return "".join(f'<path d="M{x},{y + i * 34} q{-40 * s},6 {-90 * s},2" fill="none" stroke="{INK}" '
                       f'stroke-width="6" stroke-linecap="round"/>' for i in range(3))
    if name == "pulse":
        return (f'<path d="M{x - 70},{y} l30,0 l14,-34 l18,62 l16,-46 l12,18 l40,0" fill="none" stroke="#e8746a" '
                f'stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>')
    if name == "zzz":  # calm breathing marks
        return "".join(f'<path d="M{x + i * 26},{y - i * 30} q14,-14 28,0" fill="none" stroke="#7fb0d8" stroke-width="6" stroke-linecap="round"/>'
                       for i in range(3))
    if name == "question":
        return f'<text x="{x}" y="{y}" font-size="{90 * s:.0f}" font-family="Georgia" font-weight="bold" fill="#e8746a" stroke="{INK}" stroke-width="3">?</text>'
    if name == "exclaim":
        return f'<text x="{x}" y="{y}" font-size="{100 * s:.0f}" font-family="Georgia" font-weight="bold" fill="#f2b632" stroke="{INK}" stroke-width="3">!</text>'
    return ""


# ---------- face ----------

def face(eyes, mouth, glasses=False):
    out = []
    ex = (-52, 52)
    if eyes == "open":
        for x in ex:
            out.append(f'<ellipse cx="{x}" cy="10" rx="13" ry="18" fill="{INK}"/><circle cx="{x + 4}" cy="3" r="5" fill="#fff"/>')
    elif eyes == "closed":  # relaxed, eyes softly shut
        for x in ex:
            out.append(f'<path d="M{x - 18},8 Q{x},24 {x + 18},8" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>')
    elif eyes == "happy":
        for x in ex:
            out.append(f'<path d="M{x - 18},16 Q{x},-6 {x + 18},16" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>')
    elif eyes == "sparkle":
        for x in ex:
            out.append(f'<ellipse cx="{x}" cy="10" rx="15" ry="20" fill="{INK}"/><circle cx="{x + 5}" cy="2" r="6" fill="#fff"/>'
                       f'<circle cx="{x - 5}" cy="18" r="3" fill="#fff"/>')
    elif eyes == "look_up":
        for x in ex:
            out.append(f'<ellipse cx="{x + 4}" cy="2" rx="13" ry="18" fill="{INK}"/><circle cx="{x + 8}" cy="-6" r="5" fill="#fff"/>')
    elif eyes == "wide":
        for x in ex:
            out.append(f'<circle cx="{x}" cy="10" r="20" fill="#fff" stroke="{INK}" stroke-width="5"/><circle cx="{x}" cy="12" r="9" fill="{INK}"/>')
    # brows
    by = -26 if eyes in ("wide", "sparkle", "look_up") else -20
    for x in ex:
        out.append(f'<path d="M{x - 16},{by} Q{x},{by - 8} {x + 16},{by}" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>')
    if glasses:
        for x in ex:
            out.append(f'<circle cx="{x}" cy="10" r="31" fill="none" stroke="{INK}" stroke-width="6"/>')
        out.append(f'<path d="M-21,6 Q0,-4 21,6" fill="none" stroke="{INK}" stroke-width="6"/>')
    # blush
    for x in (-74, 74):
        out.append(f'<ellipse cx="{x}" cy="48" rx="20" ry="11" fill="{BLUSH}" opacity=".8"/>')
    # mouth
    if mouth == "smile":
        out.append(f'<path d="M-16,58 Q0,72 16,58" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>')
    elif mouth == "open":
        out.append(f'<path d="M-20,54 Q0,54 20,54 Q18,84 0,86 Q-18,84 -20,54 Z" fill="#c8545e" stroke="{INK}" stroke-width="5"/>'
                   f'<path d="M-10,76 Q0,68 10,76 Q6,84 0,84 Q-6,84 -10,76 Z" fill="#f09098"/>')
    elif mouth == "o":
        out.append(f'<ellipse cx="0" cy="64" rx="10" ry="12" fill="#c8545e" stroke="{INK}" stroke-width="5"/>')
    elif mouth == "grin":
        out.append(f'<path d="M-26,52 Q0,56 26,52 Q22,82 0,84 Q-22,82 -26,52 Z" fill="#fff" stroke="{INK}" stroke-width="5"/>')
    elif mouth == "calm":
        out.append(f'<path d="M-10,62 Q0,66 10,62" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>')
    return "".join(out)


# ---------- heads ----------

def sena_head(c, eyes, mouth, sway=0):
    h = SENA
    back = (f'<path d="M-150,-40 C-180,80 -200,200 -170,300 C-150,330 -120,300 -130,250 C-110,300 -60,320 -70,250 '
            f'L70,250 C60,320 110,300 130,250 C120,300 150,330 170,300 C200,200 180,80 150,-40 Z" '
            f'transform="rotate({sway})" fill="{h["hair"]}" stroke="{INK}" stroke-width="{LW}" stroke-linejoin="round"/>')
    wave = "".join(f'<path d="M{s * 150},{40 + i * 70} q{s * 20},30 0,60" fill="none" stroke="{h["hair_hi"]}" stroke-width="6" stroke-linecap="round"/>'
                   for s in (-1, 1) for i in range(3))
    head = f'<ellipse cx="0" cy="10" rx="138" ry="140" fill="{SKIN}" stroke="{INK}" stroke-width="{LW}"/>'
    ears = "".join(f'<circle cx="{s * 136}" cy="40" r="10" fill="#f1c35b" stroke="{INK}" stroke-width="4"/>' for s in (-1, 1))
    bangs = (f'<path d="M-150,30 C-160,-90 -70,-160 10,-150 C110,-150 170,-80 150,30 C130,-30 100,-60 60,-66 '
             f'C40,-30 -10,-20 -40,-50 C-70,-40 -110,-10 -150,30 Z" fill="{h["hair"]}" stroke="{INK}" stroke-width="{LW}" stroke-linejoin="round"/>'
             f'<path d="M-60,-130 Q-90,-80 -100,-30" fill="none" stroke="{h["hair_hi"]}" stroke-width="6" stroke-linecap="round"/>')
    shades = (f'<g transform="translate(0,-150) rotate(-4)">'
              f'<rect x="-92" y="-24" width="72" height="44" rx="16" fill="#2b2a2e" stroke="{INK}" stroke-width="5"/>'
              f'<rect x="20" y="-24" width="72" height="44" rx="16" fill="#2b2a2e" stroke="{INK}" stroke-width="5"/>'
              f'<path d="M-20,-6 Q0,-16 20,-6" fill="none" stroke="{INK}" stroke-width="6"/></g>')
    back = back + wave
    return back, (f'<g transform="translate({c[0]:.1f},{c[1]:.1f})">{head}{ears}'
                  f'<g transform="translate(0,20)">{face(eyes, mouth)}</g>{bangs}{shades}</g>')


def daniel_head(c, eyes, mouth, sway=0):
    h = DANIEL
    head = f'<ellipse cx="0" cy="14" rx="128" ry="136" fill="{SKIN}" stroke="{INK}" stroke-width="{LW}"/>'
    ears = "".join(f'<ellipse cx="{s * 128}" cy="34" rx="18" ry="26" fill="{SKIN}" stroke="{INK}" stroke-width="{LW - 1}"/>' for s in (-1, 1))
    hair = (f'<path d="M-140,30 C-170,-80 -90,-170 10,-160 C120,-160 170,-90 140,30 C130,-10 118,-36 100,-50 '
            f'C90,-26 60,-30 50,-60 C20,-30 -30,-34 -50,-62 C-70,-30 -100,-30 -110,-46 C-124,-20 -134,0 -140,30 Z" '
            f'fill="{h["hair"]}" stroke="{INK}" stroke-width="{LW}" stroke-linejoin="round"/>'
            f'<path d="M-40,-140 q30,-30 70,-10 q30,16 50,-10" fill="none" stroke="{h["hair_hi"]}" stroke-width="6" stroke-linecap="round"/>')
    return "", (f'<g transform="translate({c[0]:.1f},{c[1]:.1f})">{ears}{head}'
                f'<g transform="translate(0,22)">{face(eyes, mouth, glasses=False)}</g>{hair}</g>')


# ---------- bodies ----------

def torso(who, colors):
    c = colors
    body = (f'<path d="M-150,-10 C-150,-70 -90,-90 0,-90 C90,-90 150,-70 150,-10 L170,190 C120,215 -120,215 -170,190 Z" '
            f'fill="{c["top"]}" stroke="{INK}" stroke-width="{LW}" stroke-linejoin="round"/>')
    if who == "SENA":
        collar = (f'<path d="M-62,-92 C-60,-50 60,-50 62,-92 C40,-112 -40,-112 -62,-92 Z" fill="{c["cuff"]}" stroke="{INK}" stroke-width="{LW - 1}"/>'
                  + "".join(f'<line x1="{x}" y1="-96" x2="{x}" y2="-66" stroke="{c["top_sh"]}" stroke-width="4"/>' for x in range(-40, 41, 16))
                  + f'<path d="M-160,170 C-80,200 80,200 160,170 L166,196 C80,226 -80,226 -166,196 Z" fill="{c["cuff"]}" stroke="{INK}" stroke-width="{LW - 1}"/>')
        detail = f'<path d="M-90,40 Q-60,80 -80,140 M90,40 Q60,80 80,140" fill="none" stroke="{c["top_sh"]}" stroke-width="6" stroke-linecap="round"/>'
    else:
        collar = (f'<path d="M-50,-92 L0,-40 L50,-92 L30,-104 L0,-74 L-30,-104 Z" fill="#fff" stroke="{INK}" stroke-width="{LW - 1}" stroke-linejoin="round"/>'
                  f'<line x1="0" y1="-40" x2="0" y2="190" stroke="{c["top_sh"]}" stroke-width="5"/>'
                  + "".join(f'<circle cx="0" cy="{y}" r="5" fill="{INK}"/>' for y in (-10, 50, 110))
                  + f'<rect x="-168" y="180" width="336" height="26" rx="6" fill="{c["belt"]}" stroke="{INK}" stroke-width="{LW - 1}"/>'
                  f'<rect x="-18" y="178" width="36" height="30" rx="4" fill="#d9b25a" stroke="{INK}" stroke-width="4"/>')
        detail = (f'<path d="M-50,-92 L-30,-104 M50,-92" fill="none"/>'
                  f'<path d="M-24,-60 L-6,90 M24,-60 L6,90" fill="none" stroke="#25427a" stroke-width="7"/>'
                  f'<rect x="-22" y="86" width="44" height="58" rx="5" fill="#fff" stroke="{INK}" stroke-width="5"/>')
    return body + detail + collar


def legs(kind, colors, who):
    c = colors
    if kind == "desk":
        return ""
    if kind == "walk":
        L = [(-40, 0), (-150, 290)]
        R = [(40, 0), (120, 300)]
        feet = [(-170, 300, -14), (130, 316, 18)]
    elif kind == "jump":
        L = [(-40, 0), (-120, 150), (-90, 270)]
        R = [(40, 0), (110, 200), (190, 250)]
        feet = [(-96, 286, 10), (206, 254, -40)]
    else:  # stand
        L = [(-50, 0), (-80, 300)]
        R = [(50, 0), (80, 300)]
        feet = [(-92, 314, -4), (92, 314, 4)]
    w = 120 if who == "SENA" else 104
    out = tube(R, c["pants"], w, cap="butt") + tube(L, c["pants"], w, cap="butt")
    for fx_, fy, a in feet:
        out += (f'<g transform="translate({fx_},{fy}) rotate({a})">'
                f'<path d="M-60,-24 C-60,-50 50,-50 66,-10 C74,10 60,22 40,22 L-52,22 C-66,22 -66,0 -60,-24 Z" '
                f'fill="{c["shoe"]}" stroke="{INK}" stroke-width="{LW}"/>'
                f'<line x1="-58" y1="10" x2="62" y2="10" stroke="{c["shoe_sh"]}" stroke-width="7"/></g>')
    return out


def character(who, pose):
    """Return an SVG group string for the whole character in a pose."""
    colors = SENA if who == "SENA" else DANIEL
    hip = (400, 760)
    tilt = pose.get("tilt", 0)
    head_tilt = pose.get("head_tilt", 0)
    neck = (400, 600)
    head_c = (400, 430)

    def T(p):  # pose points are given relative to the hip, before body tilt
        return rot((hip[0] + p[0], hip[1] + p[1]), hip, tilt)

    parts_back, parts_mid, parts_front = [], [], []
    hc = rot(rot(head_c, neck, head_tilt), hip, tilt)
    if who == "SENA":
        back_hair, head = sena_head(hc, pose["eyes"], pose["mouth"], sway=pose.get("hair_sway", 0))
        parts_back.append(f'<g transform="translate({hc[0]:.1f},{hc[1]:.1f}) rotate({tilt + head_tilt})">{back_hair}</g>')
        head = head.replace(f'translate({hc[0]:.1f},{hc[1]:.1f})', f'translate({hc[0]:.1f},{hc[1]:.1f}) rotate({tilt + head_tilt})')
    else:
        _, head = daniel_head(hc, pose["eyes"], pose["mouth"])
        head = head.replace(f'translate({hc[0]:.1f},{hc[1]:.1f})', f'translate({hc[0]:.1f},{hc[1]:.1f}) rotate({tilt + head_tilt})')

    leg_svg = f'<g transform="translate({hip[0]},{hip[1] - 20})">{legs(pose.get("legs", "stand"), colors, who)}</g>'
    body_c = T((0, -150))
    body_svg = f'<g transform="translate({body_c[0]:.1f},{body_c[1]:.1f}) rotate({tilt})">{torso(who, colors)}</g>'
    sleeve_w = 78 if who == "SENA" else 70

    arms_back, arms_front, arms_over_head = [], [], []
    for side in ("R", "L"):
        arm = pose.get(side)
        if not arm:
            continue
        sh = T((-118 if side == "R" else 118, -210))
        pts = [sh] + [T(p) for p in arm["pts"]]
        svg = ""
        for pr in arm.get("props_under", []):
            svg += prop(pr, pts[-1], who)
        svg += tube(pts, colors["top"], sleeve_w)
        svg += cuff(pts[-1], pts[-2], colors["cuff"], sleeve_w - 10)
        svg += hand(pts[-1], 27)
        for pr in arm.get("props", []):
            svg += prop(pr, pts[-1], who)
        where = arm.get("layer", "front")
        (arms_back if where == "back" else arms_over_head if where == "over" else arms_front).append(svg)

    extra_back = "".join(prop(p, T(xy), who) for p, xy in pose.get("scene_back", []))
    extra_front = "".join(prop(p, T(xy), who) for p, xy in pose.get("scene_front", []))
    effects = "".join(fx(n, x, y, s) for n, x, y, s in pose.get("fx", []))

    return ("".join(parts_back) + extra_back + "".join(arms_back) + leg_svg + body_svg + "".join(arms_front)
            + head + "".join(arms_over_head) + extra_front + effects)


def desk(y=880):
    return (f'<rect x="60" y="{y}" width="680" height="200" rx="10" fill="#e9d9c0" stroke="{INK}" stroke-width="{LW}"/>'
            f'<line x1="60" y1="{y + 24}" x2="740" y2="{y + 24}" stroke="#cdb795" stroke-width="5"/>')


# ---------- the pose library ----------
# points are relative to the hip (400, 760); shoulders sit at (-118,-210) and (118,-210)

POSES = {
    # Sena
    "sena_think": ("SENA", dict(tilt=-6, head_tilt=-12, eyes="closed", mouth="smile", legs="desk", hair_sway=4,
                                 R=dict(pts=[(-150, 30), (-40, -150)], layer="over"),
                                 L=dict(pts=[(170, -40), (110, 70)], props=["pen"]),
                                 scene_front=[], fx=[("pulse", 640, 300, 1), ("heart", 150, 260, 0.9)],
                                 desk=True)),
    "sena_idea": ("SENA", dict(tilt=5, head_tilt=8, eyes="sparkle", mouth="open", legs="stand",
                                R=dict(pts=[(-200, -300), (-180, -470)]),
                                L=dict(pts=[(190, -110), (150, -40)], props_under=["notebook"]),
                                fx=[("bulb", 150, 150, 0.9), ("sparkle", 650, 230, 1)])),
    "sena_walk": ("SENA", dict(tilt=8, head_tilt=-6, eyes="open", mouth="smile", legs="walk", hair_sway=-10,
                                R=dict(pts=[(-220, -110), (-250, -10)], props=["coffee"]),
                                L=dict(pts=[(200, -120), (250, -60)], layer="back"),
                                scene_back=[("suitcase", (300, -40))],
                                fx=[("motion", 110, 520, 1), ("sparkle", 640, 180, 0.8)])),
    "sena_write": ("SENA", dict(tilt=-3, head_tilt=-14, eyes="look_up", mouth="o", legs="desk",
                                 R=dict(pts=[(-170, -30), (-60, 60)], props_under=["notebook"]),
                                 L=dict(pts=[(170, -60), (60, -10)], props=["pen"]),
                                 fx=[("question", 600, 220, 1.1), ("sparkle", 170, 210, 0.7)], desk=True)),
    "sena_cheer": ("SENA", dict(tilt=-4, head_tilt=6, eyes="happy", mouth="open", legs="jump", hair_sway=8,
                                 R=dict(pts=[(-230, -300), (-210, -460)]),
                                 L=dict(pts=[(200, -60), (140, -130)]),
                                 fx=[("sparkle", 160, 170, 1), ("sparkle", 630, 120, 0.8), ("motion", 120, 700, 0.8)])),
    "sena_breathe": ("SENA", dict(tilt=0, head_tilt=-4, eyes="closed", mouth="calm", legs="stand",
                                   R=dict(pts=[(-150, -90), (-30, -150)]),
                                   L=dict(pts=[(170, -40), (60, -100)]),
                                   fx=[("zzz", 600, 300, 1), ("heart", 170, 300, 0.8)])),
    "sena_phone": ("SENA", dict(tilt=4, head_tilt=10, eyes="wide", mouth="o", legs="stand",
                                 R=dict(pts=[(-180, -120), (-90, -230)], props=["phone"]),
                                 L=dict(pts=[(160, -60), (190, 40)]),
                                 fx=[("sweat", 560, 260, 1.2), ("exclaim", 620, 230, 1)])),
    "sena_talk": ("SENA", dict(tilt=-4, head_tilt=6, eyes="open", mouth="open", legs="stand",
                                R=dict(pts=[(-200, -130), (-260, -230)]),
                                L=dict(pts=[(180, -80), (140, 10)], props=["coffee"]),
                                fx=[("sparkle", 150, 200, 0.7)])),
    # Daniel
    "daniel_talk": ("DANIEL", dict(tilt=4, head_tilt=-6, eyes="open", mouth="open", legs="stand",
                                    R=dict(pts=[(-200, -120), (-270, -210)]),
                                    L=dict(pts=[(170, -80), (120, -30)], props=["mug"]),
                                    scene_front=[("dog", (230, 250))],
                                    fx=[("sparkle", 140, 190, 0.7)])),
    "daniel_point": ("DANIEL", dict(tilt=-6, head_tilt=6, eyes="sparkle", mouth="grin", legs="walk",
                                     R=dict(pts=[(-230, -250), (-300, -360)]),
                                     L=dict(pts=[(170, -60), (130, 10)], props=["mug"]),
                                     fx=[("exclaim", 110, 230, 1), ("sparkle", 640, 170, 0.8)])),
    "daniel_think": ("DANIEL", dict(tilt=3, head_tilt=10, eyes="look_up", mouth="calm", legs="stand",
                                     R=dict(pts=[(-150, -40), (-40, -170)], layer="over"),
                                     L=dict(pts=[(170, -60), (60, -60)]),
                                     fx=[("question", 600, 230, 1)])),
    "daniel_cheer": ("DANIEL", dict(tilt=-3, head_tilt=-6, eyes="happy", mouth="grin", legs="jump",
                                     R=dict(pts=[(-230, -290), (-200, -450)]),
                                     L=dict(pts=[(220, -150), (290, -250)]),
                                     fx=[("sparkle", 160, 160, 1), ("sparkle", 640, 140, 0.9)])),
}


def svg_for(name):
    who, pose = POSES[name]
    body = character(who, pose)
    scene = desk() if pose.get("desk") else ""
    # desk scenes: the desk goes in front of the body, arms resting on it are drawn again on top
    if pose.get("desk"):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="800" height="1120" viewBox="0 0 800 1120">'
                f'{body}{scene}</svg>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="800" height="1120" viewBox="0 0 800 1120">{body}</svg>'


def render_all(names=None):
    from playwright.sync_api import sync_playwright
    os.makedirs(OUT, exist_ok=True)
    names = names or list(POSES)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 800, "height": 1120}, device_scale_factor=1.5)
        for n in names:
            pg.set_content(f'<html><body style="margin:0;background:transparent">{svg_for(n)}</body></html>')
            path = os.path.join(OUT, f"{n}.png")
            pg.screenshot(path=path, omit_background=True)
            print(path)
        b.close()


if __name__ == "__main__":
    render_all(sys.argv[1:] or None)
