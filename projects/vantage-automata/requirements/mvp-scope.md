# Vantage Automata MVP Scope

**Status:** Specified — implementation has not yet been verified.

## 1. Purpose

The first Vantage Automata MVP will demonstrate a controlled way to turn a user's instruction into a proposed action. The system will use AI to interpret the instruction, but it will not execute the proposed action until a person has reviewed and approved it.

The goal is to prove one complete workflow, not to build the full long-term platform.

## 2. Problem being addressed

AI systems can produce useful plans and suggestions, but a system that acts on those suggestions needs clear boundaries. Users should be able to see what the AI understood, what it proposes to do and what will happen if they approve it.

The MVP will make that review step part of the workflow rather than treating it as an optional extra.

## 3. Intended user

The initial user is the person operating the Vantage Automata prototype. The first version is not being designed for multiple organisations, teams or customer accounts.

## 4. Main user journey

1. The user opens the prototype.
2. The user enters a plain-language instruction.
3. The frontend sends the instruction to the backend.
4. The backend asks an AI model to interpret it and return a structured proposal.
5. The backend validates the response.
6. The frontend displays the interpretation and proposed action.
7. The user approves or rejects the proposal.
8. If rejected, the system records the rejection and stops.
9. If approved, the system runs a safe mock action.
10. The system records the outcome and displays a status message.

## 5. Functional requirements

| ID | Requirement | Acceptance evidence |
|---|---|---|
| FR-01 | Accept a plain-language task instruction. | A user can submit a non-empty instruction. |
| FR-02 | Send the instruction from the frontend to a backend endpoint. | A request and response can be observed during a test. |
| FR-03 | Obtain an AI interpretation or use a clearly labelled mock response during early development. | The response identifies the interpreted task and proposed action. |
| FR-04 | Return a structured response. | The response follows the documented JSON shape. |
| FR-05 | Validate the response before showing it as an actionable proposal. | Missing or malformed fields produce a controlled error. |
| FR-06 | Show the proposal to the user before execution. | The user can read the proposed action. |
| FR-07 | Allow approval or rejection. | Both decisions can be submitted and recorded. |
| FR-08 | Stop execution after rejection. | A rejected proposal does not call the action adapter. |
| FR-09 | Run only a safe mock action after approval. | An approved proposal creates a test result without changing an external account. |
| FR-10 | Record the request, proposal, decision and result. | An audit record can be inspected after the test. |
| FR-11 | Show the final status to the user. | The interface reports completed, rejected or failed. |

## 6. Initial structured response

The exact schema may change during implementation, but the first version should contain these fields:

```json
{
  "task_summary": "A short description of what the system understood",
  "proposed_action": {
    "type": "mock_action",
    "description": "A plain-language description of the test action"
  },
  "requires_approval": true,
  "risk_level": "low"
}
```

This is an example contract for the prototype, not evidence that an AI integration already exists.

## 7. Non-functional requirements

- **Clarity:** the user must be able to understand the proposal before deciding.
- **Safety:** no real external action runs without approval.
- **Validation:** invalid input and malformed model output must be handled.
- **Traceability:** the system records the decision and outcome.
- **Maintainability:** the workflow should be divided into understandable components.
- **Privacy:** development should use test data; secrets must not be committed to the repository.

## 8. Out of scope for the first MVP

- Sending real emails or messages.
- Making payments or financial transactions.
- Editing real customer or business records.
- Connecting multiple third-party services.
- Multi-user permissions and organisation management.
- Autonomous execution without human approval.
- A large collection of specialist agents.
- Production deployment or commercial availability.

These may be considered later, after the small workflow has been built, tested and reviewed.

## 9. Test cases required

| Test | Expected result |
|---|---|
| Valid instruction and valid proposal | Proposal is displayed for review. |
| Empty instruction | Submission is rejected with a clear message. |
| Malformed AI response | No action is offered for execution; an error is recorded. |
| User rejects proposal | Workflow stops and records rejection. |
| User approves proposal | Only the mock action runs. |
| Mock action fails | Failure is recorded and shown to the user. |
| Duplicate approval request | The same action is not accidentally executed twice. |

## 10. Completion criteria

The MVP can be described as implemented only when the complete journey works in a running environment. It can be described as tested only when the required test cases have been run and their results recorded.

Until then, the status remains **specified** or **in progress**, depending on the evidence available.
