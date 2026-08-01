# Exam-day playbook

The exam runs two hours and carries 50 to 60 multiple-choice and multiple-select
questions, of which 20 to 30 per cent attach to two case studies shown on a
split screen. It costs $200 and the certification is valid for two years. The
renewal exam is shorter — around an hour and roughly 25 questions at about half
the cost — and it weights whatever Google has added since, which currently means
generative AI. Confirm all of this on the certification page before you book;
these figures move.

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
