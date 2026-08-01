"""Inject mirrored margins into a built DOCX.

Pandoc copies styles and the section properties from a reference document, but
regenerates `word/settings.xml` from scratch, which drops the mirror-margins
flag set in `scripts/make_reference_docx.py`.

Without mirroring, the wide 0.875in margin sits on the left of every page. On a
printed book that is correct for recto pages and wrong for verso ones, where
the gutter falls on the outside edge. KDP will accept the file; it just prints
badly. Run this over the built file so the gutter alternates.

Run: python scripts/patch_docx.py build/book.docx
"""
import shutil
import sys
import zipfile
from pathlib import Path

SETTINGS = "word/settings.xml"
FLAG = "<w:mirrorMargins/>"


def patch_settings(xml: str) -> str:
    if FLAG in xml:
        return xml
    # w:mirrorMargins sits early in the CT_Settings sequence, so placing it
    # immediately after the opening tag keeps Word's schema validator happy.
    open_tag_end = xml.find(">", xml.find("<w:settings"))
    if open_tag_end == -1:
        raise RuntimeError("settings.xml has no <w:settings> element")
    return xml[: open_tag_end + 1] + FLAG + xml[open_tag_end + 1 :]


def patch(path: Path) -> bool:
    src = zipfile.ZipFile(path)
    if SETTINGS not in src.namelist():
        src.close()
        return False

    tmp = path.with_suffix(".tmp.docx")
    changed = False
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as dst:
        for item in src.namelist():
            data = src.read(item)
            if item == SETTINGS:
                patched = patch_settings(data.decode("utf-8"))
                changed = patched != data.decode("utf-8")
                data = patched.encode("utf-8")
            dst.writestr(item, data)
    src.close()
    shutil.move(str(tmp), str(path))
    return changed


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        target = Path(arg)
        if patch(target):
            print(f"patched {target}: mirrored margins enabled")
        else:
            print(f"{target}: already mirrored")
