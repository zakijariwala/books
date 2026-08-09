# Figures

Twelve figures, one per chapter, collected from the `<!-- FIGURE: -->` markers in
the manuscript. **Not drawn yet, on purpose.** TASKS.md holds drawing until Stage
6, after three approved chapters, and figures drawn on the experiment branch
would be discarded when the consolidated version is built.

This file is the specification. It survives the shred; the drawings do not exist
yet.

## Production rules

From CLAUDE.md and TASKS.md:

- **Grayscale only.** No colour-dependent meaning. Assume the reader is holding a
  black and white paperback.
- **One idea per figure.** If it needs two sentences to explain, it is two
  figures or it is not a figure.
- **At most six labels.** Counted, not estimated.
- 300 DPI grayscale PNG, roughly 1350px wide for a 6x9 trim.
- Weight, shading and position carry the meaning, since colour cannot.

## The shared visual vocabulary

Drawing these as twelve unrelated pictures would waste their best property. Three
groups repeat, and the repetition is the argument.

**The six stops** appear in three figures and must look identical in all three,
same order, same icons, same left-to-right reading:

- **Fig 2** introduces them as the request path.
- **Fig 10** turns them into a ship's compartments to show blast radius.
- **Fig 11** turns them into cost bars to show which two never stop.

A reader who recognises the shape in figure 10 as the thing they met in figure 2
gets the chapter's argument before reading a word of it. That only works if they
are drawn as the same object three times.

**The gap** appears twice and is a deliberate visual rhyme:

- **Fig 1** is demand against capacity for one company, over eighteen months.
- **Fig 12** is the same drawing at planetary scale, 2022 to 2026, with the axes
  relabelled to industry demand against chip and power supply.

Figure 12 should be recognisable as figure 1 redrawn. Same line weights, same
shading, same composition. The closer's whole argument is that the reader has
seen this picture before.

**The photograph** is a single recurring icon, appearing in figures 3 and 11 and
implied in 2. One icon, used consistently.

## The twelve

| # | Ch | Shows | Labels |
|---|----|-------|--------|
| 1 | 1 | Demand rising smoothly against capacity as a step function jumping every eighteen months. Gap between them shaded. | ≤6 |
| 2 | 2 | The request path as six stops left to right: phone, front door, warehouse (the file), day labourer (the thumbnail), ledger (the record), back to the friend's phone. | 6 |
| 3 | 3 | Three nested boxes: country (courthouse icon), region (a city), availability zone (a building). Photo icon in the innermost. Outer box labelled "whose law reaches it". | ≤6 |
| 4 | 4 | Two panels. Left, "bigger": one van becoming a lorry, ceiling line above labelled "largest size sold". Right, "more": one van becoming five, front door distributing work, no ceiling. | ≤6 |
| 5 | 5 | A warehouse with three arrows: thick "in, free or close to it", small circular "keep, a little every month, forever", thick "out, metered" drawn heaviest. | ≤6 |
| 6 | 6 | Two lanes. "Near": short road, twenty return arrows, "under a second". "Far": identical twenty arrows over a road many times longer, "four seconds". Arrow count identical. | ≤6 |
| 7 | 7 | One desk left, "changes go here, decides what is true", single arrow in. Two desks right, "questions go here", many arrows in. Thin arrows between, "news, a moment late". | ≤6 |
| 8 | 8 | Traffic rising vertically at minute zero. Capacity flat until minute one, then rising in steps, meeting traffic at minute six. Area between shaded, "the outage". | ≤6 |
| 9 | 9 | A bar representing one month: small shaded segment "permitted, about forty minutes", rest "promised". Thinner bar beneath, "what the credit refunds", a sliver of the shaded segment. | ≤6 |
| 10 | 10 | Ship's hull, six compartments matching fig 2. Top panel: bulkheads hold, one compartment shaded. Bottom panel: bulkheads open, shading across all six. | ≤6 |
| 11 | 11 | One photograph icon above six horizontal bars, one per stop, no numbers. Two shaded: warehouse "every month, forever", road out "every view". | ≤6 |
| 12 | 12 | Figure 1 redrawn at planetary scale. Same two lines, same shaded gap, axes relabelled to industry demand against chip and power supply, 2022 to 2026. | ≤6 |

## Notes on the hard ones

**Figure 9** is the only one carrying a quantity, and CLAUDE.md bans prices but
not durations. Keep it to minutes and proportions, never money. The refund bar
must be visibly a sliver; that proportion is the entire point of the figure.

**Figure 6** fails if the two lanes have different numbers of arrows. The
argument is that the round-trip count is identical and only the distance changed.
Count them when drawing.

**Figure 12** is not a new drawing. It is figure 1 with new labels, and any
divergence in style weakens the closer.

**Figures 4 and 5** use vans and warehouses, which are on the approved analogy
list. Do not substitute anything from outside airports, warehouses, hotels,
utilities, transportation, or supply chains.

## Tooling, when the time comes

TASKS.md specifies Graphviz, the Python diagrams library, and mermaid-cli, all
currently commented out in `setup.sh` with a note. None is installed. Uncomment
that block and re-run setup before drawing.

Most of these are not graph-shaped and would fight Graphviz. Figures 1, 8 and 12
are plots; 2, 3, 5, 7, 10 and 11 are diagrams that want hand placement. Consider
hand-authored SVG converted to grayscale PNG rather than generated layouts, and
decide once rather than per figure.
