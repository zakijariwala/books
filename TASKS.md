# Tasks

Ordered. Each block unblocks the next. Owner marked **you** cannot be delegated
to a model without deleting the reason the book exists.

---

## Voice: unblocked via the reference article (2026-08-08)

The transcript no longer blocks everything. The author supplied an article as a
register target (`voice/reference-article.md`), the CLAUDE.md voice rules were
blended to fit it, and a pilot (`voice/pilot-ch01.md`) confirmed the voice
holds. Drafting can proceed. The transcript is still wanted, but its job is now
to fill `STORY-TODO` markers with first-hand beats, not to gate the project.

- [ ] **you** Record three voice notes per `voice/BRIEF.md`. 25 minutes, no
      preparation, no restarts. The night something broke. What you do all day,
      told to a cousin who sells insurance. The thing non-technical colleagues
      believe that is wrong. Fills the STORY-TODO markers.
- [ ] **you** Transcribe with Whisper. Delete filler and nothing else. No
      tidying. Paste into `voice/sample.md`, replacing the stub.

## TOC freeze (done 2026-08-08)

- [x] Thesis written into `CLAUDE.md` (the eighteen-month gap), replacing the placeholder.
- [x] Kill test decided: cut old 10 and old 14 (merged), shrink ch1. Chapter 13
      (AI Infrastructure Wars) kept as an authored override and re-aimed as the
      closer, ch12. See `docs/toc.md`.
- [x] Part IV question resolved: keeping AI Wars gives Part IV two chapters
      (Economics + AI Wars). No promotion needed.
- [x] Cuts folded into `docs/toc.md` and frozen.
- [ ] **you** Decide where the discussion guide lives. Back matter,
      downloadable, or both. Deferred; does not block drafting.

## Cost rule (done 2026-08-08)

- [x] Cost rule written into `CLAUDE.md` hard content rules: teach cost shape,
      not price. No dollars, no rate cards.

## Stage 3 scaffolding (done 2026-08-08, except tooling)

- [x] `docs/chapter-template.md` with per-section word budgets totalling 3,800
      to 4,200 and the buyer.md layer rule reflected per section.
- [x] `docs/terminology.md` seeded. One definition per term.
- [ ] **you** Edit `docs/terminology.md` yourself. This one does not survive
      being left to a model. Seeded definitions are marked for your review.
- [x] `docs/concept-registry.md`, prefilled from the frozen TOC.
- [x] `docs/case-study-registry.md`. Borrowed rows seeded (verify before use),
      first-hand rows left as STORY-TODO for you.
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
