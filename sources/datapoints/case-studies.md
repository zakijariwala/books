# Case studies observed

Six scenarios found in `gcp-pca-prep/case-studies/`. Requirements and service
picks below are the repo author's reading, not Google's answer key. Treat the
*shape* as the datapoint: what kind of business problem, what constraint drives
the design.

Target chapters: ch10 (migration), ch13-ch17 (Part II case studies).

Status of the set itself: `UNVERIFIED`. See `flags-stale-and-legal.md`.

## The classic four

### EHR Healthcare

Regulated healthcare, co-location replacement.

- Existing stack: Active Directory, MSSQL, MySQL, Redis, MongoDB, containers
- Constraint that drives everything: **stack stays as-is**. This is a
  replatform, not a refactor. Rules out "rewrite it as serverless" answers
- 99.9% availability, centralised monitoring, multi-environment, dynamic
  provisioning, low-latency link to on-prem
- Author's picks: GCE instance as AD replica, Cloud Identity federated to AD,
  GKE for containers, Cloud SQL for MySQL and MSSQL, Memorystore for Redis,
  MongoDB Atlas or self-managed for NoSQL, Cloud Interconnect to on-prem

Maps to book case study 1 (regulated healthcare) and 5 (legacy modernization).
The AD-federation and same-stack-different-venue framing is the purest example
of the on-prem-beside-GCP device.

### Helicopter Racing League

Media, already in another cloud, moving to GCP with prediction workloads.

- Existing: object storage on another provider, per-job VMs for transcoding,
  TensorFlow on dedicated VMs for race prediction
- Wants: partner-facing prediction API, richer live predictions, global reach,
  more concurrent viewers, less operational complexity, compliance,
  merchandising revenue
- Author's picks: Cloud CDN, Apigee for partner API, Vertex AI for prediction,
  Natural Language for crowd sentiment, Cloud Run for transcode jobs, GCS

Note this is a **cloud-to-cloud** migration, not on-prem. Maps to book case
study 2 (live-event streaming).

### Mountkirk Games

Global game launch.

- Existing: Kubernetes, GPUs
- Wants: low latency, high scale, strongly consistent real-time data, pooled
  resources, GPU rendering, structured activity logs
- Author's picks: multi-region GKE with multiple node pools, GPU node affinity
  for rendering, namespaces for tenant pooling, multi-region Cloud Spanner for
  leaderboards, GCS for logs, global load balancer with anycast

The strong-consistency-plus-global-scale requirement is the Spanner tell. That
pairing is a recurring exam pattern worth teaching explicitly in ch06.

### TerramEarth

Industrial vehicle fleet telemetry. Readme is empty in the repo, but the
questions in the other repo probe it heavily.

Themes visible from those questions: capture all raw data cheaply for unknown
future use, and serve per-vehicle time-series graphs at low latency.

Two decisions worth teaching in ch07:

- Cheap durable capture of raw data of unknown future value points at Cloud
  Storage, not at a warehouse or a running cluster
- Per-entity time-series lookup keyed by `entity.timestamp` points at Bigtable,
  not BigQuery. BigQuery is the analytics answer, Bigtable is the low-latency
  keyed-lookup answer. The exam tests this split repeatedly

Maps to book case study 4 (fleet telemetry).

## The two newer ones

Both are generative-AI modernization scenarios. Their presence is the main
signal that the exam has moved toward AI workloads.

### Altostrat

Media company, already GCP-native, modernizing with generative AI.

- Existing: GKE, GCS for media, BigQuery warehouse, Cloud Run functions,
  native GCP monitoring plus Prometheus, some on-prem data-lifecycle workflows
- Wants: reliability, an infrastructure management framework, automated media
  analysis and metadata generation, LLM and computer vision, analysis on top,
  hybrid on-prem plus cloud Kubernetes, CI/CD modernization

Notable: the customer is **already on GCP**. The scenario is optimization and
AI adoption, not migration. Different question shape from the classic four.

### Cymbal

Online retailer, hybrid, generative AI in the catalog.

- Existing: on-prem plus cloud, MySQL, SQL Server, Redis, MongoDB, Kubernetes,
  file-based on-prem integration over SFTP and ETL, product web app, IVR,
  call centre, Grafana and Elastic for monitoring
- Wants: automatic product metadata generation, cost reduction, GenAI catalog
  improvements including image generation, human-in-the-loop review,
  scalability, compliance

Human-in-the-loop on AI output is a governance requirement, not a technical one.
Worth teaching in ch08 as its own decision.

## Pattern across all six

Every scenario is a migration, a modernization, or an optimization of something
that already exists. None is greenfield.

That is the justification for the book's core visual device and for putting
migration in its own chapter when Google's learning path has no migration
course at all.

Second pattern: the constraint sentence is always the answer key. "Stack stays
as-is," "strongly consistent," "unknown future use," "human-in-the-loop." Teach
readers to find that sentence first. That technique is the spine of ch01 and of
the Part II opening.
