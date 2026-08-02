# Book Spec

Working spec for the Google Cloud Professional Cloud Architect exam-prep book.
Structure, budget, and formatting decisions live here. Not book content.

## Positioning

A decision-mapping guide, not a service encyclopedia.

Every chapter answers: you run X today, what is the GCP target, and what does
the exam expect you to justify. This fits the word budget, differentiates from
the 450-page official guides, and matches what the exam actually tests. The
case studies are migration and modernization scenarios, not trivia.

Excluded on purpose: service feature enumeration, quota tables, console
click-paths, anything the docs do better and that goes stale.

## Reader

Experienced architect, new to GCP. Knows AWS or Azure or on-prem enterprise
architecture.

Assume without explanation: Active Directory, VLANs, SANs, RTO/RPO, three-tier
applications, load balancing concepts, cloud economics.

Spend words on the deltas that trip cross-cloud architects:

- Global VPC versus AWS regional VPC
- IAM bindings attached to resources versus policies attached to principals
- Project as billing and quota boundary
- Live migration
- Organization and folder hierarchy, which has no AWS or Azure equivalent

AWS and Azure comparison discipline: one appendix table for naming. Inline
callouts only where the mental model differs, never where a service is merely
renamed. Otherwise the book degrades into a translation table.

## Relationship to Google's official learning path

Google's Professional Cloud Architect learning path runs 24 activities and
roughly 182 hours. This book is about two and a half hours of reading, plus
appendices to revise from. That is still better than a 70:1 compression ratio,
and it settles the positioning: the book is not a coverage substitute. Position
it as read-alongside, not read-instead.

Do not reweight chapters to mirror the path's hour distribution. The path
optimizes for hands-on practitioner skill. The exam optimizes for architectural
judgment. The divergence is where the book earns its place.

Three areas the exam tests hard and the official path barely covers. These are
the book's clearest opening:

- **Migration.** No migration course exists in the path, yet every official case
  study is a migration or modernization scenario.
- **Business process analysis.** The exam section on analyzing and optimizing
  technical and business processes carries real weight. The path is almost
  entirely technical labs.
- **Cost and FinOps.** No dedicated course, but cost shows up in every case
  study.

Competitive note: the path now includes a course teaching candidates to build
their own study guide with Gemini Notebook. The book must offer what a generated
guide cannot, which is opinionated tradeoffs, curated judgment, and original
worked case studies.

## Word budget

Target 33,000 words. Enforced by `make wordcount` against `WORD_BUDGET` in the
Makefile.

| Component | Words |
| --- | --- |
| Front matter and coverage map | 600 |
| Part I, 12 decision chapters | 19,500 |
| Part I architecture drills | 3,000 |
| Part II, 5 case studies | 6,000 |
| Back matter and appendices | 4,000 |
| Total | 33,100 |

Raised from 28,000 after editorial review. The added words are drills,
decision tables, and revision appendices rather than more exposition: they are
reference material a reader consults, not prose read end to end. Reading time
therefore rises by less than the word count suggests, and the positioning below
survives. Do not spend the increase on more narrative.

Projected extent at 6x9 trim, 11pt serif, ~310 words per page: about 115 pages
including figure space.

Do not cut below roughly 20,000 words. KDP requires 79+ pages for spine text.
A book without spine text looks amateur shelved spine-out.

## Structure

### Part I, decision areas

| File | Topic | Words |
| --- | --- | --- |
| ch01.md | Exam anatomy, how GCP's model differs from AWS and Azure | 1,500 |
| ch02.md | Resource hierarchy and identity | 1,600 |
| ch03.md | Networking: VPC and hybrid connectivity | 1,800 |
| ch04.md | Compute: VMs and serverless | 1,600 |
| ch05.md | Containers: GKE, Autopilot, fleets, service mesh | 1,600 |
| ch06.md | Storage and databases | 1,700 |
| ch07.md | Data pipelines and analytics | 1,500 |
| ch08.md | AI/ML infrastructure | 1,300 |
| ch09.md | Security and compliance | 1,700 |
| ch10.md | Migration patterns and data transfer | 1,700 |
| ch11.md | Reliability, observability, DR | 1,800 |
| ch12.md | Operations, IaC, and cost | 1,700 |

Identity sits at chapter 2, not late. For a cross-cloud architect the
organization, folder, and project hierarchy is the one construct with no AWS or
Azure equivalent, and everything downstream hangs off it. Teach it before
anything references a project.

Data pipelines split from storage. The exam tests BigQuery, Dataflow, and
Pub/Sub heavily and they do not belong under storage.

Containers split from compute. Google's own path gives GKE a dedicated course
plus a skill badge, covering GKE Enterprise, Fleets, Cloud Service Mesh, and
Config Management. It cannot share a chapter with VMs.

AI/ML infrastructure earns a chapter because the official path now carries two
courses on it, including AI Hypercomputer. GPU and TPU selection and AI platform
choice are architecture decisions the exam can reach.

Chapter order does not mirror the official exam guide. Front matter carries a
domain-coverage map so readers can verify coverage.

### Part II, case studies

Five original case studies, 1,200 words each.

| File | Case study | Exercises |
| --- | --- | --- |
| ch13.md | Regulated healthcare leaving a co-location facility | Compliance, residency, CMEK, VPC Service Controls, AD federation |
| ch14.md | Media company adopting generative AI | Prebuilt APIs, retrieval against tuning, fleets, SLO diagnosis |
| ch15.md | Hybrid retailer with a generative catalogue | Human-in-the-loop approval, database consolidation, event-driven ingest, cost |
| ch16.md | Connected vehicle telemetry | Ingest at scale, Pub/Sub, Dataflow, the three-store split, ML pipeline |
| ch17.md | Legacy monolith against a lease expiry | Rehost versus refactor, CDC cutover, Interconnect, programme management |

