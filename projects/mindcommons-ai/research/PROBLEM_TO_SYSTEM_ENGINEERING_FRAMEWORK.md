# Problem-to-System Engineering Framework

**Opportunity context:** Mozilla Foundation Fellowship 2027–2028 — Track I Embedded, SRHIN  
**Status:** Proposed engineering approach for fellowship preparation. It is self-directed work, not an SRHIN-approved process, confirmed set of requirements, commissioned design or claim of implementation.  
**Relationship to the research method:** This framework sits underneath and operationalises the existing [six-stage Problem Discovery & Co-Design Framework](PROBLEM_DISCOVERY_AND_CO_DESIGN_FRAMEWORK.md). It does not replace that methodology or assume that every validated problem requires software.

---

## 1. Purpose

The research methodology helps us understand the host's challenge, investigate the current situation, diagnose root causes, compare interventions, implement what is justified and evaluate the result.

The Problem-to-System Engineering Framework explains how we move from that evidence into a practical intervention that can work in a real organisational and community environment.

**The central question is not, “What website should we build?” It is:**

> What capability do the organisation and affected communities need, what prevents them from exercising that capability today, and what proportionate intervention can reliably provide it?

A build may be software, an internal system, an AI-enabled workflow, an integration, an API, a data structure, a governance mechanism, a documented operating process, training, or a combination. It may also be the improvement of an existing system—or a justified decision not to build anything.

## 2. How the two frameworks fit together

The six-stage research method is the outer problem-solving process. Engineering activities sit within the relevant stages and become more detailed as evidence and authorisation allow.

| Research methodology | Engineering activity underneath it | Typical engineering output |
|---|---|---|
| 1. Problem understanding | Identify users, goals, context, boundaries and decision authorities | Problem and context brief |
| 2. Investigation | Map current systems, workflows, roles, data, tools and hand-offs | Current-state system map |
| 3. Root-cause diagnosis | Translate evidence into needs, constraints and testable requirements | Validated problem and requirements baseline |
| 4. Solution architecture | Compare build, buy, adapt, integrate, process and non-technical options | Options appraisal and provisional architecture |
| 5. Engineering and implementation | Design, build, configure, integrate, test, document and prepare operations | Working intervention and implementation record |
| 6. Evaluation and iteration | Test against acceptance criteria, learn from use and improve or stop | Evaluation and improvement report |

The stages are iterative. New technical findings, user feedback or safety concerns may send the work back to problem discovery or requirements.

## 3. Engineering workflow

### A. Understand the operating environment

Before selecting technology, establish:

- Who experiences the problem and who will use or be affected by the intervention.
- What people are trying to achieve and what currently prevents them.
- Which decisions belong to the host, community representatives, professional staff, ethics bodies or other authorised actors.
- What existing systems, documents, policies, tools and manual workarounds are already in use.
- What must remain unchanged, what can be improved and what is outside the fellowship scope.
- The practical operating context: connectivity, devices, language, accessibility, staff capacity, budget and maintenance.

**Output:** An evidence-linked context map. Distinguish what has been observed, what stakeholders have confirmed, what public sources say and what remains an assumption.

### B. Map the current state

Map the process as it actually operates—not only as a policy says it should operate.

Inspect, where authorised:

- People, roles, responsibilities and decision points.
- Inputs, outputs, records and hand-offs.
- Existing software, spreadsheets, forms, APIs and communication channels.
- Data movement, storage, access, retention and deletion.
- Manual work, duplication, bottlenecks, exceptions and failure points.
- External organisations, vendors and dependencies.
- Existing controls, audit trails and escalation routes.

Use a process map, system-context diagram, data-flow diagram or service blueprint when it helps explain the situation. Do not create diagrams for appearance alone.

**Output:** Current-state map with evidence references, known gaps, effective existing practices and unanswered questions.

### C. Define requirements

Requirements should come from validated needs and authorised stakeholders, not from a preferred technology.

**Functional requirements** describe what the intervention must do. Examples may include recording a decision, routing a request, notifying an authorised reviewer or producing an auditable status report—but only where discovery establishes that the capability is needed.

**Non-functional requirements** describe how it must operate:

