# Vantage Automata — Implementation Plan

**Status:** Build plan; no implementation has been verified yet.  
**Chosen route:** Backend/API-first.

## 1. Why this route

The first MVP will use a small web application with a backend API. This keeps the approval rule, validation and action control in application code, where they can be inspected and tested.

An automation platform such as Make.com or n8n may be useful later, but adding it now would introduce another system to learn and debug. The first goal is to make one complete workflow understandable and testable.

## 2. Proposed starter stack

Use the simplest stack that can run reliably in the existing development environment:

- **Frontend:** React with Vite.
- **Backend:** Node.js with Express.
- **Language:** JavaScript initially, unless the existing project already uses TypeScript.
- **AI:** begin with a deterministic mock response; add one real model API after the workflow and validation work.
- **Storage:** start with a small local development store or JSON-backed store. Move to a database only when the basic flow is working and persistence requirements are clear.
- **Tests:** use the test framework already present in the project. If none exists, add a lightweight Node-compatible test setup.

This is a proposed stack, not a claim about the current Replit project. Before changing or recreating code, inspect the existing workspace and preserve any working implementation.

## 3. Build in small stages

### Stage 0 — Inspect what already exists

- Open the existing Vantage Automata Replit workspace, if it is still accessible.
- Identify the frontend framework, backend framework, entry points and installed dependencies.
- Check whether any form, API route, AI call or approval screen already exists.
- Record what runs and what does not.
- Do not replace the project before checking whether useful code can be recovered.

**Exit evidence:** a short note describing the existing stack, files and current run status.

### Stage 1 — Make the request path work without AI

- Create or confirm a task submission form.
- Add a backend endpoint that accepts the instruction.
- Reject empty or excessively long input.
- Return a predictable mock proposal.
- Display that proposal in the interface.

**Exit evidence:** a request submitted in the browser receives a valid proposal from the backend.

### Stage 2 — Add the approval gate

- Give each proposal a unique identifier.
- Display explicit Approve and Reject controls.
- Send the decision to the backend.
- Keep the decision and execution state on the backend, not only in browser state.
- Make rejection terminal: it must not call the action handler.
- Make approval idempotent: repeated approval requests must not execute the same proposal twice.

**Exit evidence:** tests show that rejection stops and approval permits one mock execution only.

### Stage 3 — Add the safe mock action and audit record

- Create one action handler that performs no external side effect.
- For example, it can create a mock task record and return a result message.
- Record the request, proposal, decision, timestamps, action status and result.
- Display the outcome to the user.

**Exit evidence:** a complete test run can be traced from submission to final result.

### Stage 4 — Add one real AI provider

Only after the mock workflow passes its tests:

- Select one model provider.
- Store the API key in environment secrets, never in source code.
- Ask the model for the documented structured response.
- Validate the response on the backend.
- Treat invalid, incomplete or uncertain output as a failure requiring review; do not execute it.
- Keep the mock provider available for repeatable tests.

**Exit evidence:** a real model response can be validated and shown for approval, while malformed output is safely rejected.

### Stage 5 — Review and document

- Run the full test list.
- Record actual results, including failures.
- Add setup instructions based on the real project.
- Capture screenshots only after the interface works.
- Update project status from “specified” to “in progress”, “prototyped” or “tested” only when the evidence supports it.

## 4. API responsibilities

The frontend should not call the AI provider directly. The backend must own input validation, AI requests, proposal state, approval decisions, action execution and audit records.

See [API Contract](../architecture/api-contract.md) for the initial endpoint design.

## 5. Safety rules for the first build

- The only executable action is a mock action.
- The AI can propose; it cannot approve.
- The browser cannot directly trigger the action handler.
- The backend checks the proposal state before execution.
- Rejected, malformed or expired proposals cannot execute.
- Duplicate approval requests cannot cause duplicate execution.
- API keys and other secrets must remain in environment variables.
- No real emails, payments, customer records or external business accounts are connected.

## 6. Learning and contribution record

For each stage, keep a short record of:

- What was changed.
- Why the change was needed.
- Which files or components were involved.
- What was learned.
- What was tested and what happened.
- Who completed and can explain the work.

AI-assisted code should be reviewed and understood by the person claiming the contribution. Do not list generated code as independently understood work until it has been checked and explained.

## 7. Immediate next action

Inspect the existing Vantage Automata workspace and write down its actual stack and current state. Then implement Stage 1 in that project rather than starting a second application.
