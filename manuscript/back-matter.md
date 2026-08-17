# Exam-day playbook

The exam runs two hours and carries 50 to 60 multiple-choice and multiple-select
questions, of which 20 to 30 per cent attach to two case studies shown on a
split screen. It costs $200 and the certification is valid for two years. The
renewal exam is shorter — around an hour and roughly 25 questions at about half
the cost — and it weights whatever Google has added since. At the time of
writing that means a single generative-AI case study carrying almost the whole
paper, so renewal is a narrower examination than the one you are sitting now,
not a lighter version of it. Confirm all of this on the certification page
before you book; these figures move.

That arithmetic gives you a little over two minutes a question, and the case
studies eat reading time before you answer anything.

**Read both case studies before you answer a single question.** They are
available on screen throughout, but reading one cold in the middle of a question
costs more than reading it deliberately at the start. You are looking for the
sentences that constrain, not the sentences that describe.

**Write down the constraint sentences.** Every scenario has one or two that
eliminate half the options: a support matrix, a residency clause, a fixed date,
an approval obligation, a team that has never run the technology in the
attractive answer. Have them in front of you so you are not re-reading the
scenario each time.

**Answer the question asked.** The exam distinguishes between the cheapest
option that meets a requirement, the most reliable option, and the option with
least operational overhead. Two of those are usually wrong for any given
question, and they are all defensible in isolation.

**Flag anything over ninety seconds and move on.** Later questions are worth the
same as the one you are stuck on, and the case study you have not reached yet
needs reading time.

**When two options survive, go back to the constraint, not to the technology.**
The tiebreaker is almost always in the scenario rather than in the merits of the
services.

**Watch for process questions.** Section 4 rewards answers that are
organisational: a root cause analysis, a stakeholder sign-off, a communication
plan, a blameless postmortem. When a scenario describes something that already
went wrong, the impressive technical answer is usually the distractor.

**Prefer the answer that removes credentials, and be suspicious of the answer
that stores them better.** This single heuristic settles a surprising number of
identity questions.

**Cost answers follow workload shape.** Steady baseline is commitments,
interruptible batch is Spot, and neither substitutes for the other however much
cheaper the headline rate.

# The golden rules

Nine rules that generate correct answers across the whole exam. Where a chapter
states one, it states it once; this is where they live together.

1. **The constraint sentence outranks the technology.** When two options both
   work, the scenario has already told you which one it wants.
2. **Never distribute a credential.** Attached identities, Workload Identity,
   and impersonation cover every real case. An answer that stores a key more
   securely is still the wrong answer.
3. **The cheapest design that meets the stated requirement wins.** Extra
   redundancy nobody asked for is a distractor with a price tag.
4. **Capability is an architectural input.** Recommending a platform the team
   cannot operate is a wrong answer however well it scales.
5. **Business constraints beat engineering preferences.** Approval gates,
   residency clauses, and vendor support matrices are requirements, not
   obstacles to design around.
6. **Land raw data cheaply before deciding what it is worth.** Cloud Storage
   first; load into a warehouse what has earned it.
7. **Prevent rather than review.** Organization policy, perimeters, and
   pipelines beat any control that depends on somebody remembering.
8. **Managed until a constraint says otherwise.** Take the managed service, and
   let the scenario tell you when it cannot.
9. **Process answers process questions.** Root cause analysis, a named
   approver, a communication plan. The impressive technical answer to an
   organisational question is the trap.

# Appendix A: Decision cheat sheets

Revision pages. Each condenses a chapter to the sentence you will be given and
the answer it selects.

**Compute**

| Scenario says | Answer |
| --- | --- |
| Cannot modify the application | Compute Engine |
| Licensed per physical core | Sole-tenant nodes |
| Stateless HTTP, containerised | Cloud Run |
| Event handler | Cloud Functions |
| Runs to completion | Cloud Run jobs |
| Interruptible batch | Spot VMs in a MIG |
| Existing Kubernetes team and estate | GKE |

**Storage and data**

