# CORA AI — Mozilla Fellowship Evidence & Delivery Roadmap

**Purpose:** Convert the existing CORA AI design specification into inspectable, honest evidence of problem analysis, technical reasoning, execution, learning and public-benefit intent.

**Current stage:** Specification and architecture documentation. The working application is not yet implemented. No community validation, deployment, host endorsement or integration is claimed.

## Evidence strategy

We will use three connected frameworks:

### Project qualities
- **Passion:** sustained exploration and documented learning.
- **Leadership:** project ownership, decisions, coordination and follow-through.
- **Creativity:** a carefully bounded design that addresses a defined gap.
- **Technical evidence:** implementation, tests, code review and reproducible demonstration.
- **Community impact:** co-design and feedback pathway; impact is not claimed before it is demonstrated.
- **Persistence:** iterations, setbacks, corrections and lessons recorded transparently.

### Evidence formula
**Claim → Artifact → Explanation → Validation**

For each claim, identify a visible artifact, explain the reasoning, and show how it was checked. Claims must not exceed what the artifacts demonstrate.

### Execution assessment
**Experience → Capability → Feasibility → Execution Plan**

Use prior work, current skills, scope, dependencies, resources and milestones to make delivery credible. Identify support or review needed rather than concealing gaps.

## Current evidence inventory

| Area | Evidence currently in repository | Status / gap |
|---|---|---|
| Problem framing | Product definition and architecture | Documented; community input not yet gathered |
| Product scope | Locked MVP scope | Documented; implementation not yet tested |
| System design | Architecture and AI operating model | Documented; requires technical review |
| Consent rules | Defined grant/refusal/withdrawal and purpose matching | Specified; code and tests needed |
| AI boundaries | Bounded assistant; deterministic permission service | Specified; implementation and adversarial tests needed |
| Execution | Implementation and handover plan | Planned; no functional milestone yet |
| Community engagement | Proposed co-design pathway | Not yet conducted |
| Validation | Acceptance criteria | Test evidence not yet produced |
| Public benefit | Open-source intention and project rationale | Pathway proposed; outcomes not yet demonstrated |

## Build roadmap

### Milestone 0 — Rule freeze and project setup
- Confirm purpose keys, statuses, roles, resource and participant identifiers.
- Establish repository layout and development instructions.
- Create a traceable acceptance-test list.
- Keep demo data synthetic.

**Exit evidence:** decision log, rules specification, repository setup instructions.

### Milestone 1 — Deterministic consent and permission core
- Implement consent grant/refusal records.
- Implement withdrawal.
- Implement purpose-specific permission checks.
- Implement default-deny behaviour.
- Record auditable events.

**Exit evidence:** source code and automated tests for the rules.

### Milestone 2 — Testable API and demo workflow
- Expose consent and permission operations through the API.
- Run the P001/D001 synthetic scenario.
- Record allowed and denied results.
- Test missing, mismatched and withdrawn consent.

**Exit evidence:** API examples, test results, reproducible demonstration.

### Milestone 3 — Minimal interface
- Implement participant consent/status views.
- Implement access-request and decision views.
- Implement administrator audit view with demo data.

**Exit evidence:** screenshots or short recording, usability notes, code.

### Milestone 4 — Bounded AI operating interface
- Add a server-side configurable AI adapter.
- Allow-list tools and validate tool calls on the backend.
- Require explicit confirmation and backend validation for consequential actions.
- Prove that AI cannot override permission decisions.
- Prove core functionality remains available without AI.

**Exit evidence:** implementation, tests, recorded demonstration and boundary documentation.

### Milestone 5 — Review, documentation and handover
- Review code and security assumptions with a qualified reviewer where available.
- Document limitations and unresolved risks.
- Publish setup, API, test and handover documentation.
- Make clear that this synthetic demonstrator is not production-ready.

**Exit evidence:** review notes, completed documentation and release checklist.

## Evidence log

For each development session, record:

- **Date:**
- **Goal:**
- **Work completed:**
- **Artifact / commit / link:**
- **Reasoning and decisions:**
- **Tests or validation performed:**
- **Result:**
- **Failure or limitation:**
- **Next action:**

## Community engagement and impact

The project must not presume that its design reflects the preferences of affected communities. A future engagement plan should identify participants and community health workers in consultation with an appropriate host or community partner, use accessible consent and participation practices, and document feedback and changes. Do not claim engagement or approval until it has occurred.

## Honest project status

- This repository currently contains a specification and plan, not a completed application.
- The demonstrator will use synthetic data only.
- No partnership, endorsement or integration with SRHIN is claimed.
- The project is not a consent certification, legal compliance guarantee or production access-control solution.
- An access-check API does not control datasets unless the adopting system connects and enforces it on every relevant release path.
