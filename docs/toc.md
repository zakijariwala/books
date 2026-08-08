# Table of contents

FROZEN 2026-08-08. Kill test folded in (docs/toc-review.md), with one authored
override on chapter 12. Do not reorder or renumber without the author. 12
chapters, four parts, budgeted at 3,800 to 4,200 words each.

## PART I
1. The Great Pizza Box Purge          (shrunk; carries the thesis, the gap)
2. What Happens When You Upload a Photo (the spine; must read cold as an article)
3. Meet the Landlords                 (absorbs half of old 14, lock-in as a landlord property)

## PART II
4. Compute, Renting Brains            (absorbs the shipping-cadence story and GPU cost shape)
5. Storage, The Infinite Warehouse
6. Networking, Roads and Bouncers
7. Databases, The Librarians

## PART III
8. Scaling, Surviving Black Friday    (absorbs serverless as elasticity)
9. Reliability, The Day the Internet Broke
10. Security, The Perimeter is Dead   (misconception carries it: blast radius, not a wall)

## PART IV
11. Cloud Economics, Why Your CFO is Crying  (absorbs serverless billing, the AI bill line, and the exit cost from old 14)
12. The AI Infrastructure Wars        (the closer; the gap at planetary scale)

---

## What changed from the seeded 14

- **Cut: old 10, Containers and Serverless (standalone).** The business story is
  two facts and neither needs the word Docker. Redistributed: shipping cadence to
  ch4, serverless billing to ch11, serverless elasticity to ch8.
- **Merged: old 14, Vendor Lock-In.** Half into ch3 (what you buy when you pick a
  landlord), half into ch11 (what the exit costs).
- **Shrunk: ch1.** It earns its place as the origin of the gap, not as datacenter
  nostalgia. Low end of the budget.

## Authored override: chapter 12, The AI Infrastructure Wars

The kill test recommended cutting this chapter (docs/toc-review.md section 2).
The author kept it, with eyes open on the staleness cost, because the industry
turmoil of the AI era does not survive being merged into cost sidebars. The
turmoil is a narrative, not a cost shape, and the reader is meant to feel it.

Terms of the override, so the chapter earns its place:

- **It is the closer, and it depends on the whole book.** The book opens on the
  eighteen-month gap inside one company's server room and closes on the same gap
  at planetary scale in the AI era. This gives it the inbound dependency the kill
  test correctly said a standalone ch13 lacked.
- **It carries turmoil and the strategic argument, not billing mechanics.** GPU
  cost shape still lives in ch4; AI as the fastest-growing line on a bill still
  lives in ch11. This chapter is the scramble for capacity, the capex, the
  capacity-locked regions, the gap the industry could not close fast enough.
- **Every figure carries the year it was true.** The argument leans on the gap,
  which is durable. The numbers only illustrate it. A later reader sees dated
  figures under a claim that still holds, not a chapter that went wrong.

## Open, deferred (do not block drafting)

- **Discussion guide** for the bulk buyer: back matter built from the twelve
  Monday questions. Decide "downloadable too" later.
