# Vantage Automata — Requirements-to-Tests Traceability

**Status:** Proposed verification matrix; no implementation or test execution is claimed.  
**Purpose:** Connect the documented MVP requirements to observable checks so that a future prototype can be evaluated without treating a written design as proof that the system works.

## Scope

The documented Vantage flow is a human-supervised task proposal process:

1. A user submits a task.
2. The backend validates the request.
3. An AI or mock provider prepares a structured proposal.
4. The backend validates the proposal.
5. The user reviews the proposal.
6. Rejection stops the workflow.
7. Approval permits one bounded mock action.
8. The result is recorded.

This matrix uses that proposed flow as its baseline. It does not add live integrations, autonomous external actions or capabilities that have not been specified.

## Traceability matrix

| ID | Requirement / control | Expected observable behaviour | Proposed verification | Evidence to retain |
|---|---|---|---|---|
| VA-R01 | Accept a task request | A valid request is accepted and assigned a trackable identifier. | Submit a valid test request and inspect the response. | Request/response record with test data. |
| VA-R02 | Validate user input | Missing, malformed or out-of-scope input is rejected with a clear error. | Test empty, malformed and unsupported requests. | Test cases and actual results. |
| VA-R03 | Prepare a structured proposal | The provider returns a proposal in the agreed schema. | Use a deterministic mock provider first; validate required fields. | Sanitised provider output and schema result. |
| VA-R04 | Validate provider output | Invalid or incomplete output cannot proceed to user approval. | Supply missing fields, wrong types and malformed output. | Validation logs and rejection result. |
| VA-R05 | Require human review | A proposal is shown as pending and no action occurs before an explicit decision. | Submit a request and inspect state before approval. | State record and interface evidence. |
| VA-R06 | Support rejection | Rejection ends the action path and records the decision. | Reject a pending proposal and verify no action handler runs. | Decision record and action counter/log. |
| VA-R07 | Require explicit approval | Only an authorised approval moves the proposal to the approved state. | Test no decision, rejection, approval and unauthorised decision attempts. | State transition records. |
| VA-R08 | Limit approved action | Approval permits only the single action described in the approved proposal. | Use a mock action handler and verify its input and call count. | Mock action log. |
| VA-R09 | Prevent duplicate execution | Repeated approval requests do not cause duplicate mock actions. | Replay the same approval request and test idempotency behaviour. | Request identifiers and action count. |
| VA-R10 | Record outcome | The workflow records success or failure without exposing unnecessary sensitive data. | Run mock success and failure paths and inspect stored records. | Sanitised audit record. |
| VA-R11 | Handle provider failure | Provider timeout or failure produces a safe error state; no action is taken. | Simulate timeout, unavailable provider and invalid response. | Error record and state result. |
| VA-R12 | Protect data | Test data is minimised; secrets and private values are not written to logs. | Inspect configuration, sample logs and error responses. | Review notes; never include live secrets. |

## Proposed workflow states

| State | Meaning | Permitted next states |
|---|---|---|
| received | Request has arrived. | validated, rejected_input |
| validated | Input passed basic checks. | proposal_pending, provider_error |
| proposal_pending | Structured proposal is ready for human review. | approved, rejected |
| approved | An authorised person approved the specific proposal. | action_succeeded, action_failed |
| rejected | Human reviewer rejected the proposal. | Terminal |
| rejected_input | Input did not meet requirements. | Terminal |
| provider_error | Proposal could not be safely prepared. | Terminal or explicit user resubmission |
| action_succeeded | The bounded mock action completed. | Terminal |
| action_failed | The bounded mock action failed. | Terminal pending human handling |

A future implementation should define the exact state storage, transition enforcement and retry rules. A user-interface label alone is not sufficient to enforce a security boundary.

## Minimum acceptance conditions for a first prototype

A prototype should not be described as passing until the following have been demonstrated and recorded:

- Invalid input cannot reach the action stage.
- Invalid provider output cannot reach the approval stage.
- No action occurs while a proposal is pending.
- Rejection produces no action.
- Approval is checked by the backend, not trusted solely because the interface sends an approval flag.
- A proposal can trigger only its approved, bounded action.
- Replayed approval requests cannot cause unintended duplicate actions.
- Provider failures stop safely.
- The record of decisions is sufficient to reconstruct what happened without storing unnecessary personal data.
- The tests are repeatable and their actual results are documented.

## Test record template

| Field | Record |
|---|---|
| Test ID | Unique identifier linked to VA-R requirement |
| Date and version | Actual test date and code/version identifier |
| Setup | Test data and configuration used |
| Steps | Exact actions performed |
| Expected result | Requirement-based expected behaviour |
| Actual result | What happened, without rewriting it to match expectations |
| Pass/fail | Based on the expected result |
| Evidence | Link to screenshot, log or test output with secrets removed |
| Follow-up | Defect, owner and next action |

## Out of scope for the current design

- Sending messages to real customers or third parties.
- Making payments, refunds, bookings or account changes.
- Connecting to live email, CRM or business systems.
- Giving the AI unrestricted access to tools or data.
- Treating a successful mock action as proof of a production integration.
- Claiming security, reliability or performance until these have been tested.

## Evidence boundary

This is a design and verification-planning document. The checks above are proposed; they have not been executed. The earlier Vantage workspace and source export are unavailable for verification. Any future prototype should be version-controlled and its actual test outputs retained before the project status is changed.
