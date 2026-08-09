#!/usr/bin/env python3
"""
Generate the twelve book figures as grayscale SVG.

One script rather than twelve files on purpose. docs/figures.md records that
three figures reuse the six stops from chapter 2 and that figures 1 and 12 are a
deliberate visual rhyme. Shared drawing functions are what make that true; twelve
hand-drawn files would drift.

Usage:  python3 scripts/figures.py           writes figures/fig-NN-*.svg
        scripts/render-figures.sh            converts them to 300 DPI PNG
"""

import os
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "figures"

# ---------------------------------------------------------------------------
# The system. Grayscale only: weight, shade and position carry all meaning.
# ---------------------------------------------------------------------------
INK = "#1a1a1a"
MID = "#6f6f6f"
LIGHT = "#c4c4c4"
PALE = "#e9e9e9"
WHITE = "#ffffff"

HEAVY, NORMAL, THIN = 3.6, 2.2, 1.4
FONT = "'Helvetica Neue', Helvetica, Arial, sans-serif"
T_TITLE, T_LABEL, T_SMALL = 25, 19, 15.5

W = 900


def head(h, title=None):
    s = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" '
        f'width="{W}" height="{h}" font-family="{FONT}">',
        f'<rect width="{W}" height="{h}" fill="{WHITE}"/>',
        '<defs>',
        f'<pattern id="hatch" width="8" height="8" patternUnits="userSpaceOnUse" '
        f'patternTransform="rotate(45)">'
        f'<line x1="0" y1="0" x2="0" y2="8" stroke="{LIGHT}" stroke-width="3.2"/></pattern>',
        f'<marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
        f'markerHeight="7" orient="auto-start-reverse">'
        f'<path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker>',
        f'<marker id="arm" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
        f'markerHeight="6" orient="auto-start-reverse">'
        f'<path d="M0,0 L10,5 L0,10 z" fill="{MID}"/></marker>',
        '</defs>',
    ]
    if title:
        s.append(txt(W / 2, 42, title, T_TITLE, weight="600", anchor="middle"))
    return s


def txt(x, y, s, size=T_LABEL, weight="400", anchor="start", fill=INK, italic=False):
    st = ' font-style="italic"' if italic else ""
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" '
            f'text-anchor="{anchor}" fill="{fill}"{st}>{s}</text>')


def line(x1, y1, x2, y2, w=NORMAL, c=INK, dash=None, marker=False, cap="round"):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = ' marker-end="url(#ar)"' if marker else ""
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{c}" stroke-width="{w}" stroke-linecap="{cap}"{d}{m}/>')


def rect(x, y, w, h, fill=WHITE, stroke=INK, sw=NORMAL, r=0):
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


def path(d, fill="none", stroke=INK, sw=NORMAL, marker=False):
    m = ' marker-end="url(#ar)"' if marker else ""
    return (f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" '
            f'stroke-linejoin="round" stroke-linecap="round"{m}/>')


def write(name, body, h):
    OUT.mkdir(exist_ok=True)
    svg = "\n".join(head(h, None) if body[0].startswith("<text") is False else head(h))
    doc = "\n".join(body) + "\n</svg>"
    (OUT / name).write_text(doc)
    print(f"  {name}")


def doc(name, h, parts, title=None):
    body = head(h, title) + parts
    OUT.mkdir(exist_ok=True)
    (OUT / name).write_text("\n".join(body) + "\n</svg>")
    print(f"  {name}")


# ---------------------------------------------------------------------------
# Shared vocabulary 1: the six stops. Used identically by figures 2, 10 and 11.
# ---------------------------------------------------------------------------
STOPS = ["phone", "door", "warehouse", "worker", "ledger", "phone"]
STOP_LABELS = ["the tap", "front door", "warehouse", "the worker",
               "ledger", "her screen"]


