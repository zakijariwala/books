# Book Spec

The working spec for THIS book: what it is, who it is for, how long it runs, and
how it is structured. Decisions live here; book *content* does not. This is the
first document to fill in for a new book, and the one to keep honest as the book
changes — reconcile it with the manuscript rather than letting it drift.

Replace every TODO. Delete guidance you have acted on.

## Positioning

<!-- One sentence naming what the book IS, and one naming what it deliberately
     is NOT. A sharp negative is as useful as the positive: "a decision guide,
     not an encyclopedia" tells you what to leave out. -->

TODO: What is this book, in one sentence? What is it explicitly not?

TODO: What does every chapter promise to deliver? (A repeatable question each
chapter answers keeps the book coherent and the word count predictable.)

Excluded on purpose:

- TODO: name the things you will NOT cover, and why. Anything that goes stale
  fast, or that another source does better, is a candidate.

## Reader

<!-- The tighter this is, the shorter the book can be, because you can skip what
     the reader already knows. -->

TODO: Who is the reader? What can you assume they already know and therefore
skip? What do they lack that this book supplies?

## Word budget

Target: **TODO** words. Enforced by `make wordcount` against `WORD_BUDGET` in
the `Makefile` — keep the two numbers in step.

| Component | Words |
| --- | --- |
| Front matter | TODO |
| Main chapters | TODO |
| Back matter / appendices | TODO |
| Total | TODO |

Projected extent at 6x9 trim, ~310 words per page: about TODO pages including
figure space.

> **Print note.** A print-on-demand paperback needs enough pages for spine text
> (KDP wants 79+). A book that falls short looks amateur shelved spine-out.
> Solve a thin book with reference appendices, not with padding.

## Structure

TODO: List the chapters, one row each, with the topic and its word budget.

| File | Topic | Words |
| --- | --- | --- |
| ch01.md | TODO | TODO |
| ch02.md | TODO | TODO |

Explain any non-obvious ordering choices here — why a topic comes early, why two
things are split or merged. The reasoning is what keeps the structure stable
under editing.

## Chapter template

The repeatable skeleton lives in `manuscript/ch01.md`. Adjust the element
budget for your book and keep it consistent across chapters:

| Element | Words |
| --- | --- |
| Opening hook / scene | TODO |
| Figure(s) | figure |
| Body sections, each stating a tradeoff | TODO |
| Decision figure | figure |
| Exercise / questions | TODO |
| Recap | TODO |

## Figures

- Architecture figures: one `.py` per figure in `diagrams/architecture/`.
- Flowcharts: one `.mmd` per figure in `diagrams/flowcharts/`.
- Captions numbered per chapter, `Figure 3.2`; source filename matches.

TODO: What is the book's core visual device, if it has one? A recurring figure
shape (before/after, decision tree, layered map) gives the book a signature and
makes figures faster to produce.

> **The print constraint on figure density.** A 4.5in-wide figure holds about
> two columns of short labels before its type drops below the 8pt floor that
> `scripts/normalize_image.py` enforces. A figure that fails the check must be
> simplified or split — it cannot be fixed by enlarging the image, because the
> page size does not move.

## Formatting

Print constraints are enforced in the render scripts and the test suite, not by
hand. The defaults, all changeable if you change the trim in
`make_reference_docx.py` and `normalize_image.py` together:

- Trim 6x9in, black-and-white interior, figures at 300 DPI / ~4.5in wide.
- Headings stop at H3. Tables at most three columns. Code hard-wrapped at 60
  characters. Callouts as blockquotes.

See `STYLE-GUIDE.md` for prose mechanics and `PRODUCTION-NOTES.md` for the
layout decisions that happen after the build.

## Facts to verify

TODO: List the facts in this book that could be wrong or could go stale, where
they appear, and whether each is verified yet. Keep this current — it is the
pre-publication checklist. Detail and sources go in `sources/research/`.

| Fact | Where | Status |
| --- | --- | --- |
| TODO | ch0x | unverified |
