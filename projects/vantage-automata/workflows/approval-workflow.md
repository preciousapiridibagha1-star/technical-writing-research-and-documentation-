# Vantage Automata — Instruction and Approval Workflow

**Status:** Proposed workflow for the first MVP; not yet implemented or verified.

## 1. Objective

Define exactly how an instruction moves through Vantage Automata, from submission to a recorded decision. The workflow is deliberately narrow: AI prepares a proposal, but a person decides whether the proposed mock action may proceed.

## 2. Actors and responsibilities

| Actor | Responsibility | Must not do |
|---|---|---|
| User | Submit an instruction and approve or reject the proposal. | Assume that submitting an instruction automatically authorises execution. |
| Frontend | Collect input, display the proposal and submit the user's decision. | Enforce security rules on its own or execute actions directly. |
| Backend | Validate input, manage task state, enforce approval and coordinate the action. | Treat an AI response as user approval. |
| AI provider or mock provider | Interpret the instruction and return a structured proposal. | Approve or execute the action. |
| Mock action handler | Simulate the approved action and return a test result. | Connect to or modify real external services in the MVP. |
| Audit record | Preserve the request, proposal, decision and outcome. | Store secrets or unnecessary personal data. |

## 3. Main workflow

### Step 1 — Submit an instruction

The user enters a plain-language task and submits it.

**Backend checks:**
- The instruction is present and not only whitespace.
- The instruction is within the configured length limit.
- The request format is valid.

If validation fails, the backend returns a clear error. No AI proposal or action is created.

### Step 2 — Interpret the instruction

The backend sends the validated instruction to the selected AI provider. During early development, a mock provider may be used to test the workflow without an external model.

The provider returns a structured proposal containing:
- A short task summary.
- A proposed action type.
- A plain-language action description.
- An explicit indication that approval is required.
- A preliminary risk classification.

The backend validates the response. Missing or malformed fields cause the proposal to be rejected. The model must not be allowed to decide that approval is unnecessary.

### Step 3 — Present the proposal

The frontend displays the task summary and proposed action. The user should be able to understand what would happen before making a decision.

The proposal enters the `awaiting_approval` state. No action handler is called at this stage.

### Step 4A — Rejection path

If the user rejects the proposal:
1. The frontend sends the rejection decision to the backend.
2. The backend confirms that the task exists and is awaiting a decision.
3. The backend records the rejection and timestamp.
4. The task state changes to `rejected`.
5. The workflow ends.

**Control:** a rejected task cannot later be approved. The action handler is never called.

### Step 4B — Approval path

If the user approves the proposal:
1. The frontend sends the approval decision to the backend.
2. The backend confirms that the task exists and is awaiting approval.
3. The backend checks that the proposal has not expired or already been processed.
4. The backend records the approval.
5. The backend calls the mock action handler once.
6. The backend records the returned result.
7. The task state becomes `completed` or `failed`.
8. The frontend displays the outcome.

Approval authorises only the specific action shown in the proposal. If the proposed action changes, a new approval is required.

## 4. State transition model

| Current state | Event | Next state | Action permitted? |
|---|---|---|---|
| New request | Input passes validation and proposal is valid | `awaiting_approval` | No |
| New request | Input or provider output is invalid | `invalid` | No |
| `awaiting_approval` | User rejects | `rejected` | No |
| `awaiting_approval` | User approves and mock action succeeds | `completed` | Mock action only |
| `awaiting_approval` | User approves and mock action fails | `failed` | Mock action attempted once |
| `rejected` | Later approval attempt | Remains `rejected` | No |
| `completed` | Duplicate approval attempt | Remains `completed` | No repeat execution |
| `failed` | Duplicate approval attempt | Remains `failed` unless an explicit retry design is added | No automatic repeat |

## 5. Essential safeguards

- **Server-side enforcement:** approval checks happen in the backend, not only in the browser.
- **Specific approval:** the decision applies to the exact proposal the user reviewed.
- **Single execution:** repeated requests must not trigger duplicate actions.
- **Terminal rejection:** rejection cannot be reversed by a later request.
- **Safe first action:** the MVP uses a mock action with no external side effects.
- **Validated model output:** untrusted model output is checked before it becomes a proposal.
- **Traceability:** important state changes and results are recorded.
- **Controlled errors:** failures should be understandable without exposing credentials or internal secrets.

## 6. Exceptions and unresolved design decisions

A technical implementation must decide:
- How long an approval-ready proposal remains valid.
- How simultaneous approval requests are handled safely.
- Whether a failed mock action can be retried and under what conditions.
- How task records are stored and protected.
- How provider timeouts and unavailable services are handled.
- What information is retained and for how long.

These decisions should be recorded before implementation rather than assumed.

## 7. What would prove this workflow works?

A future demonstration should show:
1. A valid instruction produces a proposal.
2. The proposal is visible before any action.
3. Rejecting it stops the workflow.
4. Approving it runs the mock action once.
5. Repeated approval does not run it again.
6. Invalid model output is blocked.
7. The audit record matches the actual decision and result.

Until those scenarios have been run and recorded, this document remains a proposed workflow.
