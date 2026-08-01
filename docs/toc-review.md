# TOC review: the kill test

Run against docs/toc.md (seeded, 14 chapters), docs/buyer.md, and CLAUDE.md.
The thesis paragraph is still a placeholder, so promises were written against
Meera's six outcomes instead. Where a promise below does not map to one of those
six, the chapter is in trouble and the section says so.

Meera's six outcomes, used as the scoring rubric throughout:

- **O1** Read an architecture diagram and name what each box costs.
- **O2** Ask three questions in the architecture review that change the decision.
- **O3** Tell which parts of an estimate are hard and which are habit.
- **O4** Answer the data residency question herself.
- **O5** Read the cloud bill and find the line that grew.
- **O6** Know what breaks in production, and why the vendor slide never mentions it.

---

## 1. The one-line promises

| # | Chapter | Promise: what she can do at work after | Outcome |
|---|---------|----------------------------------------|---------|
| 1 | The Great Pizza Box Purge | Answer the "why don't we just self-host, it's cheaper" question in a roadmap meeting by naming what the company would be buying back: capital approval cycles, lead time, and a maintenance contract. | O3 |
| 2 | What Happens When You Upload a Photo | Trace one user action across every box in the architecture diagram, in order, and say which box she is actually asking about. | O1, O2 |
| 3 | Meet the Landlords | Answer the customer's data residency question on the call, without looking at the solutions engineer. | O4 |
| 4 | Compute, Renting Brains | Hear "we need bigger instances" and know whether that is a two-hour change or a two-week one, and which way the bill moves. | O1, O3, O5 |
| 5 | Storage, The Infinite Warehouse | Know why storing the data costs almost nothing and moving it costs real money, so she stops treating "we'll just export it" as free. | O5 |
| 6 | Networking, Roads and Bouncers | Explain why the Singapore customer sees a slower product than the London one, and what fixing that costs. | O1, O4 |
| 7 | Databases, The Librarians | Ask, in the second-Tuesday architecture review, what the replication lag is and who sees stale data. That is the read replica meeting, answered. | O2, O6 |
| 8 | Scaling, Surviving Black Friday | Tell the VP what the system does at ten times traffic, and what has to be decided in advance rather than on the day. | O3, O6 |
| 9 | Reliability, The Day the Internet Broke | Read an SLA and know what it does not cover, before she writes the next customer apology email. | O6 |
| 10 | Containers and Serverless, The Shipping Revolution | **Could not be written without inventing one.** See section 3. | none |
| 11 | Security, The Perimeter is Dead | Ask who can reach the data if one service is compromised, instead of asking whether the system is secure. | O2, O6 |
| 12 | Cloud Economics, Why Your CFO is Crying | Open the bill, find the line that grew, and name the product decision that grew it. | O5, O1 |
| 13 | The AI Infrastructure Wars | **Could not be written without inventing one.** See section 2. | none |
| 14 | The Vendor Lock-In Trap | Say what leaving this vendor would cost in time and rewritten code, when someone floats it in a planning meeting. | O3, O4 |

Nine of fourteen chapters carry a promise that a person could act on within a
week. That is a healthy ratio for a seeded TOC.

---

## 2. Chapters whose promise required inventing

### 13. The AI Infrastructure Wars — cut

I could not write a Monday action for this chapter without fabricating one.
Every candidate promise turned out to be "she can follow the news better,"
which is not a capability. Three further problems:

- **It ages fastest and the book cannot hedge it.** CLAUDE.md requires every
  stale-able figure to carry the year it was true. This chapter is nothing but
  stale-able figures. A reader in 2028 finds one chapter that is visibly wrong
  and distrusts the other ten.
- **It has no dependency in either direction.** Nothing before it is required to
  read it, and nothing after it needs it. See section 4.
- **It is the chapter a chatbot writes best.** Vendor capex announcements and
  GPU supply commentary are exactly the material sitting in every model's
  training data. buyer.md says her reason for buying is the material a chatbot
  cannot generate.

What survives: GPU compute as a cost shape belongs in chapter 4, and AI
workloads as the fastest-growing line on a bill belongs in chapter 12. Both
places let the material carry a date without owning a chapter.

### 14. The Vendor Lock-In Trap — merge, do not cut