- **Privacy and data minimisation:** collect and expose only what is necessary.
- **Security:** authentication, authorisation, least privilege, secure configuration and appropriate protection of records.
- **Reliability:** predictable behaviour, recoverability and clear handling of failures.
- **Usability and accessibility:** understandable language, accessible interaction and suitability for intended users.
- **Interoperability:** appropriate exchange with existing tools and formats, without unnecessary integration.
- **Maintainability:** clear ownership, documentation, support arrangements and manageable operating costs.
- **Auditability:** traceable actions and decisions where required, without creating excessive surveillance.
- **Portability and sustainability:** avoid avoidable lock-in and ensure the host can continue or responsibly retire the intervention.
- **Safety and human oversight:** consequential decisions remain with the authorised people and processes.

For each requirement, record its source, rationale, priority, acceptance test, owner and status. Mark requirements as proposed until the relevant stakeholders validate them.

**Output:** Requirements register and acceptance criteria.

### D. Explore solution options before choosing an architecture

Compare options against the validated requirements. Possible forms include:

| Intervention form | When it may be appropriate |
|---|---|
| Improve an existing system | The capability already exists but is difficult to use, incomplete or poorly connected |
| Internal organisational tool | Staff or authorised stewards need a repeatable operational capability |
| Workflow or process redesign | The main issue is unclear roles, hand-offs, approvals or follow-up |
| AI assistant or agent | Language-heavy support or information navigation is useful, bounded and safe; not for delegated authority |
| API or integration | Existing systems need a controlled exchange of information |
| Data model or register | Information needs a consistent, structured and traceable representation |
| Web application or interface | Users genuinely need an interactive interface for a validated task |
| Policy, governance or training intervention | The root cause is primarily institutional, legal, procedural or capacity-related |
| Hybrid intervention | The problem crosses people, processes, governance and technology |
| No-build recommendation | Existing arrangements are adequate, or a new intervention would add risk or burden |

Assess each option for usefulness, community agency, feasibility, privacy, security, accessibility, cost, maintenance, integration burden, operational ownership and unintended consequences.

**Output:** Options comparison with a reasoned recommendation—or a documented decision not to build.

### E. Design the target system

Only after requirements and an intervention direction are validated should a target design be developed.

Depending on the intervention, design may include:

- System context and component boundaries.
- User roles, permissions and decision authority.
- Process and interaction flows.
- Data entities, relationships and lifecycle.
- Data-flow and trust-boundary diagrams.
- Interfaces, APIs and integration contracts.
- Human review and escalation points.
- Logging, monitoring and audit requirements.
- Error states, misuse cases and recovery behaviour.
- Deployment environment, dependencies and operating costs.

Architecture should be proportionate. A small, well-documented workflow may be more appropriate than a complex platform. Avoid unnecessary services, sensitive-data duplication and technology choices that the host cannot maintain.

**Output:** Architecture decision record, diagrams where useful, data-flow description and implementation plan.

### F. Build, configure or implement

Implementation follows the approved scope and access conditions.

- Start with the smallest useful increment.
- Use synthetic data for early demonstrations and tests.
- Use real or sensitive data only when the host has authorised the exact access and processing, and all required privacy, security, ethics and legal approvals are in place.
- Keep secrets and credentials out of source control.
- Use version control and readable project structure.
- Separate configuration from code where appropriate.
- Document dependencies, setup, operation and known limitations.
- Integrate with existing systems only with permission and appropriate review.
- Keep human decision-makers responsible for consequential actions.

The intervention may be technical or non-technical. A working operating procedure, revised governance workflow or training package can be a legitimate implementation when that is what the evidence supports.

**Output:** A reproducible implementation, demonstration or documented intervention, with its actual status stated accurately.

### G. Test, evaluate and improve

Testing must match the intervention and its risks. Possible checks include:

- Functional tests against requirements.
- Unit and integration tests for software.
- Permission and access-control tests.
- Data validation and error-handling tests.
- Usability and accessibility checks with appropriate participants.
- Reliability and recovery tests.
- Privacy and security review by suitably qualified people.
- Workflow walkthroughs and operational acceptance.
- Evaluation of user burden, usefulness and unintended effects.

Record test environment, test data, expected result, actual result, defects, limitations and retest status. Passing a local test suite does not establish production readiness, security certification or real-world impact.

**Output:** Test report, acceptance record, issue log and prioritised improvements.

### H. Prepare for operation and handover

A prototype is not automatically an operational system. Before any pilot or handover, clarify:

- Who owns the intervention and its decisions.
- Who administers users, permissions and configuration.
- Who responds to incidents and support requests.
- Where it runs, who pays for hosting and ongoing services, and what happens if funding ends.
- How backups, retention, deletion and recovery are handled.
- What training and documentation users need.
- How changes are approved and recorded.
- How the system can be maintained, transferred or retired responsibly.

