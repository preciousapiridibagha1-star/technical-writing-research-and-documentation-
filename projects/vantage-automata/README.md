# Vantage Automata

**Project status: Local deterministic proof of concept implemented and unit-tested; not a deployed AI product.**

Vantage Automata is a self-directed concept for a human-supervised task-approval system. It explores how a user instruction can be converted into a structured proposal, checked against application rules, presented for explicit approval and then handled through a controlled action pathway.

The broader product remains a concept. The first local proof of concept demonstrates only one narrow reminder workflow. It does not call an AI model, connect external services or alter real business data.

## The problem the concept explores

AI tools can interpret instructions and prepare actions, but allowing a system to act without clear review can create mistakes, unwanted changes and loss of user trust. Vantage explores a controlled alternative: the application prepares and explains a proposed action, and an authorised person decides whether it may proceed.

The intended user group and first commercial use case have not yet been validated. The project is not presented as a universal automation platform.

## Proposed system workflow

1. A user enters a task or instruction.
2. The application validates the request and checks whether it is within the permitted scope.
3. An AI component may later suggest a structured action proposal.
4. Application logic validates the proposal independently.
5. The user sees the exact proposed action and relevant details.
6. The user approves or rejects it.
7. Rejection stops the workflow. Approval permits only the specific authorised action.
8. The system records the decision and outcome.

The AI component is not the permission authority. The application must enforce scope and approval rules.

## Implemented local proof of concept

A bounded local demo is available in the prototype folder. It uses deterministic proposal generation and a mock reminder action. It validates the input, binds approval to the exact proposal content displayed, blocks duplicate execution attempts within one process, handles action failure without automatic retry and writes a local audit record.

**Verification:** Nine unit tests passed on 9 November 2026 (`python -m unittest -v`; 9 passed, 0 failures, 0 errors). The test run checks only the behaviours covered by the test suite; it is not a security audit or production validation.

- Prototype run guide and evidence: [README](prototype/README.md)
- [Source code](prototype/vantage_mvp.py)
- [Unit tests](prototype/test_vantage_mvp.py)

## Strategic and systems-design work

The wider project documentation records problem framing and user assumptions, MVP scope and acceptance criteria, proposed architecture and API contract, approval workflow, risk and control register, technical decisions, implementation plan, test plan and requirements-to-tests traceability. These materials support future development planning; they do not mean that external integrations have been implemented.

## Safety boundaries and known limitations

- The current action is a mock; it does not create a real reminder.
- Proposal generation is deterministic, not AI-powered.
- Duplicate protection is in-memory and does not survive a restart.
- The local JSONL audit file is not tamper-proof.
- Authentication, multi-user permissions, durable storage, monitoring, deployment and real integrations are not implemented.
- No user testing, client validation or independent security review has been conducted.

Real integrations and consequential actions should be considered only after a threat model, permission model, durable execution controls, audit design and further testing are complete.

## Jarvis AI relationship

Jarvis AI remains the broader proposed multi-agent business operating ecosystem. Vantage is a narrower implementation experiment whose approval controls can be examined and tested before the broader concept is considered. Jarvis is not a deployed multi-agent system.

## Future evidence

A later iteration should add persistent idempotency, an explicit permission model, stronger audit integrity and tests for malformed or adversarial proposals. If a model is introduced, it should remain a proposal generator and must not grant itself execution authority.

The original Vantage architecture diagram will be added when the original image asset is available. It will illustrate a proposed design, not proof of implementation.

**Evidence boundary:** This is a self-directed local proof of concept with passing unit tests. It is not a commissioned client project, deployed application, integrated AI agent or production-ready service.
