# About this book

You already know how to architect systems. You have sized databases, argued
about blast radius, and explained to a finance director why the cheap option
costs more in year three. What you lack is Google Cloud, and an exam in a few
weeks.

This book maps what you know onto what Google calls it, then teaches the
judgment the exam actually tests.

## What this book is not

It does not enumerate services. Google's documentation covers every quota,
every flag, and every console screen, and it stays current in a way print
cannot. Chasing that coverage in 120 pages would produce a worse version of
something free.

It also does not replace hands-on work. Google's official learning path runs
around 180 hours of courses and labs. This book takes two hours to read. Read
it alongside the labs, not instead of them.

## What it does

Every chapter starts from a system that already exists. You run Active
Directory, a SQL Server cluster, and a Kubernetes estate someone stood up in
2021. The chapter names the Google Cloud target for each piece, then spends
its remaining pages on the part that earns your salary: which tradeoff you
accepted, and how you defend it.

That framing matches the exam. All four case studies describe companies with
existing systems and awkward constraints. None of them asks you to design
something from nothing.

## How to read this book

Two hours, straight through, is the intended first pass. It is short on purpose:
the point is to hold the whole decision space in your head at once, which you
cannot do across a 450-page reference. Read it early in your preparation rather
than the night before, because its job is to give the labs somewhere to land.

Then use it three more times, differently each time.

**Work the drills properly.** Every chapter in Part I ends with an architecture
drill: a scenario, four questions, then a discussion. The discussion is
deliberately placed after the questions, and you should treat that gap as real.
Stop reading. Write your four answers down — on paper, in a file, anywhere you
cannot quietly revise them once you see the argument. Then read the discussion
and compare.

The value is entirely in the gap between what you wrote and what the discussion
argues. Where they agree, you have confirmed a decision you can defend under
time pressure. Where they differ, you have found something worth understanding
before somebody asks you about it in a scored exam. Reading the discussion first
feels faster and teaches nothing: recognising a good argument is not the same
skill as producing one, and the exam only pays for the second.

**Argue with it.** The book takes positions. Some are contestable, and a few
are stated more bluntly than the evidence strictly supports, because a hedged
claim is impossible to disagree with and therefore impossible to learn from. If
you think a recommendation is wrong for your context, work out why. That
reasoning is the exam's actual subject.

**Revise from the back.** The appendices are built for the week before you sit:
cheat sheets condensing each chapter to the sentence you will be given,
grouped exam traps, and a method for attacking whichever case studies are live
on the day. The decision matrices in chapters 6 and 9 belong in the same
category — mark them now, because you will want them later.

## Exam coverage

Chapters follow architectural decisions rather than the exam guide's section
order. The exam guide splits its material six ways:

| Section | Weight | Covered in |
| --- | --- | --- |
| Designing and planning a cloud solution architecture | ~25% | 1-8 |
| Managing and provisioning a cloud solution infrastructure | ~17.5% | 4, 5, 12 |
| Designing for security and compliance | ~17.5% | 2, 9 |
| Analyzing and optimizing technical and business processes | ~15% | 10, 12, 13-17 |
| Managing implementation | ~12.5% | 12, 13-17 |
| Ensuring solution and operations excellence | ~12.5% | 11 |

Two case studies appear in every sitting, and questions tied to them make up
20 to 30 per cent of the exam. Part II earns its quarter of this book.

## A note on currency

Google revises the exam. At the time of writing the four case studies are
Altostrat Media, Cymbal Retail, EHR Healthcare, and KnightMotives Automotive.
Older material teaches Mountkirk Games, Helicopter Racing League, TerramEarth,
and Dress4Win. Google retired all four.

If a study guide still drills you on Mountkirk, check its publication date
before you trust anything else in it. Check the exam guide yourself before you
sit. It takes five minutes and it is the only source that counts.