| Scenario says | Answer |
| --- | --- |
| Value unknown, keep it all | Cloud Storage, lifecycle rules |
| Immutable for N years | Retention policy, locked |
| Shared POSIX, app unchangeable | Filestore |
| Global plus strongly consistent | Spanner |
| Keyed lookup at volume, time series | Bigtable |
| Analytical scans over history | BigQuery |
| Offline mobile clients | Firestore |
| Session or hot cache | Memorystore |

**Networking**

| Scenario says | Answer |
| --- | --- |
| Several regions, private addressing | One global VPC |
| Central network team, separate app teams | Shared VPC |
| No external IP, needs Google APIs | Private Google Access |
| Endpoint in your own range | Private Service Connect |
| Cloud SQL privately | Private Services Access |
| SLA or bandwidth floor | Interconnect |
| Encryption, modest throughput | HA VPN |
| One global entry point | Global external Application Load Balancer |

**Security**

| Scenario says | Answer |
| --- | --- |
| Must not leave the region | Organization policy plus regional resources |
| We hold the keys | CMEK |
| Keys never in the provider | External Key Manager |
| Authorised user must not copy data out | VPC Service Controls |
| Internal apps without a VPN | Identity-Aware Proxy |
| Managed devices only | Context-aware access |
| Partners get data, not access | Apigee or API Gateway |
| Partners query a curated slice | Authorised view or Analytics Hub |
| Prove who read the data | Data Access logs, enabled in advance |

**Reliability and cost**

| Scenario says | Answer |
| --- | --- |
| Survive a zone | Regional deployment |
| Survive a region | Multi-region, only if stated |
| RPO near zero | Continuous or synchronous replication |
| RTO in minutes | Warm or hot standby |
| Steady baseline, multi-year | Committed use discounts |
| Interruptible work | Spot |
| Cannot attribute the bill | Projects and labels, then billing export |

# Appendix B: Exam traps

Each row is a requirement, the answer that looks right, and the one that is.
Grouped by area so you can revise a weak domain on its own.

**Hierarchy and identity**

| Requirement | Wrong | Right |
| --- | --- | --- |
| Revoke a leaver everywhere | Delete their bindings | Roles on groups, federated directory |
| App needs Google API access | Service account key | Attached identity or Workload Identity |
| CI outside Google Cloud | Exported key in the CI system | Workload Identity Federation |
| Nobody may create external IPs | IAM role restriction | Organization policy constraint |
| Teams must not see each other | One project, careful IAM | Separate projects, folder policy |
| Least privilege for a job | Custom role by default | Predefined role first |
| Separation of duties | One custom role | Split across two principals |
| Cost per team | Tagging policy | Project structure plus labels |

**Networking**

| Requirement | Wrong | Right |
| --- | --- | --- |
| Private connectivity across regions | VPC peering | One global VPC |
| Hub and spoke, spokes must talk | Peering | Network Connectivity Center |
| SLA on the link | Cloud VPN | Interconnect |
| Cloud SQL from on-premises | Peering alone | Export custom routes |
| No public IP, needs Cloud Storage | NAT to the internet | Private Google Access |
| API endpoint must stay in-region | Regional bucket | Private Service Connect endpoint |
| Firewall that survives careless edits | Network tags | Service account targets |
| One address, global users | DNS round-robin | Global external Application Load Balancer |

**Compute and containers**

| Requirement | Wrong | Right |
| --- | --- | --- |
| Vendor-certified OS only | Containerise it | Rehost to Compute Engine |
| Audited per-core licence | Standard VMs | Sole-tenant nodes |
| Minimise ops, containerised | GKE | Cloud Run |
| Team has no Kubernetes skill | GKE Autopilot | Cloud Run |
| Nightly transformation | An HTTP service | Cloud Run job |
| Nine-hour job | Request-scoped serverless | VM or job |
| Survive zone loss | Zonal MIG or cluster | Regional |
| No credentials in the image | Key in a secret | Workload Identity |
| Untrusted tenant workloads | Namespaces | GKE Sandbox |
| Fleet needs frequent rollback | Blue-green | Rolling updates on a MIG |

