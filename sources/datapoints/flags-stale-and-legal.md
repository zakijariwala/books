# Flags: stale terminology and copyright exposure

Read this before using anything else in this folder.

## Legal exposure found in the source repos

Three distinct problems. All of them would follow the content into a commercial
KDP book if copied.

### Real exam questions

`GCP_Professional_Architect/Q&A.md` contains what read as verbatim exam
questions with lettered options, several tagged "VALID" as if answer-keyed from
a sitting.

Do not reuse any of it, not even reworded. Reproducing live exam items breaches
Google's exam terms and the certification agreement, independent of copyright.
A prep book carrying recognisable item text is the single fastest way to draw a
takedown and to lose standing with the certification program.

The *topics* those questions probe are fair to note. The items are not.

### Redistributed official case studies

- `GCP_Professional_Architect/images/` holds PNG screenshots of EHR Healthcare,
  Helicopter Racing League, and Mountkirk Games
- `gcp-pca-prep/case-studies/ehr/master_case_study_ehr_healthcare.pdf`
- `gcp-pca-prep/case-studies/helicopter/master_case_study_helicopter_racing_league.pdf`

Google's copyrighted text, redistributed without licence. Already flagged in
`BOOK-SPEC.md`. The book ships five original case studies instead.

### Third-party architecture diagrams

Suggested-architecture diagrams in `gcp-pca-prep` are hosted on Lucidchart and
diagrams.net under the repo author's accounts. Useful to look at. Not yours to
redraw closely. Every figure in the book is generated from source in
`diagrams/`.

## Stale terminology

`GCP_Professional_Architect` dates to 2022. Anything below is wrong now and
should be recognised as a staleness signal in any other source too.

| Stale | Current | Note |
| --- | --- | --- |
| Stackdriver | Cloud Logging / Cloud Monitoring | Renamed to Cloud Operations well before 2022 |
| Cloud Dataproc, Cloud Dataflow, Cloud Pub/Sub | Dataproc, Dataflow, Pub/Sub | Google dropped the "Cloud" prefix on most of these |
| Cloud Datastore | Firestore in Datastore mode | Datastore is legacy |
| Cloud ML | Vertex AI | Vertex consolidated the ML products |
| Cloud Natural Language API | Cloud Natural Language, or Vertex AI | Partly absorbed |
| `debian-9`, `nodejs8` runtimes | Long out of support | Any lab using these is old |
| `gcloud functions deploy --stage-bucket` | Flag removed | Cloud Run functions is the current framing |
| `terraform taint` | `terraform apply -replace=ADDRESS` | Deprecated since Terraform 0.15.2 |
| Legacy HTTP health checks, target pools | Regional backend services, modern health checks | Target-pool network LB is the legacy path |
| Dress4Win case study | Retired | Appears throughout `Q&A.md` |

`STALE` marks in the other datapoint files point back here.

## Positive signal buried in the staleness

`gcp-pca-prep/case-studies/` carries six folders, not four: the classic EHR,
Helicopter Racing League, Mountkirk Games, and TerramEarth, plus **Altostrat**
and **Cymbal**.

Both new ones are generative-AI modernization scenarios. That lines up with
Google's learning path adding two AI courses. Two independent sources pointing
the same direction is the strongest available evidence that the case-study set
has moved toward AI workloads.

Still `UNVERIFIED`. Confirm the current official list against the exam guide
before weighting chapter 8 or the Part II case studies around it.
