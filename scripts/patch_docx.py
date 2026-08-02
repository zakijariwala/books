"""Fix up a built DOCX where Pandoc's output does not match the print spec.

Two patches, both applied to `build/book.docx` after Pandoc runs.

**Mirrored margins.** Pandoc copies styles and section properties from the
reference document, but regenerates `word/settings.xml` from scratch, which
drops the mirror-margins flag set in `scripts/make_reference_docx.py`.

Without mirroring, the wide 0.875in margin sits on the left of every page. On a
printed book that is correct for recto pages and wrong for verso ones, where
the gutter falls on the outside edge. KDP will accept the file; it just prints
badly.

**Table widths.** Pandoc sizes tables to its own default measure rather than to
the reference document's text block, which on this 6x9 trim comes out an inch
wider than the page allows. The tables then run into the outside margin. This
rescales every table proportionally to the real measure, so column proportions
are preserved and nothing overflows.

Run: python scripts/patch_docx.py build/book.docx
"""
import os
import re
import sys
import zipfile
from pathlib import Path

SETTINGS = "word/settings.xml"
DOCUMENT = "word/document.xml"
FLAG = "<w:mirrorMargins/>"

TWIPS_PER_INCH = 1440


def patch_settings(xml: str) -> str:
    if FLAG in xml:
        return xml
    # w:mirrorMargins sits early in the CT_Settings sequence, so placing it
    # immediately after the opening tag keeps Word's schema validator happy.
    open_tag_end = xml.find(">", xml.find("<w:settings"))
    if open_tag_end == -1:
        raise RuntimeError("settings.xml has no <w:settings> element")
    return xml[: open_tag_end + 1] + FLAG + xml[open_tag_end + 1 :]


def measure_twips(xml: str) -> int:
    """Text block width from the document's own page size and margins."""
    size = re.search(r'<w:pgSz\b[^>]*w:w="(\d+)"', xml)
    margins = re.search(r"<w:pgMar\b[^>]*/>", xml)
    if not size or not margins:
        raise RuntimeError("document.xml has no page size or margins")

    left = re.search(r'w:left="(\d+)"', margins.group(0))
    right = re.search(r'w:right="(\d+)"', margins.group(0))
    if not left or not right:
        raise RuntimeError("page margins are missing left or right")

    return int(size.group(1)) - int(left.group(1)) - int(right.group(1))


def _rescale_table(table: str, measure: int) -> str:
    """Scale one table's grid and cell widths to fit the measure."""
    cols = [int(w) for w in re.findall(r'<w:gridCol w:w="(\d+)"', table)]
    total = sum(cols)
    if not total or total <= measure:
        return table

    # Distribute by the original proportions, then give any rounding remainder
    # to the last column so the widths still sum to exactly the measure.
    scaled = [round(c * measure / total) for c in cols]
    scaled[-1] += measure - sum(scaled)

    grid_iter = iter(scaled)
    table = re.sub(
        r'(<w:gridCol w:w=")\d+(")',
        lambda m: f"{m.group(1)}{next(grid_iter)}{m.group(2)}",
        table,
    )

    # Cell widths repeat the grid, row by row, so cycle through the same list.
    cell_iter = iter(scaled * (table.count("<w:tcW") // len(scaled) + 1))
    table = re.sub(
        r'(<w:tcW w:w=")\d+(")',
        lambda m: f"{m.group(1)}{next(cell_iter)}{m.group(2)}",
        table,
    )

    return re.sub(
        r'(<w:tblW w:w=")\d+(")', lambda m: f"{m.group(1)}{measure}{m.group(2)}", table
    )


def patch_tables(xml: str) -> tuple[str, int]:
    measure = measure_twips(xml)
    count = 0

    def sub(match):
        nonlocal count
        patched = _rescale_table(match.group(0), measure)
        if patched != match.group(0):
            count += 1
        return patched

    return re.sub(r"<w:tbl>.*?</w:tbl>", sub, xml, flags=re.S), count


class TargetLocked(Exception):
    """The DOCX is open in another process, most often Word."""


def patch(path: Path) -> list[str]:
    src = zipfile.ZipFile(path)
    names = src.namelist()
    if SETTINGS not in names:
        src.close()
        return []

    notes = []
    tmp = path.with_suffix(".tmp.docx")
    try:
        with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as dst:
            for item in names:
                data = src.read(item)
                if item == SETTINGS:
                    before = data.decode("utf-8")
                    after = patch_settings(before)
                    if after != before:
                        notes.append("mirrored margins enabled")
                    data = after.encode("utf-8")
                elif item == DOCUMENT:
                    after, count = patch_tables(data.decode("utf-8"))
                    if count:
                        inches = measure_twips(after) / TWIPS_PER_INCH
                        notes.append(f"{count} table(s) rescaled to {inches:.2f}in")
                    data = after.encode("utf-8")
                dst.writestr(item, data)
        src.close()

        # os.replace is atomic and overwrites; shutil.move refuses when the
        # destination exists on Windows. Either way a file open in Word cannot
        # be replaced, which happens constantly when proofing a layout.
        try:
            os.replace(tmp, path)
        except PermissionError as exc:
            raise TargetLocked(
                f"{path} is open in another process (probably Word). "
                "Close it and re-run."
            ) from exc
    finally:
        src.close()
        # Never leave a half-written .tmp.docx beside the real one.
        tmp.unlink(missing_ok=True)

    return notes


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        target = Path(arg)
        try:
            applied = patch(target)
        except TargetLocked as exc:
            print(f"patch_docx: {exc}", file=sys.stderr)
            sys.exit(1)
        if applied:
            print(f"patched {target}: {'; '.join(applied)}")
        else:
            print(f"{target}: nothing to patch")
