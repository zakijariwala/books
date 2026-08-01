# Stage 2: freeze the structure

Run after docs/buyer.md and the CLAUDE.md thesis are written.

```
Read docs/toc.md, docs/buyer.md, and the thesis in CLAUDE.md.

For each of the 14 chapters, write the one-line promise: what the reader can do
at work after finishing it.

Then:
- Name every chapter whose promise you could not write without inventing one.
  Argue for cutting or merging each.
- Chapter 10 goes first. Test whether a product manager needs containers,
  Docker, or orchestration to understand why software ships faster now, or
  whether the business story survives without them.
- Mark, for each chapter, which earlier chapter it depends on. Flag any chapter
  that depends on nothing, since that one restarts the book.
- Chapter 2 introduces the photo upload thread. List the later chapters that
  should call back to it and what each callback carries.

Write the result to docs/toc-review.md. Do not write chapter content.
```

Fold the answers into docs/toc.md yourself. Freeze it. Commit.