def icon(kind, cx, cy, s=1.0, stroke=INK, fill=WHITE):
    """One stop. Same geometry everywhere it appears."""
    g = [f'<g transform="translate({cx:.1f},{cy:.1f}) scale({s})">']
    if kind == "phone":
        g.append(rect(-15, -24, 30, 48, fill, stroke, NORMAL, r=4))
        g.append(line(-8, -17, 8, -17, THIN, stroke))
        g.append(f'<circle cx="0" cy="16" r="2.6" fill="{stroke}"/>')
    elif kind == "door":
        g.append(path("M -20 26 L -20 -8 A 20 20 0 0 1 20 -8 L 20 26 Z", fill, stroke, NORMAL))
        g.append(f'<circle cx="10" cy="10" r="2.6" fill="{stroke}"/>')
    elif kind == "warehouse":
        g.append(path("M -26 26 L -26 -4 L 0 -22 L 26 -4 L 26 26 Z", fill, stroke, NORMAL))
        g.append(line(-13, 26, -13, 6, THIN, stroke))
        g.append(line(13, 26, 13, 6, THIN, stroke))
        g.append(line(-26, 6, 26, 6, THIN, stroke))
    elif kind == "worker":  # stopwatch: the nine seconds
        g.append(f'<circle cx="0" cy="4" r="20" fill="{fill}" stroke="{stroke}" stroke-width="{NORMAL}"/>')
        g.append(line(-7, -20, 7, -20, NORMAL, stroke))
        g.append(line(0, -20, 0, -16, NORMAL, stroke))
        g.append(line(0, 4, 0, -8, NORMAL, stroke))
        g.append(line(0, 4, 9, 9, THIN, stroke))
    elif kind == "ledger":
        g.append(rect(-19, -23, 38, 46, fill, stroke, NORMAL, r=3))
        for i, yy in enumerate((-12, -3, 6, 15)):
            g.append(line(-11, yy, 11 if i % 2 == 0 else 4, yy, THIN, stroke))
    elif kind == "photo":
        g.append(rect(-21, -16, 42, 32, fill, stroke, NORMAL, r=3))
        g.append(path("M -21 10 L -8 -3 L 1 6 L 9 -1 L 21 10", "none", stroke, THIN))
        g.append(f'<circle cx="9" cy="-8" r="3.4" fill="{stroke}"/>')
    g.append("</g>")
    return g


