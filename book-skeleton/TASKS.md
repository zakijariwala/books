# Outstanding Work

The living backlog, ordered so each block unblocks the next. Tasks marked
**you** need the author and cannot be delegated to a model without deleting the
reason the book exists. Keep it current; a stale task list is worse than none.

This is the starter set for a new book. Delete what you finish, add what you find.

## Stage 0 — setup

- [ ] `bash scripts/bootstrap.sh` — venv, dependencies, tool check, `vale sync`.
- [ ] `make hooks` — install the pre-commit gate.
- [ ] `make test` passes green on the empty skeleton.
- [ ] Fill in `metadata.yaml` (title, author, imprint, UUID, lang).

## Stage 1 — decide (blocks everything)

- [ ] **you** Write the thesis into `BOOK-SPEC.md`. One paragraph every chapter serves.
- [ ] **you** Write `docs/buyer.md`: the one reader, their outcomes, the second
      layer if any, the purchase moment, any bulk buyer.
- [ ] **you** Set the word budget in `BOOK-SPEC.md` and `WORD_BUDGET` in the `Makefile`.

## Stage 1b — find the voice (blocks drafting)

- [ ] **you** Record voice notes per `voice/BRIEF.md`. Talk, do not write.
- [ ] **you** Transcribe, delete filler only, paste into `voice/sample.md`.
- [ ] **you** React to the specimen in `voice/BRIEF.md`; fold each correction into
      `CLAUDE.md`'s voice list and, where mechanical, into Vale.

## Stage 2 — freeze the structure

- [ ] Run `prompts/stage2-kill-test.md` → `docs/toc-review.md`.
- [ ] **you** Accept/reject/amend each cut and merge. Fold into `docs/toc.md`. Freeze. Commit.

## Stage 3 — standards

- [ ] Run `prompts/stage3-standards.md`: chapter template, terminology,
      registries, voice lint rules.
- [ ] **you** Edit `docs/terminology.md` yourself afterward.

## Stage 4 — pilots (these carry the project)

- [ ] `/article N` for two or three chapters that test different demands.
- [ ] **you** Fill every STORY-TODO. Publish. Watch who forwards. Collect replier emails.
- [ ] **you** Confirm or reopen the reader direction on the evidence.

## Stage 5 — chapters

- [ ] Per chapter: `/draft N`, `/review N`, revise, `/verify N`, `/approve N`.
- [ ] Keep `make wordcount` inside budget and the registries current.
- [ ] **you** Send the first two chapters to three people who match `buyer.md`;
      adjust standards on what they say.

## Stage 6 — figures and build

- [ ] After three approved chapters, run `prompts/stage6-figures.md`.
- [ ] `make lint` clean at error level; `make test-build` passes against EPUB + DOCX.
- [ ] Human read of the built book: figure placement, orphaned captions, table
      breaks at 6x9, EPUB reflow.

## Pre-publication

- [ ] Cover made; imprint set; layout pass done (`PRODUCTION-NOTES.md`).
- [ ] All stale-able facts verified and logged; `BOOK-SPEC.md` "Facts to verify" clear.
- [ ] Store description drafted (`AGENT-BRIEF.md`).
