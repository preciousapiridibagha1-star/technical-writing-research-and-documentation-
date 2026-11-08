# Project & Programme Delivery — Vantage MVP Case

**Evidence type:** Self-directed project planning case. The plan is documented; delivery of a complete product is not claimed.

## Objective

Produce a small demonstration of a human approval gate for a proposed AI-assisted task workflow. The demonstration should show that a user can inspect a proposed action, approve or reject it, and review a local record of the outcome.

## Scope

**Included**
- One fixed mock instruction and proposal.
- An explicit approve/reject decision.
- A harmless local mock action.
- A local audit record.
- Basic manual verification of both decision paths.

**Excluded**
- Real AI model calls.
- External integrations or account access.
- Payments, messages or customer-data changes.
- Multi-user access, production hosting and commercial use.

## Delivery plan

| Stage | Output | Completion evidence |
|---|---|---|
| 1. Define | Narrow problem and scope | Approved scope document |
| 2. Design | Workflow and proposal fields | System overview and MVP requirements |
| 3. Build | Local Python demonstration | Source file runs locally |
| 4. Verify | Approval and rejection checks | Recorded test observations |
| 5. Document | Run instructions and limitations | README and review notes |

## Risks and controls

| Risk | Control |
|---|---|
| Reader assumes this is a live AI product | Label it as a local mock demonstration in every project index. |
| Approval is bypassed | Keep the action handler behind the explicit decision branch. |
| A real external action occurs accidentally | Use a fixed local mock action only. |
| Audit information is mistaken for secure logging | State that the JSONL file is a simple local demonstration, not tamper-proof storage. |
| Scope expands before the core flow is understood | Keep integrations and multi-agent features out of this milestone. |

## Review criteria

The milestone is useful if another person can run it, understand the approval boundary, choose rejection and see that no action occurs, then approve and see only the harmless mock action. The audit file should show the sequence.

## Current status

The project plan and source artefact are present in this repository. The code must still be run in a local environment and its results recorded before the portfolio describes the demonstration as locally verified. No user testing or external deployment is claimed.
