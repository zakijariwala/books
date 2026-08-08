# Concept registry

Where each concept is introduced and where it is revisited. Prefilled from the
frozen TOC (docs/toc.md) and the dependency map and callback thread in
docs/toc-review.md. /approve updates this file as chapters are approved.

Rule: a concept is *introduced* once, in plain language, at the chapter in the
Introduced column. Every later use is a *revisit* that assumes the introduction
and does not re-explain it. If a draft re-explains a concept already introduced,
/review flags it.

| Concept | Introduced | Revisited | Notes |
|---------|-----------|-----------|-------|
| The gap (demand moves in weeks, capacity in eighteen months) | 1 | 3, 4, 8, 11, 12 | The thesis. Ch12 is the gap at planetary scale. |
| Rent vs own (opex vs capex, the freedom to leave) | 1 | 3, 11 | Introduced as the pizza-box purge. |
| The request path (one user action across every box) | 2 | 4, 5, 6, 7, 9, 11 | The spine. Ch2 must read cold. |
| The photo thread (one upload, followed end to end) | 2 | 3, 4, 5, 6, 7, 8, 9, 10, 11 | Callback carrier. See toc-review.md section 5. |
| Region / data residency (where the data physically sits) | 3 | 6, 10, 11, 12 | Answers buyer.md outcome O4. |
| Landlord model (who owns the building, shared responsibility) | 3 | 10, 11 | Absorbs lock-in as a landlord property. |
| Compute / instance (renting the machine that does the work) | 4 | 8, 11, 12 | The box in the diagram that does the work. |
| Shipping cadence (self-contained unit, ships several times a week) | 4 | 8 | Absorbed from old ch10. No Docker vocabulary. |
| GPU cost shape | 4 | 11, 12 | Cost shape here; turmoil in ch12. Year-stamp figures. |
| Storage (the file that is written once, read rarely) | 5 | 7, 9, 11 | Storing is cheap, moving is not. |
| Egress (moving data out costs real money) | 5 | 6, 11 | Kills "we'll just export it" as free. |
| Latency / distance (why Singapore waits longer than London) | 6 | 8, 10 | Answers O1 and O4 together. |
| Read replica / replication lag | 7 | 9 | The highest-value callback for Meera. The read-replica sentence, answered with her own photo. |
| Autoscaling / elasticity (capacity that appears and disappears) | 8 | 11 | Absorbs serverless as elasticity. |
| Failure modes (what scale does when it stops) | 9 | 10, 11 | The half-succeeded upload: file arrived, row did not. |
| SLA (what the guarantee does not cover) | 9 | 11 | Read before the next apology email. |
| Blast radius (security as containment, not a wall) | 10 | 11 | The misconception carries the chapter. |
| Serverless as a billing model (pay per request) | 11 | — | Absorbed from old ch10. Billing frame, not technology. |
| Cost shape (which line dominates, surprises, grows with what) | 11 | 12 | The synthesis chapter. Every layer priced as shape. |
| Exit cost / lock-in (what leaving a vendor costs) | 11 | — | Merged from old ch14. |
| The AI capacity scramble (the gap at planetary scale) | 12 | — | The closer. Turmoil, not billing. |