**Output:** Operational guide, ownership and support plan, training materials and handover record, where implementation reaches that stage.

## 4. Engineering principles and safeguards

1. **Problem before product.** Do not select a website, agent or platform before validating the need.
2. **Preserve what works.** Understand existing tools and governance before proposing replacements.
3. **Community authority matters.** Technical design must respect legitimate community decision-making and lived-experience expertise.
4. **Least data, least privilege.** Minimise sensitive data and restrict access according to role and purpose.
5. **Human accountability.** AI may assist with explanation, navigation, drafting or summarisation, but it must not silently make consequential decisions or override authorised people.
6. **Security and safety from the beginning.** Treat threat, misuse, privacy and failure analysis as design work, not final decoration.
7. **Build for the operating context.** Connectivity, language, accessibility, staff capacity, costs and maintenance affect whether a system is genuinely useful.
8. **Make evidence inspectable.** Requirements, architecture decisions, tests, limitations and changes should be documented.
9. **Prefer the smallest maintainable intervention.** Complexity must earn its place.
10. **Be willing not to build.** If an existing process is adequate or a technical intervention creates more harm or burden than value, document that conclusion.

## 5. Demonstrating engineering ability before host engagement

We should demonstrate the ability to reason about and implement systems without presenting a self-directed demonstration as the solution SRHIN needs.

### A. System-engineering capability document

This framework is the foundation. Supporting evidence can include requirements examples, architecture decisions, data-flow diagrams, security and human-oversight considerations, testing approach and deployment/handover thinking.

### B. Small technical demonstration

Prepare a self-contained proof of concept using synthetic data. Its purpose is to demonstrate the translation of a governance or organisational problem into a working technical workflow.

The demonstration's use case must be selected only after comparing the strongest evidence-backed opportunities in the research. It must be clearly labelled as an independent technical demonstration—not an SRHIN-approved product, a host requirement, a production system or a community-validated solution.

### C. Host discovery and co-design toolkit

The [Problem Discovery & Co-Design Framework](PROBLEM_DISCOVERY_AND_CO_DESIGN_FRAMEWORK.md) is the starting point. It can be extended with practical templates for interviews, workflow mapping, evidence capture, requirements validation and decision records. Actual host or community engagement must only be claimed after it has taken place with appropriate authorisation.

## 6. Engineering evidence structure in this portfolio

The Mozilla/SRHIN preparation area will make the progression from research to implementation visible:

| Portfolio item | Purpose | Current status |
|---|---|---|
| [Problem Discovery & Co-Design Framework](PROBLEM_DISCOVERY_AND_CO_DESIGN_FRAMEWORK.md) | Research stages, stakeholder discovery, evidence safeguards and validation | Created; proposed self-directed framework |
| **Problem-to-System Engineering Framework** | Method for translating validated needs into proportionate interventions | Created; proposed self-directed framework |
| **System Architecture and Design Methodology** | Detailed architecture decisions, diagrams, data flows and design records | Planned; not yet created |
| **Prototype and Implementation Evidence** | Source code, setup instructions, demonstrations and implementation notes | To be developed after selecting a justified demonstration |
| **Testing and Evaluation Reports** | Test results, acceptance evidence, limitations and iteration | To be developed when an implementation exists |
| **Host Validation and Requirements Record** | Authorised host-confirmed needs, requirements and decisions | Only after authorised SRHIN engagement |

This structure is a roadmap, not a claim that all listed artefacts or activities already exist.

## 7. The capabilities this work is intended to demonstrate

- **Researcher:** investigates complex problems, evaluates evidence and distinguishes root causes from assumptions.
- **Systems thinker:** understands people, institutions, governance, processes, data and technology as a connected environment.
- **Builder:** translates validated requirements into working technical or non-technical interventions and evaluates their results.

These are the capabilities this preparation is designed to develop and evidence. The portfolio must show the actual work completed at each stage rather than claim expertise or outcomes that have not been demonstrated.

## 8. Relationship to MindCommons

MindCommons AI is one provisional design hypothesis arising from the public-source assessment. It is not the predetermined destination of this framework.

If authorised discovery establishes that its proposed accountability workflow is useful and not already adequately supported, it may be refined and tested. If the evidence points to a different system, an improvement to an existing tool, a governance or process intervention, or no new build, the work should follow that evidence.

**Working principle:** Research to understand. Diagnose to focus. Engineer to serve the validated need. Test to learn. Hand over responsibly.
