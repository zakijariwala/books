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

## 3. Volatile facts — verified against the certification page

Checked against Google's live Professional Cloud Architect certification page.
Both of the two figures the book actually asserts are correct, and the four it
deliberately declines to print need no action, because there is no number in the
text to be wrong.

| Fact | Where | Status |
| --- | --- | --- |
| Exam cost, duration, question count, renewal terms | back-matter.md | Verified. Two hours, 50-60 questions, 20-30% on two case studies, $200, two years' validity, renewal one hour and 25 questions at $100 |
| Current case-study list | back-matter.md, ch01 | Verified. Altostrat Media, Cymbal Retail, EHR Healthcare, KnightMotives Automotive. The four named as retired are retired |
| Interconnect bandwidth tiers and SLA terms | ch03, ch13 | No figures printed; ch03:107 tells the reader to confirm. Nothing to correct |
| Cloud Run request timeout ceiling | ch04 | No figure printed; ch04:117 says the maximum has moved and to verify it. Nothing to correct |
| Vertex AI product and model names | ch08 | Written at decision level; ch08:19 flags the churn. No model names or versions anywhere in the chapter |
| Security Command Center tier contents | ch09 | No tier contents listed; ch09:103 tells the reader to verify. Nothing to correct |

One figure was sharpened rather than corrected. The renewal exam is now a single
generative-AI case study carrying 90-100% of the paper, which is a stronger
claim than "weights whatever Google has added since". back-matter.md now says
renewal is a narrower examination than the standard exam rather than a lighter
one, since a reader planning a renewal sit needs to know that.

Chapters 7 and 8 will still date soonest. Treat them as the first candidates for
review on any reprint.

## 4. ch16 against KnightMotives Automotive — checked, one decision open

**Caveat on the source.** Google serves the exam guide from a host this check
could not reach, so the comparison below is drawn from published third-party
summaries of KnightMotives rather than from Google's own text. That is adequate
for judging premise overlap and it is *safer* for the copyright question, since
no official prose was read. It is not adequate for concluding the requirement
sets differ in detail. Re-run this against the real guide before publishing.

**ch17 (Brandell) is clear.** The live set is Altostrat Media (GKE content
platform, generative AI), Cymbal Retail (retail modernisation, generative AI),
EHR Healthcare (co-location exit, already containerised) and KnightMotives
Automotive (vehicle telemetry). None is a legacy monolith against a fixed
external deadline. EHR Healthcare is the nearest and is not close: it moves a
modern stack for scale and disaster recovery, where Brandell cannot rearchitect
at all because the clock is the binding constraint. The slot the chapter was
written to occupy is still empty, and it is the only chapter carrying
team-capability-as-constraint as its central tradeoff.

**ch16 (Ardwick) does overlap, and it is worth deciding about deliberately.**

Not a legal problem. Different company, different sector (commercial
refrigerated haulage against consumer connected-car), different numbers, no
reproduced text, and a requirement set Ardwick does not share — see below. The
AGENT-BRIEF claim of no copyright exposure holds.

A perception problem, yes. Both scenarios are vehicle telemetry, both have an
on-premises current state that will not scale, both are driven by predictive
maintenance, and the canonical answer to both is the same trio: Pub/Sub in
front, Bigtable keyed on vehicle identifier plus timestamp for the point
lookup, BigQuery for the analytical scan. A reader who has studied
KnightMotives will read ch16 as KnightMotives with refrigerated trucks.

That convergence is mostly unavoidable and partly the point. Pub/Sub plus
Bigtable plus BigQuery *is* the correct answer for vehicle telemetry, so any
original scenario on that premise lands there. Avoiding the domain to look
original would serve the reader worse, because the domain is on the exam
precisely while KnightMotives is live.

What Ardwick genuinely owns, and what the chapter should lean on harder if it
stays as it is: the purge job. A retention hole nobody decided to create is the
chapter's own teaching, it produces the Cloud Storage tier that KnightMotives'
canonical answer does not have, and it is the part a reader cannot get from
studying the official scenario. Same for intermittent connectivity producing
late and out-of-order arrival, which forces event-time windowing.

