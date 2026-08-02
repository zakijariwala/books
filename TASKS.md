# Outstanding Work

State as of the drafting pass that completed Part I, Part II, the back matter,
and all 32 figures. Manuscript is ~22,300 words against a 28,000 target.

Ordered by risk: the things most likely to force rework sit at the top.

## 1. Build the outputs — building, needs a human read

Both formats now build. EPUB and DOCX each carry all 32 figures, and the
structure checks out: valid EPUB zip with correct mimetype, 23 spine items, no
broken image references; DOCX at 6x9 with a 4.5in measure and mirrored margins.

Two defects were found and fixed in the process, both of which had been silently
producing wrong output:

- **The Makefile's `--resource-path` used the Unix `:` separator.** On Windows
  Pandoc wants `;`. This does not fail the build. It warns
  `Could not fetch resource` once per figure and emits a book with no images at
  all. Now switched on `$(OS)`.
- **Pandoc sized every table to 5.50in inside a 4.5in text block**, running an
  inch into the outside margin. Not a template fault — `reference.docx` is
  correct. `scripts/patch_docx.py` now rescales tables proportionally to the
  real measure, alongside the mirrored-margins patch it already did.

**Still needs a human eye**, because these are judgement calls a script cannot
make:

- Open `build/book.docx` in Word and read it. Check that figures sit near their
  reference rather than drifting pages away, and that no caption is orphaned
  from its figure.
- 11 of the 32 figures are 7.02in tall against a 7.5in text block, so they
  become full-page figures. That is legitimate but it leaves partly blank pages
  before them. Decide whether that reads acceptably or whether those figures
  should be cut down further. Note that shrinking them costs type size, and
  several are already close to the 8pt floor.
- Open the EPUB in a reader and check reflow, particularly the two 33-row
  mapping tables.

**Extent:** roughly 71 text pages plus figure space, so about 90 pages. That
clears KDP's 79-page threshold for spine text, but not by a wide margin. If
content is cut, re-check it.

Note that `assets/` is gitignored, so a fresh clone must render the figures
before either build will produce a book with images.

## 1b. Tests — in place

There is now a suite: `make test` for the fast checks, `make test-build` for
assertions against the built book. 156 tests. The fast set also runs in the
pre-commit hook alongside Vale.

What it covers: `normalize_image.py` fit-to-block maths, grayscale conversion,
the stored-scale idempotency, and the 8pt legibility floor; `patch_docx.py`
table rescaling, proportion preservation, and mirrored margins; manuscript
invariants (heading depth, three-column tables, no placeholders, figure
references resolving to real sources, unique figure numbers, code-line width);
and the built DOCX and EPUB.

Both defects that previously reached the built book — the Unix resource-path
separator producing an image-less book at exit 0, and Pandoc's oversized tables
— were reproduced and confirmed to fail the suite before it was committed. An
assertion never seen failing is not protection.

**Not covered**, and worth knowing: `wordcount.py` and `figstyle.py` have no
tests, and nothing verifies the figures' *content* — only their dimensions. A
diagram can be wrong and still pass.

## 2. Lint — done at error level, open at warning level

Vale now runs clean at error level across all 19 manuscript files, which is what
the pre-commit hook gates on. Getting there involved three changes worth
knowing about:

- `styles/config/vocabularies/Book/accept.txt` was expanded from 21 entries to
  the full technical vocabulary of the book, grouped by category. Most of the
  293 initial errors were Vale not knowing words like `Bigtable`, `cutover`, or
  the invented case-study company names.
- `.vale.ini` disables three more Google rules — `EmDash`, `Quotes`, and
  `LyHyphens` — each with a comment explaining why. All three encode US
  documentation convention that contradicts the book's British house style, or
  in the case of `LyHyphens`, flags `exactly-once` as a mistake when it is a
  term of art. This extends the pattern already set by the four disabled rules.
