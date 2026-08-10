# Handover

## Two branches, two jobs. Read this before merging anything.

**`claude/voice-feature-2hvzrj` is an experiment. It is not a candidate for
merge.** It exists to produce a complete first draft at the target register with
no first-hand story anywhere in it, so the author can read it cold, analyse it,
and shred it. The prose is not the deliverable. The deliverable is the evidence
of where a story is load-bearing and where a `STORY-TODO` marker was inserted out
of habit and carries nothing.

**`book/clouds` is where the lessons get applied.** After the shred, the author
picks roughly five stories that apply to this book and are worth telling, records
in the directions the shred points, and the consolidated result lands there.
Nothing on the experiment branch moves across wholesale.

Consequences for anyone drafting on the experiment branch:

- A `STORY-TODO` is a finding, not a placeholder. Write the marker so it states
  what the story has to prove and what the chapter loses without it. A marker
  that cannot say what it would prove is itself the finding: that chapter does
  not need a story.
- Do not thin the markers to hit a target. The point of drafting all twelve is to
  let the ranking fall out of the reading.
- `docs/story-candidates.md` collects every marker in one place for that ranking.
- CLAUDE.md still says every chapter carries at least one first-hand story. That
  rule describes the finished book on `book/clouds`, and it is in tension with
  picking five. The shred settles it. Do not quietly relax the rule here.


**Book:** The Clouds, for People Who Don't Do Servers
**State as of 2026-08-09:** First draft complete on the experiment branch. All
twelve chapters drafted, 45,891 words, every chapter inside the 3,800 to 4,200
budget and clean on the hard lint rules. Twelve first-hand markers, one per
chapter, each stating what the story must prove and what the chapter loses
without it. Four pilot articles drafted.
**Next action:** the shred. Read `build/draft.html`, fill the Verdict column in
`docs/story-candidates.md`, and pick roughly five stories to record. See the
two-branch note below before merging anything.

**The reading copy:** `scripts/build-draft.sh` consolidates the twelve chapters
into one file, places the figures where the prose refers to them, and turns the
STORY-TODO markers into visible annotations rather than hidden comments, since a
hidden comment cannot be judged. Output is `build/draft.md` and
`build/draft.html`, both ignored by git because the manuscript is the source.
Built ahead of the Stage 6 gate for the same reason as the figures: the draft
cannot be judged as a whole in twelve pieces.

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
| `prompts/` | Stage 2, 3, and 6 prompt text. | Stage 2 and 3 spent. Stage 6 partly overtaken: figures and the build exist. |
| `.claude/skills/` | `/article` `/draft` `/review` `/approve` `/verify` | Live. |
| `manuscript/` | Twelve chapters, ch01 to ch12. | Complete first draft, 45,891 words. |
| `articles/` | Four pilot articles (2, 3, 11, 12). | Drafted, unpublished. |
| `figures/` | Twelve grayscale SVGs plus rendered PNGs. | Drawn 2026-08-09. SVG tracked, PNG ignored. |
| `docs/figures.md` `docs/story-candidates.md` | Figure spec; story ranking instrument. | Live. Verdict column awaits the shred. |
| `scripts/` | `figures.py` `render-figures.sh` `build-draft.py` `build-draft.sh` `draft.css` | Live. |
| `setup.sh` `.claude/hooks/` | Toolchain install and SessionStart hook. | Live. Vale, Pandoc, poppler, librsvg. |
| `.vale.ini` `.vale/styles/Book/` | Seven prose rules from CLAUDE.md. | Live, warning severity. |
| `reviews/` | Empty. | `/review` has not been run on the draft. |

Still not built, and not needed yet: a `Makefile` and `scripts/wordcount.py`.
The governing rule is build only what the next work needs.
`scripts/build-draft.sh` covers assembly, and word counts come from the chapter
headers in the reading copy.

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

**14 chapters become 12.** From `docs/toc-review.md`, with one authored
override. The kill test recommended eleven; the author kept The AI Infrastructure
Wars and re-aimed it as the closer, which also gave Part IV two chapters. See
`docs/toc.md`:

- **Chapter 13, The AI Infrastructure Wars: recommended for cutting, kept.** The
  kill test was right that it aged fastest and depended on nothing. The author
  overruled it because the turmoil of the AI era does not survive being merged
  into cost sidebars. Terms of the override: it becomes the closer, it depends on
  the whole book, it carries turmoil rather than billing mechanics, and every
  figure carries the year it was true. GPU cost shape still moved to compute and
  the AI bill line still moved to economics.
- **Cut chapter 10, Containers and Serverless, as a standalone.** The business
  story is two facts and neither needs the word Docker. Position 10 is where
  buyer.md predicts she stops reading. Redistributed: shipping cadence into
  compute, serverless billing into economics, serverless elasticity into scaling.
- **Merge chapter 14, Vendor Lock-In,** half into Meet the Landlords and half
  into Cloud Economics. If it stays standalone it moves to Part I, never the end.
- **Shrink chapter 1** to carry the thesis rather than datacenter nostalgia.
- **Guard chapter 10, Security,** against growing a service catalogue. Its
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

## Open items (nothing blocks drafting)

**Resolved: the cost rule.** Written into CLAUDE.md hard content rules. The book
teaches cost shape rather than cost: which line dominates, which surprises, which
grows with users and which with data. No dollars, no rate cards. Every chapter
was drafted against it and the Vale `Book.Prices` rule enforces it.

**Resolved: Part IV.** Keeping The AI Infrastructure Wars gave Part IV two
chapters, Economics and the closer. No promotion needed.

**Open: the discussion guide.** buyer.md's bulk buyer needs it and the TOC does
not hold it. The twelve Monday questions are the raw material and all twelve are
now written. Decide back matter, downloadable, or both.

**Open: `docs/terminology.md` needs the author's edit.** TASKS.md is right that
the definitions do not survive being left to a model, and the seeded ones have
not been reviewed.

**Open: the shred.** The whole point of this branch. See the top of this file.

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
