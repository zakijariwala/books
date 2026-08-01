# Networking and identity

Target chapters: ch02 (hierarchy and identity), ch03 (networking).

Source: `gcp-pca-prep/services/vpc/readme.md` and `services/iam/readme.md`. The
author came to GCP from AWS, so the framing already matches the book's reader.
All `UNVERIFIED` until checked against current docs.

## The private-access trio

The highest-value item found in either repo. Three services with confusingly
similar names, all commonly used, all exam-tested.

| Service | What it does | Closest AWS idea |
| --- | --- | --- |
| Private Google Access | Lets a VM with no external IP reach Google APIs at their public endpoints over Google's backbone, without an internet gateway or NAT | No clean equivalent |
| Private Service Connect | Exposes a service in one VPC to consumers, across VPCs, or lets you consume Google APIs through a regional endpoint you control | VPC endpoints, roughly |
| Private Services Access | Reserves a CIDR block for Google-managed services, creating a Google-owned service VPC peered to yours | No clean equivalent |

Two consequences worth teaching rather than just naming:

**Private Service Connect can enforce regionality.** Resources in one region
consume APIs via an endpoint in that same region. That makes it a data-residency
control, not only a connectivity one. Ties directly to case study 1.

**Private Services Access peering only shares subnet routes by default.** If
on-prem or other networks need to reach those private services, the routes must
exist in your VPC *and* be exported to the service VPC. This is a classic
misconfiguration and exactly the kind of thing an exam scenario hides in one
sentence.

## VPC differences from AWS

For the cross-cloud reader these are the deltas that matter, not the renames.

- **Peering is non-transitive**, same as AWS. Hub-and-spoke spokes cannot reach
  each other through the hub. Needs Cloud Router or an appliance
- **Network tags** replace security groups. Rules attach to tags, instances
  carry tags
- **Shared VPC has no AWS equivalent.** Compute in one project sits inside a
  network owned by another project. One host project can carry networking for
  an entire org. This is the intended answer whenever separate teams need to
  communicate over private addressing, and it beats peering for that case
- **VPC Service Controls** draw security perimeters around resources within and
  between projects. Data-exfiltration control, distinct from firewalling

Verify one thing I did not see stated in the source and that trips every AWS
architect: GCP VPCs are **global**, with regional subnets. AWS VPCs are
regional. Confirm and teach early in ch03.

## IAM

- **Permissions never attach to principals directly.** Only roles do. Basic
  roles, predefined roles, or custom roles. The AWS mental model of attaching a
  policy to a principal does not carry over. Flag explicitly in ch02
- IAM reaches down to Kubernetes API objects in GKE, not just to GCP services
- Control surfaces available: who (principal), what (service), which (resource),
  and with advanced configuration how (request origin, auth method)

### Workload Identity

GKE-specific mapping between a Kubernetes service account and a Google service
account. Pods then make identity claims as the Google service account, so they
reach GCP APIs with no credential in the image, no key file, no vault fetch.

This is the correct answer to "how should pods authenticate to GCP services" and
the wrong answers are all credential-distribution schemes. Strong ch05 content
and a likely exam item shape.

### Gaps in the source

The repo's IAM notes leave Service Accounts, Identity Federation, and Security
Perimeters as empty headings. Nothing to extract. Fetch from documentation.

Organization and folder hierarchy is barely covered in either repo, despite
being the construct with no AWS or Azure equivalent and the reason ch02 sits
early. This is the largest documentation gap for the chapters I care most about.