- Seven genuine prose nits were fixed rather than silenced: two `very`s, two
  sentences opening with `So`, a cliche, and a gendered term.

**Still open:** 546 warnings and 1,302 suggestions. These do not block commits
and most should not be actioned — `write-good.E-Prime` objects to the verb "to
be", and `Google.Contractions` wants contractions the house voice avoids. Worth
one skim for real finds, not a cleanup pass.

Note that Vale, like Graphviz, is installed but **not on PATH**. See
handover.md section 3.2.

## 3. Verify the volatile facts

These were deliberately left unprinted or flagged rather than written from
memory. Each needs confirming against current Google documentation before
publication.

| Fact | Where | Note |
| --- | --- | --- |
| Exam cost, duration, question count, renewal terms | back-matter.md | Carried from an earlier verification pass, not re-confirmed |
| Current case-study list | back-matter.md, ch01 | Altostrat, Cymbal, EHR, KnightMotives |
| Interconnect bandwidth tiers and SLA terms | ch03, ch13 | Text says verify rather than quoting figures |
| Cloud Run request timeout ceiling | ch04 | Deliberately unstated; has moved more than once |
| Vertex AI product and model names | ch08 | Written at decision level on purpose; fastest-moving area in the book |
| Security Command Center tier contents | ch09 | Text says verify rather than listing |

Chapters 7 and 8 will date soonest. Treat them as the first candidates for
review on any reprint.

## 4. Check ch17 against KnightMotives Automotive

The original plan was to read the official KnightMotives case study before
writing Part II, to be sure the book's own fleet-telemetry scenario (ch16,
Ardwick) did not duplicate it. **That reading never happened.** ch16 and ch17
were written as original scenarios without it.

Two open questions, both flagged in BOOK-SPEC's "still to verify" section:

- Does Ardwick (connected-vehicle telemetry) overlap KnightMotives closely
  enough to look derivative?
- ch17 (Brandell, legacy monolith) has no official analogue, which was the
  intent, but confirm nothing in the current set now occupies that slot

Reading the official case study is for *checking distinctness only*. Do not
import its details. See
[flags-stale-and-legal.md](file:///D:/books/sources/datapoints/flags-stale-and-legal.md).

## 5. Decide the spare word budget

About 5,600 words are unspent. Part I runs ~13,800 against a 19,500 allocation.

This is a positioning decision, not a gap to fill by default:

- **Spend it:** more worked examples in Part I, which is currently dense and
  argument-led with few concrete walkthroughs
- **Ship shorter:** ~22,300 words still clears the 79-page KDP threshold for
  spine text comfortably, and the book's whole pitch is compression

## 6. Sanity-check the Part II numbers

The five scenarios are original and internally consistent, but their figures
(fleet sizes, data volumes, staff counts, dates) were chosen for plausibility.
A reader who does the arithmetic may find numbers that do not hold — for
example Brandell's 11 TB database against its stated cutover window, or
Ardwick's sampling rate against 240,000 vehicles.

One inconsistency of this kind was already found and fixed in ch17. Assume
others remain.

## 7. Reconcile BOOK-SPEC with the manuscript

BOOK-SPEC lists ch14 as "global live-event streaming". The file is a media
company adopting generative AI (Wexley Broadcasting), which better matches the
current case-study set's shift toward AI scenarios. The manuscript was followed
deliberately; the spec now needs updating to match, or the divergence needs
overturning.

Also check the spec's figure count: it plans 40, the book has 32.

## 8. Housekeeping

- `current_state_review.md` is a snapshot from when only ch01–ch03 were drafted.
  Its word-count table and per-chapter status are now wrong throughout. Either
  regenerate it or delete it, since a stale review is worse than none.
- The sample figure sources (`sample_hybrid.py`, `sample_flow.mmd`) were deleted
  once real figures existed.
- `agent_feedback.md` predates this drafting pass; re-read it before the next
  one to check nothing in it went unaddressed.
