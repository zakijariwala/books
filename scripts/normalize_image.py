"""Normalize a rendered figure to KDP print spec: grayscale, fits the text block.

Trim size 6x9in, usable image width ~4.5in -> 4.5in * 300dpi = 1350px. A figure
also has to fit the page vertically: a 9in page with margins and a caption
leaves about 7in, so anything taller is scaled down to fit rather than
overflowing or being silently shrunk by the renderer.

The interior prints black and white, so images are converted to grayscale here.
A figure that only reads correctly in colour will look wrong at this point,
which is the intended moment to find out.

Used by `make diagrams` on every PNG under assets/ after render.
"""
import sys

from PIL import Image
from PIL.PngImagePlugin import PngInfo

TARGET_WIDTH = 1350
MAX_HEIGHT = 2100  # 7in at 300dpi
TARGET_DPI = (300, 300)

# Mermaid renders at this font size (scripts/mermaid-config.json). A figure is
# scaled to fill the text block, so the size type actually prints at is the
# source size times that scale. Below about 8pt it stops being readable in a
# paperback, which is a reason to simplify the figure rather than to enlarge it.
SOURCE_FONT_PX = 20
MIN_PRINT_PT = 8.0

# PNG text chunk recording the scale that was applied, so the run is idempotent.
SCALE_KEY = "book:figscale"


def print_point_size(scale: float) -> float:
    """Point size the figure's type lands at once scaled onto the page."""
    return SOURCE_FONT_PX * scale / TARGET_DPI[0] * 72


def normalize(path: str) -> float:
    """Fit the figure to the text block, convert to grayscale, return the scale.

    The scale is stored in the PNG so that re-running this on an already
    normalized file reports the same figure rather than recomputing 1.0 against
    the scaled image and declaring every figure legible.
    """
    im = Image.open(path)

    stored = im.text.get(SCALE_KEY) if hasattr(im, "text") else None
    if stored is not None:
        return float(stored)

    scale = min(TARGET_WIDTH / im.width, MAX_HEIGHT / im.height)
    if scale != 1:
        im = im.resize(
            (round(im.width * scale), round(im.height * scale)), Image.LANCZOS
        )

    if im.mode != "L":
        im = im.convert("L")

    meta = PngInfo()
    meta.add_text(SCALE_KEY, repr(scale))
    im.save(path, dpi=TARGET_DPI, pnginfo=meta)
    return scale


if __name__ == "__main__":
    too_small = []
    for p in sys.argv[1:]:
        pt = print_point_size(normalize(p))
        note = ""
        if pt < MIN_PRINT_PT:
            note = f"  TYPE TOO SMALL, simplify the figure (min {MIN_PRINT_PT}pt)"
            too_small.append(p)
        print(f"normalized {p}  prints at ~{pt:.1f}pt{note}")

    if too_small:
        print(f"\n{len(too_small)} figure(s) below {MIN_PRINT_PT}pt at print size.")
        sys.exit(1)