**Data**

| Requirement | Wrong | Right |
| --- | --- | --- |
| Capture everything cheaply | Stream into BigQuery | Cloud Storage |
| Sub-second lookup by key | BigQuery | Bigtable |
| Ad-hoc analysis over years | Bigtable | BigQuery |
| Existing Spark, no rewrite | Dataflow | Dataproc |
| Late and out-of-order events | Processing-time windows | Event-time windows |
| Messages may duplicate | Assume once | Idempotent processing |
| Reduce query cost | Smaller warehouse | Partitioning and clustering |
| Warehouse tracks a live database | Nightly extract | Datastream |
| Idle cluster sized for peak | A smaller permanent cluster | Ephemeral clusters on Cloud Storage |
| Move 500 TB before a deadline | Copy over the wire | Do the arithmetic, then Transfer Appliance |

**Security and compliance**

| Requirement | Wrong | Right |
| --- | --- | --- |
| Data must not leave the country | Firewall rules | Organization policy, regional resources |
| Insider copying data out | Tighter IAM | VPC Service Controls |
| Deploy a perimeter safely | Enforce and watch | Dry-run first |
| Keys never in Google | CMEK | External Key Manager |
| Validated hardware | CMEK | Cloud HSM |
| Key admin must not read data | One project | Separate key project |
| Who read this table last year | Admin Activity logs | Data Access logs, enabled in advance |
| Logs must survive an admin | Longer retention | Sink to another project |
| Named compliance regime | Hand-built controls | Assured Workloads |
| Store an API key | Environment variable | Secret Manager |
| Share data with partners | A role in your project | Apigee or API Gateway |
| Throttle a partner per contract | Load balancer rate limits | Quotas at the API layer |
| Partner runs their own analysis | Export a copy to them | Authorised view or Analytics Hub |

**Migration, reliability, and operations**

| Requirement | Wrong | Right |
| --- | --- | --- |
| Immovable exit date | Refactor first | Rehost, modernise after |
| Source no longer builds | Replatform | Rehost |
| 11 TB, short cutover | Export and import | Continuous replication |
| Four apps mount a file share | Rewrite them now | Filestore, defer the rewrite |
| Something failed last week | Re-architect | Root cause analysis |
| Untested recovery plan | Document it | Test it; RTO is unknown until you do |
| Intermittent bursty errors | More logging | Log-based metrics and alerting |
| Which hop is slow | Read the logs | Cloud Trace |
| Long transactions across cutover | Blue-green | Rolling or canary |
| Human must approve release | A policy document | Cloud Deploy approval gate |
| Only approved images run | Vulnerability scanning | Binary Authorization |
| Spend must stop at a limit | A budget alert | Alert wired to an action |
| Predictable steady baseline | Spot | Committed use discounts |

# Appendix C: Working any case study

Google revises its case studies, so learning four of them is a wasting asset.
The method below works on whichever pair appears on your screen, and this
appendix teaches the method rather than reproducing Google's copyrighted
scenarios. At the time of writing the live set is Altostrat Media, Cymbal Retail,
EHR Healthcare, and KnightMotives Automotive. Read them from Google's own site,
which is also the only place they are guaranteed current.

**First pass, five minutes, before any question.** Read for structure, not
detail. Every official case study carries the same sections: a company
description, a solution concept, the existing technical environment, business
requirements, technical requirements, and a statement from an executive. Know
where each sits so you can jump back to the right one under time pressure.

**Second pass, mark the constraints.** Most sentences are scenery. You are
hunting for the ones that eliminate options:

- Version, certification, or vendor support statements
- Fixed dates, contract expiries, regulatory deadlines
- Residency, sovereignty, and audit obligations
- Approval and sign-off requirements
- Statements about team size, skills, or experience
- Explicit cost or budget conditions
- Numbers: latency, availability, RPO, RTO, volumes, growth rates

**Read the executive statement carefully.** It is short, it is easy to skim as
marketing, and it usually contains the business priority that breaks ties
between two technically valid answers.

