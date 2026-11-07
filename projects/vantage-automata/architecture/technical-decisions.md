# Vantage Automata — Initial Technical Decision Record

**Status:** Proposed decisions for review; no implementation stack has been selected or validated.

## Decision 001 — Start with one narrow web workflow

**Context:** The concept could expand into a large automation platform, but that would make the first build difficult to scope and evaluate.

**Decision:** Begin with one user, one instruction-to-proposal flow, one approval decision and one mock action.

**Reasoning:** This tests the central product idea without introducing unnecessary integrations, permissions or operational risk.

**Consequences:** The MVP will not demonstrate broad automation capability, multi-user operation or commercial readiness.

## Decision 002 — Keep approval enforcement in the backend

**Context:** A user interface can display approval controls, but client-side checks alone can be bypassed.

**Decision:** The backend owns task state and independently checks whether a proposal is eligible for approval and execution.

**Reasoning:** Authorisation must not depend only on a button or browser state.

**Consequences:** Backend implementation and API tests must verify rejection, invalid state and duplicate requests.

## Decision 003 — Use a mock action before external integrations

**Context:** Real-world actions can change records, send communications or create other consequences.

**Decision:** The first action handler simulates an operation and has no external side effects.

**Reasoning:** The approval workflow can be evaluated before exposing real systems or data.

**Consequences:** The first demonstration proves workflow behaviour only, not the value or reliability of real integrations.

## Decision 004 — Keep the technology stack open

**Context:** A particular framework or automation platform has not been validated against the final requirements.

**Decision:** Select the stack after confirming developer capacity, hosting, cost, security, maintainability and the needs of the narrow MVP.

**Reasoning:** Technology should follow the requirements rather than dictate them.

**Consequences:** React/Node/Express or an automation platform may be evaluated, but none is represented as a confirmed implementation choice.

## Decision 005 — Treat model output as untrusted

**Context:** AI output may be incomplete, incorrect or inconsistent.

**Decision:** Validate the response against a defined schema and reject invalid output before creating an approval-ready proposal.

**Reasoning:** The model should assist interpretation but should not control application permissions.

**Consequences:** The implementation requires validation logic and tests for malformed responses.

## Revisit these decisions when

- The intended user or first use case changes.
- Real external actions are proposed.
- Authentication or multiple users are introduced.
- The selected model or hosting environment changes.
- Test results reveal a design weakness.
