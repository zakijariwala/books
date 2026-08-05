# Two book scaffolds, compared — and consolidated

This repository now holds two proven approaches to writing a book with Git and
AI assistance, distilled from two real book projects on their own branches, plus
one seed that merges them.

| Directory | Distilled from | Philosophy |
|-----------|----------------|------------|
| `book-skeleton/` | `book/gcp-pca` (a finished, published exam-prep book) + this consolidation | **Build-first, batteries included.** The full production pipeline from day one. Now also carries the editorial layer from clouds. **This is the recommended seed.** |
| `clouds-skeleton/` | `book/clouds` (a pre-draft, process-hardened scaffold) | **Editorial-first, lean.** Reader, thesis, voice, TOC discipline, and a staged drafting workflow. Build tooling deferred until three chapters exist. |

If you only read one line: **start a new book from `book-skeleton/`.** Reach for
`clouds-skeleton/` when you want the lightest possible start and prefer to add
production tooling only when you need it.

---

## Where each came from

**`gcp-pca` was a finished book.** Its scaffold is what survives shipping: a
cross-platform Pandoc build to EPUB and DOCX, figures generated from source
(Graphviz + Mermaid) and normalised to a 6x9 print spec, a pytest suite that
enforces print invariants, Vale prose linting, and a set of production and
launch docs. It is strong on *making the book correctly*. It was comparatively
thin on *deciding what to write and in whose voice* — those decisions had
already been made by the time the repo was distilled from it.

**`clouds` was a scaffold before any prose existed.** It encodes the decisions
that come first: a single named reader who wins every scope argument, a thesis
every chapter must serve, a voice extracted from the author's own speech (never a
model's), a "kill test" that forces every chapter to justify itself, registries
that stop repetition and overused examples, and a staged drafting workflow driven
by agent skills (`/article`, `/draft`, `/review`, `/verify`, `/approve`). Its
governing rule is *build only what the next 5,000 words need* — so it has almost
no build tooling yet, on purpose.

They are two halves of the same craft. Neither is wrong; each was hardened
against a different stage of the same problem.

---

## Side by side

| Concern | `book-skeleton` (from gcp-pca) | `clouds-skeleton` (from clouds) |
|---------|-------------------------------|----------------------------------|
| Reader definition | A "Reader" section in the spec | A full `docs/buyer.md`: outcomes, second layer, purchase moment, bulk buyer |
| Thesis discipline | Implicit in positioning | Explicit thesis in `CLAUDE.md`; every chapter must serve it |
| Structure | Chapter list in the spec | `docs/toc.md` frozen only after a kill test that cuts weak chapters |
| Voice | `STYLE-GUIDE.md` (human-authored rules) | `voice/sample.md` — the author's transcript, the *only* style source |
| Drafting workflow | Prose conventions; no workflow | `/article → /draft → /review → /verify → /approve`, staged |
| Consistency | Test suite over structure | Concept + case-study registries, terminology file |
| Fact-checking | A "facts to verify" list | `/verify` skill: WebSearch/WebFetch against primary sources, dated |
| Content governance | Print/format invariants | Hard content rules: no invented stories, dated stale facts, borrowed-example cap |
| Build pipeline | Full: Makefile, Pandoc, PDF, CI | Deferred to Stage 6; lean `setup.sh` |
| Figures | Generated + print-normalised + tested | Marked in drafts, drawn only after 3 chapters |
| Prose linting | Vale + Google package | Vale rules generated *from the voice sample* |
| Packaging / launch | `metadata.yaml`, `AGENT-BRIEF`, `PRODUCTION-NOTES` | Not addressed (pre-draft) |
| Governance/legal | `GOVERNANCE.md` (git, DoD, copyright) | Content rules in `CLAUDE.md`; no formal governance doc |

**What each was missing, plainly:**

- `book-skeleton` (build-first) lacked the *editorial front half*: a rigorous
  reader definition, thesis enforcement, voice extraction, the kill test, the
  registries, and the drafting workflow.
- `clouds-skeleton` (editorial-first) lacked the *production back half*: a build
  that runs, print-spec enforcement, a test suite, packaging, and launch/legal
  governance.

---

## The consolidation

`book-skeleton/` is now the union: the gcp-pca production pipeline **plus** the
clouds editorial workflow, generalised and reconciled. The reconciliations that
required a decision:

1. **Voice: one source of truth.** clouds is right that a voice sample beats a
   rules list. The seed keeps `voice/sample.md` as the authoritative style input
   and demotes `STYLE-GUIDE.md` to the mechanical conventions Vale can enforce,
   with a pointer to the sample for register. Both are present; the sample wins.

2. **Tooling: present but dormant.** clouds defers tooling; gcp-pca ships it all.
   The seed ships the full pipeline but the workflow docs (`TASKS.md`, the
   staged `prompts/`) walk an author through the editorial stages first, so the
   build tooling sits unused until the drafting stage that needs it. You get
   "build only what you need" *behaviourally* without having to build anything.

3. **Fact-checking: skill + log.** The `/verify` skill (clouds) writes into the
   `sources/research/` fact logs (gcp-pca). One mechanism, both halves.

4. **Content rules live in `CLAUDE.md`.** clouds's hard content rules (no
   invented stories, dated stale facts, borrowed-example cap, grayscale figures)
   join gcp-pca's print invariants in one operating manual, so an AI collaborator
   reads a single file.

5. **Governance keeps both.** `GOVERNANCE.md` (git, definition of done, copyright)
   now also references the registries and the `/approve` gate as part of the
   definition of done.

The result is one seed that covers the whole arc — reader, thesis, voice,
structure, drafting, review, verification, build, and launch — with the quality
bar of a shipped book and the editorial rigour of a well-run pre-draft.

`clouds-skeleton/` stays as the lean variant for authors who want it. Everything
in it also exists, generalised, inside `book-skeleton/`.
