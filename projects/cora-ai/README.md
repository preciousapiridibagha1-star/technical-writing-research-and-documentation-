# CORA AI
## Community-Owned Rights & Access — AI-Assisted Consent Toolkit

CORA AI is a small open-source application that records purpose-specific consent, checks whether a requested data use is permitted, and keeps an audit history.

**Principle:** One application. One bounded MVP. One integrated conversational assistant. Human-owned authority.

**Assistant upgrade:** The existing MVP is being enhanced with a guided conversational consent journey. This is an additive interface improvement, not a replacement or expansion of the locked MVP capabilities.

**Status:** Interactive browser demonstrator with SQLite-backed deterministic consent engine; free public-hosting configuration prepared, deployment not yet verified. Not production-ready.  
**Demo data:** Synthetic records only. No real mental-health or participant data.

## What CORA AI does

1. **Purpose-specific consent records.** Record whether a participant grants or refuses a defined use, such as research or AI model training. Choices are separate for each purpose. Participants can withdraw a previously granted permission.
2. **Access permission checks.** The backend checks the current consent record for the exact participant, dataset and purpose, returning deterministic ALLOW or DENY.
3. **Audit history.** Consent changes and permission checks are recorded in SQLite and can be inspected through the application.

## Try it locally

From `projects/cora-ai/implementation/api/`:

```bash
python -m venv .venv
pip install -r requirements.txt
uvicorn app:app --reload
```

Open `http://127.0.0.1:8000/`. The app stores records in
`api/data/cora_demo.sqlite3` by default. Set `CORA_DB_PATH` to use another
writable SQLite file. See [the API and deployment guide](implementation/api/README.md).

## Public demonstration deployment

A Render Blueprint is included in the repository root as `render.yaml`.
It configures a persistent disk for the SQLite database. Deploying it requires
a Render account and creates paid resources (Starter web service plus a 1 GB
persistent disk). Review the current price and approve the cost before creating
the service. A public deployment is not claimed until a live service URL has
been created and checked.

The public demo is a shared writable sandbox. Use fictional IDs and synthetic
data only; visitors can change records in the shared demonstration database.

## The integrated assistant

One assistant is the conversational operating interface across CORA. It helps participants understand each data-use purpose, navigate the platform, review consent status, prepare requests and understand permission and audit outcomes. For consent, it should explain the specific purpose and relevant consequences in plain language, check that the person has had an opportunity to ask questions, present the available choices, and request a clear final confirmation.

The participant—not the model—makes the decision. Only an explicit, authenticated participant action, validated by the backend, may create or change a consent record. The assistant cannot choose for the participant, grant or withdraw consent autonomously, approve access, override DENY or rewrite policy. If the user's intention is unclear, the assistant must pause and ask rather than infer consent.

The browser demonstration remains offline unless connected to a deployed CORA API. The FastAPI backend now includes an optional Gemini explanation endpoint (`POST /assistant/chat`), configured only through the server-side `GEMINI_API_KEY` environment secret. The provider key must never be embedded in the public GitHub Pages JavaScript. Any guided consent interaction in the browser demo uses synthetic records and browser-local state; it is not a secure or shared consent service. A production AI integration, authentication, role enforcement and privacy/security controls remain unimplemented.

## Current capabilities

- Synthetic participant and dataset inputs.
- Research and AI model training purposes.
- Grant, refuse and withdraw actions.
- Deterministic exact-purpose permission checks.
- ALLOW/DENY result with reason.
- SQLite persistence for consent records and audit events.
- FastAPI endpoints and responsive browser workspace.
- Automated tests for consent rules, API behaviour and database reopen persistence.

## Not implemented

No production authentication, authorisation, encryption, tamper-resistant
audit log, automated backups, real participant data, real dataset integration,
production monitoring or live SRHIN integration. The Gemini endpoint is not yet deployed or connected to the GitHub Pages chat UI.

No host approval, partnership, endorsement or production deployment is claimed.
No mental-health chatbot, screening or diagnosis tool, clinical record system,
research-management platform, data marketplace or full data commons is in scope.

## Demonstration workflow

Use fictional participant P001 and dataset D001:

1. P001 grants research permission.
2. P001 refuses AI model training.
3. A research access check is allowed.
4. An AI-training access check is denied.
5. P001 withdraws research permission.
6. A new research access check is denied.
7. The audit history shows the events in order.

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

The current SQLite persistence branch adds tests for database recovery after
restart. Exact CI outcomes will be recorded after the pull request workflow
completes. Earlier interactive UI verification passed 8 consent-engine tests,
the synthetic demo and 7 API tests; see [the previous interactive pull request](https://github.com/preciousapiridibagha1-star/technical-writing-research-and-documentation-/pull/6).

## Handover and maintenance boundary

The deliverable is a documented open-source MVP, not indefinite maintenance.
Adopters may fork, host, extend or integrate it. Production operation and future
feature development belong to the adopting organisation and its maintainers.

## Licence

The CORA AI project folder includes the Mozilla Public License 2.0. It does not
mean Mozilla Foundation owns, sponsors or endorses this project.

**Product boundary:** demonstrate purpose-specific consent, withdrawal,
deterministic access decisions and an audit trail—with AI assisting operation,
never replacing consent or human authority.