The tension to resolve is with the book's own positioning. Part II's argument is
that guides pinned to live scenarios teach a syllabus with an expiry date. ch16
is the one chapter whose premise is pinned to a live scenario. It survives
rotation fine, being original — but while KnightMotives is live it invites
exactly the criticism the book makes of others. **Recommended fix: name it.** A
sentence in the ch16 opener or the Part II opener saying this scenario
deliberately parallels a live one so the reader can calibrate against it, while
the other four deliberately do not. Cheapest option, honest, and it defuses the
derivative reading by getting there first.

**A gap this check turned up, which matters more than the overlap.**
KnightMotives' signature requirement is exposing selective vehicle data to
external partners — insurers, dealerships — through an API, without giving them
access to internal systems. That routes to Apigee or API Gateway. The
manuscript has **no coverage of API management anywhere**: no Apigee, no API
Gateway, no mention of the pattern. Ardwick has no partner-sharing requirement
either, so the book never raises it. This is a live case study's central
decision with zero treatment, and it is a coverage hole rather than a
positioning one.

**Both are now actioned.** The parallel is named in the Part II opener rather
than disguised, and the paragraph turns it into an exercise: work Ardwick, then
read KnightMotives and write down what it asks for that Ardwick does not. That
sends the reader at the partner-sharing decision under their own steam.

The API-management hole is closed away from ch16, deliberately. Adding a
partner-sharing requirement to Ardwick would have made it *more* like
KnightMotives, not less. It went to Northmoor in ch13 instead, which already
stated in its premise that it processes results for eight hundred external
clinics and then never said how those clinics get them — a hole in that
chapter's own worked solution, quite apart from the coverage gap. Northmoor now
carries the requirement, the SFTP-drop current state with two clinics polling
hourly, a worked paragraph resolving it to Apigee or API Gateway, and a question
in its exam-shapes list. ch09 gained the reference treatment beside
Identity-Aware Proxy, including the distinction the exam tests between an API
for on-demand records and an authorised view or Analytics Hub listing for a
partner running their own queries. Two rows went into the ch09 mapping table,
two into Appendix A's security sheet, three into Appendix B, and Apigee into the
glossary. `accept.txt` gained `Apigee` and `SFTP`, without which Vale fails at
error level and the pre-commit hook blocks.

Still open from this section: re-run the comparison against Google's real exam
guide, per the caveat above.

## 5. Spare word budget — nearly spent

436 words remain of the 33,000 budget, raised from 28,000 during the editorial
review. The drills, decision tables, and appendices consumed most of it; the
API-management work in §4 took about 720 words of what was left.

That was the right call over the alternative, which was padding Appendix B
towards the review's suggested 100 traps. A trap the book has no chapter behind
is a trivia row, and the API gap was a live case study's central decision with
no treatment anywhere.

What remains does not fund another section. Appendix B stands at 62 traps and
adding rows is still the cheapest way to spend the last of it, at roughly 15
words a row. Anything larger needs the budget raised again, which starts to cost
the compression positioning in BOOK-SPEC, and that positioning is what
`KDP-LISTING.md` leads on.

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

- **Imprint name.** Done. `metadata.yaml` says "Independently published", KDP's
  own string, chosen because the route is settled as a direct KDP launch and an
  invented imprint buys nothing. Replace it if a named imprint is registered
  later; nothing downstream reads the value.
- **Positioning copy.** Done, in `KDP-LISTING.md`: product description in plain
  text and in KDP's HTML subset, both inside the 4,000-character limit, plus the
  seven keyword slots, three categories, and a note on what the first two lines
  have to carry above the mobile fold.
- **Cover.** Still the one asset with no source in this repository. 1600x2560
  for Kindle; the paperback wrap needs the final page count for the spine, so do
  it after the layout pass.
- **Layout pass in Word**, applying `PRODUCTION-NOTES.md`, particularly the
  distinct treatment for the five high-yield pages. This and the cover are the
  two remaining blockers, and both need a human at a machine with Word.
- **Price.** Open decision. `KDP-LISTING.md` sets out the per-page against
  per-value comparison; pick which one the listing invites.

## 8. Housekeeping

- `current_state_review.md` was deleted: a snapshot from when only ch01-ch03
  were drafted, wrong throughout by the time the manuscript was finished, and a
  stale review is worse than none. Recoverable from git history at 9861160 if
  any of it is wanted. Current state lives in handover.md section 1.1 and here.
- The sample figure sources (`sample_hybrid.py`, `sample_flow.mmd`) were deleted
  once real figures existed.
- `agent_feedback.md` predates this drafting pass; re-read it before the next
  one to check nothing in it went unaddressed.