**Third pass, map requirements to decisions.** For each technical requirement,
write the decision it forces and the chapter it comes from. Most case studies
reduce to eight or ten decisions: where compute lands, which database, how the
network connects, how identity federates, what the data pipeline looks like,
which controls satisfy the compliance clause, and how it is all deployed.

**Then look for the tensions.** Every well-built case study contains at least
one pair of requirements that pull against each other — cost against
availability, speed against modernisation, autonomy against central control.
The exam's harder questions live exactly there, and the answer is usually the
one that respects the harder constraint and sequences the softer one.

**Recurring themes across the current set.** Two of the four are
generative-AI scenarios, which puts chapter 8's material — prebuilt against
tuned against retrieval, human review, inference cost — directly in scope. One
is a regulated migration, which is chapters 9 and 10. One is connected-vehicle
telemetry, which is chapters 6 and 7: keyed lookups against analytical scans,
and ingest that tolerates duplicates and late arrival. The five case studies in
Part II of this book were built to exercise the same decisions.

**Finally, do it yourself before exam day.** Take each live case study, spend
twenty minutes producing the constraint list and the decision map, and keep the
result. That artefact is worth more than any summary somebody else wrote,
including this one.

# From AWS and Azure

Naming only. Where the mental model genuinely differs, the chapters carry it
inline; a translation table cannot teach that a Google Cloud VPC is global or
that an IAM policy attaches to a resource rather than to a principal.

| Concept | AWS | Google Cloud |
| --- | --- | --- |
| Virtual machines | EC2 | Compute Engine |
| Autoscaling group | Auto Scaling group | Managed instance group |
| Managed Kubernetes | EKS | GKE |
| Container request-response | Fargate, App Runner | Cloud Run |
| Event functions | Lambda | Cloud Functions |
| Object storage | S3 | Cloud Storage |
| Block storage | EBS | Persistent Disk, Hyperdisk |
| Managed NFS | EFS | Filestore |
| Managed relational | RDS | Cloud SQL, AlloyDB |
| Global relational | Aurora Global, DynamoDB Global | Spanner |
| Wide-column store | DynamoDB | Bigtable |
| Document store | DocumentDB | Firestore |
| Managed cache | ElastiCache | Memorystore |
| Warehouse | Redshift | BigQuery |
| Messaging | SNS, SQS, Kinesis | Pub/Sub |
| Stream and batch processing | Kinesis Data Analytics, EMR | Dataflow |
| Managed Hadoop and Spark | EMR | Dataproc |
| Workflow orchestration | MWAA | Cloud Composer |
| ML platform | SageMaker | Vertex AI |
| Key management | KMS, CloudHSM | Cloud KMS, Cloud HSM |
| Secrets | Secrets Manager | Secret Manager |
| Logging and monitoring | CloudWatch | Cloud Logging, Cloud Monitoring |
| Distributed tracing | X-Ray | Cloud Trace |
| Audit trail | CloudTrail | Cloud Audit Logs |
| Security posture | Security Hub | Security Command Center |
| Private dedicated link | Direct Connect | Dedicated Interconnect |
| Application load balancing | ALB | Application Load Balancer |
| CDN | CloudFront | Cloud CDN |
| Infrastructure as code | CloudFormation | Terraform, Config Controller |
| Build pipeline | CodeBuild, CodePipeline | Cloud Build, Cloud Deploy |
| Artifact storage | ECR, CodeArtifact | Artifact Registry |
| Cost budgets | Budgets | Budgets and billing export |

