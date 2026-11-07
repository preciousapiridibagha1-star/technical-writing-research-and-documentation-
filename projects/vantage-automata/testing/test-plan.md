# Vantage Automata — MVP Test Plan

**Status:** Planned tests; no results have been recorded yet.

## Purpose

Use this plan to check the complete request, proposal, approval and mock-execution flow. Record the actual result for every test after running it. Do not mark a test as passed based on code inspection alone.

## Test cases

| ID | Scenario | Steps | Expected result |
|---|---|---|---|
| T-01 | Valid instruction | Submit a normal instruction. | Backend returns a valid proposal and the interface displays it for review. |
| T-02 | Empty instruction | Submit an empty string. | Request is rejected with a clear validation message; no proposal or action is created. |
| T-03 | Whitespace-only instruction | Submit spaces or line breaks only. | Request is rejected as empty input. |
| T-04 | Input exceeds limit | Submit text longer than the configured maximum. | Backend rejects it; no AI call or action occurs. |
| T-05 | Malformed provider response | Make the mock provider return missing or incorrectly typed fields. | Backend rejects the response; no approval-ready proposal or action is produced. |
| T-06 | User rejects | Create a valid proposal and select Reject. | Status becomes rejected; action handler is not called. |
| T-07 | User approves | Create a valid proposal and select Approve. | The safe mock action runs once and its result is recorded. |
| T-08 | Mock action fails | Configure the mock action to return a controlled failure. | Status becomes failed; error is recorded and shown without exposing secrets. |
| T-09 | Duplicate approval | Approve the same proposal twice, including rapid repeated requests. | The action runs no more than once; the second request returns the existing result or a conflict response. |
| T-10 | Approve after rejection | Reject a proposal, then attempt to approve it. | Backend refuses; action handler is not called. |
| T-11 | Unknown task identifier | Request or approve a task that does not exist. | Backend returns a not-found response; no action occurs. |
| T-12 | Backend/provider unavailable | Simulate a provider or backend failure. | User receives a controlled error; no unintended action occurs. |

## Evidence to keep

For each test, record:

| Field | What to enter |
|---|---|
| Test ID | For example, T-01 |
| Date | Date the test was run |
| Build/version | Commit or version tested |
| Result | Pass, fail or blocked |
| Evidence | Screenshot, test output or log reference |
| Notes | Actual behaviour, including unexpected results |

## Release check

The MVP is not ready to be described as tested until all critical paths have been run:

- Valid proposal displayed.
- Rejection prevents execution.
- Approval runs the mock action once.
- Malformed provider output is blocked.
- Action failure is recorded.
- Duplicate approval does not repeat execution.
- Audit record matches what happened.

Any failed or blocked test must be listed as a limitation. Do not hide failed tests to make the project appear complete.
