#!/usr/bin/env python3
"""
Cover for the reading copy. Grayscale, same drawing language as the figures.

The motif is the gap from chapter 1, drawn large and quiet: demand as a curve,
capacity as steps beneath it, the shortfall hatched. It is the book's argument in
one shape, and it is the only thing on the cover that is not type.

Writes build/cover.png at 1600x2560, which is a size Kindle is happy with.
"""

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"

W, H = 1600, 2560
INK = "#1a1a1a"
MID = "#6f6f6f"
LIGHT = "#c4c4c4"
PAPER = "#faf9f6"

TITLE_1 = "The Clouds,"
TITLE_2 = "for People Who"
TITLE_3 = "Don't Do Servers"
SUB = "Where your data actually lives, what it costs,\nand what breaks when it breaks"
FOOT = "FIRST DRAFT"

SERIF = "Georgia, 'Times New Roman', serif"
SANS = "Helvetica, Arial, sans-serif"


def build():
    BUILD.mkdir(exist_ok=True)

    # the gap motif, occupying the lower half
    L, R = 190, W - 190
    base, top = 2010, 1360
    s1, s2 = L + 400, L + 800
    y0, y1, y2 = base, base - 150, base - 300
    dem = f"M {L} {y0} C {L+380} {y0-40}, {L+640} {top+230}, {R} {top}"
    cap = f"M {L} {y0} L {s1} {y0} L {s1} {y1} L {s2} {y1} L {s2} {y2} L {R} {y2}"
    gap = (f"M {L} {y0} C {L+380} {y0-40}, {L+640} {top+230}, {R} {top} "
           f"L {R} {y2} L {s2} {y2} L {s2} {y1} L {s1} {y1} L {s1} {y0} Z")

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<defs>
<pattern id="h" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
<line x1="0" y1="0" x2="0" y2="14" stroke="{LIGHT}" stroke-width="5"/></pattern>
</defs>
<rect width="{W}" height="{H}" fill="{PAPER}"/>

<text x="{L}" y="430" font-family="{SERIF}" font-size="132" font-weight="600" fill="{INK}">{TITLE_1}</text>
<text x="{L}" y="580" font-family="{SERIF}" font-size="132" font-weight="600" fill="{INK}">{TITLE_2}</text>
<text x="{L}" y="730" font-family="{SERIF}" font-size="132" font-weight="600" fill="{INK}">{TITLE_3}</text>

<line x1="{L}" y1="820" x2="{L+300}" y2="820" stroke="{INK}" stroke-width="6"/>

<text x="{L}" y="930" font-family="{SERIF}" font-size="50" font-style="italic" fill="{MID}">Where your data actually lives,</text>
<text x="{L}" y="1000" font-family="{SERIF}" font-size="50" font-style="italic" fill="{MID}">what it costs, and what breaks</text>
<text x="{L}" y="1070" font-family="{SERIF}" font-size="50" font-style="italic" fill="{MID}">when it breaks</text>

<path d="{gap}" fill="url(#h)" stroke="none"/>
<path d="{cap}" fill="none" stroke="{INK}" stroke-width="9" stroke-linejoin="round"/>
<path d="{dem}" fill="none" stroke="{MID}" stroke-width="9" stroke-linecap="round"/>
<line x1="{L}" y1="{base}" x2="{R}" y2="{base}" stroke="{INK}" stroke-width="4"/>

<text x="{L}" y="2160" font-family="{SANS}" font-size="34" fill="{MID}" letter-spacing="6">DEMAND MOVES IN WEEKS.</text>
<text x="{L}" y="2215" font-family="{SANS}" font-size="34" fill="{MID}" letter-spacing="6">CAPACITY MOVES IN YEARS.</text>

<text x="{L}" y="{H-150}" font-family="{SANS}" font-size="30" font-weight="700" fill="{INK}" letter-spacing="8">{FOOT}</text>
</svg>'''

    src = BUILD / "cover.svg"
    src.write_text(svg)
    out = BUILD / "cover.png"
    subprocess.run(["rsvg-convert", f"--width={W}", "--background-color=white",
                    "--output", str(out), str(src)], check=True)
    print(f"build/cover.png  {W}x{H}")


if __name__ == "__main__":
    build()
