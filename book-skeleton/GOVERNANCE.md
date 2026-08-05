# Governance

How work moves through this repository: version control, definition of done,
fact-checking, and the legal discipline that keeps a self-published book safe to
sell. These are the process rules; `CLAUDE.md` is the day-to-day operating
manual and `STYLE-GUIDE.md` is the prose style.

## Version control

- **Never commit to the default branch directly.** Branch per unit of work.
- **Branch naming:** `chNN-topic` for chapter work, `fig-topic` for figures,
  `fix-topic` for corrections, `chore-topic` for toolchain. Adjust to taste but
  keep it predictable.
- **Commit messages:** imperative subject under ~70 chars, prefixed by type —
  `feat:` new content, `fix:` corrections, `docs:` process/spec, `chore:`
  toolchain, `test:` tests. A body when the *why* is not obvious. One logical
  change per commit; a chapter draft and a toolchain fix are two commits.
- **Pre-commit gate:** run `make hooks` once per clone. It runs Vale (errors
  block) and the fast test suite before every commit. Override in a genuine
  emergency with `git commit --no-verify`, and fix it immediately after.
- **What is committed:** manuscript, figure *sources*, scripts, config, docs.
  **Not committed:** `assets/` (rendered figures), `build/` (outputs), `venv/`,
  Vale style packages. All gitignored; all reproducible.

## Definition of done

A chapter is done when all of these hold:

- [ ] Content complete — no placeholders, no `STORY-TODO`, no unrendered `FIGURE`
      markers.
- [ ] `/review` verdict is ship (or its named fixes are applied).
- [ ] `/verify` run; every stale-able fact verified and logged in
      `sources/research/`.
- [ ] `/approve` run — concepts and examples recorded in the registries.
- [ ] Every figure it references has a rendered source (`make diagrams` clean).
- [ ] `make lint` passes at error level.
- [ ] `make test` passes (structural invariants hold).
- [ ] Within its word budget (`make wordcount`).
- [ ] Reads cleanly once, out loud or in a built EPUB — a human pass a linter
      cannot replace.

The book is ready to publish when every chapter is done, `make test-build`
passes against the built outputs, and the pre-publication checklist in
`BOOK-SPEC.md` and `AGENT-BRIEF.md` is clear.

## Fact-checking

The failure mode of machine-assisted writing is confident, wrong facts. Guard
against it:

1. Anything that could be wrong or go stale — prices, dates, versions,
   statistics, named entities, quotations — is checked against a **primary
   source**, not from memory and not from another secondary book.
2. Log each verified fact in `sources/research/` with its source and the date
   checked. A fact with no logged source is treated as unverified.
3. If a fact cannot be verified, either write around it or mark it explicitly
   for verification (and list it in `BOOK-SPEC.md` "Facts to verify"). Never
   print a confident guess.
4. Fast-moving topics are quarantined: write them at the level that changes
   least (decisions and tradeoffs, not version numbers), and flag them as the
   first candidates for review on any revision.

## Copyright and permissions

Self-publishing removes the publisher's legal backstop, so this is on you.

- **Write original prose.** Do not reproduce third-party text, tables, or
  figures. Reference and discuss freely; reprint nothing.
- **Research clones** (books, repos, docs you consult) stay out of the
  repository — `.gitignore` excludes `reference-clones/`. Read them, log what
  you took *as fact* (facts are not copyrightable; expression is), write your
  own words.
- **Quotations** must be genuinely brief, attributed, and defensible as fair
  use / fair dealing. If in doubt, paraphrase and cite.
- **Images and fonts** must be ones you created, licensed, or that are clearly
  free for commercial use. Record the licence in `sources/research/`.
- **Log permissions** for anything requiring them before it goes in the book.
- **Trademarks:** use them accurately and do not imply endorsement.

## Reviews and change history

- Record notable decisions and their reasoning where they live (spec decisions
  in `BOOK-SPEC.md`, layout in `PRODUCTION-NOTES.md`). Future-you will ask why.
- Keep `CHANGELOG.md` current for anything a reader of a later edition would
  care about — corrections, added material, updated facts.
