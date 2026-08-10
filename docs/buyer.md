# Buyer

Direction: Option A, layered. One structural reader, one designed second layer.
Meera carries the structure because structure needs a person. The second layer
is what lets a philosophy teacher finish the book. The layer is designed, not
hoped for, and section "The layer rule" below makes it testable during drafting.

---

## The one person

**Meera. Senior product manager, 300-person B2B SaaS company, four years in product, came up through business analysis.**

Her week has three meetings that matter here.

**The architecture review, second Tuesday.** The platform lead says the write path moves behind a queue and the read replicas take the load. Six engineers nod. Meera writes down "read replica" to look up later and never does. She has been in this meeting eleven times and has never once asked a question in it.

**Estimation.** Engineering says the feature takes six weeks. She cannot tell whether that number reflects real difficulty or a team protecting itself. She has no basis to push, so she takes it to the roadmap and defends it to the VP as though she believes it.

**The customer call.** The client's IT head asks where the data sits and whether it leaves the country. Meera looks at the solutions engineer. The client sees her look.

## What she can do after 56,000 words

- **O1** Read an architecture diagram and name what each box costs.
- **O2** Ask three questions in the architecture review that change the decision.
- **O3** Tell which parts of an estimate are hard and which are habit.
- **O4** Answer the data residency question herself.
- **O5** Read the cloud bill her CFO complains about and find the line that grew.
- **O6** Know what breaks in production, and why the vendor slide never mentions it.

## Why she does not just ask a chatbot

A chatbot answers questions she can already phrase. Her problem sits one level up: she does not know which question to ask, or which of the forty terms in that meeting actually matter. She needs sequence, judgment about what counts, and stories about what goes wrong at 2am. Nobody generates those. You lived them.

## What she already knows, so the book must not re-explain it

- What AWS is, in the sense that she knows Amazon sells it.
- What a server is, broadly.
- SaaS pricing models, better than most engineers.
- APIs at the level of "systems talk to each other".
- Why downtime costs money. She has written the customer apology email.

## Where she is not

She is not studying for a certification. She does not want to run anything. She will never open a terminal. A chapter that teaches her to configure something has lost her, and she will not say so, she will just stop reading at chapter 4.

---

## The second layer

The banker, the clerk, the accountant, the philosophy teacher, the English major.
They have no architecture review, no estimate to push back on, and no bill to
read. Four of Meera's six outcomes mean nothing to them.

Two survive, and both get stronger when the reader has no professional stake:

- **O4 becomes a citizen question.** Where does my stuff live, whose country is
  it in, and who is allowed to look at it. A product manager asks this on behalf
  of a client. Everyone else asks it on behalf of themselves, which is the more
  interesting version.
- **O6 becomes a curiosity question.** What breaks, how often, and why nobody
  tells you. This is the question that makes infrastructure worth reading about
  at all.

Beyond those two, what the second layer gets is not a capability. It is three
things a chatbot cannot supply:

1. **A mental model of a place.** After eleven chapters they can picture where
   the photo went, physically, and stop treating the cloud as weather.
2. **The gap.** Demand moves in weeks and concrete moves in eighteen months.
   That gap explains the industry, and it is a genuinely interesting idea that
   happens to be true.
3. **The stories.** The 2am call, the thing that was wrong for twenty minutes,
   the belief nobody corrected. This is the layer that makes the book readable
   by someone with no stake, and it is the only layer a model cannot fake for
   200 pages.

**What the second layer does not get, on purpose.** No foundation tutorial.
The prerequisite list above stands unchanged. A chapter does not stop to explain
what a server is. The English major who does not know reads past it and loses
nothing, because the narrative carries her and the specific term was never the
point. Paying 4,000 words to teach the foundation would cost the book its
specificity and buy very little.

## The layer rule

Operational, and testable during `/draft` and `/review`. Every chapter carries
both layers. **Which reader each job serves is fixed. Where the job appears in
the chapter is not.** The labels below match the eight jobs in
docs/chapter-template.md, which was rewritten from a running order into a
coverage requirement after twelve chapters came out with identical headings. The
mapping of reader to job has not changed.

| Job | Serves |
|-----|--------|
| Open on exposure | Second layer. A person, a place, a thing going wrong. No term the English major must already know. |
| Name the stake | Both. State it as money and consequence, not as architecture. |
| Build the model | Second layer first, Meera second. The mental model has to land before the vocabulary. |
| Work it through | Meera. This is where the utility lives and where the terms get used properly. |
| Show it happening | Meera. |
| Correct the belief | Second layer. Everyone holds a wrong belief about the cloud, and correcting it needs no job. |
| The callback | Both. The photo thread is the spine and it belongs to everyone. |
| Leave three things | Both. |
| Hand her the move | Meera. Second layer reads it and moves on. |

**The test, applied per chapter:** if a reader stops once the wrong belief has
been corrected, did they get something worth the evening? If no, the chapter is
written only for Meera and the second layer will quit before chapter 5.

**The reverse test:** if only the opening and the correction are any good, the
chapter has drifted to general interest and Meera stops paying for it.

---

## Secondary buyers, same book

- **The enterprise AE** selling into IT, who loses momentum when the customer's architect asks a question. He buys for one reason: deal confidence.
- **The pre-seed founder** picking a stack from three blog posts and a friend's advice.
- **The consultant** who has to sound credible in a room she cannot control.

## The bulk buyer

**The VP of Sales or Head of Enablement who buys 40 copies for the AE team.** This person changes the book: give them a discussion guide at the back and chapter-level questions a manager can run in a Friday session. One of these buyers beats four months of individual sales.

This buyer is the reason the direction is Option A. A general-interest book has
no institutional purchaser. Nothing in the second layer may cost this buyer
anything.

## The purchase moment

She buys within 48 hours of a meeting where she felt exposed, or her manager hands it to her in week one of a new job. Both moments reward a cover promise that names the feeling, not the topic.

The second layer has no equivalent trigger. It buys on recommendation, which
means the second layer is a word-of-mouth engine rather than a sales channel.
That is exactly what it is for. Meera buys the book. Her sister the philosophy
teacher borrows it, finishes it, and tells two people.

## The open bet

Stage 4 settles whether this direction was right. Publish the three pilot
articles and watch who forwards them. Forwards from product managers, sales
engineers, and founders confirm Option A. Forwards from people with no stake in
cloud at all, teachers, journalists, someone's cousin who sells insurance, are
evidence for a genuinely general book, and that decision reopens before chapter
4 is drafted, not after.