| Concept | Azure | Google Cloud |
| --- | --- | --- |
| Virtual machines | Virtual Machines | Compute Engine |
| Autoscaling group | Virtual Machine Scale Set | Managed instance group |
| Managed Kubernetes | AKS | GKE |
| Container request-response | Container Apps | Cloud Run |
| Event functions | Functions | Cloud Functions |
| Object storage | Blob Storage | Cloud Storage |
| Block storage | Managed Disks | Persistent Disk, Hyperdisk |
| Managed NFS | Azure Files | Filestore |
| Managed relational | Azure SQL, Database for MySQL | Cloud SQL, AlloyDB |
| Global relational | Cosmos DB | Spanner |
| Wide-column store | Cosmos DB, Table Storage | Bigtable |
| Document store | Cosmos DB | Firestore |
| Managed cache | Cache for Redis | Memorystore |
| Warehouse | Synapse Analytics | BigQuery |
| Messaging | Service Bus, Event Hubs | Pub/Sub |
| Stream and batch processing | Stream Analytics | Dataflow |
| Managed Hadoop and Spark | HDInsight | Dataproc |
| Workflow orchestration | Data Factory | Cloud Composer |
| ML platform | Azure Machine Learning | Vertex AI |
| Key management | Key Vault, Managed HSM | Cloud KMS, Cloud HSM |
| Secrets | Key Vault | Secret Manager |
| Logging and monitoring | Azure Monitor | Cloud Logging, Cloud Monitoring |
| Distributed tracing | Application Insights | Cloud Trace |
| Audit trail | Activity Log | Cloud Audit Logs |
| Security posture | Defender for Cloud | Security Command Center |
| Private dedicated link | ExpressRoute | Dedicated Interconnect |
| Application load balancing | Application Gateway | Application Load Balancer |
| CDN | Azure Front Door | Cloud CDN |
| Infrastructure as code | ARM, Bicep | Terraform, Config Controller |
| Build pipeline | Azure Pipelines | Cloud Build, Cloud Deploy |
| Artifact storage | Container Registry | Artifact Registry |
| Cost budgets | Cost Management budgets | Budgets and billing export |

Constructs with no clean equivalent are covered in the chapters rather than
here: the organization and folder hierarchy, Shared VPC, live migration, and the
global VPC model. Treating any of those as a rename is how cross-cloud
architects lose questions.

# Glossary

Google's names for things an experienced architect already understands.

**Apigee** — API management, publishing an API to consumers outside your
organisation with credentials, quotas, and analytics per consumer. API Gateway
is the lighter option for the same job.

**Autopilot** — GKE mode where Google manages nodes and you pay for pod
requests.

**CMEK** — customer-managed encryption keys, held in Cloud KMS in your project.

**EKM** — Cloud External Key Manager, keeping key material outside Google
entirely.

**Error budget** — the permitted unreliability implied by an SLO, spent on
releases and risk.

**Fleet** — a group of clusters, including on-premises ones, managed as one unit
for policy and configuration.

**Host project** — the Shared VPC project that owns the network; workloads run
in *service projects*.

**Live migration** — Compute Engine moving a running instance to another host
during maintenance, without reboot.

**Network tag** — the label firewall rules select targets by, alongside service
accounts.

**Organization policy** — a preventive constraint applied at organization,
folder, or project level.

**Private Google Access** — reaching Google APIs from instances without external
addresses.

**Private Service Connect** — a consumer-placed endpoint inside your VPC for a
Google or published service.

**Private Services Access** — a reserved range peered to Google-managed services
such as Cloud SQL.

**Release channel** — the GKE subscription setting determining how early a
cluster receives new versions.

**RPO and RTO** — permitted data loss and permitted recovery time; together they
select a DR tier.

**Service perimeter** — the VPC Service Controls boundary preventing data
leaving, independent of IAM.

**Sole-tenant node** — a physical server dedicated to your instances, usually
for licensing.

**Spot VM** — deeply discounted reclaimable capacity for interruptible work.

**Workload Identity Federation** — obtaining short-lived Google credentials
without a key file, from GKE or an external identity provider.

# Where to go next

- The exam guide, which is the only authoritative source on scope and the only
  place to confirm the current case studies
- The Google Cloud Architecture Framework, named by exam guide section 6
- Architecture Center reference designs, for worked topologies at more depth
  than this book carries
- Google Cloud Skills Boost, for the hands-on labs this book does not replace
- Release notes for the services in chapters 7 and 8, which move fastest and
  date any book soonest
