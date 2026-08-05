# Stage 6: figures, after three chapters exist

The build pipeline already ships in this seed (`make diagrams`, `make epub docx`,
the tests). What waits until three chapters are approved is *drawing the
figures* — a figure drawn for a chapter that later gets cut is wasted work, so
drafts only mark figures with `<!-- FIGURE: ... -->` and `/approve` collects them
into `docs/figures.md`.

When three chapters are approved:

```
Read docs/figures.md. For each figure marker:

1. Decide architecture (Python `diagrams`) or flowchart (Mermaid), matching the
   conventions in diagrams/architecture/fig01_1_example.py and
   diagrams/flowcharts/fig01_2_example.mmd.
2. Write one source file per figure, named figNN_M_slug to match its caption.
   Grayscale only, one idea per figure, at most six labels.
3. Run `make diagrams` and fix anything normalize_image.py flags as below the
   8pt print floor by simplifying the figure, not enlarging it.
4. Add the figure reference to the chapter's Markdown and confirm
   `make test` still passes (every reference must resolve to a real source).
```

From here the book builds end to end: `make epub docx && make test-build`.
