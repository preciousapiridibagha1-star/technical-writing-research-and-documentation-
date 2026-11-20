# CORA AI — Technical Decision Log

This log records important project decisions, their rationale, trade-offs and validation status. Add entries as decisions are made; do not retrospectively invent dates or test results.

## Entry template

### DEC-XXX — [Decision title]
- **Date:** YYYY-MM-DD
- **Status:** Proposed / Accepted / Revisited
- **Context/problem:**
- **Options considered:**
- **Decision:**
- **Reasoning/trade-offs:**
- **Validation needed or performed:**
- **Related files/issues/commit:**

---

## DEC-001 — Synthetic data for the demonstrator
- **Status:** Accepted
- **Context/problem:** The project concerns sensitive data-use and consent concepts, but a prototype should not require real participant or mental-health information.
- **Decision:** Use fictional participants and synthetic datasets for the demonstrator.
- **Reasoning/trade-offs:** This reduces exposure of personal information while allowing the permission workflow to be tested. It does not make the prototype production-safe.
- **Validation needed or performed:** Confirm all sample data is fictional; inspect the repository before each release.

## DEC-002 — Deterministic permission authority
- **Status:** Accepted
- **Context/problem:** A language model must not be the authority deciding whether a data use is permitted.
- **Decision:** The backend permission service returns ALLOW or DENY based on the exact purpose and current consent state. AI can explain and guide but cannot override the decision.
- **Reasoning/trade-offs:** Deterministic rules make the core decision testable and independent of model output. The API still must be integrated into every relevant data-release path to enforce decisions.
- **Validation needed or performed:** Implement and test default-deny, mismatched purpose, refusal and withdrawal cases.

## DEC-003 — Small bounded MVP
- **Status:** Accepted
- **Context/problem:** A broad data commons platform would exceed the initial demonstrator's scope and complicate delivery.
- **Decision:** Limit the first demonstrator to consent records, permission checks and audit history, with a bounded assistant.
- **Reasoning/trade-offs:** A small end-to-end workflow is easier to test and demonstrate, but does not address every governance, benefit-sharing or infrastructure challenge.
- **Validation needed or performed:** Track scope changes; reject or defer features that do not serve the acceptance criteria.
