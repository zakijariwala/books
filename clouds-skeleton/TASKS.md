# Tasks

Ordered. Each block unblocks the next. Tasks marked **you** need the author and
cannot be delegated to a model without deleting the reason the book exists.

---

## Blocking everything: the voice

- [ ] **you** Record voice notes per `voice/BRIEF.md`. Talk, do not write.
- [ ] **you** Transcribe (e.g. Whisper). Delete filler and nothing else. No
      tidying. Paste into `voice/sample.md`, replacing the stub.
- [ ] **you** React to the specimen in `voice/BRIEF.md`. Every "I would never say
      that" is a rule the spec cannot produce; add it to CLAUDE.md's voice list.

## Blocking the TOC freeze

- [ ] **you** Write the thesis paragraph into the top of `CLAUDE.md`.
- [ ] **you** Write `docs/buyer.md`: the one reader, their outcomes, the second
      layer if any, the purchase moment, any bulk buyer.
- [ ] Run `prompts/stage2-kill-test.md`. It writes `docs/toc-review.md`.
- [ ] **you** Accept, reject, or amend each proposed cut and merge.
- [ ] **you** Fold the accepted changes into `docs/toc.md`. Freeze it. Commit.

## Blocking any chapter that touches a recurring tension

- [ ] **you** Resolve the open items in `HANDOVER.md` by writing a one-paragraph
      rule into `CLAUDE.md`, so eleven chapters do not each invent a compromise.

## Standards, one run, after the TOC freezes and the voice exists

- [ ] Run `prompts/stage3-standards.md`. It produces `docs/chapter-template.md`,
      `docs/terminology.md`, both registries, `.vale.ini`, and `setup.sh`.
- [ ] **you** Edit `docs/terminology.md` yourself. This one does not survive
      being left to a model.

## The pilots — these carry the project

- [ ] `/article N` for two or three chapters that test different demands
      (can you explain / can you tell a story / can you carry business weight).
- [ ] **you** Fill every STORY-TODO marker. This is the part that sells the book.
- [ ] **you** Publish them. Watch who responds and forwards. Collect the email of
      everyone who replies — that list is your launch reviewer pool.
- [ ] **you** Confirm or reopen the reader direction based on who responded, not
      on what a model said.

## Chapters — not before the articles are out

- [ ] Per chapter: `/draft N`, `/review N`, revise, `/verify N`, `/approve N`.
- [ ] **you** Send the first two chapters to three people who match `buyer.md`.
      Change the standards on what they said, then continue.

## Build — after three approved chapters

- [ ] Run `prompts/stage6-deferred.md`: figures, `make diagrams`, `make build`,
      `scripts/wordcount.py`, `make status`.

## Housekeeping

- [ ] Confirm the git author name and email are correct for a published work.
