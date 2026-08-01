# Compute, data, and operations

Target chapters: ch04 (compute), ch05 (containers), ch06 (storage and
databases), ch07 (data), ch12 (operations and IaC).

All `UNVERIFIED`. Pricing figures in the sources are old and must not be
reproduced in the book at all.

## GKE

From `gcp-pca-prep/services/gke/readme.md`.

- Managed control plane. Google upgrades it automatically; nodes follow the
  maintenance window and release channel you pick. **Release channel selection
  is an architecture decision**, not an operational detail, and is worth a
  decision figure in ch05
- Management fee per cluster plus node cost, on standard clusters
- GKE-native additions beyond upstream Kubernetes: sandboxing, Workload Identity

**Autopilot.** Google manages nodes too. You pay for CPU and memory that pods
*request*, not for nodes. That changes the cost model, so the standard-versus-
Autopilot choice is partly a FinOps decision and belongs in both ch05 and ch12.

**When not to use it.** The source is blunt and correct: don't pick GKE if the
team doesn't know Kubernetes. Team capability as a legitimate architectural
input is an underused idea in prep books and fits the "business process" gap
the official learning path leaves open. Use it.

Do not carry over the source's App Engine suggestion as the alternative. Cloud
Run is the current default for that recommendation.

## Service picks observed across the Terraform

Resource types actually used across all case-study solutions in
`gcp-pca-prep`, by frequency. Useful as a signal of what a working solution
touches, not as a correctness check.

Heavily used: `google_project_service` (36 occurrences), `google_project` (9),
`google_storage_bucket` (6). API enablement and project structure dominate
every solution. Reinforces putting hierarchy in ch02.

Then: GKE clusters and node pools, Cloud Functions, Cloud SQL, Cloud DNS,
compute networks and subnetworks, Cloud Router, **Interconnect attachments**,
BigQuery datasets, Spanner, Bigtable, Redis, logging sinks and bucket configs,
API Gateway, global forwarding rules with URL maps and backend services,
Dialogflow CX, folders, service accounts.

Two things worth noting. Interconnect attachments appear in the case-study
solutions, confirming hybrid connectivity is load-bearing rather than
decorative. And logging sinks appear as designed infrastructure, not as an
afterthought, which supports pairing observability with reliability in ch11.

## Data and storage decisions

From the TerramEarth-shaped questions. These are the decision splits to teach,
stripped of the exam items themselves.

- **Cheap durable capture of raw data with unknown future value** goes to Cloud
  Storage. Not to a warehouse, not to a running Dataproc or HDFS cluster.
  Streaming everything straight into BigQuery is the expensive wrong answer
- **Low-latency lookup keyed by entity and timestamp** goes to Bigtable.
  BigQuery is for analytics over large scans; Bigtable is for keyed time-series
  reads. This split recurs constantly
- **Strong consistency plus global scale** goes to Spanner. Seen in the
  Mountkirk leaderboard picks

Storage class lifecycle: keep frequently-processed data in Standard, move to
Coldline once access drops off. The source's specific 30-day threshold came
from a scenario, not a rule. Teach the reasoning, not the number.

## Interconnect sizing

One durable decision point surfaced in the questions:

Partner Interconnect suits requirements up to roughly 10 Gbps and carries an
SLA. Dedicated Interconnect becomes the cost-effective choice above that.

`UNVERIFIED` and the exact figures matter. Confirm current tiers, per-connection
capacities, and SLA terms before writing ch03. Do not print the numbers from
these notes.

## Deployment and rollback patterns

From question topics, worth teaching as ch12 decisions:

- Managed instance groups with rolling updates are the answer for rollback
  across large fleets with frequent critical updates
- **Blue-green is the wrong pattern for long-running transactions.** It suits
  fast rollback; it does not suit workloads holding long transactions across
  the cutover. Good trap material
- Log-based metrics with threshold alerting is the answer for catching
  intermittent bursty failures, rather than more logging or manual inspection
- The correct response to a past partial failure is root-cause analysis, not
  immediate re-architecture. The exam rewards process answers here, which is
  again the business-process area the official path skips

## Terraform

`GCP_Professional_Architect/terraform.md` is a command list. Low value, and
`terraform taint` in it is deprecated. See `flags-stale-and-legal.md`.

The useful IaC datapoint is structural, from `gcp-pca-prep`: remote state in
GCS backends, one workspace per example, provider configured with **service
account impersonation** rather than exported keys, and a suggestion to scope
the Terraform service account rather than leaving it as Editor.

Service account impersonation over key files is the current recommended
practice and pairs with the Workload Identity point in
`networking-identity.md`. Both are instances of the same principle: no
long-lived credential material anywhere. That principle is worth stating once
in ch02 and referring back to from ch05 and ch12.
