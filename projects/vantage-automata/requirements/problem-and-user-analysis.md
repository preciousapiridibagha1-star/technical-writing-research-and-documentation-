# Vantage Automata — Problem and User Analysis

**Status:** Initial self-directed analysis; assumptions require validation with real users.

## 1. Project framing

Vantage Automata explores a focused problem in AI-assisted work: how can a system help someone turn a plain-language instruction into a useful proposed action without removing the person's control over whether that action happens?

The project is not based on the assumption that every task should be automated. It examines how AI interpretation and human approval could work together in a bounded workflow.

## 2. Problem statement

A user may want help carrying out routine digital tasks but may not trust an AI system to act on an instruction without showing what it has understood and what it intends to do.

The design challenge is therefore to make the proposed action visible, understandable and reviewable before execution.

This is a problem hypothesis for the self-directed project. It has not yet been validated through formal user interviews or field research.

## 3. Intended initial user

The first MVP is scoped for one individual operating the prototype. It is not initially designed for teams, multiple organisations or complex permission structures.

A later version could be assessed for:
- Small-business owners who want help preparing routine digital tasks.
- Professionals who use AI assistance but want to review actions before they occur.
- Operators of digital workflows who need a visible approval step.

These are potential user groups, not confirmed customers.

## 4. User needs and design responses

| Potential user need | Design response | How it could be evaluated |
|---|---|---|
| Understand what the AI interpreted | Display a concise task summary. | User can explain the system's interpretation. |
| Know what the system intends to do | Show a specific proposed action. | User can identify the action and its scope. |
| Retain control | Require an explicit approval or rejection. | No action occurs before approval. |
| Avoid unintended execution | Use backend approval checks and a mock action first. | Rejection and duplicate-request tests pass. |
| Understand what happened | Show the outcome and preserve an audit record. | Displayed status matches the recorded result. |
| Recover from errors | Provide controlled messages for invalid input and failures. | Error scenarios do not trigger an action. |

## 5. Root considerations

The design must account for more than the AI model's ability to interpret a sentence.

- **Ambiguous instructions:** the system may misunderstand what the user means.
- **Overly broad requests:** a request may contain several actions or unclear boundaries.
- **Incorrect model output:** the provider may return incomplete or invalid information.
- **Misleading proposals:** a summary may sound correct while the proposed action is not what the user intended.
- **Approval mistakes:** a user may approve without understanding the consequences.
- **Repeated requests:** network retries or repeated clicks may cause duplicate processing.
- **Operational failure:** the backend, model provider or action handler may be unavailable.
- **Privacy and security:** instructions may contain sensitive information or credentials.

The first MVP limits the consequences by using mock data and a mock action, while testing the approval process itself.

## 6. What the first version will and will not prove

### It aims to demonstrate

- A plain-language instruction can be received and validated.
- A structured proposal can be prepared.
- A person can inspect and decide on that proposal.
- Rejection prevents execution.
- Approval permits one safe mock action.
- The decision and outcome can be recorded.

### It will not prove

- That the system can safely automate arbitrary business tasks.
- That it can operate autonomously in production.
- That it is suitable for payments, customer records or external communications.
- That it supports multiple users or enterprise permissions.
- That a particular AI provider is always accurate.
- That a commercial market exists or that users will pay for it.

## 7. Assumptions to validate

| Assumption | Validation approach |
|---|---|
| Users want to review an AI-proposed action before it happens. | Conduct short interviews or usability sessions with intended users. |
| A structured proposal is easier to review than raw model output. | Compare user understanding across sample proposal formats. |
| A single-task MVP is sufficient to demonstrate the concept. | Test whether the narrow workflow communicates the core value. |
| Users understand the difference between approving a proposal and submitting an instruction. | Observe users completing the workflow and ask them to explain the distinction. |

No validation results are claimed at this stage.

## 8. Success measures for a future prototype

- Users can correctly describe the proposed action before approving it.
- Rejected proposals never trigger the action handler.
- Approved proposals trigger no more than one mock action.
- Invalid provider output is blocked.
- The audit record accurately reflects the request, decision and outcome.
- Users can understand the final status without technical assistance.

## 9. Strategic contribution

The work represented here is problem framing, user-needs analysis, scope definition and translation of an initial concept into requirements that a developer could review. The analysis is an initial hypothesis, not a substitute for user research or technical validation.
