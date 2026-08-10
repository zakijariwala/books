# Story candidates

The ranking instrument for the shred. Every `STORY-TODO` in the draft appears
here once, with what it would have to prove and what the chapter loses if it
stays empty. Fill the Verdict column while reading the finished first draft, not
before. The target is roughly five stories.

## How to rank

The useful question is not "do I have a story for this chapter." It is **what
breaks if this stays empty.** Three outcomes:

- **Load-bearing.** The chapter's argument depends on it. Without the story the
  section is scaffolding holding up nothing, and a reader can feel the hollow.
  These are the candidates.
- **Decorative.** The story would be pleasant and the chapter survives without
  it. Cut the marker. A decorative anecdote costs words and buys atmosphere,
  and the draft already proves the chapter stands.
- **Habit.** The marker exists because the template asked for one. This is the
  most valuable finding in the whole experiment, because it means the rule that
  every chapter carries a first-hand story is wrong for this book.

A story that serves two places at once beats two stories that serve one each.

## The candidates

Status legend: `OPEN` = marker in the draft, unranked. Verdict is the author's.

| # | Chapter | Where the marker sits | What the story must prove | What is lost if empty | Verdict |
|---|---------|----------------------|---------------------------|----------------------|---------|
| 1 | 1 | `manuscript/ch01.md`, Inside a real organization | Capacity you own is a physical place that can run out of air, on a timeline you do not control. | The chapter argues the gap but never shows it hurting anyone. The room stays a description. | OPEN |
| 2 | 2 | `manuscript/ch02.md`, Inside a real organization. Also `articles/02` | The six stops are separate businesses, because a supply chain can half-work and a single system cannot. | The strongest structural claim in the book rests on a hypothetical. Serves two places at once. | OPEN |
| 3 | 3 | `manuscript/ch03.md`, Inside a real organization. Also `articles/03` | That the residency question has teeth, and that answering it late costs more than answering it early. | The chapter is a well-organised explanation of something the reader has no evidence ever hurt anyone. Serves two places. | OPEN |
| 4 | 4 | `manuscript/ch04.md`, Inside a real organization | That bigger-versus-more is a real fork with real money on it, and that the cheap choice compounds until the ceiling arrives. | The chapter explains a distinction with no evidence anyone was ever caught by it. Weaker than 1, 2 and 7: the argument survives on logic alone. | OPEN |
| 5 | 5 | `manuscript/ch05.md`, Inside a real organization | That the cheap-to-keep, costly-to-move asymmetry is real money and real weeks, not a theoretical property. | The chapter asserts an asymmetry the reader has no reason to feel. Strong candidate: the promise is a cost the reader must believe in, and belief is what a story buys. | OPEN |
| 6 | 6 | `manuscript/ch06.md`, Inside a real organization | That the gap between what the dashboard says and what the distant customer experiences is real, expensive, and persists because everyone measuring sits in the wrong place. | The chapter has a correct explanation and no evidence any organisation was caught by it. Middling: the physics argues itself, the organisational blindness does not. | OPEN |
| 7 | 7 | `manuscript/ch07.md`, Inside a real organization | That the seam is real, that it produces confident wrong answers rather than errors, and that a confused customer finds it before any dashboard does. | `docs/toc-review.md` calls this the moment the reader trusts the book. Strongest candidate in the manuscript: the chapter answers the note she wrote down and never looked up, and a story is what makes the answer land as lived rather than taught. | OPEN |
| 8 | 8 | `manuscript/ch08.md`, Inside a real organization | That reaction time is a real number that loses races against real events, and that the decisions this chapter lists cannot be made while a graph is falling. | The chapter is a sensible checklist with no evidence any of it was learned the hard way. Strong: a peak event is inherently a story, and the checklist reads as theory without one. | OPEN |
| 9 | 9 | `manuscript/ch09.md`, Inside a real organization | That the gap between what the contract pays and what the failure costs is real and lands on a person, and that the hardest work during an outage is not technical. | The chapter is a correct reading of a contract nobody has been burned by. **Duplication resolved:** chapter 2 owns the half-succeeded write; chapter 9 carries it only as a callback and its marker is the outage instead. | OPEN |
| 10 | 10 | `manuscript/ch10.md`, Inside a real organization | That the first step is mundane and the spread is the story, and that the reach was decided years earlier by somebody solving an unrelated problem. | The chapter argues for containment with no evidence containment was ever the thing that mattered. Middling to strong, with a caveat: a real security incident may not be tellable without naming an employer. | OPEN |
| 11 | 11 | `manuscript/ch11.md`, Inside a real organization. Also `articles/11` | That the mirror is real, that a specific line traced back to a specific human decision, and that nobody was being careless. | The chapter's central claim is an assertion about invoices the reader has never seen. Strong: serves two places, and the bill is the one artefact the reader cannot picture without help. | OPEN |
| 12 | 12 | `manuscript/ch12.md`, Inside a real organization. Also `articles/12` | That the waitlist was real, that it had a date on it, and that no amount of money or seniority moved it. Include the year. | The closer argues an industry story the reader has only read about, told by somebody with no more standing than the journalists who covered it. Strong: it is the last first-hand beat in the book and serves two places. | OPEN |

