# Vantage Automata — System Overview

**Status:** Initial architecture proposal; not yet implemented or verified.

## 1. Overview

The first version of Vantage Automata can be organised into five parts:

1. **User interface** — accepts the instruction and displays the AI proposal and final result.
2. **Backend API** — receives requests, coordinates the workflow and controls which steps are allowed.
3. **AI interpretation component** — turns the instruction into a structured proposal.
4. **Approval and action control** — waits for the user's decision and permits only the approved safe test action.
5. **Audit log** — records the request, proposal, decision and execution result.

## 2. Proposed request flow

```text
User
  |
  v
Frontend form
  |
  v
Backend API
  |
  v
AI interpretation
  |
  v
Response validation
  |
  v
Proposal shown to user
  |
  +---- Reject ----> Record rejection ----> Stop
  |
  +---- Approve ---> Safe mock action
                         |
                         v
                    Record result
                         |
                         v
                    Show outcome
```

## 3. Component responsibilities

### User interface

- Collect the user's instruction.
- Show validation messages.
- Display the AI's interpretation and proposed action.
- Collect an explicit approval or rejection.
- Display the final status.

### Backend API

- Validate incoming requests.
- Call the AI component or a clearly labelled mock.
- Validate the returned structure.
- Keep approval state under backend control.
- Prevent the action adapter from running before approval.
- Record workflow events.

### AI interpretation component

- Interpret the instruction.
- Return a structured proposal.
- Avoid claiming that an action has already happened.
- Return an error or uncertain result when it cannot interpret the request safely.

### Approval and action control

- Require an explicit decision.
- Treat rejection as a terminal state for that proposal.
- Allow only the defined mock action in the first version.
- Prevent accidental duplicate execution.

### Audit log

At minimum, record a request identifier, instruction, proposal, decision, timestamp, action status and result. Avoid storing secrets or unnecessary personal information.

## 4. Important design boundary

The AI component proposes. The application controls approval and execution. The model response alone must never be treated as permission to perform an action.

## 5. Decisions still to make

- Whether the first implementation is backend/API-first or automation-platform-first.
- Which language and framework will be used.
- Which AI provider or mock response will be used initially.
- Whether the first audit log is stored in a database or a simple development store.
- How request identifiers and duplicate submissions will be handled.

Choose one implementation route for the first MVP. Do not build two parallel versions before the first one works.

## 6. Verification still required

This diagram and description are a design proposal. They do not demonstrate a running application, a working AI connection, persistence or successful tests. Those claims can be updated only after implementation evidence is available.