The promise is real and maps to O3 and O4. The chapter is not. Its first half is
the same material as chapter 3 (what you are buying when you pick a landlord)
and its second half is the same material as chapter 12 (what the exit costs).
Splitting it across those two gives both chapters a stronger ending than either
has now, and removes a Part IV that limps to a close.

Counter-argument, stated fairly: lock-in is the one topic where a business
reader most wants a standalone answer she can quote, and burying it inside two
chapters makes it unfindable. If the book keeps it, it should move to Part I as
chapter 4, immediately after Meet the Landlords, where it reads as a
consequence rather than an afterthought. It should not stay at the end.

### 1. The Great Pizza Box Purge — keep, shrink, re-aim

The promise held on the third attempt, and the first two were history for its
own sake. This chapter earns its place only as the origin of the gap between how
fast demand moves and how slowly concrete moves. It does not earn 4,000 words of
datacenter nostalgia. Budget it at the low end and make it carry the thesis.

### 11. Security, The Perimeter is Dead — keep, with a guard

The promise is fine. The risk is that this is the chapter most likely to drift
into a certification-shaped list of services, which CLAUDE.md bans outright. The
chapter template's misconception section should carry the weight here: the
misconception is that security is a wall, and the chapter is about blast radius.
Write the outline against that or the chapter will grow a service catalogue.

---

## 3. Chapter 10 goes first

**Question:** does a product manager need containers, Docker, or orchestration
to understand why software ships faster now, or does the business story survive
without them?

**It survives, and it survives better.**

The business story is two facts. Software used to ship in quarterly batches
because the thing being shipped was tangled up with the machine it ran on.
Software now ships several times a week because the unit of shipping became
self-contained and identical everywhere it lands. Meera needs both facts. She
needs them because they explain why her engineering team's release cadence is
what it is, and that touches O3 directly.

Neither fact requires the word Docker. Neither requires orchestration. A reader
who learns what a container image is has learned a noun she will never use.
buyer.md is explicit: she will never open a terminal, and a chapter that teaches
her to configure something loses her silently at chapter 4. This is that
chapter, sitting at position 10, exactly where the drop-off would land.

**Verdict: cut chapter 10 as a standalone.** Redistribute:

- The shipping-cadence story, roughly 800 words, into chapter 4. Compute is
  where the unit-of-shipping question belongs, since the whole point is what the
  code runs on.
- Serverless as a cost shape, roughly 600 words, into chapter 12. Pay-per-request
  is a billing model before it is a technology, and that is the frame she needs.
- Serverless as an elasticity story, one section, into chapter 8. It is the
  cleanest example of capacity that appears and disappears.

**What this costs:** the AE and the founder from buyer.md's secondary list both
sit in rooms where "are you containerized" gets asked. Neither can answer after
this cut. That is an acceptable loss. A book that serves the secondary buyer at
the primary buyer's expense serves nobody, and the founder is better off with
one honest paragraph in chapter 4 than a chapter that pretends she needs
Kubernetes.

---

## 4. Dependency map

| Chapter | Depends on | Note |
|---------|-----------|------|
| 1 | nothing | Correct. It is the opener and it establishes the gap the book is about. |
| 2 | 1, loosely | Near-independent by design. It is the spine, and it must read cold. |
| 3 | 1 | Needs the capital-approval problem before landlords make sense. |
| 4 | 2 | The box in the diagram that does the work. |
| 5 | 2 | The box that holds the file. |
| 6 | 2, 3 | Needs the request path and needs regions. |
| 7 | 2, 5 | Needs the file and the record to be separate ideas already. |
| 8 | 4, 6 | Cannot discuss scale without the units that scale. |
| 9 | 8 | Failure is what scale does when it stops. |
| 10 | 4 | Cut. Its only real dependency confirms it belongs inside 4. |
| 11 | 3, 6 | Needs shared responsibility and needs network boundaries. |
| 12 | 4, 5, 6 | The bill is a list of the previous three chapters. |
| 13 | **nothing** | Flagged. See below. |
| 14 | 3, 12 | Merge target, per section 2. |

**Chapters that depend on nothing, and therefore restart the book:**

Chapter 1 does, and that is what an opening chapter is for. Chapter 13 does, and
that is the strongest structural argument for cutting it. A chapter with no
inbound dependency and no outbound dependency is a magazine article that got
bound into a book. A reader who skips it loses nothing, which means the book was
already complete without it.

