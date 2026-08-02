"""DOCX patching: mirrored margins and table widths.

Both patches fix things Pandoc gets wrong for a 6x9 paperback. The table
rescaling in particular fixed a live defect where every table ran an inch into
the outside margin.
"""
import re
import zipfile

import pytest

from patch_docx import (
    DOCUMENT,
    SETTINGS,
    TWIPS_PER_INCH,
    measure_twips,
    patch,
    patch_settings,
    patch_tables,
)

# 6x9in trim with the book's margins: 4.5in of measure.
SECTPR = (
    '<w:sectPr><w:pgSz w:w="8640" w:h="12960"/>'
    '<w:pgMar w:top="1080" w:right="900" w:bottom="1080" w:left="1260" '
    'w:header="720" w:footer="720" w:gutter="0"/></w:sectPr>'
)
MEASURE = 8640 - 1260 - 900  # 6480 twips, 4.5in


def table(widths, rows=2):
    grid = "".join(f'<w:gridCol w:w="{w}"/>' for w in widths)
    row = "<w:tr>" + "".join(f'<w:tc><w:tcW w:w="{w}" w:type="dxa"/></w:tc>' for w in widths) + "</w:tr>"
    return (
        f'<w:tbl><w:tblPr><w:tblW w:w="{sum(widths)}" w:type="dxa"/></w:tblPr>'
        f"<w:tblGrid>{grid}</w:tblGrid>" + row * rows + "</w:tbl>"
    )


def document(*tables):
    return f"<w:document><w:body>{''.join(tables)}{SECTPR}</w:body></w:document>"


def grid_of(xml):
    return [int(w) for w in re.findall(r'<w:gridCol w:w="(\d+)"', xml)]


def test_measure_is_read_from_the_documents_own_page_setup():
    assert measure_twips(document()) == MEASURE
    assert measure_twips(document()) / TWIPS_PER_INCH == pytest.approx(4.5)


def test_measure_raises_when_page_setup_is_missing():
    with pytest.raises(RuntimeError):
        measure_twips("<w:document><w:body/></w:document>")


def test_oversized_table_is_brought_within_the_measure():
    # The live defect: Pandoc sized tables to 5.5in inside a 4.5in block.
    xml, count = patch_tables(document(table([2640, 2640, 2640])))
    assert count == 1
    assert sum(grid_of(xml)) == MEASURE


def test_column_proportions_are_preserved():
    xml, _ = patch_tables(document(table([4000, 2000, 2000])))
    cols = grid_of(xml)
    assert cols[0] == pytest.approx(cols[1] * 2, rel=0.01)


def test_widths_sum_exactly_despite_rounding():
    # Rounding three ways can lose a twip; the remainder goes to the last
    # column so Word is never handed a grid that does not add up.
    xml, _ = patch_tables(document(table([3333, 3333, 3334])))
    assert sum(grid_of(xml)) == MEASURE


def test_cell_widths_follow_the_grid():
    xml, _ = patch_tables(document(table([4000, 2000, 2000], rows=3)))
    cols = grid_of(xml)
    cells = [int(w) for w in re.findall(r'<w:tcW w:w="(\d+)"', xml)]
    assert cells[: len(cols)] == cols
    assert len(cells) == len(cols) * 3


def test_table_already_within_the_measure_is_left_alone():
    original = document(table([2000, 2000]))
    xml, count = patch_tables(original)
    assert count == 0
    assert xml == original


def test_every_table_in_the_document_is_patched():
    xml, count = patch_tables(
        document(table([2640, 2640, 2640]), table([4000, 4000]))
    )
    assert count == 2
    assert all(
        sum(int(w) for w in re.findall(r'<w:gridCol w:w="(\d+)"', t)) == MEASURE
        for t in re.findall(r"<w:tbl>.*?</w:tbl>", xml, re.S)
    )


def test_patching_tables_is_idempotent():
    once, _ = patch_tables(document(table([2640, 2640, 2640])))
    twice, count = patch_tables(once)
    assert count == 0
    assert twice == once


def test_mirror_margins_flag_is_added():
    # Pandoc regenerates settings.xml and drops the flag, which puts the gutter
    # on the wrong edge of every verso page.
    assert "<w:mirrorMargins/>" in patch_settings("<w:settings><w:zoom/></w:settings>")


def test_mirror_margins_is_not_added_twice():
    once = patch_settings("<w:settings/>")
    assert patch_settings(once).count("<w:mirrorMargins/>") == 1


def build_docx(path):
    with zipfile.ZipFile(path, "w") as z:
        z.writestr(SETTINGS, "<w:settings/>")
        z.writestr(DOCUMENT, document(table([2640, 2640, 2640])))
        z.writestr("word/styles.xml", "<w:styles/>")
    return path


def test_patch_rewrites_the_file_and_keeps_other_parts(tmp_path):
    p = build_docx(tmp_path / "book.docx")
    notes = patch(p)

    assert any("table" in n for n in notes)
    assert any("mirror" in n for n in notes)

    with zipfile.ZipFile(p) as z:
        assert "word/styles.xml" in z.namelist()
        assert "<w:mirrorMargins/>" in z.read(SETTINGS).decode()
        assert sum(grid_of(z.read(DOCUMENT).decode())) == MEASURE


def test_patch_leaves_a_valid_zip(tmp_path):
    p = build_docx(tmp_path / "book.docx")
    patch(p)
    with zipfile.ZipFile(p) as z:
        assert z.testzip() is None


def test_locked_target_raises_a_clear_error(tmp_path, monkeypatch):
    # Proofing a layout means the DOCX is open in Word, and a rebuild then hits
    # a locked file. That should be one readable line, not a stack trace.
    from patch_docx import TargetLocked
    import patch_docx as module

    p = build_docx(tmp_path / "book.docx")

    def refuse(src, dst):
        raise PermissionError(32, "in use")

    monkeypatch.setattr(module.os, "replace", refuse)
    with pytest.raises(TargetLocked, match="open in another process"):
        patch(p)


def test_no_temp_file_is_left_behind_when_locked(tmp_path, monkeypatch):
    import patch_docx as module

    p = build_docx(tmp_path / "book.docx")
    monkeypatch.setattr(
        module.os, "replace", lambda s, d: (_ for _ in ()).throw(PermissionError())
    )
    with pytest.raises(Exception):
        patch(p)
    assert not (tmp_path / "book.tmp.docx").exists()
