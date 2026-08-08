# Handover

**Book:** The Clouds, for People Who Don't Do Servers
**State as of 2026-08-08:** TOC frozen (12 chapters), thesis and cost rule
written, Stage 3 scaffolding built, voice unblocked via a reference article and
confirmed by a pilot. Ready to draft.
**Next action:** `/article 2` or `/draft 1`. First-hand beats land as STORY-TODO
until the transcript exists. See TASKS.md.

---

## Where things are

| Path | What it is | State |
|------|-----------|-------|
| `CLAUDE.md` | Thesis, reader, budget, voice rules, hard content rules. Loads every session. | Live. Thesis written (the eighteen-month gap). Cost rule added. Voice rules blended for the reference article. |
| `docs/buyer.md` | The reader. Wins any argument about scope. | Written. Option A, layered. |
| `docs/toc.md` | 12 chapters, four parts. | **Frozen 2026-08-08.** Cuts folded in; ch12 (AI Wars) kept as authored override. |
| `docs/toc-review.md` | Kill test output: promises, cuts, dependency map, callback thread. | Complete. Historical record; ch13 recommendation was overridden. |
| `docs/chapter-template.md` `docs/terminology.md` `docs/concept-registry.md` `docs/case-study-registry.md` | Stage 3 scaffolding. | Built 2026-08-08. terminology.md awaits author edit. |
| `voice/reference-article.md` | The register target the author supplied. | Live. Rhythm and argument source. |
| `voice/pilot-ch01.md` | Voice pilot, ch1 opening (~817 words). | Written. Confirmed the blended voice holds. |
| `voice/BRIEF.md` | Target register, extraction method, straw-man specimen. | Written. Not a voice source, do not read it as style input. |
| `voice/sample.md` | The transcript. | Stub. No longer blocking; fills STORY-TODO beats when it exists. |
| `prompts/` | Stage 2, 3, and 6 prompt text. | Stage 2 spent. Stage 3 ready. Stage 6 deferred. |
| `.claude/skills/` | `/article` `/draft` `/review` `/approve` `/verify` | Live. |
| `articles/` `manuscript/` `reviews/` `scripts/` | Empty. | Waiting on the transcript. |

Not yet built, on purpose: `docs/chapter-template.md`, `docs/terminology.md`,
both registries, `.vale.ini`, `.vale/styles/Book/`, `setup.sh`, `Makefile`,
`scripts/wordcount.py`. Governing rule is build only what the next 5,000 words
need. Stage 3 makes the first six. Stage 6 makes the rest after three chapters
exist.

---

## Decisions taken, and why

**Direction is Option A: one structural reader, one designed second layer.**
Meera the product manager carries the structure. The banker, clerk, accountant,
philosophy teacher, and English major are served by fixed sections of every
chapter rather than by a widened target. Reason: Option A has a purchase trigger
(48 hours after a meeting where she felt exposed), a bulk buyer (40 copies for an
AE team), and a findable category. A general-interest book has none of the three
and needs an author platform that does not exist yet. Option A can widen later.
A general book cannot retrofit the utility that made it worth 40 copies.

**The layer rule is operational, not aspirational.** `docs/buyer.md` maps every
chapter-template section to the reader it serves, and states two failure tests.
`/review` checks them.

**14 chapters become 11.** From `docs/toc-review.md`:

- **Cut chapter 13, The AI Infrastructure Wars.** No Monday action without
  inventing one. All stale-able figures in a book that dates its figures. Zero
  dependencies in either direction. Best-written by a chatbot, which is the
  material buyer.md says the reader is escaping. GPU cost shape moves to compute,
  AI as a growing bill line moves to economics.
- **Cut chapter 10, Containers and Serverless, as a standalone.** The business
  story is two facts and neither needs the word Docker. Position 10 is where
  buyer.md predicts she stops reading. Redistributed: shipping cadence into
  compute, serverless billing into economics, serverless elasticity into scaling.
- **Merge chapter 14, Vendor Lock-In,** half into Meet the Landlords and half
  into Cloud Economics. If it stays standalone it moves to Part I, never the end.
- **Shrink chapter 1** to carry the thesis rather than datacenter nostalgia.
- **Guard chapter 11, Security,** against growing a service catalogue. Its
  misconception section carries the chapter: security is not a wall, it is blast
  radius.

**Part II is a structural bottleneck.** Compute, storage, networking, and
databases all depend on chapter 2 and feed nothing until Part III. Four chapters
of the same shape is where a business reader stops, and a general reader never
needed four. Both readers want the same cut. Economics is the antidote and the
current TOC saves it for last.

**The photo upload thread is the spine.** Chapter 2 follows one upload end to
end. Nine later chapters call back to it, two or three sentences each.
`docs/toc-review.md` section 5 has the full table. The chapter 7 callback answers
"read replica" with her own photo, six chapters after she wrote the term down and
never looked it up. That is the moment the reader trusts the book.

---

## Open items that block drafting

**The cost rule.** Outcome O1 asks the reader to name what each box costs.
CLAUDE.md bans vendor prices outright. Both are correct and they collide in six
of eleven chapters. Resolution has to be written into CLAUDE.md once, before
chapter 4: the book teaches cost **shape**, not cost. Which line dominates, which
surprises, which grows with users and which grows with data, and the ratios
between them. No dollars, no rate cards. Without that sentence, eleven chapters
each invent their own compromise.

**Part IV holds one chapter after the cuts,** which is not a part. Either promote
economics into Part III and run three parts, or keep lock-in as a short chapter
12. Reasonable people take either.

**The discussion guide has no home.** buyer.md's bulk buyer needs it and the TOC
does not hold it. The eleven Monday questions are the raw material. Decide back
matter, downloadable, or both, before drafting, so the Monday questions get
written to carry it.

---

## Rules a new session must not break

- Never write chapter content without reading `docs/toc.md`,
  `docs/chapter-template.md`, `docs/concept-registry.md`, `docs/terminology.md`.
- Never invent a first-hand story or attribute one to the author. Mark it
  `<!-- STORY-TODO: ... -->` and move on.
- Never read `voice/BRIEF.md` as a voice source. `voice/sample.md` is the only
  style input. The specimen inside BRIEF.md is model prose and matching it
  deletes the book's one advantage.
- No vendor prices, no SKU tiers, no quotas. Dates on anything that can go stale.
- Borrowed case studies fill at most half of any chapter's examples.
- Do not build diagrams, the Pandoc build, or the word-count script until three
  chapters are approved.

---

## The bet, and when it gets settled

Stage 4 decides whether Option A was right. Publish the three pilot articles and
watch who forwards them. Forwards from product managers, sales engineers, and
founders confirm the direction. Forwards from people with no stake in cloud at
all are evidence for a genuinely general book, and that decision reopens before
chapter 4 is drafted, not after.

Collect the email address of everyone who replies. That list is the launch
reviewer pool.
