# Cloud Infrastructure Fundamentals

**Document type:** Technical overview  
**Audience:** Early-career technical researchers and readers exploring cloud systems  
**Scope:** Conceptual introduction; not a deployment guide.

## 1. What cloud infrastructure means

Cloud infrastructure is the collection of computing resources delivered over a network. Instead of owning and maintaining every physical server, an organisation can use services from a cloud provider to run applications, store data, manage networks and monitor systems.

The exact responsibilities depend on the service model and the provider.

## 2. Core building blocks

### Compute

Compute resources run application code and workloads. Examples include virtual machines, containers and serverless functions.

### Storage

Storage services hold files, backups, application objects and other data. Different storage types suit different access patterns and durability needs.

### Networking

Networking connects users, applications and services. It includes virtual networks, routing, firewalls, load balancing and domain-name services.

### Databases

Databases store structured or semi-structured application data. Selection depends on query patterns, consistency needs, scale, operational expertise and data relationships.

### Identity and access management

Identity and access management determines who or what can access a resource and which actions are permitted. Least privilege is a key design principle: grant only the access required for a defined task.

### Monitoring and logging

Monitoring helps operators understand system health and performance. Logs provide records of events that support troubleshooting, security review and operational analysis.

## 3. Common service models

| Model | Provider generally manages | Customer generally manages |
|---|---|---|
| Infrastructure as a Service (IaaS) | Physical infrastructure and virtualisation | Operating systems, applications, data and much of configuration |
| Platform as a Service (PaaS) | Infrastructure and much of the application platform | Application code, data and service configuration |
| Software as a Service (SaaS) | The application and underlying service | Users, data, access settings and use of the service |

The shared-responsibility boundary varies by provider and product. Always consult the provider's current documentation.

## 4. Design considerations

Before selecting a cloud service, consider:
- Workload and performance requirements.
- Availability and recovery objectives.
- Security responsibilities and access controls.
- Data classification, location and retention.
- Cost model and expected usage.
- Monitoring and incident response.
- Backup and recovery.
- Portability and vendor dependency.
- Skills available to operate the environment.

## 5. Security foundations

A sound design should consider identity controls, least privilege, secure secret storage, encryption, network boundaries, patching, logging, backups and a documented response to incidents. The appropriate controls depend on the system's sensitivity and risk.

## 6. Cost awareness

Cloud services are not automatically inexpensive. Costs may arise from compute time, storage, network transfer, managed services, support, monitoring and idle resources. A design should include estimates and a method for reviewing actual usage.

## 7. Research and documentation approach

When documenting a cloud product:
1. Identify the exact service and product version.
2. Consult official provider documentation.
3. State prerequisites and assumptions.
4. Distinguish conceptual explanation from tested instructions.
5. Explain security and cost implications.
6. Record the date reviewed.
7. Recheck links and product behaviour before publication.

This overview introduces the main concepts. It does not describe a specific deployment or claim hands-on configuration.
