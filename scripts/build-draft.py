#!/usr/bin/env python3
"""
Consolidate the manuscript into one reading copy for the shred.

Takes the twelve chapters, places the figures where their markers sit, turns the
STORY-TODO markers into visible annotations rather than hidden comments, and adds
per-chapter apparatus (promise, word count, story verdict).

The point of the experiment branch is to read the draft cold and judge where a
story is load-bearing. Hidden HTML comments cannot be judged, so this build
surfaces every one of them.

Usage:  python3 scripts/build-draft.py
        pandoc build/draft.md -o build/draft.html --embed-resources --standalone
        (scripts/build-draft.sh does both)
"""

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MS = ROOT / "manuscript"
FIGS = ROOT / "figures"
BUILD = ROOT / "build"

# Short legends. The marker text is a drawing instruction; this is what a reader
# is told the picture shows.
CAPTIONS = {
    1: "Demand moves in weeks. Capacity moves in eighteen months. The shaded area is the gap.",
    2: "One tap, six businesses. The request path, end to end.",
    3: "A country holds regions; a region holds zones. The country decides whose law reaches the file.",
    4: "Bigger has a ceiling. More does not, provided the thing can be copied.",
    5: "Cheap to fill. Metered to empty.",
    6: "The same twenty round trips. Only the distance changed.",
    7: "Changes go to the one desk that decides. Questions go to copies, a moment behind.",
    8: "Capacity arrives at minute six. The customers arrived at minute zero.",
    9: "The permitted absence, and the sliver a credit refunds.",
    10: "The same hole. The bulkheads decide how far the water gets.",
    11: "One photograph, priced by stop. Two of the six never stop.",
    12: "The same drawing, at planetary scale.",
}

TITLES = {
    1: "The Great Pizza Box Purge", 2: "What Happens When You Upload a Photo",
    3: "Meet the Landlords", 4: "Compute, Renting Brains",
    5: "Storage, The Infinite Warehouse", 6: "Networking, Roads and Bouncers",
    7: "Databases, The Librarians", 8: "Scaling, Surviving Black Friday",
    9: "Reliability, The Day the Internet Broke", 10: "Security, The Perimeter is Dead",
    11: "Cloud Economics, Why Your CFO is Crying", 12: "The AI Infrastructure Wars",
}

PARTS = {1: "Part I", 4: "Part II", 8: "Part III", 11: "Part IV"}
PART_NAMES = {1: "Part I", 4: "Part II", 8: "Part III", 11: "Part IV"}

COMMENT = re.compile(r"<!--(.*?)-->", re.S)


def words(md: str) -> int:
    body = COMMENT.sub("", md)
    body = "\n".join(l for l in body.splitlines() if not l.startswith("#"))
    return len(body.split())


def promise(header: str) -> str:
    m = re.search(r"Promise[^:]*:\s*(.+?)(?:\n[A-Z]|\nIntroduces|\nReferences|\nArc|\n-->)",
                  header, re.S)
    if not m:
        return ""
    return " ".join(m.group(1).split())


def annotation(kind: str, title: str, body: str) -> str:
    body = " ".join(body.split())
    return (f'\n<div class="annot {kind}">\n'
            f'<div class="annot-h">{title}</div>\n'
            f'<div class="annot-b">{body}</div>\n</div>\n')


def build():
    BUILD.mkdir(exist_ok=True)
    out = []
    total = 0
    stories = []

    out.append("---\ntitle: The Clouds, for People Who Don't Do Servers\n"
               "subtitle: First draft, experiment branch\n---\n")

    out.append('<div class="frontnote">\n\n'
               "## Reading this draft\n\n"
               "This is the complete first draft from the experiment branch. It carries no "
               "first-hand story anywhere in it, on purpose. The point of the draft is to be "
               "read cold and shredded, so that the twelve places where a story might go can "
               "be ranked by what actually breaks without one.\n\n"
               "Two kinds of apparatus appear in the text and are not part of the book:\n\n"
               "- **Story markers** in dashed boxes. Each states what the story would have to "
               "prove and what the chapter loses if it stays empty. Judge these as you read, "
               "and record verdicts in `docs/story-candidates.md`.\n"
               "- **Chapter headers** giving the promise the chapter is meant to deliver and "
               "its word count.\n\n"
               "Figures are placed where the prose refers to them. Style is provisional.\n\n"
               "</div>\n")

    for n in range(1, 13):
        src = MS / f"ch{n:02d}.md"
        raw = src.read_text()
        hdr = COMMENT.search(raw)
        header_text = hdr.group(1) if hdr else ""
        w = words(raw)
        total += w

        if n in PARTS:
            out.append(f'\n<div class="partbreak">{PART_NAMES[n]}</div>\n')

        body = raw
        # strip the leading draft-note comment only
        if hdr:
            body = body[:hdr.start()] + body[hdr.end():]

        p = promise(header_text)
        head = annotation("chap", f"Chapter {n} &middot; {w:,} words",
                          (f"<b>Promise:</b> {p}" if p else "&nbsp;"))

        # figure: place it where the marker sits
        fig_file = next(FIGS.glob(f"fig-{n:02d}-*.png"), None)

        def fig_sub(m):
            if fig_file is None:
                return ""
            rel = f"../figures/{fig_file.name}"
            cap = CAPTIONS.get(n, "")
            return (f'\n<figure>\n<img src="{rel}" alt="Figure {n}">\n'
                    f'<figcaption><b>Figure {n}.</b> {cap}</figcaption>\n</figure>\n')

        def story_sub(m):
            text = m.group(1).replace("STORY-TODO:", "").strip()
            stories.append((n, text))
            return annotation("story", f"Story marker &middot; chapter {n}", text)

        body = re.sub(r"<!--\s*FIGURE:.*?-->", fig_sub, body, flags=re.S)
        body = re.sub(r"<!--\s*(STORY-TODO:.*?)-->", story_sub, body, flags=re.S)
        body = COMMENT.sub("", body)  # anything left over

        # insert the chapter annotation after the chapter heading
        lines = body.strip().splitlines()
        for i, l in enumerate(lines):
            if l.startswith("# "):
                lines.insert(i + 1, head)
                break
        out.append("\n".join(lines) + "\n")

    out.append('\n<div class="partbreak">Apparatus</div>\n')
    out.append("\n# The twelve story markers, collected\n\n"
               "Every marker in one place, for ranking after the read. "
               "Verdicts belong in `docs/story-candidates.md`.\n")
    for n, text in stories:
        out.append(annotation("story", f"Chapter {n} &middot; {TITLES[n]}", text))

    out.append(f"\n<div class=\"frontnote\">\n\n**Draft total: {total:,} words across "
               f"twelve chapters.** Budget is 56,000, leaving room for front and back "
               f"matter.\n\n</div>\n")

    md = "\n".join(out)
    (BUILD / "draft.md").write_text(md)
    print(f"build/draft.md  {total:,} words, {len(stories)} story markers")
    return total, len(stories)


if __name__ == "__main__":
    build()
