"""Neon line icons in the style of res/drawable/icon_cards_*.xml (512 viewport, stroke-only, 4 layers per stroke).

An icon is a list of strokes (path_data, width). Text is drawn with a small single-stroke font (x-height 84 at scale 1).
"""
import re, math, json

# ── layers, copied from the existing icons ─────────────────────────────
STOPS = ['#D21CFF', '#5B1BFF', '#0A63FF']
CORE = ['#FFB8FB', '#C9B5FF', '#A6ECFF']
LAYERS = [(3.0, '16', STOPS), (1.9, '30', STOPS), (1.0, 'FF', STOPS), (0.3, 'D8', CORE)]
GRAD = (60, 90, 452, 422)


def fmt(v):
    v = round(v, 1)
    return str(int(v)) if v == int(v) else str(v)


# ── path transform (absolute M L Q C A Z only) ─────────────────────────
TOK = re.compile(r'[MLQCAZ]|-?\d*\.?\d+')


def transform(d, sx, dx, dy, sy=None):
    sy = sx if sy is None else sy
    t = TOK.findall(d); out = []; i = 0
    n = {'M': 2, 'L': 2, 'Q': 4, 'C': 6, 'A': 7, 'Z': 0}
    while i < len(t):
        c = t[i]; i += 1
        out.append(c)
        k = n[c]
        while i < len(t) and t[i] not in n:
            vals = [float(x) for x in t[i:i + k]]; i += k
            if c == 'A':
                rx, ry, rot, la, sw, x, y = vals
                if sx * sy < 0: sw = 1 - sw
                out.append(f'{fmt(abs(rx * sx))},{fmt(abs(ry * sy))} {fmt(rot)} {int(la)},{int(sw)} {fmt(x * sx + dx)},{fmt(y * sy + dy)}')
            else:
                out.append(' '.join(f'{fmt(vals[j] * sx + dx)},{fmt(vals[j + 1] * sy + dy)}' for j in range(0, k, 2)))
    s = ' '.join(out)
    return re.sub(r'([MLQCAZ]) ', r'\1', s)


def dot(x, y):
    return f'M{fmt(x - 0.5)},{fmt(y)} L{fmt(x + 0.5)},{fmt(y)}'


# ── single-stroke font; baseline y=0, x-height -84, ascender -126, descender +44 ──
G = {
 'a': ('M84,-42 A42,42 0 1,0 0,-42 A42,42 0 1,0 84,-42 Z M84,-84 L84,0', 84),
 'b': ('M0,-126 L0,0 M0,-42 A42,42 0 1,0 84,-42 A42,42 0 1,0 0,-42', 84),
 'c': ('M76.4,-66.1 A42,42 0 1,0 76.4,-17.9', 78),
 'd': ('M84,-42 A42,42 0 1,0 0,-42 A42,42 0 1,0 84,-42 Z M84,-126 L84,0', 84),
 'e': ('M0,-42 L84,-42 A42,42 0 1,0 71.7,-12.3', 84),
 'f': ('M52,-122 Q22,-132 22,-100 L22,0 M0,-84 L48,-84', 50),
 'g': ('M84,-42 A42,42 0 1,0 0,-42 A42,42 0 1,0 84,-42 Z M84,-84 L84,12 Q84,52 42,52 Q15,52 4,36', 84),
 'h': ('M0,-126 L0,0 M0,-42 A42,42 0 0,1 84,-42 L84,0', 84),
 'i': ('M0,-84 L0,0 ' + dot(0, -116), 0),
 'j': ('M18,-84 L18,12 Q18,48 -14,46 ' + dot(18, -116), 18),
 'k': ('M0,-126 L0,0 M64,-84 L0,-30 M22,-48 L68,0', 68),
 'l': ('M0,-126 L0,0', 0),
 'm': ('M0,-84 L0,0 M0,-50 A24,24 0 0,1 48,-50 L48,0 M48,-50 A24,24 0 0,1 96,-50 L96,0', 96),
 'n': ('M0,-84 L0,0 M0,-42 A42,42 0 0,1 84,-42 L84,0', 84),
 'o': ('M84,-42 A42,42 0 1,0 0,-42 A42,42 0 1,0 84,-42', 84),
 'p': ('M0,-84 L0,44 M0,-42 A42,42 0 1,0 84,-42 A42,42 0 1,0 0,-42', 84),
 'q': ('M84,-42 A42,42 0 1,0 0,-42 A42,42 0 1,0 84,-42 Z M84,-84 L84,44', 84),
 'r': ('M0,-84 L0,0 M0,-46 Q6,-84 48,-84', 48),
 's': ('M68,-72 Q58,-84 38,-84 Q8,-84 8,-63 Q8,-45 38,-42 Q72,-39 72,-20 Q72,0 38,0 Q14,0 2,-14', 74),
 't': ('M20,-116 L20,-22 Q20,0 46,0 M0,-84 L46,-84', 46),
 'u': ('M0,-84 L0,-42 A42,42 0 0,0 84,-42 M84,-84 L84,0', 84),
 'v': ('M0,-84 L38,0 L76,-84', 76),
 'w': ('M0,-84 L26,0 L52,-68 L78,0 L104,-84', 104),
 'x': ('M0,-84 L72,0 M72,-84 L0,0', 72),
 'y': ('M0,-84 L38,-4 M76,-84 L28,44', 76),
 'z': ('M0,-84 L72,-84 L0,0 L72,0', 72),
 "'": ('M6,-126 L0,-98', 6),
 '?': ('M0,-100 Q0,-128 32,-128 Q64,-128 64,-100 Q64,-80 32,-66 L32,-42 ' + dot(32, -6), 64),
 '!': ('M0,-126 L0,-42 ' + dot(0, -6), 0),
 '-': ('M0,-42 L42,-42', 42),
 '+': ('M0,-42 L60,-42 M30,-72 L30,-12', 60),
 '.': (dot(0, -6), 0),
 '1': ('M0,-100 L30,-126 L30,0', 30),
 '2': ('M2,-100 Q4,-128 38,-128 Q72,-128 72,-96 Q72,-74 40,-48 L0,0 L74,0', 74),
 '3': ('M4,-114 Q16,-128 38,-128 Q70,-128 70,-98 Q70,-68 36,-68 Q74,-68 74,-34 Q74,0 38,0 Q12,0 0,-16', 74),
 'A': ('M0,0 L48,-126 L96,0 M18,-46 L78,-46', 96),
 'M': ('M0,0 L0,-126 L52,-50 L104,-126 L104,0', 104),
 'I': ('M0,-126 L0,0', 0),
 '0': ('M37,-128 Q74,-128 74,-64 Q74,0 37,0 Q0,0 0,-64 Q0,-128 37,-128 Z', 74),
 '%': ('M70,-126 L4,0 ' + 'M44,-104 A20,20 0 1,0 4,-104 A20,20 0 1,0 44,-104 M74,-22 A20,20 0 1,0 34,-22 A20,20 0 1,0 74,-22', 78),
 'U': ('M0,-126 L0,-48 Q0,0 46,0 Q92,0 92,-48 L92,-126', 92),
 'K': ('M0,-126 L0,0 M84,-126 L0,-44 M30,-72 L88,0', 88),
 'S': ('M80,-108 Q66,-128 42,-128 Q6,-128 6,-96 Q6,-70 44,-64 Q86,-58 86,-30 Q86,0 44,0 Q14,0 0,-22', 86),
 ' ': ('', 40),
}
GAP = 30


