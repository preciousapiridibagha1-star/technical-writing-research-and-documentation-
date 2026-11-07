# Vantage Automata

**Project status: Self-directed system concept documented for a future rebuild with a developer. It is not a currently working or verified product.**

Vantage Automata is a proposed AI-assisted task and action-approval system. It is intended to help individuals, businesses, companies and agencies turn plain-language instructions into structured action proposals while keeping the user in control of whether an action proceeds.

The project is being retained as a documented system design and future product direction. The intended next implementation route is to rebuild the prototype in collaboration with a developer. The earlier exploratory prototype is not being treated as a deliverable or as evidence of a functioning system.

## The problem the concept explores

AI tools can interpret instructions and prepare actions, but allowing a system to act without clear review can create mistakes, unwanted changes and loss of user trust. Vantage Automata explores a controlled alternative: the system prepares and explains a proposed action, and an authorised person decides whether it may proceed.

The intended users are not limited to one industry. Potential settings include individuals managing digital tasks, small and growing businesses, companies and agencies. The exact first customer group and use case must be selected and validated before development.

## Proposed first workflow

1. A user enters a task or instruction.
2. The system validates the request and checks whether it is within the permitted scope.
3. An AI component prepares a structured action proposal.
4. The backend validates the proposal against the system's rules.
5. The user sees the proposed action and relevant details.
6. The user approves or rejects it.
7. Rejection stops the workflow. Approval permits only the specifically authorised, safe action.
8. The system records the decision and outcome.

This describes the proposed workflow, not a currently running application.

## Intended product direction

The longer-term direction is to develop Vantage Automata into a dependable task-approval product that could be adapted to different customer and organisational workflows. It should not be marketed as a finished universal automation platform. Each use case would need defined permissions, integrations, data boundaries, safeguards and acceptance tests.

The first rebuild should remain narrow and use mock data and mock actions. Real integrations and consequential actions should only be considered after the core approval flow has been implemented, reviewed and tested.

## Strategic and systems-design work

The portfolio documents:
- Problem framing and initial user assumptions.
- MVP scope and acceptance criteria.
- Proposed system architecture and API contract.
- Task proposal and human approval workflow.
- Risk and control register.
- Technical decision records.
- Proposed implementation plan.
- Test plan and requirements-to-tests traceability.

These materials are intended to support a future developer collaboration and make the system's expected behaviour and boundaries understandable before implementation.

## Project documentation

### Problem and requirements
- [Problem and User Analysis](requirements/problem-and-user-analysis.md)
- [MVP Scope and Acceptance Criteria](requirements/mvp-scope.md)
- [Risk and Control Register](requirements/risk-and-control-register.md)

### Architecture and workflow
- [System Overview](architecture/system-overview.md)
- [Initial API Contract](architecture/api-contract.md)
- [Initial Technical Decisions](architecture/technical-decisions.md)
- [Instruction and Approval Workflow](workflows/approval-workflow.md)

### Implementation and testing
- [Proposed Implementation Plan](implementation/implementation-plan.md)
- [MVP Test Plan](testing/test-plan.md)
- [Requirements-to-Tests Traceability Matrix](testing/requirements-to-tests-traceability.md)

## Future rebuild approach

The intended next step is a fresh, inspectable implementation with a developer. The collaboration should establish:
1. The first customer group and one concrete task workflow.
2. The agreed MVP requirements and exclusions.
3. A simple architecture and documented technology choices.
4. A working prototype using mock data and mock actions.
5. Test cases, recorded results and fixes.
6. A short demonstration of the verified workflow.

The original Vantage Automata architecture diagram will be added to this repository when supplied. The diagram will be presented as a proposed architecture, not as proof of implementation.

## Safety and evidence boundaries

Human approval is central to the design. The first build should not execute payments, send external messages or change customer records. Any later real integration would require explicit permissions, security and privacy review, and tests.

No current working MVP, verified integration, user validation or executed test results are claimed. The earlier exploratory prototype is not required as evidence for this documented concept; the future rebuild will be assessed on its own source, tests and demonstration.
