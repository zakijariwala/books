"""Invariants the manuscript has to hold to survive a 6x9 print layout.

These are cheap structural checks over the Markdown, not style opinions: Vale
owns prose. Everything here has a print or build consequence.
"""
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
MANUSCRIPT = ROOT / "manuscript"
DIAGRAMS = ROOT / "diagrams"

CHAPTERS = sorted(MANUSCRIPT.glob("ch*.md"))
ALL_FILES = sorted(MANUSCRIPT.glob("*.md"))

FIGURE_REF = re.compile(r"!\[Figure (\d+\.\d+):[^\]]*\]\(([^)]+)\)")
# Drafting scaffolding looked like *[FIGURE 4.1: description]*. Match that
# shape only: a case-insensitive \[FIGURE also matches every real caption.
PLACEHOLDER = re.compile(r"\*\[FIGURE\b")


def read(path):
    return path.read_text(encoding="utf-8")


def figure_sources():
    """Every figure source, by output filename stem."""
    stems = {p.stem for p in DIAGRAMS.glob("architecture/fig*.py")}
    stems |= {p.stem for p in DIAGRAMS.glob("flowcharts/fig*.mmd")}
    return stems


def test_manuscript_has_chapters():
    assert len(CHAPTERS) >= 17


@pytest.mark.parametrize("path", ALL_FILES, ids=lambda p: p.name)
def test_headings_stop_at_h3(path):
    # Deeper nesting reads badly in EPUB reflow and in a book this short.
    too_deep = [ln for ln in read(path).splitlines() if re.match(r"^#{4,}\s", ln)]
    assert not too_deep, f"{path.name} has headings below H3: {too_deep[:3]}"


@pytest.mark.parametrize("path", ALL_FILES, ids=lambda p: p.name)
def test_tables_have_at_most_three_columns(path):
    # Wider tables break at 6x9 and in EPUB.
    for i, line in enumerate(read(path).splitlines(), 1):
        if not re.match(r"^\s*\|[-: |]+\|\s*$", line):
            continue  # only the delimiter row states the column count
        columns = len([c for c in line.strip().strip("|").split("|") if c.strip()])
        assert columns <= 3, f"{path.name}:{i} has {columns} columns"


@pytest.mark.parametrize("path", ALL_FILES, ids=lambda p: p.name)
def test_no_figure_placeholders_remain(path):
    # Bracketed [FIGURE n.n: ...] markers are drafting scaffolding. Shipping
    # one means a figure was described but never drawn.
    assert not PLACEHOLDER.search(read(path)), f"{path.name} still has a placeholder"


@pytest.mark.parametrize("path", ALL_FILES, ids=lambda p: p.name)
def test_every_figure_reference_has_a_source(path):
    # Pandoc warns and carries on when an image is missing, so a broken
    # reference ships as a book with a hole in it.
    sources = figure_sources()
    for _, target in FIGURE_REF.findall(read(path)):
        assert target.endswith(".png"), f"{path.name} references {target}"
        assert Path(target).stem in sources, f"{path.name}: no source for {target}"


def test_figure_numbers_are_unique():
    # Two figures sharing a number means one caption points at the wrong image.
    seen = {}
    for path in ALL_FILES:
        for number, target in FIGURE_REF.findall(read(path)):
            assert number not in seen, f"Figure {number} used twice: {seen.get(number)} and {target}"
            seen[number] = target
    assert seen


def test_figure_numbers_match_their_chapter():
    for path in CHAPTERS:
        chapter = str(int(re.search(r"ch(\d+)", path.name).group(1)))
        for number, _ in FIGURE_REF.findall(read(path)):
            assert number.split(".")[0] == chapter, f"{path.name} carries Figure {number}"


def test_no_figure_is_referenced_from_two_places():
    targets = [t for p in ALL_FILES for _, t in FIGURE_REF.findall(read(p))]
    duplicates = {t for t in targets if targets.count(t) > 1}
    assert not duplicates, f"reused figure images: {duplicates}"


@pytest.mark.parametrize("path", ALL_FILES, ids=lambda p: p.name)
def test_code_blocks_wrap_for_the_measure(path):
    # Monospace overflows the text block at 6x9 past roughly 60 characters.
    inside, offenders = False, []
    for i, line in enumerate(read(path).splitlines(), 1):
        if line.startswith("```"):
            inside = not inside
        elif inside and len(line) > 60:
            offenders.append(i)
    assert not offenders, f"{path.name} has long code lines at {offenders[:3]}"


@pytest.mark.parametrize("path", ALL_FILES, ids=lambda p: p.name)
def test_callouts_are_blockquotes_not_html(path):
    # Fenced divs and raw HTML do not survive both EPUB and DOCX cleanly.
    text = read(path)
    assert "<div" not in text, f"{path.name} uses a raw HTML div"
    assert not re.search(r"^:::", text, re.M), f"{path.name} uses a fenced div"


def test_part_two_chapters_carry_a_drill_or_questions():
    # Every chapter should make the reader decide something before it ends.
    for path in CHAPTERS:
        text = read(path)
        assert (
            "## Architecture drill" in text or "## What the exam would ask" in text
        ), f"{path.name} ends without asking the reader anything"
