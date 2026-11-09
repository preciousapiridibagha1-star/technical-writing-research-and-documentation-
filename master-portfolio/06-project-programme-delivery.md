# 6. Project & Programme Delivery

## Evidence project: Delivering a bounded Vantage Automata prototype

**Status:** Local proof of concept committed; nine unit tests passed on 9 November 2026.  
**Purpose:** Demonstrate how a broad system concept was reduced to a small, testable delivery increment with observable acceptance evidence.

### Delivery objective

Deliver one low-risk workflow: instruction → validation → proposal → human decision → mock action or safe stop → local audit record.

### Scope delivered

- One reminder-shaped instruction.
- Input validation and a restricted action type.
- Structured proposal with a unique identifier.
- Approval bound to the fingerprint of the exact proposal shown.
- Duplicate-attempt protection within one running process.
- Mock action only.
- Safe failure response without automatic retry.
- Local JSON Lines audit record.

### Delivery and verification record

| Evidence item | Record |
|---|---|
| Repository location | `projects/vantage-automata/prototype/` |
| Main implementation | `vantage_mvp.py` |
| Automated tests | `test_vantage_mvp.py` |
| User-facing explanation | `README.md` |
| Delivery status | Source, tests and run guide committed to the portfolio repository |
| Test command | `python -m unittest -v` |
| Test result | **9 tests passed; 0 failures; 0 errors** |
| Verification date | 9 November 2026 |
| Verification method | Retrieved exact committed files from GitHub and ran them in an isolated Python 3 directory |
| CI status | No CI run is claimed |
| Deployment status | Not deployed; local mock only |

### Acceptance criteria and outcomes

| Acceptance check | Outcome |
|---|---|
| Reject empty, overlong and out-of-scope instructions | Covered by unit tests |
| Reject an unauthorised action type | Covered by unit test |
| Reject approval if proposal content changes after review | Covered by unit test |
| Reject approval referring to another proposal ID | Covered by unit test |
| Block a second execution attempt | Covered by unit test |
| On action failure, stop without automatic retry | Covered by unit test |
| Keep the action mocked and avoid external services | Verified by code inspection; no external call is present in the prototype |

### Before → after

**Before:** “Build Vantage Automata with AI agents and business integrations.”

**After:** “Deliver one local approval journey with validation, exact-content approval, duplicate-attempt protection, safe failure and a local audit record.” The revised scope is observable and testable.

### Delivery decisions and limitations

- Deterministic proposal generation was retained so the control flow could be tested without model variability.
- The action remains a mock; no reminder is actually created.
- Duplicate protection is in-memory and does not persist across restarts.
- The local audit file is not tamper-proof.
- Authentication, multi-user permissions, durable storage, deployment, monitoring and AI integration remain outside this increment.
- The nine passing unit tests establish only the behaviour covered by those tests; they do not prove security, reliability under load or production readiness.

### What remains to improve

A future iteration should add persistent idempotency, stronger audit integrity, a clearer permission model and tests for malformed or hostile proposal content. Any move to real integrations should begin with a threat model and narrowly scoped credentials. A short demonstration recording and independent code review would add useful evidence.

### What this demonstrates

The record shows scope control, acceptance criteria, delivery decisions, implementation evidence and actual test execution. It does not claim a client delivery, production release or operational AI system.