Chapter 2's near-independence is a different thing and it is a feature. It has
to work as a standalone article for the Stage 4 pilot, and the callback thread
in section 5 means every later chapter depends on **it**. High out-degree, low
in-degree. That is what a spine looks like.

**Structural finding: Part II is a bottleneck.** Chapters 4, 5, 6, and 7 all
depend on 2 and almost nothing depends on them until Part III. Four chapters in
a row with the same shape is where a business reader puts the book down. Chapter
12's material is the strongest antidote, and the current TOC saves it for the
end. Consider seeding one page of the bill in chapter 4 and referring forward,
so Part II has a destination visible from inside it.

---

## 5. The photo upload thread

Chapter 2 introduces one user action and follows it end to end. Every callback
below reuses the same photo, the same user, and the same moment. The callbacks
are what turn eleven chapters into one book, and they are cheap: two or three
sentences each, at the top of the chapter's core explanation section.

| Chapter | The callback carries |
|---------|---------------------|
| 3 | Which country the photo landed in, and who signed the contract that put it there. This is the data residency answer in physical form. |
| 4 | The machine that made the thumbnail, and the fact that it existed for nine seconds. |
| 5 | The original and the thumbnail are two different storage decisions with two different costs. The original will never be read again. |
| 6 | How the photo travelled, and why the friend in Singapore waited longer to see it than the friend in the same city. |
| 7 | The row that says the photo exists, written to one database and read from another. Her friend refreshed and saw nothing. That is replication lag, and it is the read replica sentence from her second-Tuesday meeting, answered with her own photo. |
| 8 | The same upload, times four hundred thousand, in the ninety seconds after a match ends. |
| 9 | The upload that half-succeeded. The file arrived, the row did not. Now there is a photo nobody can find and it is still being paid for. |
| 11 | The photo has a URL. Who else can open it, and what stops them. |
| 12 | Every layer above, priced as one line each, for one photo. Then multiplied by the month. This is where the bill stops being abstract. |

Chapter 7's callback is the highest-value sentence in the book for this reader.
buyer.md opens on her writing down "read replica" and never looking it up.
Answering it with her own photo, six chapters later, is the moment she trusts
the book.

---

## 6. Recommended TOC after the kill test

Eleven chapters. Lands inside the CLAUDE.md expectation of 11 or 12, and inside
56,000 words at 3,800 to 4,200 each with room for front and back matter.

```
PART I
1. The Great Pizza Box Purge          (shrink, carries the thesis)
2. What Happens When You Upload a Photo
3. Meet the Landlords                 (absorbs half of old 14)

PART II
4. Compute, Renting Brains            (absorbs the shipping-cadence story)
5. Storage, The Infinite Warehouse
6. Networking, Roads and Bouncers
7. Databases, The Librarians

PART III
8. Scaling, Surviving Black Friday    (absorbs serverless elasticity)
9. Reliability, The Day the Internet Broke
10. Security, The Perimeter is Dead

PART IV
11. Cloud Economics, Why Your CFO is Crying  (absorbs serverless billing,
                                              AI cost growth, and the exit cost
                                              from old 14)
```

Cut: old 10 and old 13. Merged: old 14.

Open question for the author, not resolvable from these three files: Part IV is
now one chapter, which is not a part. Either promote economics into Part III and
run three parts, or move the merged lock-in material back out as a short
chapter 12 so Part IV has two. The second option contradicts section 2's
recommendation, and reasonable people would take either.

---

## 7. Two things the TOC does not hold

**The discussion guide.** buyer.md names a bulk buyer, the VP of Sales or Head
of Enablement buying forty copies for an AE team, and calls that buyer worth
four months of individual sales. That buyer needs a discussion guide and
per-chapter questions a manager can run on a Friday. The chapter template
already ends every chapter on one question the reader should ask at work on
Monday. Those eleven questions are the raw material. Someone has to decide
whether the guide is back matter, a downloadable, or both, and the decision
should be made before drafting so the Monday questions get written to carry it.

**The cost rule.** Outcome O1 asks her to name what each box costs, and CLAUDE.md
bans vendor prices outright. Both are correct and they collide in at least six
of the eleven chapters. The resolution has to be written down once, in CLAUDE.md,
before chapter 4: the book teaches cost **shape** rather than cost. Which line
dominates, which one surprises, which one grows with users and which grows with
data, and what the ratios between them are. No dollars, no rate cards. If that
sentence does not exist before drafting, eleven chapters will each invent their
own compromise.
