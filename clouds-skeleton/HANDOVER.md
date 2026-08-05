# Handover

**Book:** [TITLE]
**State as of [DATE]:** [one line — e.g. scaffold complete, no prose written]
**Next action:** [the single most important next step]

The living state doc. Update it at the end of any session that changes the
project's state, so the next session (human or AI) starts oriented. Prefer this
over a long chat scrollback.

---

## Where things are

| Path | What it is | State |
|------|-----------|-------|
| `CLAUDE.md` | Thesis, reader, budget, voice and content rules. Loads every session. | [state] |
| `docs/buyer.md` | The reader. Wins scope arguments. | [state] |
| `docs/toc.md` | Chapter list. | [frozen? / not frozen] |
| `voice/sample.md` | The voice transcript. The only style input. | [real / stub — blocks drafting] |
| `.claude/skills/` | `/article /draft /review /approve /verify` | [state] |
| `manuscript/` | Chapters. | [count] |

## Decisions taken, and why

[Record the load-bearing decisions and their reasoning. Future sessions will ask
why the TOC is shaped as it is, why a chapter was cut, why the reader is who they
are. Write the reasoning down once, here, so it is not re-litigated every
session. Examples of the kind of decision worth recording:]

- Direction / reader choice, and the alternative rejected.
- Chapters cut or merged in the kill test, and why.
- Any rule added to `CLAUDE.md` mid-project, and what forced it.

## Open items that block drafting

[The unresolved questions that will otherwise get answered inconsistently across
chapters. Resolve them once, in CLAUDE.md, before the chapters that hit them.]

## Rules a new session must not break

[The short list of traps specific to this book. Seeded with the universal ones:]

- Never write chapter content without reading the four files CLAUDE.md names.
- Never invent a first-hand story. Mark `<!-- STORY-TODO: ... -->` and move on.
- `voice/sample.md` is the only style source. Never read `voice/BRIEF.md` as one.
- Verify stale-able facts against a primary source; date anything that ages.
- Do not build the diagram or Pandoc pipeline until three chapters are approved.
