# Outstanding Work

The living backlog. Order by risk — the things most likely to force rework sit
at the top. Keep it current; a stale task list is worse than none.

This is the starter set for a new book. Delete what you have done, add what you
discover.

## Setup

- [ ] `bash scripts/bootstrap.sh` — venv, dependencies, tool check, `vale sync`.
- [ ] `make hooks` — install the pre-commit gate.
- [ ] Fill in `metadata.yaml` (title, author, imprint, UUID, lang).
- [ ] Write `BOOK-SPEC.md`: positioning, reader, word budget, structure.
- [ ] Set `WORD_BUDGET` in the `Makefile` to match the spec.
- [ ] Decide voice and spelling in `STYLE-GUIDE.md` (and `lang` in metadata).
- [ ] Confirm `make test` passes green on the empty skeleton.

## Writing

- [ ] Draft chapters from the template in `manuscript/ch01.md`, one branch each.
- [ ] Render each figure as you reference it (`make diagrams`) — no placeholders.
- [ ] Keep `make wordcount` inside budget.

## Verification

- [ ] Log every stale-able fact in `sources/research/` with source and date.
- [ ] Keep `BOOK-SPEC.md` "Facts to verify" current.

## Pre-publication

- [ ] `make lint` clean at error level across the manuscript.
- [ ] `make test-build` passes against built EPUB and DOCX.
- [ ] Human read of the built book: figure placement, orphaned captions, table
      breaks at 6x9, EPUB reflow.
- [ ] Cover made; imprint set; layout pass done (`PRODUCTION-NOTES.md`).
- [ ] Store description drafted (`AGENT-BRIEF.md`).
