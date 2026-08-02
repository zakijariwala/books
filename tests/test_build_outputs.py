"""Assertions against the built book.

Marked `build` and excluded from the pre-commit hook: these need Pandoc to have
run. Run them with `make test-build` after `make epub docx`.

Two defects reached the built files before these existed. Pandoc's resource
path was passed with a Unix separator, so it emitted a complete-looking book
with no images and still exited 0. And Pandoc sized tables an inch wider than
the text block, so they ran into the outside margin. Neither failed a build.
Both fail here.
"""
import re
import zipfile
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"
EPUB = BUILD / "book.epub"
DOCX = BUILD / "book.docx"
MANUSCRIPT = ROOT / "manuscript"

TWIPS_PER_INCH = 1440
TRIM_W, TRIM_H = 6.0, 9.0
MEASURE_INCHES = 4.5

pytestmark = pytest.mark.build


def figure_count():
    pattern = re.compile(r"!\[Figure \d+\.\d+:")
    return sum(len(pattern.findall(p.read_text(encoding="utf-8")))
               for p in MANUSCRIPT.glob("*.md"))


@pytest.fixture(scope="module")
def docx():
    if not DOCX.exists():
        pytest.skip("build/book.docx not built; run `make docx`")
    with zipfile.ZipFile(DOCX) as z:
        yield z


@pytest.fixture(scope="module")
def document_xml(docx):
    return docx.read("word/document.xml").decode("utf-8")


@pytest.fixture(scope="module")
def epub():
    if not EPUB.exists():
        pytest.skip("build/book.epub not built; run `make epub`")
    with zipfile.ZipFile(EPUB) as z:
        yield z


# --- DOCX -----------------------------------------------------------------

def attr(tag_name, attribute, xml):
    """Read one attribute off a tag. Attribute order in OOXML is not fixed:
    Pandoc emits w:h before w:w, so anything matching a fixed order is brittle.
    """
    tag = re.search(rf"<w:{tag_name}\b[^>]*/>", xml)
    assert tag, f"no <w:{tag_name}> in the built document"
    found = re.search(rf'{attribute}="(\d+)"', tag.group(0))
    assert found, f"<w:{tag_name}> has no {attribute}"
    return int(found.group(1))


def test_docx_page_is_six_by_nine(document_xml):
    width = attr("pgSz", "w:w", document_xml) / TWIPS_PER_INCH
    height = attr("pgSz", "w:h", document_xml) / TWIPS_PER_INCH
    assert (width, height) == (TRIM_W, TRIM_H)


def test_docx_measure_is_four_and_a_half_inches(document_xml):
    size = attr("pgSz", "w:w", document_xml)
    left = attr("pgMar", "w:left", document_xml)
    right = attr("pgMar", "w:right", document_xml)
    assert (size - left - right) / TWIPS_PER_INCH == MEASURE_INCHES


def test_docx_has_mirrored_margins(docx):
    # Without it the gutter sits on the left of every page, which is wrong for
    # verso pages in a printed book.
    assert "<w:mirrorMargins/>" in docx.read("word/settings.xml").decode("utf-8")


def test_docx_embeds_every_figure(docx):
    embedded = [n for n in docx.namelist() if n.lower().endswith(".png")]
    assert len(embedded) == figure_count()


def test_docx_has_images_at_all(docx):
    # The resource-path bug produced exactly this: a book, no images, exit 0.
    assert any(n.lower().endswith(".png") for n in docx.namelist())


def test_no_docx_table_exceeds_the_measure(document_xml):
    limit = MEASURE_INCHES * TWIPS_PER_INCH
    for i, table in enumerate(re.findall(r"<w:tbl>.*?</w:tbl>", document_xml, re.S), 1):
        width = sum(int(w) for w in re.findall(r'<w:gridCol w:w="(\d+)"', table))
        assert width <= limit, f"table {i} is {width / TWIPS_PER_INCH:.2f}in wide"


def test_docx_tables_exist(document_xml):
    assert re.search(r"<w:tbl>", document_xml), "no tables in the built document"


def test_no_docx_figure_exceeds_the_text_block(document_xml):
    # EMU: 914400 to the inch. A figure taller than the block either overflows
    # or gets silently shrunk by the renderer.
    max_height = TRIM_H - 1.5  # top and bottom margins
    for cx, cy in re.findall(r'<wp:extent cx="(\d+)" cy="(\d+)"', document_xml):
        width, height = int(cx) / 914400, int(cy) / 914400
        assert width <= MEASURE_INCHES + 0.01, f"figure {width:.2f}in wide"
        assert height <= max_height + 0.05, f"figure {height:.2f}in tall"


# --- EPUB -----------------------------------------------------------------

def test_epub_zip_is_intact(epub):
    assert epub.testzip() is None


def test_epub_mimetype_is_first_and_correct(epub):
    # The one ordering rule in the EPUB container spec.
    assert epub.namelist()[0] == "mimetype"
    assert epub.read("mimetype").decode("utf-8").strip() == "application/epub+zip"


def test_epub_manifest_lists_every_figure(epub):
    opf = next(n for n in epub.namelist() if n.endswith(".opf"))
    assert epub.read(opf).decode("utf-8").count("image/png") == figure_count()


def test_epub_has_a_spine_and_a_toc(epub):
    opf = epub.read(next(n for n in epub.namelist() if n.endswith(".opf"))).decode("utf-8")
    assert opf.count("<itemref") >= 17
    assert "nav" in opf or "ncx" in opf


def test_no_broken_image_references_in_epub(epub):
    names = set(epub.namelist())
    for doc in (n for n in epub.namelist() if n.endswith((".xhtml", ".html"))):
        html = epub.read(doc).decode("utf-8")
        for src in re.findall(r'src="([^"]+\.png)"', html):
            target = src.split("/")[-1]
            assert any(target in n for n in names), f"{doc} references missing {src}"
