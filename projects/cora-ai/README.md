# CORA AI
## Community-Owned Rights & Access — AI-Assisted Consent Toolkit

CORA AI is a small open-source application that records purpose-specific consent, checks whether a requested data use is permitted, and keeps an audit history.

**Principle:** One application. One bounded MVP. AI-assisted operation. Human-owned authority.

**Status:** Early interactive browser demonstrator and FastAPI prototype. Not production-ready.  
**Demo data:** Synthetic records only. No real mental-health or participant data.

## What CORA AI does

It is one reusable web application with a REST API. It can run independently or later be connected to another system by a developer.

The MVP has exactly three core capabilities:

1. **Purpose-specific consent records.** Record whether a participant grants or refuses a defined use, such as research or AI model training. Choices are separate for each purpose. Participants can withdraw a previously granted permission.
2. **Access permission checks.** When a user or connected system requests a data use, the backend checks the current consent record for that exact purpose and returns allow or deny.
3. **Consent and access audit history.** Record consent creation, refusal, withdrawal and permission checks so authorised users can inspect what happened and when.

## Try the interactive prototype

The first browser workspace is served by the FastAPI application.

1. Open the API directory: [implementation/api](implementation/api/).
2. Follow [the local setup guide](implementation/api/README.md).
3. Run `uvicorn app:app --reload` from that directory.
4. Open `http://127.0.0.1:8000/`.

The workspace lets a user select synthetic participant and dataset identifiers, choose Research or AI model training, grant/refuse/withdraw consent, run a permission check and inspect the audit history.

**Current technical boundary:** the API still stores state in memory. Records disappear when the server restarts. SQLite persistence is a planned next milestone, not an implemented feature. The browser interface is not yet deployed as a public hosted demo.

## AI is the operating assistant — not the authority

The planned integrated AI assistant may explain purposes and consent status, guide users through forms, help prepare access requests, check for missing information, explain backend allow/deny reasons and summarise authorised audit events.

AI must not choose or grant consent, withdraw consent on someone's behalf, approve access, override a denial, change a participant's choice or invent policy. The backend permission service applies the rules deterministically. The AI receives only context the current user is authorised to see and can use only a small set of approved application tools.

The AI assistant is **not implemented** in the current browser demonstrator. The core application is designed to work without an AI provider.

## What is included now

- Synthetic participant and dataset inputs.
- Separate Research and AI model training purposes.
- Grant, refuse and withdraw actions.
- Backend permission checks for the exact selected purpose.
- Allow/deny result with reason.
- Chronological in-memory audit history.
- FastAPI endpoints and a browser workspace.
- Automated consent-engine and API tests.
- Setup instructions and contributor guidance.

## What is not included yet

No AI assistant, persistent database, authentication, authorisation, production identity verification, encryption, tamper-resistant audit log, real participant data, real dataset integration, public hosted demo or live SRHIN integration.

No host approval, partnership, endorsement or production deployment is claimed. No mental-health chatbot, screening or diagnosis tool, clinical record system, research-management platform, general-purpose autonomous agent, data marketplace or full data commons is in scope.

## Demonstration workflow

Use fictional participant P001 and dataset D001:

1. P001 grants research permission.
2. P001 refuses AI model training.
3. A research access request is allowed.
4. An AI-training request is denied.
5. P001 withdraws research permission.
6. A new research request is denied.
7. The audit history shows the events in order.

## Application structure

- Browser interface: synthetic consent and permission workflow.
- Consent service: records grant, refusal and withdrawal.
- Permission service: makes the authoritative allow/deny decision.
- Audit service: records consequential events.
- REST API: exposes the prototype operations.
- Future database: planned persistent storage for consent and audit metadata.
- Future AI assistant: bounded explanation and navigation, never the consent authority.

## Proposed future implementation

SQLite persistence, stronger API validation, authentication and authorisation design, independent privacy/security review, and a bounded AI assistant are future work. These are not completed capabilities.

## Project documents

- [Evidence and delivery roadmap](PROJECT_EVIDENCE_AND_DELIVERY_ROADMAP.md)
- [Technical decision log](TECHNICAL_DECISION_LOG.md)
- [Product definition](product/PRODUCT_DEFINITION.md)
- [Locked MVP scope](product/MVP_SCOPE.md)
- [System architecture](architecture/SYSTEM_ARCHITECTURE.md)
- [AI operating model](architecture/AI_OPERATING_MODEL.md)
- [Implementation and handover](product/IMPLEMENTATION_AND_HANDOVER.md)
- [User experience](design/PRODUCT_EXPERIENCE.md)
- [Screen layout](design/DASHBOARD_LAYOUT.md)
- [Contributor guide](CONTRIBUTING.md)

## Verification

The GitHub Actions run for the interactive workspace branch passed:
- 8 deterministic consent-engine unit tests.
- Synthetic demonstration execution.
- 7 API tests, including a check that the browser workspace is served.

See [the implementation test report](implementation/TEST_RESULTS.md) for earlier evidence and limitations. The interactive branch's current CI run is linked from [pull request #6](https://github.com/preciousapiridibagha1-star/technical-writing-research-and-documentation-/pull/6).

## Handover and maintenance boundary

The deliverable is a documented open-source MVP, not indefinite maintenance. The repository will explain how to run, test, configure and integrate it. After handover, adopters may fork, host, extend or integrate it themselves. Production operation and future feature development belong to the adopting organisation and its technical maintainers.

## Licence

The CORA AI project folder includes the Mozilla Public License 2.0. It does not mean Mozilla Foundation owns, sponsors or endorses this project.

**Product boundary:** Build the smallest complete tool that demonstrates purpose-specific consent, withdrawal, access decisions and an audit trail—with AI assisting operation, never replacing consent or human authority.
