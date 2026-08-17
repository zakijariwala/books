# KDP Listing Copy

Everything the KDP upload form asks for as prose. Drawn from `AGENT-BRIEF.md`,
and it leads where that brief says to lead: on compression and on the original
case studies, not on coverage. "Everything you need" is the incumbents' claim
and this book cannot make it honestly.

British spelling throughout, matching the manuscript's `lang: en-GB`. Amazon
does not normalise it and a description written in a different register from the
sample pages reads as outsourced.

---

## Product description

KDP accepts a 4,000-character limit and a small set of HTML tags. The plain
version below is the source of truth; the HTML version follows and must be kept
in step with it.

### Plain text

Google's own learning path for the Professional Cloud Architect exam runs about
182 hours across 24 activities. This book is a two-hour read.

Read it alongside that path. It teaches what the labs leave out: how to choose
under stated constraints, and how to defend the choice you made.

**For architects who already have a cloud**

Five years on AWS or Azure and you know how to size a database and reason about
blast radius. What you lack is Google's vocabulary and a feel for how this
exam thinks. Most guides assume you have never seen a cloud. This one assumes
you have seen plenty, and spends its pages on the deltas: why the VPC is
global, why the project draws the blast-radius boundary, why service account
impersonation replaces the key file you would have reached for anywhere else.

**Five original case studies, and why that matters**

Google retires case studies. Mountkirk Games, Helicopter Racing League,
TerramEarth and Dress4Win were all live, and all four are gone. Any guide built
on them drills a syllabus that no longer exists, and any guide built on today's
four will read the same way after the next rotation.

Part II uses five original scenarios: a regulated migration, two generative-AI
modernisations, connected-vehicle telemetry, and a legacy monolith against a
lease that expires on a fixed date. They exercise the decisions the live set
exercises. They also teach the method for attacking whichever scenarios you
face, and an appendix applies that method to whatever is live on exam day.

**It leaves out what will be wrong next year**

No console screenshots. No quota tables. No pricing. Where a figure moves, such
as Cloud Run's request timeout or Security Command Center's tier contents, the
book says so and sends you to current documentation instead of printing a
number that will be stale. The AI chapter works at the level of retrieval
against fine-tuning, and batch against online serving, with no model names in
it.

**It holds positions**

Most organisations running Kubernetes should not be. Team capability is an
architectural constraint rather than an excuse. The book names the
anti-patterns you have already met: everyone holding Editor, service account
keys committed to Git.

**Inside**

- 17 chapters and 33 figures, every architecture figure showing on-premises
  beside Google Cloud
- An architecture drill per chapter in Part I, with worked discussion
- Appendix A: five one-page decision cheat sheets, one per domain
- Appendix B: 59 exam traps, each giving the requirement, the answer that looks
  right, and the one that scores
- Mapping tables from AWS and Azure services to their Google Cloud equivalents

**Skip it if** you want a 500-page reference, you have never worked in a cloud,
or you came for practice questions in bulk. This book teaches judgement and
expects you to bring experience to it.

### HTML version

```html
<p>Google's own learning path for the Professional Cloud Architect exam runs about 182 hours across 24 activities. This book is a two-hour read.</p>
<p>Read it alongside that path. It teaches what the labs leave out: how to choose under stated constraints, and how to defend the choice you made.</p>
<h4>For architects who already have a cloud</h4>
<p>Five years on AWS or Azure and you know how to size a database and reason about blast radius. What you lack is Google's vocabulary and a feel for how this exam thinks. Most guides assume you have never seen a cloud. This one assumes you have seen plenty, and spends its pages on the deltas: why the VPC is global, why the project draws the blast-radius boundary, why service account impersonation replaces the key file you would have reached for anywhere else.</p>
<h4>Five original case studies, and why that matters</h4>
<p>Google retires case studies. Mountkirk Games, Helicopter Racing League, TerramEarth and Dress4Win were all live, and all four are gone. Any guide built on them drills a syllabus that no longer exists, and any guide built on today's four will read the same way after the next rotation.</p>
<p>Part II uses five original scenarios: a regulated migration, two generative-AI modernisations, connected-vehicle telemetry, and a legacy monolith against a lease that expires on a fixed date. They exercise the decisions the live set exercises. They also teach the method for attacking whichever scenarios you face, and an appendix applies that method to whatever is live on exam day.</p>
<h4>It leaves out what will be wrong next year</h4>
<p>No console screenshots. No quota tables. No pricing. Where a figure moves, such as Cloud Run's request timeout or Security Command Center's tier contents, the book says so and sends you to current documentation instead of printing a number that will be stale. The AI chapter works at the level of retrieval against fine-tuning, and batch against online serving, with no model names in it.</p>
<h4>It holds positions</h4>
<p>Most organisations running Kubernetes should not be. Team capability is an architectural constraint rather than an excuse. The book names the anti-patterns you have already met: everyone holding Editor, service account keys committed to Git.</p>
<h4>Inside</h4>
<ul>
<li>17 chapters and 33 figures, every architecture figure showing on-premises beside Google Cloud</li>
<li>An architecture drill per chapter in Part I, with worked discussion</li>
<li>Appendix A: five one-page decision cheat sheets, one per domain</li>
<li>Appendix B: 59 exam traps, each giving the requirement, the answer that looks right, and the one that scores</li>
<li>Mapping tables from AWS and Azure services to their Google Cloud equivalents</li>
</ul>
<p><b>Skip it if</b> you want a 500-page reference, you have never worked in a cloud, or you came for practice questions in bulk. This book teaches judgement and expects you to bring experience to it.</p>
```

---

## Keywords

Seven slots, 50 characters each. These avoid repeating the title and subtitle,
which Amazon already indexes, and they spend three slots on the cross-cloud
framing because `AGENT-BRIEF.md` identifies it as the under-served angle.

| Slot | Keyword string |
| --- | --- |
| 1 | `GCP PCA certification exam` |
| 2 | `AWS architect moving to Google Cloud` |
| 3 | `Azure to Google Cloud migration` |
| 4 | `cloud architect exam case studies` |
| 5 | `Google Cloud certification study guide` |
| 6 | `cloud architecture decision making` |
| 7 | `enterprise cloud migration design` |

Deliberately absent: "Mountkirk", "TerramEarth" and the other retired
scenarios. They draw search traffic from people wanting exactly what this book
argues against, and the reviews would say so.

## Categories

KDP takes three. First two carry the exam intent; the third reaches the
practitioner who is not shopping for a certification.

1. Computers & Technology > Certification > Cloud Computing
2. Computers & Technology > Networking & Cloud Computing > Cloud Computing
3. Computers & Technology > Programming > Software Architecture

## Pricing note

`AGENT-BRIEF.md` argues the price should track compression rather than page
count, and the appendices carry that argument. At ~115 pages the book sits
against 400-to-500-page incumbents, so pricing at their level invites a
per-page comparison the book loses and a value comparison it wins. Decide which
comparison the listing invites before setting the number.

## A9 note

The description's first two lines are what Amazon shows above the fold on
mobile before "Read more". They currently carry the 182-hours-to-two-hours
contrast, which is the single strongest claim in the listing. Keep any future
edit from pushing it below the fold.
