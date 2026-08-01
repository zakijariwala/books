"""Generate a Pandoc reference.docx set up for a KDP 6x9 paperback interior.

Pandoc's stock reference document is US Letter with Word's default margins.
Handing that to KDP produces a rejected or badly-laid-out interior. This script
patches page size, margins, and mirrored-margin behaviour so `make docx` emits
something that matches the trim size the figures were rendered for.

Run: python scripts/make_reference_docx.py
Output: styles/reference.docx

Layout, in inches:

    trim            6.0 x 9.0
    inside margin   0.875   (gutter side, alternates on facing pages)
    outside margin  0.625
    top / bottom    0.75
    text block      4.5 wide

That 4.5in text block is the same number figures render to, so a full-width
figure fills the measure exactly. Changing a margin here means re-rendering
every figure. Keep them in step.

KDP's own minimum for a book of 24-150 pages is 0.375in inside and 0.25in
outside. The values above sit well clear of those, for readability rather than
mere compliance.
"""
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

TWIPS_PER_INCH = 1440

PAGE_W = int(6.0 * TWIPS_PER_INCH)
PAGE_H = int(9.0 * TWIPS_PER_INCH)
MARGIN_INSIDE = int(0.875 * TWIPS_PER_INCH)
MARGIN_OUTSIDE = int(0.625 * TWIPS_PER_INCH)
MARGIN_TOP = int(0.75 * TWIPS_PER_INCH)
MARGIN_BOTTOM = int(0.75 * TWIPS_PER_INCH)

OUT_PATH = Path("styles") / "reference.docx"

PG_SZ = f'<w:pgSz w:w="{PAGE_W}" w:h="{PAGE_H}"/>'
PG_MAR = (
    f'<w:pgMar w:top="{MARGIN_TOP}" w:right="{MARGIN_OUTSIDE}" '
    f'w:bottom="{MARGIN_BOTTOM}" w:left="{MARGIN_INSIDE}" '
    f'w:header="720" w:footer="720" w:gutter="0"/>'
)


def _upsert_in_sectpr(xml: str, tag: str, replacement: str) -> str:
    """Replace an element inside <w:sectPr>, or insert it if absent.

    Pandoc's stock reference.docx carries a <w:sectPr> holding only footnote
    properties, with no page size or margins at all, so a pure substitution
    silently does nothing. Insert before </w:sectPr>, which also lands pgSz and
    pgMar after footnotePr as the OOXML schema sequence requires.
    """
    pattern = re.compile(rf"<w:{tag}\b[^>]*?/>|<w:{tag}\b.*?</w:{tag}>", re.DOTALL)
    if pattern.search(xml):
        return pattern.sub(replacement, xml)

    closing = "</w:sectPr>"
    idx = xml.rfind(closing)
    if idx == -1:
        raise RuntimeError("reference.docx has no <w:sectPr> to patch")
    return xml[:idx] + replacement + xml[idx:]


def patch_document(xml: str) -> str:
    xml = _upsert_in_sectpr(xml, "pgSz", PG_SZ)
    xml = _upsert_in_sectpr(xml, "pgMar", PG_MAR)
    return xml


def patch_settings(xml: str) -> str:
    """Turn on mirrored margins so the gutter alternates on facing pages."""
    if "<w:mirrorMargins/>" in xml:
        return xml
    marker = "<w:settings"
    idx = xml.find(">", xml.find(marker))
    if idx == -1:
        return xml
    return xml[: idx + 1] + "<w:mirrorMargins/>" + xml[idx + 1 :]


def main() -> int:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    base = OUT_PATH.with_suffix(".base.docx")

    with base.open("wb") as fh:
        result = subprocess.run(
            ["pandoc", "--print-default-data-file", "reference.docx"],
            stdout=fh,
            stderr=subprocess.PIPE,
        )
    if result.returncode != 0:
        print(result.stderr.decode(errors="replace"), file=sys.stderr)
        print("Could not get Pandoc's default reference.docx.", file=sys.stderr)
        return 1

    src = zipfile.ZipFile(base)
    tmp = OUT_PATH.with_suffix(".tmp.docx")

    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as dst:
        for item in src.namelist():
            data = src.read(item)
            if item == "word/document.xml":
                data = patch_document(data.decode("utf-8")).encode("utf-8")
            elif item == "word/settings.xml":
                data = patch_settings(data.decode("utf-8")).encode("utf-8")
            dst.writestr(item, data)

    src.close()
    shutil.move(str(tmp), str(OUT_PATH))
    base.unlink()

    print(f"wrote {OUT_PATH} -- 6x9in, {MARGIN_INSIDE / TWIPS_PER_INCH}in inside margin")
    return 0


if __name__ == "__main__":
    sys.exit(main())
