# Vantage Automata — Risk and Control Register

**Status:** Initial design analysis; controls require technical validation.

| ID | Risk | Potential impact | Proposed control | Evidence needed |
|---|---|---|---|---|
| R-01 | AI misunderstands the instruction | Wrong proposal is shown | Display a plain-language proposal and require user review | Usability tests with varied instructions |
| R-02 | Model returns malformed or incomplete data | Invalid proposal enters workflow | Validate all required fields on the backend | Automated validation tests |
| R-03 | User approves without understanding | Unintended action | Show a specific action description and clear approval choice | User comprehension tests |
| R-04 | Frontend is manipulated to bypass approval | Unauthorised action | Enforce state and approval rules on the backend | API-level negative tests |
| R-05 | Duplicate requests trigger repeated action | Duplicate side effects | Use task state checks and idempotency protection | Repeated-request test evidence |
| R-06 | Rejected task is later executed | User decision is ignored | Treat rejection as terminal | Attempted re-approval test |
| R-07 | Provider or backend fails | Incomplete or uncertain task state | Controlled error handling and explicit status | Failure and recovery tests |
| R-08 | Sensitive information is included in prompts or logs | Privacy exposure | Use test data, minimise retention and exclude secrets | Data-flow and log review |
| R-09 | Real integrations are added prematurely | External harm or data changes | Keep MVP actions mocked; require separate risk review for integrations | Scope review and integration approval |
| R-10 | Audit record does not match actual events | Poor traceability | Record state transitions and action outcomes consistently | Audit-record reconciliation tests |

## Design rules

1. A model response is untrusted input until validated.
2. Approval must be explicit and apply to the exact proposal shown.
3. The backend, not the browser, enforces execution permissions.
4. Rejection ends the task.
5. The first implementation uses a mock action only.
6. A real integration requires a new scope, permissions review, threat assessment and test plan.
7. Unknown behaviour must fail safely rather than default to execution.

## Residual risks and open questions

The register is an initial design aid, not a completed security assessment. A technical review must determine the storage design, authentication needs, access control, data retention, threat model, monitoring and incident response appropriate to any future deployment.
