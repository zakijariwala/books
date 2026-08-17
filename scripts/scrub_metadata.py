"""Remove toolchain fingerprints from the built DOCX and EPUB.

Pandoc stamps what produced a file into the container's metadata: an
`<Application>` string in the DOCX's `docProps/app.xml`, and a
`<meta name="generator">` element in the EPUB's package document. Neither
affects how the book renders and neither is anything a reader wants. On the DOCX
`cp:lastModifiedBy` is the one worth removing on principle, because on some
toolchains it carries an account name.

What this deliberately does **not** touch: `dc:title`, `dc:creator`,
`dc:language`, `dc:rights`, `dc:date`, and `dc:identifier`. Those come from
`metadata.yaml`, they are the author's own bibliographic data, and the EPUB
identifier in particular is what readers' devices use to track the file across
updates. Stripping it would orphan an updated copy from the one already on a
device. This removes what the tools said about themselves, nothing the author
said about the book.

Idempotent: running it twice reports nothing the second time.

Run: python scripts/scrub_metadata.py build/book.docx build/book.epub
"""
import os
import re
import sys
import zipfile
from pathlib import Path

DOCX_CORE = "docProps/core.xml"
DOCX_APP = "docProps/app.xml"

# Emptied rather than deleted. Both elements are typed as strings by the OOXML
# schema, so an empty one validates, where a missing one risks an opinion from
# Word about a malformed part.
APP_TAGS = ("Application", "AppVersion", "Company", "Manager", "Template")
CORE_TAGS = ("cp:lastModifiedBy", "cp:revision")

EPUB_MIMETYPE = "mimetype"


def _empty_tags(xml: str, tags: tuple[str, ...]) -> str:
    """Blank the text content of each named element, leaving the element."""
    for tag in tags:
        # Paired form with content. Self-closing and already-empty forms carry
        # nothing to remove, so they are left alone and keep this idempotent.
        xml = re.sub(
            rf"(<{re.escape(tag)}(?:\s[^>]*)?>)[^<]+(</{re.escape(tag)}>)",
            r"\1\2",
            xml,
        )
    return xml


def scrub_core(xml: str) -> str:
    return _empty_tags(xml, CORE_TAGS)


def scrub_app(xml: str) -> str:
    return _empty_tags(xml, APP_TAGS)


def scrub_opf(xml: str) -> str:
    """Drop generator declarations from an EPUB package document.

    Pandoc has used both spellings across versions: an OPF2 `<meta name=...>`
    and an OPF3 `<meta property=...>`. Removing the element is correct for both,
    since generator metadata is optional in either revision.
    """
    xml = re.sub(
        r"\s*<meta\b[^>]*\bname\s*=\s*[\"']generator[\"'][^>]*/>",
        "",
        xml,
    )
    xml = re.sub(
        r"\s*<meta\b[^>]*\bproperty\s*=\s*[\"']generator[\"'][^>]*>.*?</meta>",
        "",
        xml,
        flags=re.S,
    )
    return xml


def _is_opf(name: str) -> bool:
    return name.endswith(".opf")


class TargetLocked(Exception):
    """The file is open in another process, most often Word or a reader."""


def scrub(path: Path) -> list[str]:
    """Rewrite path in place. Returns a note per part actually changed."""
    suffix = path.suffix.lower()
    if suffix not in (".docx", ".epub"):
        raise ValueError(f"{path}: expected a .docx or .epub")

    notes = []
    tmp = path.with_suffix(path.suffix + ".tmp")
    src = zipfile.ZipFile(path)
    try:
        infos = src.infolist()

        with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as dst:
            for info in infos:
                data = src.read(info.filename)
                before = data

                if suffix == ".docx" and info.filename == DOCX_CORE:
                    data = scrub_core(data.decode("utf-8")).encode("utf-8")
                elif suffix == ".docx" and info.filename == DOCX_APP:
                    data = scrub_app(data.decode("utf-8")).encode("utf-8")
                elif suffix == ".epub" and _is_opf(info.filename):
                    data = scrub_opf(data.decode("utf-8")).encode("utf-8")

                if data != before:
                    notes.append(f"{info.filename} scrubbed")

                # Pass the ZipInfo, never info.filename. EPUB requires the
                # `mimetype` entry to come first and to be stored uncompressed,
                # and reusing the source ZipInfo is what carries its
                # ZIP_STORED across; a bare filename would inherit this
                # archive's ZIP_DEFLATED and produce a container that readers
                # and epubcheck both reject. Iterating infolist() in order keeps
                # the entry first. The damage is invisible in a diff and only
                # shows up when someone opens the book, so
                # test_scrub_metadata.py asserts both properties.
                dst.writestr(info, data)

        src.close()

        # Matches patch_docx.py: os.replace is atomic and overwrites, where
        # shutil.move refuses an existing destination on Windows. A file open in
        # Word or a reader cannot be replaced at all, which happens constantly
        # while proofing.
        try:
            os.replace(tmp, path)
        except PermissionError as exc:
            raise TargetLocked(
                f"{path} is open in another process. Close it and re-run."
            ) from exc
    finally:
        src.close()
        tmp.unlink(missing_ok=True)

    return notes


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        target = Path(arg)
        try:
            applied = scrub(target)
        except TargetLocked as exc:
            print(f"scrub_metadata: {exc}", file=sys.stderr)
            sys.exit(1)
        if applied:
            print(f"scrubbed {target}: {'; '.join(applied)}")
        else:
            print(f"{target}: no toolchain metadata found")
