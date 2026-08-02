# Launch Brief

Positioning and go-to-market for a self-published KDP release. Everything here
is drawn from the finished manuscript rather than from intention: the book
described below exists and builds.

## The book

**Title:** Google Cloud Professional Cloud Architect
**Subtitle:** A Decision-Mapping Guide for Experienced Architects
**Author:** Zaki Jariwala
**Extent:** ~31,800 words, ~115 pages at 6x9, 33 figures
**Formats:** Paperback (KDP print) and Kindle. Both build from this repository.
**Status:** Complete manuscript, print-ready interior.

## The pitch

A decision-mapping guide for senior engineers — particularly those crossing
from AWS or Azure — who need to pass the Google Cloud Professional Cloud
Architect exam and do not have 180 hours to spend getting there.

Google's own learning path runs roughly 182 hours across 24 activities. This is
a two-hour read. It is not a coverage substitute and does not pretend to be:
it is positioned explicitly as read-alongside, and it earns that position by
teaching what the labs do not, which is architectural judgment under stated
constraints.

The reader is assumed to be an adult. They already know how to size a database,
reason about blast radius, and explain to a finance director why the cheap
option costs more in year three. What they lack is Google's vocabulary and an
understanding of how this particular exam thinks.

## Why it is different from what is on the shelf

Standard certification guides run 400 to 500 pages of documentation rehash and
console walkthroughs — a worse version of something Google publishes free and
keeps current. This book does none of that. It teaches the meta-game: how to
read a scenario, find the one or two sentences that eliminate half the answers,
and defend the tradeoff.

It also holds positions. It says most organisations running Kubernetes should
not be. It treats team capability as a legitimate architectural constraint. It
names real enterprise anti-patterns — everyone gets Editor, service account
keys in Git — because readers learn faster from failures than from feature
lists.

## The page-count question on KDP

Self-publishing removes the acquisition conversation but introduces a shelf
problem: at ~115 pages this is a fraction of the incumbents' bulk, and browsers
equate thickness with value.

Do not solve it by padding. Solve it in the copy and the cover. The book's
entire proposition is compression — 182 hours to two — and the description
should lead with time-to-value rather than coverage. "Everything you need" is
the competitors' claim and it is not this book's.

Two practical notes. The extent comfortably clears KDP's 79-page threshold for
spine text, so it will not look amateur shelved spine-out. And the price should
reflect compression rather than page count; the appendices support a premium
position against thicker, cheaper books.

## Handling the staleness problem

Cloud books date fast, and buyers know it. Three defences, in order of
strength, all of which belong in the description:

**It does not enumerate the perishable things.** No console screens, no quota
tables, no pricing, no click-paths. Where a figure genuinely moves — Cloud Run's
request timeout, Interconnect bandwidth tiers, Security Command Center tier
contents — the book says so and tells the reader to check current
documentation, rather than printing a number that will be wrong by the second
printing.

**The case studies are original and therefore immune.** See below.

**The fastest-moving chapter is quarantined.** Chapter 8 covers AI
infrastructure and is written at the decision level — retrieval against
fine-tuning, batch against online serving, accelerator capacity as a scheduling
constraint — with no model names or version numbers.

Self-publishing turns this from a liability into an advantage: a revised
edition ships the same week Google changes something, which no trade publisher
can match. Keep the repository ready to rebuild.

## The evergreen case-study strategy

The strongest single differentiator, and worth leading the description with.

Google retires case studies. Mountkirk Games, Helicopter Racing League,
TerramEarth, and Dress4Win were all live, and are all gone. Every competing
guide that drills those four now teaches a syllabus that does not exist, and
any guide teaching today's four will be in the same position after the next
rotation. Amazon reviews of the incumbents already say this.

Part II — a quarter of this book — uses five original case studies instead,
written to exercise the same decisions as the live set: a regulated migration,
two generative-AI modernisations, connected-vehicle telemetry, and a legacy
monolith against a hard deadline. It teaches the method of attacking any case
study, and an appendix applies that method to whatever is live on exam day.

Two consequences: no new edition is needed when Google rotates its scenarios,
and the book carries no copyright exposure from reproducing Google's text.
That second point is not theoretical — reproducing those scenarios is an
infringement KDP acts on, and several competing guides are exposed to it.

## Marketing assets already in the manuscript

The appendices were built to be excerpted, and cost nothing to repurpose:

- **Appendix A, decision cheat sheets.** Five one-page tables — compute,
  storage and data, networking, security, reliability and cost — each
  condensing a chapter to the sentence the exam gives you and the answer it
  selects. Natural lead magnets and LinkedIn carousels.
- **Appendix B, exam traps.** Requirement, the answer that looks right, the one
  that is. Grouped by domain, 59 of them. Individually postable; collectively a
  reason to buy.
- **The database selection matrix (ch06) and security control mapping (ch09).**
  The two highest-yield pages and the most screenshot-able.
- **The architecture drills.** One per chapter in Part I. Each is a
  self-contained scenario with questions — usable as a newsletter series, or as
  a sample that demonstrates the method rather than describing it.

A free PDF of Appendix A in exchange for an email address is the obvious list
builder, and it previews the book's actual value rather than its front matter.

The voice excerpts well too. It is quotable in a way documentation is not.

## Keywords and categories

Target the exam name and its abbreviations, the cross-cloud angle (AWS or Azure
architects moving to Google Cloud), and the compression promise. The
cross-cloud framing is under-served: most guides assume no prior cloud
experience, and this one assumes a great deal.

## Outstanding before publishing

- **Imprint name.** KDP needs a publisher line; `metadata.yaml` still says
  TODO. Either invent an imprint or use "Independently published"
- **Cover.** Not started. The interior is complete
- **ISBN.** KDP assigns a free one for paperback, or supply your own. The EPUB
  identifier is already set
- **Technical review** against the current exam guide. The short list of facts
  flagged for verification is in `TASKS.md`
- **A layout pass** in Word, particularly the high-yield page treatment in
  `PRODUCTION-NOTES.md`
