# Outstanding Work

State after the editorial-review pass and the test suite. Manuscript is 31,112
words against a 33,000 budget, with 33 figures. Vale clean at error level, 156
tests passing, both formats building.

Ordered by risk: the things most likely to force rework sit at the top.

## 1. Build the outputs — building, needs a human read

Both formats build, and the structure is now asserted by the test suite rather
than checked by hand: valid EPUB zip, every figure embedded, DOCX at 6x9 with a
4.5in measure and mirrored margins, no table exceeding the measure.

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
- 11 of the 33 figures are 7.02in tall against a 7.5in text block, so they
  become full-page figures. That is legitimate but it leaves partly blank pages
  before them. Decide whether that reads acceptably or whether those figures
  should be cut down further. Note that shrinking them costs type size, and
  several are already close to the 8pt floor.
- Open the EPUB in a reader and check reflow, particularly the two 33-row
  mapping tables and the long Appendix B trap tables.

**Extent:** roughly 100 text pages plus figure space, so about 115 pages after
the review additions. Comfortably past KDP's 79-page spine threshold now.

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

## 5. Spare word budget — mostly spent

1,888 words remain of the 33,000 budget, raised from 28,000 during the editorial
review. The drills, decision tables, and appendices consumed the rest.

The obvious use for what is left is Appendix B, which has 59 traps against the
review's suggested 100. Adding rows is cheap and the appendix is pure revision
value. Anything else needs the budget raised again, which would start to cost
the compression positioning in BOOK-SPEC.

## 6. Part II numbers — checked

Every quantity in the five scenarios was worked through. Two did not hold and
are fixed:

- **Ardwick (ch16).** 240,000 vehicles sampling every few seconds generates
  roughly 1.4 billion readings a day, which fills a nine-terabyte database in
  about six weeks. The scenario simultaneously had warranty engineers analysing
  "several years" of history out of that same database. The fix turns the hole
  into the point: the current system purges after two months, keeping only a
  daily average, which is exactly why "retain all raw telemetry" is a stated
  requirement.
- **Wexley (ch14).** 400,000 hours of archive across sixty years works out to
  18 hours of finished programming every single day, which no factual
  broadcaster produces. Reduced to 120,000 hours, or about 5.5 hours a day.

Checked and sound: Halverston's backlog (90,000 items at 400 a week is 4.3
years, which supports the argument being made), and Brandell's 11 TB against its
cutover window (24 hours at 1 Gbps, so an export-and-import genuinely does not
fit, as the text claims).

## 7. BOOK-SPEC reconciled

Done. The Part II table listed ch14 as live-event streaming and ch15 as a game
backend; both had drifted in the skeletons before drafting and the manuscript
versions are better, so the spec now matches the book and records why the
divergence was kept. Figure count corrected from the planned 40 to the 33 built,
with the print constraint that caused it written down: a 4.5in figure holds
about two columns of short labels before type drops below the 8pt floor.

## 7b. Before uploading to KDP

- **Imprint name.** `metadata.yaml` still says TODO. KDP needs one: invent an
  imprint or use "Independently published". Everything else in that file is
  filled: author, rights, date, and a generated EPUB identifier.
- **Cover.** Not started, and it is the one asset with no source in this
  repository. 1600x2560 for Kindle; the paperback wrap needs the final page
  count for the spine, so do it after the layout pass.
- **Layout pass in Word**, applying `PRODUCTION-NOTES.md` — particularly the
  distinct treatment for the five high-yield pages.
- **Positioning copy.** Draft the KDP description from `AGENT-BRIEF.md`, which
  leads on compression and the evergreen case studies rather than coverage.

## 8. Housekeeping

- `current_state_review.md` was deleted: a snapshot from when only ch01-ch03
  were drafted, wrong throughout by the time the manuscript was finished, and a
  stale review is worse than none. Recoverable from git history at 9861160 if
  any of it is wanted. Current state lives in handover.md section 1.1 and here.
- The sample figure sources (`sample_hybrid.py`, `sample_flow.mmd`) were deleted
  once real figures existed.
- `agent_feedback.md` predates this drafting pass; re-read it before the next
  one to check nothing in it went unaddressed.
