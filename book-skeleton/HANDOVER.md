# Handover

**Book:** [TITLE]
**State as of [DATE]:** [one line — e.g. scaffold complete, no prose written]
**Next action:** [the single most important next step]

The living state doc. Update it at the end of any session that changes the
project's state, so the next session — human or AI — starts oriented instead of
reconstructing context from a chat scrollback. This is the first file to read
after `CLAUDE.md`.

---

## Where things are

| Path | What it is | State |
|------|-----------|-------|
| `BOOK-SPEC.md` | Thesis, positioning, word budget, structure. | [state] |
| `docs/buyer.md` | The reader. Wins scope arguments. | [state] |
| `docs/toc.md` | Chapter list. | [frozen? / not frozen] |
| `voice/sample.md` | The voice transcript. The only style input. | [real / stub — blocks drafting] |
| `manuscript/` | Chapters. | [count against budget] |
| Build (`make epub docx`) | EPUB + DOCX. | [never run / builds / verified in a reader] |

## Decisions taken, and why

[Record the load-bearing decisions and their reasoning: reader direction and the
alternative rejected, chapters cut or merged in the kill test, any rule added to
CLAUDE.md mid-project and what forced it. Future sessions will ask why; answer
once, here.]

## Open items that block drafting

[Unresolved questions that would otherwise be answered inconsistently across
chapters. Resolve each once, in CLAUDE.md, before the chapters that hit it.]

## Rules a new session must not break

- Never draft a chapter without reading the four files `CLAUDE.md` names.
- Never invent a first-hand story. Mark `<!-- STORY-TODO: ... -->` and move on.
- `voice/sample.md` is the only style source. Never read `voice/BRIEF.md` as one.
- Verify stale-able facts against a primary source; date anything that ages.
- Do not draw figures until three chapters are approved.
