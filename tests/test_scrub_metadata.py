"""Metadata scrubbing: toolchain fingerprints out, bibliographic data in.

Two things here are worth more than the rest. The scrubber must not touch the
EPUB's `dc:identifier`, because that is what a reader's device uses to recognise
an updated file as the same book. And it must not break the EPUB container: the
`mimetype` entry has to stay first and stored uncompressed, which a naive zip
rewrite silently destroys. Both are asserted below.
"""
import zipfile

import pytest

from scrub_metadata import (
    DOCX_APP,
    DOCX_CORE,
    EPUB_MIMETYPE,
    scrub,
    scrub_app,
    scrub_core,
    scrub_opf,
)

CORE = (
    '<?xml version="1.0" encoding="UTF-8"?>'
    "<cp:coreProperties>"
    "<dc:title>Google Cloud Professional Cloud Architect</dc:title>"
    "<dc:creator>Zaki Jariwala</dc:creator>"
    "<cp:lastModifiedBy>some-account-name</cp:lastModifiedBy>"
    "<cp:revision>7</cp:revision>"
    "</cp:coreProperties>"
)

APP = (
    '<?xml version="1.0" encoding="UTF-8"?>'
    "<Properties>"
    "<Application>Microsoft Office Word</Application>"
    "<AppVersion>16.0000</AppVersion>"
    "<Company>Some Company</Company>"
    "<Pages>115</Pages>"
    "</Properties>"
)

OPF2 = (
    '<?xml version="1.0" encoding="UTF-8"?>'
    '<package version="2.0"><metadata>'
    '<dc:identifier id="epub-id">2d8ac606-9d99-4f9e-a700-7ce03b7e5bf0</dc:identifier>'
    "<dc:title>Google Cloud Professional Cloud Architect</dc:title>"
    "<dc:creator>Zaki Jariwala</dc:creator>"
    '<meta name="generator" content="pandoc 3.1.11"/>'
    "</metadata></package>"
)

OPF3 = (
    '<?xml version="1.0" encoding="UTF-8"?>'
    '<package version="3.0"><metadata>'
    '<dc:identifier id="epub-id">2d8ac606-9d99-4f9e-a700-7ce03b7e5bf0</dc:identifier>'
    '<meta property="generator">pandoc 3.1.11</meta>'
    "</metadata></package>"
)


def test_lastmodifiedby_and_revision_are_emptied():
    out = scrub_core(CORE)
    assert "some-account-name" not in out
    assert "<cp:lastModifiedBy></cp:lastModifiedBy>" in out
    assert "<cp:revision></cp:revision>" in out


def test_core_keeps_the_authors_own_bibliographic_data():
    out = scrub_core(CORE)
    assert "<dc:creator>Zaki Jariwala</dc:creator>" in out
    assert "Google Cloud Professional Cloud Architect" in out


def test_application_fingerprint_is_emptied():
    out = scrub_app(APP)
    assert "Microsoft Office Word" not in out
    assert "16.0000" not in out
    assert "Some Company" not in out


def test_app_leaves_unrelated_properties_alone():
    assert "<Pages>115</Pages>" in scrub_app(APP)


def test_opf2_generator_meta_is_removed():
    out = scrub_opf(OPF2)
    assert "generator" not in out
    assert "pandoc" not in out


def test_opf3_generator_meta_is_removed():
    out = scrub_opf(OPF3)
    assert "generator" not in out
    assert "pandoc" not in out


def test_opf_keeps_the_identifier_that_tracks_updates():
    # Losing this orphans an updated file from the copy already on a device.
    for src in (OPF2, OPF3):
        assert "2d8ac606-9d99-4f9e-a700-7ce03b7e5bf0" in scrub_opf(src)


def test_scrubbing_is_idempotent():
    once = scrub_core(CORE), scrub_app(APP), scrub_opf(OPF2)
    twice = scrub_core(once[0]), scrub_app(once[1]), scrub_opf(once[2])
    assert once == twice


def write_epub(path):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(
            zipfile.ZipInfo(EPUB_MIMETYPE),
            "application/epub+zip",
            compress_type=zipfile.ZIP_STORED,
        )
        z.writestr("META-INF/container.xml", "<container/>")
        z.writestr("EPUB/content.opf", OPF2)
        z.writestr("EPUB/ch01.xhtml", "<html/>")
    return path


def write_docx(path):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", "<Types/>")
        z.writestr(DOCX_CORE, CORE)
        z.writestr(DOCX_APP, APP)
        z.writestr("word/document.xml", "<w:document/>")
    return path


def test_epub_mimetype_stays_first_and_uncompressed(tmp_path):
    # The failure this guards against is invisible in a diff and fatal in a
    # reader: deflating mimetype makes the container invalid.
    book = write_epub(tmp_path / "book.epub")
    scrub(book)

    with zipfile.ZipFile(book) as z:
        infos = z.infolist()
        assert infos[0].filename == EPUB_MIMETYPE
        assert infos[0].compress_type == zipfile.ZIP_STORED
        assert z.read(EPUB_MIMETYPE) == b"application/epub+zip"


def test_epub_round_trip_scrubs_the_opf_and_keeps_everything_else(tmp_path):
    book = write_epub(tmp_path / "book.epub")
    notes = scrub(book)
    assert any("content.opf" in n for n in notes)

    with zipfile.ZipFile(book) as z:
        assert sorted(z.namelist()) == sorted(
            [EPUB_MIMETYPE, "META-INF/container.xml", "EPUB/content.opf", "EPUB/ch01.xhtml"]
        )
        opf = z.read("EPUB/content.opf").decode("utf-8")
        assert "pandoc" not in opf
        assert "2d8ac606-9d99-4f9e-a700-7ce03b7e5bf0" in opf
        assert z.read("EPUB/ch01.xhtml") == b"<html/>"


def test_docx_round_trip_scrubs_both_property_parts(tmp_path):
    doc = write_docx(tmp_path / "book.docx")
    notes = scrub(doc)
    assert len(notes) == 2

    with zipfile.ZipFile(doc) as z:
        assert "Microsoft Office Word" not in z.read(DOCX_APP).decode("utf-8")
        core = z.read(DOCX_CORE).decode("utf-8")
        assert "some-account-name" not in core
        assert "Zaki Jariwala" in core
        assert z.read("word/document.xml") == b"<w:document/>"


def test_second_run_reports_nothing(tmp_path):
    doc = write_docx(tmp_path / "book.docx")
    scrub(doc)
    assert scrub(doc) == []


def test_unexpected_suffix_is_refused(tmp_path):
    stray = tmp_path / "book.pdf"
    stray.write_bytes(b"%PDF-1.7")
    with pytest.raises(ValueError):
        scrub(stray)
