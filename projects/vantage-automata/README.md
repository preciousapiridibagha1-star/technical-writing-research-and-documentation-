# Vantage Automata

**Project status: Concept and architecture documented; earlier prototype is unavailable for verification.**

Vantage Automata is a self-directed AI-assisted task-system concept. A person describes a task, AI interprets the instruction and proposes what should happen, and the person reviews the proposal before an action is allowed.

The project is approached from a strategic and systems perspective. It focuses on problem analysis, user needs, MVP scope, system architecture, workflow, requirements, safety boundaries and technical hand-off. It is not presented as a completed software product.

## Problem and intended value

An AI assistant may help interpret instructions and prepare digital actions, but allowing software to act without clear oversight can create mistakes and reduce trust. Vantage Automata explores a human-supervised approach: AI can recommend an action, while the person remains in control of whether it proceeds.

The initial user and problem analysis is a project hypothesis. Formal user interviews and validation have not yet been completed.

## Proposed first workflow

1. A user enters a task or instruction.
2. The backend validates the input.
3. An AI or mock provider prepares a structured proposal.
4. The backend validates the proposal.
5. The user reviews the proposed action.
6. The user approves or rejects it.
7. Rejection stops the workflow; approval permits one safe mock action.
8. The system records and displays the outcome.

This is the proposed workflow, not a description of a currently running application.

## Strategic contribution

The work represented in this project includes:
- Framing the problem and identifying an initial user.
- Analysing user needs and design assumptions.
- Defining a proportionate MVP and its exclusions.
- Mapping system components and information flow.
- Defining human approval and backend enforcement requirements.
- Identifying risks, safeguards and open technical questions.
- Preparing an API proposal, implementation plan and test design.
- Communicating the concept for technical review and future implementation.

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

## Project history and evidence limitations

An earlier version was explored in Replit, and a video showing parts of its interface, including the landing page and dashboard, remains available to the project owner. The Replit workspace and downloaded source code were later deleted after the code export became corrupted.

The earlier source code cannot currently be inspected, run or verified. The video may be used as visual reference for the interface that was explored, but it cannot verify backend behaviour, AI integration, data storage, security or completed tests.

The current portfolio documents therefore describe the concept and proposed architecture. They do not claim that the earlier prototype is recoverable or that a working MVP exists.

## Safety and scope

The proposed first version keeps a person involved before any action is taken. A future prototype should begin with mock data and test actions, not real payments, external messages or changes to customer records. Any later real integration would require separate permissions, security review and testing.

## Current status and next evidence

The concept, initial problem analysis, requirements, architecture proposal, API contract, workflow, risk register, implementation plan and test plan are documented. Implementation, user validation and testing remain outstanding.

The next evidence milestone is a fresh, inspectable implementation or a documented technical review. Any future claim that the system is implemented or tested must be supported by a working build and recorded results.


## Verification planning

- [Requirements-to-tests traceability matrix](testing/requirements-to-tests-traceability.md) — maps the proposed MVP controls to observable checks and evidence to retain. The checks are planned, not executed.