Case study 5 is the differentiator. It is the purest expression of the book's
core visual device.

Two of these diverged from an earlier plan and the divergence was kept
deliberately. ch14 was drafted as a live-event streaming scenario and became a
generative-AI one, because two of the four current official case studies are
generative-AI scenarios and the book needed to exercise chapter 8 against a
customer that has already migrated. ch15 was a game backend and became a hybrid
retailer, which carries the human-approval governance constraint that the game
scenario had nowhere to put.

### Copyright constraint

Do not reproduce Google's official case studies. EHR Healthcare, Helicopter
Racing League, Mountkirk Games, and TerramEarth are copyrighted text.
Referencing and discussing them is fine. Reprinting the scenarios in a
commercial book is not, and KDP acts on claims. They also go stale when Google
swaps them.

The five case studies above are original, and mirror the shape and domain
spread of the official set. Part II opens by showing readers how to point the
method at whatever case studies are live on exam day.

## Chapter template

Repeatable skeleton. Keeps word count predictable and the book consistent.

| Element | Words |
| --- | --- |
| Opening on-prem scenario | 150 |
| Mapping figure, on-prem beside GCP | figure |
| Three or four decision sections, each stating the tradeoff | 900 |
| Decision flowchart | figure |
| Exam traps: what the test actually asks | 250 |
| Recap, five bullets | 150 |

## Figures

Thirty-three built: two per chapter across Part I and Part II, plus a migration
programme diagram in ch10. The original plan said forty at roughly three per
chapter, which the 6x9 measure did not support — see the print constraint
below.

Figure-dense and prose-lean is deliberate. In a decision-mapping book the
flowchart carries the decision logic and the prose only explains the tradeoff.
That buys back coverage without inflating word count.

The core visual device is an on-prem node and a GCP node in the same figure.
Every architecture figure should carry it where the topic allows.

- Architecture figures: one `.py` per figure in `diagrams/architecture/`
- Flowcharts: one `.mmd` per figure in `diagrams/flowcharts/`
- Captions numbered per chapter, `Figure 3.2`

**The print constraint on figure density.** A 4.5in-wide figure holds about two
columns of short labels before its type drops below 8pt, which is the floor
`scripts/normalize_image.py` enforces. This is a hard limit on how much decision
logic one figure can carry, and it is why the flowcharts use terse labels rather
than sentences. A figure that fails the check should be simplified or split; it
cannot be fixed by enlarging the image, because the page size does not move.

## Formatting

Print constraints are enforced in the render scripts, not by hand. See the
Makefile and `scripts/normalize_image.py`.

- Trim size 6x9 inches, black-and-white interior
- Figures render at 300 DPI, 1350px wide, about 4.5 inches on the page
- Grayscale is the render setting. No color-coded legends anywhere
- Headings: H1 chapter, H2 section, H3 subsection. Stop at H3. Deeper nesting
  reads badly in EPUB reflow and in a book this short
- Tables: three columns maximum. Wider breaks at 6x9 and in EPUB
- Code blocks: hard-wrap `gcloud` lines at about 60 characters. Longer lines
  overflow the text block in monospace at 6x9
- Callouts: blockquote, not fenced div. Survives both EPUB and DOCX cleanly

### Vale configuration

The Google package encodes Google's documentation house style, which conflicts
with book convention in four places. Disabled in `.vale.ini`:

- `Google.Headings` demands sentence-case headings; books use title case
- `Google.WordListCase` flags the word "Chapter"
- `Google.FirstPerson` blocks the preface voice
- `Google.We` blocks addressing the reader directly

Everything else in the package stays active. Add technical terms to
`styles/config/vocabularies/Book/accept.txt` as spelling errors surface.

## Exam guide facts

`VERIFIED` against the official exam guide PDF, version 6.1. Full detail and
sources in `sources/datapoints/exam-guide-verified.md`.

| # | Section | Weight |
| --- | --- | --- |
| 1 | Designing and planning a cloud solution architecture | ~25% |
| 2 | Managing and provisioning a cloud solution infrastructure | ~17.5% |
| 3 | Designing for security and compliance | ~17.5% |
| 4 | Analyzing and optimizing technical and business processes | ~15% |
| 5 | Managing implementation | ~12.5% |
| 6 | Ensuring solution and operations excellence | ~12.5% |

Each exam includes two case studies, shown on a split screen. Case study
questions are 20-30% of the exam, which justifies Part II taking roughly a
quarter of the word budget.

The four current case studies are **Altostrat Media**, **Cymbal Retail**,
**EHR Healthcare**, and **KnightMotives Automotive**.

Mountkirk Games, Helicopter Racing League, TerramEarth, and Dress4Win are all
retired. Any prep material still teaching them is out of date, which is a
useful thing to say plainly in chapter 1.

Two of the four current case studies, Altostrat and Cymbal, are generative-AI
scenarios. That confirms chapter 8 and means the Part II case studies should
weight toward AI-era problems rather than classic lift-and-shift.

## Still to verify

- Question count, duration, cost, recertification period
- KnightMotives Automotive: unread, may overlap the fleet-telemetry case study
  planned for Part II
