# Stage 2: freeze the structure

Run after `docs/buyer.md` and the CLAUDE.md thesis are written. The purpose is to
stop a topic-list TOC from becoming a book by forcing every chapter to justify
its existence against what the reader can *do*.

```
Read docs/toc.md, docs/buyer.md, and the thesis in CLAUDE.md.

For each chapter, write the one-line promise: what the reader can do after
finishing it, and which buyer outcome (O1, O2, ...) it maps to.

Then:
- Name every chapter whose promise you could not write without inventing a
  capability. Argue for cutting or merging each.
- Take the chapter you most suspect is filler and test it hardest: does the
  reader actually need it, or does the business/practical story survive without
  it? Redistribute what survives into the chapters that need it.
- Mark, for each chapter, which earlier chapter it depends on. Flag any chapter
  that depends on nothing and feeds nothing — that one is a bound magazine
  article, and the book was complete without it.
- Identify the bottleneck: a run of same-shaped chapters that all depend on one
  earlier chapter and feed nothing until much later is where a reader stops.
  Propose a fix (seed a payoff early, reorder, or cut).
- If the book has a spine thread, list the chapters that should call back to it
  and what each callback carries.

Write the result to docs/toc-review.md. Do not write chapter content.
```

Fold the accepted answers into `docs/toc.md` yourself. Freeze it. Commit.
