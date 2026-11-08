# 6. Project & Programme Delivery

## Evidence project: Delivering a bounded Vantage Automata prototype

**Status:** Local prototype code committed to the portfolio repository; updated test execution is pending independent verification.  
**Purpose:** Show how a broad system concept was reduced to a small, testable delivery increment.

### Delivery objective

Demonstrate one low-risk journey: instruction → validation → proposal → human decision → mock action or safe stop → local audit record.

### Scope delivered in code

- One reminder-shaped instruction.
- Input validation and restricted action type.
- Structured proposal.
- Approval tied to a fingerprint of the displayed proposal.
- Duplicate-execution protection within one running process.
- Mock action only.
- Safe failure response with no automatic retry.
- Local JSON Lines audit record.

### Evidence record

| Evidence item | Record |
|---|---|
| Repository location | `projects/vantage-automata/prototype/` |
| Main implementation | `vantage_mvp.py` |
| Automated tests | `test_vantage_mvp.py` |
| User-facing explanation | `README.md` |
| Change recorded | Code, tests and README committed to the portfolio repository |
| Test status | Nine tests are written; execution output has not yet been captured in this record |
| Deployment status | Not deployed; local mock only |

### Safety acceptance checks

1. Reject empty, overlong and out-of-scope instructions.
2. Reject an unauthorised action type.
3. Reject approval if the proposal content changes after review.
4. Reject an approval referring to another proposal ID.
5. Block a second execution attempt.
6. On action failure, stop and do not automatically retry.
7. Keep the action mocked; no external account or business data is touched.

### Before → after

**Before:** “Build Vantage Automata with AI agents and business integrations.”

**After:** “Deliver one local, low-risk approval journey with proposal validation, exact-content approval, duplicate protection, safe failure and a local audit record.” The revised scope is testable and makes the exclusions explicit.

### Delivery decisions and limitations

- Deterministic proposal generation was retained so the approval controls can be tested without model variability.
- The action remains a mock; no reminder is actually created.
- Duplicate protection is in-memory and does not persist across restarts.
- The local audit file is not tamper-proof.
- Authentication, multi-user permissions, durable storage, deployment, monitoring and AI integration remain outside this increment.

### What would complete this delivery case

Capture the actual test command and output; resolve any failures; demonstrate both approval and rejection paths; record defects and fixes; and add a short reflection on what changed. Do not claim a successful test run until the output is available.

### What this demonstrates

The record shows scope control, acceptance criteria, risk handling and traceable implementation work. It does not claim a client delivery, production release or operational AI system.
