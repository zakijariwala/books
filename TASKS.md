# Tasks

Ordered. Each block unblocks the next. Owner marked **you** cannot be delegated
to a model without deleting the reason the book exists.

---

## Blocking everything

- [ ] **you** Record three voice notes per `voice/BRIEF.md`. 25 minutes, no
      preparation, no restarts. The night something broke. What you do all day,
      told to a cousin who sells insurance. The thing non-technical colleagues
      believe that is wrong.
- [ ] **you** Transcribe with Whisper. Delete filler and nothing else. No
      tidying. Paste into `voice/sample.md`, replacing the stub.
- [ ] **you** React to the specimen in `voice/BRIEF.md`. Every "I would never
      say that" is a rule the spec cannot produce.

## Blocking the TOC freeze

- [ ] **you** Write the thesis paragraph into the top of `CLAUDE.md`, replacing
      the bracketed placeholder.
- [ ] **you** Read `docs/toc-review.md`. Accept, reject, or amend each cut:
      chapter 13 cut, chapter 10 cut and redistributed, chapter 14 merged,
      chapter 1 shrunk.
- [ ] **you** Decide the Part IV question. Three parts with economics promoted,
      or lock-in stays as a short chapter 12.
- [ ] **you** Decide where the discussion guide lives. Back matter,
      downloadable, or both.
- [ ] **you** Fold the accepted cuts into `docs/toc.md`. Freeze it. Commit.

## Blocking chapter 4

- [ ] Write the cost rule into `CLAUDE.md`. The book teaches cost shape, not
      cost. No dollars, no rate cards. One paragraph, before any chapter that
      touches money.

## Stage 3, one run, after the TOC freezes

- [ ] `docs/chapter-template.md` with per-section word budgets totalling 3,800
      to 4,200, optional sections marked, and the layer rule from
      `docs/buyer.md` reflected in the section notes.
- [ ] `docs/terminology.md`. One approved definition per term.
- [ ] **you** Edit `docs/terminology.md` yourself afterward. This one does not
      survive being left to a model.
- [ ] `docs/concept-registry.md`, prefilled from the frozen TOC.
- [ ] `docs/case-study-registry.md`. Borrowed rows filled with sources and
      fact-check dates, first-hand rows left empty for you.
- [ ] `.vale.ini` and `.vale/styles/Book/`. Six rule families come straight from
      CLAUDE.md today: em dashes, `-ly` adverbs, not-X-it's-Y, corporate jargon,
      vendor evangelism, exam-prep phrasing. Severity warning, not error.
- [ ] `setup.sh`. Vale and Pandoc installed and verified. Graphviz, the Python
      diagrams library, and mermaid-cli commented out with a note.
- [ ] Append three voice rules extracted from the transcript to CLAUDE.md, each
      quoting the sentence it came from.

## Stage 4, the pilots. These carry the project.

- [ ] `/article 2` What happens when you upload a photo. Tests whether you can
      explain.
- [ ] `/article 3` Meet the landlords. Tests whether you can tell a story.
- [ ] `/article 12` Cloud economics. Tests whether you can carry business weight.
- [ ] **you** Fill every STORY-TODO marker. This is the part that sells the book.
- [ ] **you** Publish all three. Test both subtitle candidates as headlines.
- [ ] **you** Wait. Read the comments. Collect the email address of everyone who
      replies. That list is the launch reviewer pool.
- [ ] **you** Settle the Option A bet. Who forwarded them? Product managers and
      founders confirm the direction. Teachers and journalists reopen it.
- [ ] **you** Change the standards based on what strangers said, not on what a
      model said.

## Stage 5, chapters. Not before the articles are published.

- [ ] `/draft 2`, `/review 2`, revise, `/verify 2`, `/approve 2`
- [ ] `/draft 3`, `/review 3`, revise, `/verify 3`, `/approve 3`
- [ ] Send both chapters to three people who match `docs/buyer.md`.
- [ ] Change the standards on what those three said. Then continue.
- [ ] Remaining chapters, same loop.

## Stage 6, after three approved chapters

- [ ] Draw the figures listed in `docs/figures.md`. Grayscale, one idea each, at
      most six labels.
- [ ] `make diagrams`, 300 DPI grayscale PNG, roughly 1350px for a 6x9 trim.
- [ ] `make build`, Pandoc assembly.
- [ ] `scripts/wordcount.py` and `make status`. Words per chapter against budget,
      total against 56,000, remaining STORY-TODO and FIGURE markers.

## Housekeeping

- [ ] **you** Fix the git author name. See the note at the bottom of the first
      commit message.
- [ ] Decide whether `voice/BRIEF.md` moves to `docs/`, or whether CLAUDE.md
      gets the line naming `voice/sample.md` as the only style input. Second is
      cheaper and survives file moves.
