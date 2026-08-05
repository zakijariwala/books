# Stage 6: deferred until three chapters exist

Do not run this now. It has no input until three chapters are approved and
`docs/figures.md` lists their figures. Building the pipeline earlier means
drawing figures for chapters that may still be cut.

If you would rather start with the build pipeline already in place, use the
consolidated seed (`../book-skeleton/`) instead — it ships the whole Makefile,
figure pipeline, and tests from day one, dormant until you need them.

```
Now that manuscript/ holds three approved chapters and docs/figures.md lists
their figures:

1. Draw the listed figures with Mermaid or the Python diagrams library.
   Grayscale, one idea per figure, at most six labels, readable in isolation.
2. Add a `make diagrams` target that renders to 300 DPI grayscale PNG at roughly
   1350px width for a 6x9 trim.
3. Add a `make build` target that assembles the manuscript with Pandoc.
4. Write scripts/wordcount.py: parse manuscript/, report words per chapter
   against budget, total against the CLAUDE.md target, and count remaining
   STORY-TODO and FIGURE markers. Add a `make status` target.
```

At this point the project has grown into what the consolidated seed provides out
of the box. You can either keep building here or lift the scripts, Makefile, and
tests from `../book-skeleton/`.
