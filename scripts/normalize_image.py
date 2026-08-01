"""Normalize a rendered figure to KDP print spec: ~1350px wide, 300 DPI metadata.

Trim size 6x9in, usable image width ~4.5in -> 4.5in * 300dpi = 1350px.
Used by `make diagrams` on every PNG under assets/ after render.
"""
import sys

from PIL import Image

TARGET_WIDTH = 1350
TARGET_DPI = (300, 300)


def normalize(path: str) -> None:
    im = Image.open(path)
    if im.width != TARGET_WIDTH:
        ratio = TARGET_WIDTH / im.width
        new_size = (TARGET_WIDTH, round(im.height * ratio))
        im = im.resize(new_size, Image.LANCZOS)
    im.save(path, dpi=TARGET_DPI)


if __name__ == "__main__":
    for p in sys.argv[1:]:
        normalize(p)
        print(f"normalized {p}")
