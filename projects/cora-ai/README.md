# CORA AI
## Community-Owned Rights & Access — AI-Assisted Consent Toolkit

CORA AI is a small open-source application that records purpose-specific consent, checks whether a requested data use is permitted, and keeps an audit history.

**Principle:** One application. One bounded MVP. AI-assisted operation. Human-owned authority.

**Status:** MVP specification and implementation plan; working application not yet claimed.  
**Demonstrator target:** 28 November 2026.  
**Demo data:** Synthetic records only. No real mental-health or participant data.

## What CORA AI does

It is one reusable web application with a REST API. It can run independently or later be connected to another system by a developer.

The MVP has exactly three capabilities:

1. **Purpose-specific consent records.** Record whether a participant grants or refuses a defined use, such as research or AI model training. Choices are separate for each purpose. Participants can withdraw a previously granted permission.
2. **Access permission checks.** When a user or connected system requests a data use, the backend checks the current consent record for that exact purpose and returns allow or deny.
3. **Consent and access audit history.** Record consent creation, refusal, withdrawal, access requests, approvals and denials so authorised users can inspect what happened and when.

## AI is the operating assistant — not the authority

One integrated AI assistant is the main conversational guide inside the application. It explains purposes and consent status, guides users through forms, helps prepare access requests, checks for missing information, explains backend allow/deny reasons and summarises authorised audit events.

AI does not choose or grant consent, withdraw consent on someone's behalf, approve access, override a denial, change a participant's choice or invent policy. The backend permission service applies the rules deterministically. The AI receives only context the current user is authorised to see and can use only a small set of approved application tools.

If the AI provider is unavailable or no API key is configured, the core application still works through ordinary forms and API endpoints.

## What is included

- Participant consent screen with separate purposes.
- Grant, refuse and withdraw actions.
- Administrator view of pseudonymous demo participants and consent status.
- Access-request form.
- Backend permission check for the exact requested purpose.
- Allow/deny result with reason.
- Chronological audit history.
- One bounded, permission-aware AI assistant.
- Small REST API for future integration.
- Synthetic sample data, automated tests and setup documentation.

## What is excluded

No mental-health chatbot, screening or diagnosis tool, clinical record system, research-management platform, general-purpose autonomous agent, data marketplace or full data commons. No real participant data, production identity verification, benefit payments, blockchain, federated learning, differential privacy, advanced cryptography, mobile-native app, multiple AI agents or live SRHIN integration.

No host approval, partnership, endorsement or production deployment is claimed.

## Demonstration workflow

Use fictional participant P001 and dataset D001:

1. P001 grants research permission.
2. P001 refuses AI model training.
3. A research access request is allowed.
4. An AI-training request is denied.
5. P001 withdraws research permission.
6. A new research request is denied.
7. The audit history shows all consent and access events in order.

## Application structure

- Web interface: participant, requester and administrator screens.
- AI assistant: explains and guides the workflow through approved tools.
- Consent service: records grant, refusal and withdrawal.
- Permission service: makes the authoritative allow/deny decision.
- Audit service: records consequential events.
- Database: stores minimum pseudonymous consent, request and audit metadata.
- REST API: allows another system's trusted backend to submit a permission check.

## Proposed implementation

React frontend; Python/FastAPI backend; SQLite local demo database; pytest automated tests; one configurable AI model provider accessed through a server-side adapter. These are proposed choices, not completed implementation.

## Build sequence

1. Freeze data model, purposes and permission rules.
2. Build consent and withdrawal backend operations.
3. Build access-check service and audit events.
4. Add automated tests.
5. Build the participant, requester and administrator screens.
6. Add the bounded AI assistant.
7. Run the synthetic demonstration end to end.
8. Publish setup, API, limitations and handover documentation.

The first demonstrator is local and synthetic-data-only. It is not safe for real mental-health data or production use until authentication, authorisation, secure hosting, secrets management, database hardening, backups, monitoring and independent security/privacy review are completed.

## Evidence and delivery

- [Evidence and delivery roadmap](PROJECT_EVIDENCE_AND_DELIVERY_ROADMAP.md): project qualities, evidence inventory, milestones and honest status.
- [Technical decision log](TECHNICAL_DECISION_LOG.md): documented decisions, rationale and validation requirements.

## Handover and maintenance boundary

The deliverable is a documented open-source MVP, not indefinite maintenance. The repository will explain how to run, test, configure and integrate it. After handover, adopters may fork, host, extend or integrate it themselves. Production operation and future feature development belong to the adopting organisation and its technical maintainers.

## Licence intention

The project includes the full Mozilla Public License 2.0 text in [LICENSE](LICENSE). The licence applies to the CORA AI project files in this folder, not automatically to the rest of the portfolio repository. MPL-2.0 does not mean Mozilla Foundation owns, sponsors or endorses this project.

## Project documents

- Product definition: product/PRODUCT_DEFINITION.md
- Locked MVP scope: product/MVP_SCOPE.md
- System architecture: architecture/SYSTEM_ARCHITECTURE.md
- AI operating model: architecture/AI_OPERATING_MODEL.md
- Implementation and handover: product/IMPLEMENTATION_AND_HANDOVER.md
- User experience: design/PRODUCT_EXPERIENCE.md
- Screen layout: design/DASHBOARD_LAYOUT.md

**Product boundary:** Build the smallest complete tool that proves purpose-specific consent, withdrawal, access enforcement and an audit trail—with AI assisting operation, never replacing consent or human authority.

## Working prototype

The first runnable implementation milestone is now in [implementation/](implementation/).
It contains the deterministic consent engine, a synthetic demonstration, automated
test cases and setup instructions. It is an early in-memory prototype, not a
production application; see the implementation README for its limitations and
the exact evidence status.