def stops_row(y, xs, s=1.0, shaded=(), stroke=INK):
    """The six stops in a row. shaded = indices drawn with a hatched backing."""
    out = []
    for i, (k, x) in enumerate(zip(STOPS, xs)):
        if i in shaded:
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{38*s:.1f}" fill="url(#hatch)" stroke="none"/>')
        out += icon(k, x, y, s, stroke)
    return out


# ---------------------------------------------------------------------------
# Shared vocabulary 2: the gap plot. Figures 1 and 12 must look like one drawing.
# ---------------------------------------------------------------------------
def gap_plot(h, y_label, demand_label, capacity_label, gap_label, x_ticks):
    """Demand outruns capacity. Capacity stays below the curve throughout and the
    hatched area is the shortfall, never the surplus. Figures 1 and 12 both call
    this so they read as one drawing twice."""
    L, R, T, B = 112, 848, 104, h - 112
    s1, s2 = L + 246, L + 494
    y0, y1, y2 = B - 8, B - 96, B - 186
    dem = f"M {L} {y0} C {L+228} {y0-24}, {L+398} {T+150}, {R} {T+24}"
    cap = f"M {L} {y0} L {s1} {y0} L {s1} {y1} L {s2} {y1} L {s2} {y2} L {R} {y2}"
    gapd = (f"M {L} {y0} C {L+228} {y0-24}, {L+398} {T+150}, {R} {T+24} "
            f"L {R} {y2} L {s2} {y2} L {s2} {y1} L {s1} {y1} L {s1} {y0} Z")
    p = [path(gapd, "url(#hatch)", "none", 0)]
    p.append(line(L, T, L, B, NORMAL, INK))
    p.append(line(L, B, R, B, NORMAL, INK))
    p.append(path(cap, "none", INK, HEAVY))
    p.append(path(dem, "none", MID, HEAVY))
    p.append(txt(L - 16, T + 2, y_label, T_SMALL, anchor="end", fill=MID))
    p.append(txt(R - 4, T + 4, demand_label, T_LABEL, weight="700", anchor="end", fill=MID))
    p.append(txt(s1 + 14, y1 + 30, capacity_label, T_LABEL, weight="700"))
    p.append(txt(L + 318, T + 96, gap_label, T_LABEL, weight="700", italic=True))
    for i, t in enumerate(x_ticks):
        x = L + (R - L) * (i / (len(x_ticks) - 1))
        p.append(line(x, B, x, B + 8, THIN, INK))
        a = "start" if i == 0 else ("end" if i == len(x_ticks) - 1 else "middle")
        p.append(txt(x, B + 32, t, T_SMALL, anchor=a, fill=MID))
    return p


# ---------------------------------------------------------------------------
def fig01():
    doc("fig-01-the-gap.svg", 560,
        gap_plot(560, "capacity", "demand", "what you have", "the gap",
                 ["now", "6 months", "12 months", "18 months"]))


def fig02():
    h = 420
    xs = [95 + i * 142 for i in range(6)]
    p = []
    p.append(line(60, 214, 852, 214, THIN, LIGHT))
    p += stops_row(214, xs, 1.0)
    for i in range(5):
        p.append(line(xs[i] + 44, 214, xs[i + 1] - 44, 214, NORMAL, INK, marker=True))
    for x, lab in zip(xs, STOP_LABELS):
        for j, part in enumerate(lab.split("\n")):
            p.append(txt(x, 292 + j * 21, part, T_SMALL, anchor="middle", weight="600"))
    doc("fig-02-the-request-path.svg", h, p)


def fig03():
    h = 520
    p = []
    p.append(rect(70, 70, 760, 380, PALE, INK, HEAVY, r=6))
    p.append(rect(150, 130, 600, 262, WHITE, INK, NORMAL, r=5))
    p.append(rect(240, 190, 420, 146, WHITE, INK, NORMAL, r=4))
    p += icon("photo", 450, 262, 1.15)
    p.append(txt(92, 104, "country", T_LABEL, weight="600"))
    p.append(txt(172, 164, "region", T_LABEL, weight="600"))
    p.append(txt(262, 224, "availability zone", T_LABEL, weight="600"))
    p.append(txt(450, 474, "whose law reaches it", T_LABEL, anchor="middle", italic=True, fill=MID))
    p.append(line(70, 452, 70, 466, THIN, MID))
    p.append(line(830, 452, 830, 466, THIN, MID))
    p.append(line(70, 466, 300, 466, THIN, MID))
    p.append(line(600, 466, 830, 466, THIN, MID))
    doc("fig-03-country-region-zone.svg", h, p)


def van(x, y, w=86, hgt=44, stroke=INK, fill=WHITE):
    g = [path(f"M {x} {y} L {x+w*0.62} {y} L {x+w*0.62} {y-hgt*0.55} "
              f"L {x+w} {y-hgt*0.55} L {x+w} {y-hgt} L {x} {y-hgt} Z".replace(
                  f"{y-hgt}", f"{y-hgt}"), fill, stroke, NORMAL)]
    g = [path(f"M {x} {y-hgt} L {x+w*0.60} {y-hgt} L {x+w*0.60} {y-hgt*0.42} "
              f"L {x+w} {y-hgt*0.42} L {x+w} {y} L {x} {y} Z", fill, stroke, NORMAL)]
    g.append(f'<circle cx="{x+w*0.20:.1f}" cy="{y+9}" r="9" fill="{WHITE}" stroke="{stroke}" stroke-width="{NORMAL}"/>')
    g.append(f'<circle cx="{x+w*0.80:.1f}" cy="{y+9}" r="9" fill="{WHITE}" stroke="{stroke}" stroke-width="{NORMAL}"/>')
    return g


def fig04():
    h = 500
    p = []
    p.append(line(450, 92, 450, 428, THIN, LIGHT))
    # left: bigger
    p.append(txt(60, 122, "bigger", T_LABEL, weight="700"))
    p.append(line(60, 168, 410, 168, NORMAL, INK, dash="7 6"))
    p.append(txt(410, 158, "largest size sold", T_SMALL, anchor="end", fill=MID))
    p += van(72, 322, 78, 40)
    p.append(line(172, 302, 212, 302, NORMAL, INK, marker=True))
    p += van(232, 322, 150, 92)
    p.append(txt(226, 396, "one machine, a ceiling", T_SMALL, anchor="middle", italic=True, fill=MID))
    # right: more. Same van, five times.
    p.append(txt(492, 122, "more", T_LABEL, weight="700"))
    p += icon("door", 676, 200, 0.80)
    for i in range(5):
        x = 500 + i * 76
        p += van(x, 322, 66, 36)
        p.append(line(676, 232, x + 39, 274, THIN, MID, marker=True))
    p.append(txt(676, 396, "copies, no ceiling", T_SMALL, anchor="middle", italic=True, fill=MID))
    doc("fig-04-bigger-or-more.svg", h, p)


def fig05():
    h = 420
    p = []
    p += icon("warehouse", 450, 214, 2.9)
    # in: light, unremarkable
    p.append(line(96, 214, 330, 214, NORMAL, MID, marker=True))
    p.append(txt(96, 188, "in, free or close to it", T_SMALL, fill=MID))
    # keep: a small loop inside the building
    p.append(path("M 424 250 A 30 30 0 1 1 452 262", "none", INK, THIN, marker=True))
    p.append(txt(450, 332, "keep, a little every month, forever", T_SMALL,
                 anchor="middle"))
    # out: the heavy one. This is the whole figure.
    p.append(line(572, 214, 820, 214, 9.0, INK, marker=True, cap="butt"))
    p.append(txt(820, 186, "out, metered", T_LABEL, anchor="end", weight="700"))
    p.append(txt(450, 386, "storing is cheap, moving is not", T_SMALL,
                 anchor="middle", italic=True, fill=MID))
    return doc("fig-05-the-warehouse.svg", h, p)


def _trips(p, x1, x2, y, n=20, c=INK):
    p.append(line(x1, y, x2, y, HEAVY, c))
    step = (x2 - x1) / n
    for i in range(n):
        cx = x1 + step * (i + 0.5)
        p.append(path(f"M {cx-step*0.34:.1f} {y-9} A {step*0.34:.1f} 13 0 0 1 {cx+step*0.34:.1f} {y-9}",
                      "none", MID, THIN))


def fig06():
    h = 440
    p = []
    p.append(txt(60, 132, "near", T_LABEL, weight="700"))
    _trips(p, 176, 396, 150)
    p.append(txt(414, 156, "under a second", T_LABEL, weight="600"))
    p.append(txt(60, 306, "far", T_LABEL, weight="700"))
    _trips(p, 176, 700, 324)
    p.append(txt(716, 330, "four seconds", T_LABEL, weight="600"))
    p.append(txt(450, 398, "same twenty round trips, longer road", T_SMALL,
                 anchor="middle", italic=True, fill=MID))
    doc("fig-06-round-trips.svg", h, p)


def desk(x, y, w=150, hh=54, stroke=INK):
    g = [rect(x, y, w, hh, WHITE, stroke, NORMAL, r=4)]
    g.append(line(x + 16, y + hh, x + 16, y + hh + 16, NORMAL, stroke))
    g.append(line(x + w - 16, y + hh, x + w - 16, y + hh + 16, NORMAL, stroke))
    return g


def fig07():
    h = 470
    p = []
    p += desk(96, 196, 186, 64)
    p.append(txt(189, 300, "changes go here", T_LABEL, anchor="middle", weight="700"))
    p.append(txt(189, 324, "decides what is true", T_SMALL, anchor="middle", fill=MID))
    p.append(line(189, 116, 189, 184, NORMAL, INK, marker=True))
    p.append(txt(189, 100, "one change at a time", T_SMALL, anchor="middle"))
    for yy in (150, 306):
        p += desk(600, yy, 186, 56)
        for i in range(4):
            ay = yy + 12 + i * 12
            p.append(line(858, ay, 796, ay, THIN, MID, marker=True))
        p.append(line(292, 224, 592, yy + 26, THIN, MID, dash="6 6", marker=True))
    p.append(txt(693, 418, "questions go here", T_LABEL, anchor="middle", weight="700"))
    p.append(txt(440, 238, "news, a moment late", T_SMALL, anchor="middle", italic=True, fill=MID))
    doc("fig-07-one-desk-many-copies.svg", h, p)


def fig08():
    h = 520
    L, R, T, B = 96, 856, 96, 400
    p = []
    p.append(f'<path d="M {L+60} {B} L {L+60} {T+30} L {L+600} {T+30} '
             f'L {L+600} {B-190} L {L+430} {B-190} L {L+430} {B-92} '
             f'L {L+230} {B-92} L {L+230} {B} Z" fill="url(#hatch)" stroke="none"/>')
    p.append(line(L, T, L, B, NORMAL, INK))
    p.append(line(L, B, R, B, NORMAL, INK))
    p.append(path(f"M {L} {B-6} L {L+58} {B-6} L {L+60} {T+30} L {R} {T+30}", "none", MID, HEAVY))
    p.append(path(f"M {L} {B-6} L {L+230} {B-6} L {L+230} {B-92} L {L+430} {B-92} "
                  f"L {L+430} {B-190} L {L+600} {B-190} L {L+600} {T+30} L {R} {T+30}",
                  "none", INK, HEAVY))
    p.append(txt(R - 6, T + 18, "traffic", T_LABEL, anchor="end", weight="700", fill=MID))
    p.append(txt(L + 596, B - 202, "capacity", T_LABEL, anchor="end", weight="700"))
    p.append(txt(L + 250, T + 128, "the outage", T_LABEL, weight="700", italic=True))
    for i, t in enumerate(["0", "2 min", "4 min", "6 min"]):
        x = L + (R - L) * (i / 3)
        p.append(line(x, B, x, B + 8, THIN, INK))
        p.append(txt(x, B + 32, t, T_SMALL, anchor="middle", fill=MID))
    p.append(txt(L, B + 76, "capacity arrives. the customers did not wait.", T_SMALL, italic=True, fill=MID))
    doc("fig-08-reaction-time.svg", h, p)


def fig09():
    h = 400
    p = []
    p.append(rect(96, 128, 700, 62, WHITE, INK, NORMAL, r=3))
    p.append(rect(736, 128, 60, 62, "url(#hatch)", INK, NORMAL, r=3))
    p.append(txt(96, 112, "one month", T_SMALL, fill=MID))
    p.append(txt(440, 168, "promised", T_LABEL, anchor="middle", weight="600"))
    p.append(txt(796, 220, "permitted, about forty minutes", T_SMALL, anchor="end"))
    p.append(rect(736, 268, 9, 30, INK, INK, NORMAL))
    p.append(txt(722, 292, "what the credit refunds", T_SMALL, anchor="end", weight="600"))
    p.append(txt(96, 344, "the guarantee measures their component, not your customer",
                 T_SMALL, italic=True, fill=MID))
    doc("fig-09-the-time-budget.svg", h, p)


def _hull(p, y, open_bulkheads, flooded):
    x0, x1, hgt = 130, 790, 96
    p.append(path(f"M {x0} {y} L {x1} {y} L {x1-40} {y+hgt} L {x0+40} {y+hgt} Z",
                  WHITE, INK, HEAVY))
    step = (x1 - x0 - 80) / 6
    for i in range(6):
        cx = x0 + 40 + step * (i + 0.5)
        if i in flooded:
            inset = 40 * (1 - 0)
            p.append(f'<rect x="{x0+40+step*i:.1f}" y="{y+8}" width="{step:.1f}" '
                     f'height="{hgt-16}" fill="url(#hatch)" stroke="none"/>')
        p += icon(STOPS[i], cx, y + hgt / 2, 0.42, INK)
    for i in range(1, 6):
        bx = x0 + 40 + step * i
        if i in open_bulkheads:
            p.append(line(bx, y + 4, bx, y + 30, THIN, INK))
            p.append(line(bx, y + hgt - 30, bx, y + hgt - 4, THIN, INK))
        else:
            p.append(line(bx, y + 2, bx, y + hgt - 2, NORMAL, INK))


def fig10():
    h = 520
    p = []
    _hull(p, 96, open_bulkheads=(), flooded=(2,))
    p.append(txt(96, 84, "bulkheads hold", T_LABEL, weight="700"))
    p.append(txt(790, 232, "one compartment", T_SMALL, anchor="end", fill=MID))
    _hull(p, 312, open_bulkheads=(1, 2, 3, 4, 5), flooded=(0, 1, 2, 3, 4, 5))
    p.append(txt(96, 300, "bulkheads open", T_LABEL, weight="700"))
    p.append(txt(790, 448, "all six", T_SMALL, anchor="end", fill=MID))
    p.append(txt(450, 486, "same hole, different blast radius", T_LABEL,
                 anchor="middle", italic=True, fill=MID))
    doc("fig-10-blast-radius.svg", h, p)


def fig11():
    h = 556
    p = []
    p += icon("photo", 450, 92, 1.25)
    widths = [58, 96, 300, 130, 108, 360]
    shaded = {2, 5}
    notes = {2: "every month, forever", 5: "every view"}
    for i, wd in enumerate(widths):
        y = 168 + i * 56
        p += icon(STOPS[i], 132, y + 16, 0.40, INK)
        fill = "url(#hatch)" if i in shaded else PALE
        sw = HEAVY if i in shaded else NORMAL
        p.append(rect(180, y, wd, 32, fill, INK, sw, r=3))
        if i in notes:
            p.append(txt(180 + wd + 14, y + 23, notes[i], T_SMALL, weight="700"))
    p.append(txt(132, 520, "one photograph, priced by stop", T_SMALL, italic=True, fill=MID))
    doc("fig-11-one-photograph-priced.svg", h, p)


def fig12():
    doc("fig-12-the-gap-at-scale.svg", 560,
        gap_plot(560, "capacity", "industry demand", "chips and power", "the gap",
                 ["2022", "2023", "2024", "2026"]))


if __name__ == "__main__":
    print("figures ->", OUT)
    for f in (fig01, fig02, fig03, fig04, fig05, fig06,
              fig07, fig08, fig09, fig10, fig11, fig12):
        f()
    print("done")
