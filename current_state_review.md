# Repository Technical Review & Current State Analysis

This review analyzes the current state of the GCP Professional Cloud Architect (PCA) exam-prep book project repository. It covers the manuscript writing progress, technical content evaluation, copyright/legal risk assessment, and toolchain capabilities.

---

## 1. Manuscript Writing Progress & Word Counts

The project targets a word count of **28,000 words** (enforced by the wordcount tool in [`scripts/wordcount.py`](file:///D:/books/scripts/wordcount.py)). Currently, the repository contains **7,023 words** (approx. **25.1% complete**).

Here is the breakdown of each manuscript file:

| File | Chapter Topic / Section | Target Words | Actual Words | Status | Details / Actions Needed |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [`front-matter.md`](file:///D:/books/manuscript/front-matter.md) | Preface & Exam Domain Mapping | 600 | 454 | **Partial** | Outlines target audience and maps chapters to exam sections. Needs final review once chapters are complete. |
| [`ch01.md`](file:///D:/books/manuscript/ch01.md) | Exam anatomy & case study reading | 1,500 | 848 | **Drafted** | Strong overview of finding "constraint sentences" and identifying distractor patterns. |
| [`ch02.md`](file:///D:/books/manuscript/ch02.md) | Hierarchy and identity | 1,600 | 1,103 | **Drafted** | Covers GCP Resource Hierarchy, IAM policy binding patterns, and directory synchronization/federation. |
| [`ch03.md`](file:///D:/books/manuscript/ch03.md) | Networking: VPC & hybrid | 1,800 | 1,135 | **Drafted** | Details Global VPC, Shared VPC, Private Access variants, and Interconnect lines. |
| [`ch04.md`](file:///D:/books/manuscript/ch04.md) | Compute: VMs and serverless | 1,600 | 222 | **Skeleton** | Placeholders for sole-tenant nodes, MIGs, Cloud Run vs Cloud Functions. |
| [`ch05.md`](file:///D:/books/manuscript/ch05.md) | Containers: GKE, Fleets, CSM | 1,600 | 258 | **Skeleton** | Placeholders for Autopilot vs Standard, release channels, Workload Identity. |
| [`ch06.md`](file:///D:/books/manuscript/ch06.md) | Storage and databases | 1,700 | 272 | **Skeleton** | Focuses on Cloud SQL, Spanner vs others, and regional consistency. |
| [`ch07.md`](file:///D:/books/manuscript/ch07.md) | Data pipelines and analytics | 1,500 | 210 | **Skeleton** | Placeholders for Pub/Sub, Dataflow, Bigtable time-series lookups, BigQuery. |
| [`ch08.md`](file:///D:/books/manuscript/ch08.md) | AI/ML infrastructure | 1,300 | 200 | **Skeleton** | Key chapter for PCA v6.1. GPU/TPU selection, Vertex AI, human-in-the-loop controls. |
| [`ch09.md`](file:///D:/books/manuscript/ch09.md) | Security and compliance | 1,700 | 292 | **Skeleton** | VPC Service Controls, Cloud KMS (CMEK), Cloud HSM, compliance mapping. |
| [`ch10.md`](file:///D:/books/manuscript/ch10.md) | Migration patterns | 1,700 | 282 | **Skeleton** | Replatform vs Refactor, Database Migration Service, Transfer Service. |
| [`ch11.md`](file:///D:/books/manuscript/ch11.md) | Reliability, observability, DR | 1,800 | 241 | **Skeleton** | Multi-region designs, Cloud Operations Suite, SLOs/SLAs, log sinks. |
| [`ch12.md`](file:///D:/books/manuscript/ch12.md) | Operations, IaC, and cost | 1,700 | 248 | **Skeleton** | Terraform state in GCS, service impersonation, cost optimization (FinOps). |
| [`ch13.md`](file:///D:/books/manuscript/ch13.md) | Case Study 1: Regulated Healthcare | 1,200 | 271 | **Skeleton** | Original scenario mirroring EHR Healthcare (Compliance, CMEK, VPC-SC). |
| [`ch14.md`](file:///D:/books/manuscript/ch14.md) | Case Study 2: Live-Event Streaming | 1,200 | 191 | **Skeleton** | Original scenario mirroring HRL (CDN, autoscaling, Cloud Run transcoding). |
| [`ch15.md`](file:///D:/books/manuscript/ch15.md) | Case Study 3: Game Backend | 1,200 | 198 | **Skeleton** | Original scenario mirroring Mountkirk (Spanner, GKE pools, global LB). |
| [`ch16.md`](file:///D:/books/manuscript/ch16.md) | Case Study 4: Fleet Telemetry | 1,200 | 194 | **Skeleton** | Original scenario mirroring TerramEarth / KnightMotives (IoT, Bigtable, ML). |
| [`ch17.md`](file:///D:/books/manuscript/ch17.md) | Case Study 5: Legacy Monolith | 1,200 | 249 | **Skeleton** | Replatforming, hybrid identity federation, network bridging. |
| [`back-matter.md`](file:///D:/books/manuscript/back-matter.md) | Appendices & Glossary | 1,400 | 155 | **Outline** | Contains outlines for playbooks, AWS/Azure translation tables, and glossary. |

---

## 2. Technical Evaluation of Drafted Chapters

### Chapter 1: Reading the Exam
*   **Focus:** Excellent strategy shift from memorizing services to decoding exam questions. It introduces the critical technique of locating the "constraint sentence" (the business requirement that eliminates two of the four answers).
*   **Quality:** High. The tone is practical, cynical, and authoritative, matching what a senior cross-cloud architect expects.

### Chapter 2: Hierarchy and Identity
*   **Focus:** Places resource hierarchy early because folders, projects, and organizations have no clean equivalents in AWS or Azure. 
*   **Strengths:** Correctly notes that AWS accounts are treated as heavy and expensive, whereas Google Cloud projects are lightweight and should be spawned frequently as quota and billing boundaries. Emphasizes Workload Identity and Service Account impersonation over long-lived JSON keys.
*   **Deficit:** The underlying raw notes in `sources/datapoints` left folders and organization policies blank. The chapter's structure was successfully built from scratch using official GCP patterns.

### Chapter 3: Networking and Hybrid Connectivity
*   **Focus:** Highlights that Google VPCs are global with regional subnets (unlike regional AWS VPCs), firewall rules targeting tags/service accounts, and Shared VPC structures.
*   **Quality:** Very strong. It correctly clarifies the confusing "private-access trio" (Private Google Access, Private Service Connect, Private Services Access) and explains the routes exporting trap in Private Services Access peering.

---

## 3. Copyright, Legal, and Terminology Risks

### 3.1 Legal & Copyright Risks
*   **Verification:** Confirmed that the `GCP_Professional_Architect` folder (not tracked in Git) contains raw exam questions and Q&A dumps. **These must never be copied or rephrased.**
*   **Official Case Studies:** Official Google PDFs (EHR Healthcare, Mountkirk Games, TerramEarth, etc.) are present in untracked folders. Google's case studies are copyrighted materials and subject to change. The book correctly avoids reprinting them, replacing them with original, functionally identical scenarios in Part II.

### 3.2 Terminology Staleness (Observed in Reference Repos vs. Book Standard)
To ensure the book passes technical reviews, the following terminology translations must be enforced during drafting:

| Legacy / Stale Term | Current Google Cloud Term | Status / Rationale |
| :--- | :--- | :--- |
| **Stackdriver** | Cloud Logging / Cloud Monitoring | Renamed to Cloud Operations Suite (refer to logging/monitoring specifically). |
| **Cloud Dataproc** | Dataproc | Google dropped the "Cloud" prefix on most analytics engines. |
| **Cloud Dataflow** | Dataflow | Dropped "Cloud" prefix. |
| **Cloud Pub/Sub** | Pub/Sub | Dropped "Cloud" prefix. |
| **Cloud Datastore** | Firestore (in Datastore mode) | Datastore is legacy; Firestore is the modern default database mode. |
| **Cloud ML** | Vertex AI | Consolidated product suite. |
| **Cloud Natural Language API** | Cloud Natural Language | Updated name. |
| `debian-9` / `nodejs8` | `debian-11` / `nodejs20` | Runtimes cited in older lab notes are long out of support. |
| `gcloud functions deploy --stage-bucket` | `gcloud functions deploy` | Flag removed; functions now integrate directly under Cloud Run. |
| `terraform taint` | `terraform apply -replace=ADDR` | Deprecated since Terraform 0.15.2. |
| Legacy HTTP health checks | Regional backend health checks | Modern health checks are standard. |
| **Dress4Win** / **Mountkirk Games** / **HRL** / **TerramEarth** | *Retired* | Google retired these case studies in version 6.x of the exam. |

---

## 4. Verification of "Still to Verify" Section

The items flagged in [`BOOK-SPEC.md`](file:///D:/books/BOOK-SPEC.md) as "Still to verify" have been researched and verified against official Google Cloud learning resources:

### 4.1 GCP PCA Exam Metrics
*   **Exam Cost:** $200 USD.
*   **Exam Duration:** 2 hours (120 minutes).
*   **Question Count:** 50–60 multiple-choice and multiple-select questions.
*   **Validity:** 2 years.
*   **Recertification Renewal:** Validated that Google offers a shorter renewal exam (1 hour, ~25 questions, ~$100 USD) focusing on updated topics like Generative AI.

### 4.2 Case Studies (Exam Version 6.1)
The active case studies on the exam are:
1.  **Altostrat Media:** Adopting generative AI for media cataloging and automated metadata generation.
2.  **Cymbal Retail:** Hybrid scaling, database sprawl, and catalog enhancement using image/metadata generative AI.
3.  **EHR Healthcare:** Traditional migration of regulated medical database workloads from on-prem to Google Cloud.
4.  **KnightMotives Automotive:** Connected-vehicle telemetry, streaming ingestion, time-series querying, and machine learning model pipelines.

> [!NOTE]
> *KnightMotives Automotive* occupies the slot previously held by *TerramEarth*. It focuses on telemetry scale (IoT/connected cars), confirming that Chapter 16 (Fleet Telemetry) must detail streaming architectures (Pub/Sub + Dataflow + Bigtable) without replicating Google's copyrighted details.

---

## 5. Toolchain and Compilation Pipeline Status

### 5.1 Build Environment
*   **Makefile Limitation:** The `Makefile` relies on UNIX utility configurations (`make`, `magick`, `mmdc`). In native Windows environments, running `make` commands directly fails. 
*   **Resolution:** Python build targets can be executed manually via `venv/Scripts/python.exe`. A comprehensive list of replacement commands has been added to [`handover.md`](file:///D:/books/handover.md).
*   **Vale Linter:** Properly configured. Rule blocks like `Google.Headings`, `Google.FirstPerson`, and `Google.We` are disabled in [`.vale.ini`](file:///D:/books/.vale.ini) to allow title-case headings, prefacing in first-person, and addressing the reader as "you" (standard for trade books).

### 5.2 Diagram & Image Compilation
*   **Architecture Diagrams:** Written using the Python `diagrams` library. Requires `diagrams` and `pillow` installed in the venv. Outputs are generated directly.
*   **Flowcharts:** Written in Mermaid (`.mmd`). Requires the Mermaid CLI (`mmdc`) installed globally. Normalization script [`normalize_image.py`](file:///D:/books/scripts/normalize_image.py) automatically formats these to 300 DPI, 1350px wide for grayscale print proofs.