## Known duplication

**Resolved during drafting.** Chapter 2 owns the half-succeeded write, because
that chapter needs it as proof that the six stops are separate businesses.
Chapter 9 carries it as a two-sentence callback and its own marker is a different
incident: the outage where the thing that broke belonged to the landlord. Two
markers, two recordings, no overlap.

Candidate 1 also appears in `voice/pilot-ch01.md`, which is a voice test rather
than manuscript and does not need its own recording.

## Two outside reads, and where they landed

The draft was reviewed twice by a reader who had it as a finished document. Both
reads are recorded here because they converge, and because one corrected a
ranking made during drafting.

**Confirmed by the second read, with evidence produced afterwards:**

- **Structural repetition.** All twelve chapters ended with the same five
  identically titled sections. Twelve of twelve share three headings verbatim.
  docs/chapter-template.md has been rewritten from a running order into a
  coverage requirement as a result.
- **Over-teaching.** Chapter 1 restates its central rent-versus-own trade four
  times. CLAUDE.md now says to say it once.
- **Padding toward the budget.** Eight of twelve chapters landed within 26 words
  of the 3,800 floor, which is a fingerprint rather than a coincidence. The
  budget is now a range with the failure mode named.

**Where the outside read beat the drafting judgement:**

- **Chapter 1 was under-ranked here.** It was not on the strong list. The better
  argument: chapter 1 is the physical foundation the whole book rests on, and it
  currently runs on an invented composite room. If that room is not real, every
  later chapter inherits a hollow root. Promoted to the top group.
- **Chapters 2 and 7 may overlap in felt experience.** The mechanisms differ, a
  permanent inconsistency against a transient one, but both land on the reader as
  "someone reported something the system denied." If both are told, the second
  reads as a repeat. Decide rather than discover.

**Ranking after both reads.** The top group is 7, 5, 1, 11, and then either 9 or
12: 9 if the book needs the gap between what a contract pays and what a failure
costs proven, 12 if the closer needs standing. Two independent reads agreed on 5,
7 and 11 without conferring, which is the strongest signal in this table.

## Drafting notes, recorded before the shred

The first draft is complete: twelve chapters, 45,891 words, every chapter in
budget and clean on the hard lint rules. What drafting revealed, before anyone
has read it cold:

- **No marker turned out to be pure habit.** Every chapter produced a marker that
  could state what it would prove. That is a finding in itself, and it means the
  CLAUDE.md rule survives the draft. Whether it survives the reading is the
  question the shred answers.
- **Strength is uneven and the register says so.** Candidates 2, 5, 7, 8, 11 and
  12 were logged as strong; 4 and 6 as the weakest, because their arguments carry
  themselves on logic and a story would confirm rather than prove.
- **Four candidates serve two places each** (2, 3, 11, 12 also appear in the
  pilot articles), which is the tie-breaker the ranking rules already name.
- **One caveat sits on candidate 10.** A real security incident may not be
  tellable without identifying an employer, so it may fail on grounds unrelated
  to its strength.

None of that substitutes for reading the draft cold. It is written down so the
shred can disagree with it.

## What the shred produces

1. A Verdict on every row above.
2. Roughly five rows marked load-bearing.
3. A recording list, ordered by what the draft showed was missing rather than by
   what was easy to remember. `voice/recording-checklist.md` gets rewritten from
   that list, not the other way round.
4. A decision on the CLAUDE.md rule that every chapter carries a first-hand
   story, which the count of habit markers will settle.