def text_width(s, scale=1.0):
    w = 0
    for i, ch in enumerate(s):
        w += G[ch][1] + (GAP if i < len(s) - 1 else 0)
    return w * scale


def text(s, x, y, scale=1.0, center=False):
    """Path data for s; (x, y) — left end of the baseline, or its centre with center=True."""
    if center: x -= text_width(s, scale) / 2
    out = []
    for ch in s:
        d, w = G[ch]
        if d: out.append(transform(d, scale, x, y))
        x += (w + GAP) * scale
    return ' '.join(out)


# ── shapes ─────────────────────────────────────────────────────────────
def rrect(x1, y1, x2, y2, r):
    return (f'M{fmt(x1 + r)},{fmt(y1)} L{fmt(x2 - r)},{fmt(y1)} Q{fmt(x2)},{fmt(y1)} {fmt(x2)},{fmt(y1 + r)} L{fmt(x2)},{fmt(y2 - r)} '
            f'Q{fmt(x2)},{fmt(y2)} {fmt(x2 - r)},{fmt(y2)} L{fmt(x1 + r)},{fmt(y2)} Q{fmt(x1)},{fmt(y2)} {fmt(x1)},{fmt(y2 - r)} '
            f'L{fmt(x1)},{fmt(y1 + r)} Q{fmt(x1)},{fmt(y1)} {fmt(x1 + r)},{fmt(y1)} Z')


def circle(cx, cy, r):
    return f'M{fmt(cx + r)},{fmt(cy)} A{fmt(r)},{fmt(r)} 0 1,0 {fmt(cx - r)},{fmt(cy)} A{fmt(r)},{fmt(r)} 0 1,0 {fmt(cx + r)},{fmt(cy)} Z'


def arc(cx, cy, r, a1, a2):
    """Arc from angle a1 to a2 (degrees, 0 = right, clockwise on screen)."""
    p = lambda a: (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
    (x1, y1), (x2, y2) = p(a1), p(a2)
    large = 1 if (a2 - a1) % 360 > 180 else 0
    return f'M{fmt(x1)},{fmt(y1)} A{fmt(r)},{fmt(r)} 0 {large},1 {fmt(x2)},{fmt(y2)}'


def line(*pts):
    return 'M' + ' L'.join(f'{fmt(x)},{fmt(y)}' for x, y in pts)


def arrowhead(x, y, angle, size=26):
    """Open arrowhead with tip at (x, y) pointing along angle (degrees)."""
    a = math.radians(angle)
    l = (x - size * math.cos(a - 0.6), y - size * math.sin(a - 0.6))
    r = (x - size * math.cos(a + 0.6), y - size * math.sin(a + 0.6))
    return line(l, (x, y), r)


def bubble(x1, y1, x2, y2, r=34, tail='left'):
    """Speech bubble with a tail at the bottom."""
    if tail == 'left':
        tx = x1 + 60
        return (f'M{fmt(x1 + r)},{fmt(y1)} L{fmt(x2 - r)},{fmt(y1)} Q{fmt(x2)},{fmt(y1)} {fmt(x2)},{fmt(y1 + r)} L{fmt(x2)},{fmt(y2 - r)} '
                f'Q{fmt(x2)},{fmt(y2)} {fmt(x2 - r)},{fmt(y2)} L{fmt(tx + 34)},{fmt(y2)} L{fmt(tx - 10)},{fmt(y2 + 44)} L{fmt(tx)},{fmt(y2)} '
                f'L{fmt(x1 + r)},{fmt(y2)} Q{fmt(x1)},{fmt(y2)} {fmt(x1)},{fmt(y2 - r)} L{fmt(x1)},{fmt(y1 + r)} Q{fmt(x1)},{fmt(y1)} {fmt(x1 + r)},{fmt(y1)} Z')
    tx = x2 - 60
    return (f'M{fmt(x1 + r)},{fmt(y1)} L{fmt(x2 - r)},{fmt(y1)} Q{fmt(x2)},{fmt(y1)} {fmt(x2)},{fmt(y1 + r)} L{fmt(x2)},{fmt(y2 - r)} '
            f'Q{fmt(x2)},{fmt(y2)} {fmt(x2 - r)},{fmt(y2)} L{fmt(tx)},{fmt(y2)} L{fmt(tx + 10)},{fmt(y2 + 44)} L{fmt(tx - 34)},{fmt(y2)} '
            f'L{fmt(x1 + r)},{fmt(y2)} Q{fmt(x1)},{fmt(y2)} {fmt(x1)},{fmt(y2 - r)} L{fmt(x1)},{fmt(y1 + r)} Q{fmt(x1)},{fmt(y1)} {fmt(x1 + r)},{fmt(y1)} Z')


# ── output ─────────────────────────────────────────────────────────────
def to_xml(strokes, comment):
    x1, y1, x2, y2 = GRAD
    out = ['<?xml version="1.0" encoding="utf-8"?>', f'<!-- {comment} -->',
           '<!-- Неоновый стиль: два слоя свечения (широкие полупрозрачные линии), основная линия, светлая сердцевина. -->',
           '<vector xmlns:android="http://schemas.android.com/apk/res/android"', '    xmlns:aapt="http://schemas.android.com/aapt"',
           '    android:width="48dp"', '    android:height="48dp"', '    android:viewportWidth="512"', '    android:viewportHeight="512">', '']
    names = ['свечение', 'мягкое свечение', 'основная линия', 'сердцевина']
    for (k, a, cols), nm in zip(LAYERS, names):
        out.append(f'    <!-- {nm} -->')
        for d, w in strokes:
            out += ['    <path', f'        android:pathData="{d}"', f'        android:strokeWidth="{fmt(w * k)}"',
                    '        android:strokeLineCap="round"', '        android:strokeLineJoin="round">',
                    '        <aapt:attr name="android:strokeColor">', '            <gradient', '                android:type="linear"',
                    f'                android:startX="{x1}" android:startY="{y1}"', f'                android:endX="{x2}" android:endY="{y2}">']
            for off, c in zip(['0.0', '0.5', '1.0'], cols):
                out.append(f'                <item android:offset="{off}" android:color="#{a}{c[1:]}" />')
            out += ['            </gradient>', '        </aapt:attr>', '    </path>']
        out.append('')
    out.append('</vector>')
    return '\n'.join(out) + '\n'


def to_svg(strokes, size=512):
    x1, y1, x2, y2 = GRAD
    defs, body = [], []
    for li, (k, a, cols) in enumerate(LAYERS):
        op = int(a, 16) / 255
        defs.append(f'<linearGradient id="L{li}" gradientUnits="userSpaceOnUse" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">' +
                    ''.join(f'<stop offset="{o}" stop-color="{c}" stop-opacity="{op:.3f}"/>' for o, c in zip([0, 0.5, 1], cols)) + '</linearGradient>')
        for d, w in strokes:
            body.append(f'<path d="{d}" fill="none" stroke="url(#L{li})" stroke-width="{fmt(w * k)}" stroke-linecap="round" stroke-linejoin="round"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="{size}" height="{size}"><defs>{"".join(defs)}</defs>'
            f'{"".join(body)}</svg>')


def to_json(strokes, comment):
    return {'comment': comment, 'viewport': 512, 'gradient': {'from': list(GRAD[:2]), 'to': list(GRAD[2:]), 'colors': STOPS, 'core': CORE},
            'layers': [{'widthFactor': k, 'alpha': a} for k, a, _ in LAYERS], 'strokes': [{'d': d, 'width': w} for d, w in strokes]}
