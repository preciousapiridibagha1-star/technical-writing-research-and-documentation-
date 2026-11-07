# Vantage Automata

**Project status: Concept and architecture documented; prototype not currently available.**

Vantage Automata is an AI-assisted task-system concept. It is based on a simple idea: a person describes a task, AI interprets the instruction and proposes what should happen, and the person reviews the proposal before an action is allowed.

The project is approached from a strategic and systems perspective. The work focuses on the problem being addressed, the intended users, the workflow, the system structure, safety boundaries and a realistic first version. It is not presented as a completed software product.

## The problem and intended value

Businesses use different tools and processes to handle routine tasks. An AI assistant could help interpret instructions and prepare actions, but allowing software to act without clear oversight can create mistakes and loss of trust.

Vantage Automata explores a human-supervised approach: AI can recommend an action, while the person remains in control of whether it proceeds.

## Intended first workflow

1. A user enters a task or instruction.
2. The system interprets the request.
3. It presents a structured summary and proposed action.
4. The user reviews the proposal.
5. The user approves or rejects it.
6. A future prototype would run only a safe test action after approval.
7. The system would record the decision and outcome.

This is the proposed workflow, not a description of a currently running application.

## Strategic and architectural work

The portfolio work for this project includes:

- Defining the problem and intended user.
- Considering the value to businesses and the people using the system.
- Scoping a small first version rather than attempting a large autonomous platform.
- Mapping the main system components and how information should move between them.
- Defining the role of human approval.
- Identifying risks, constraints and requirements.
- Preparing an implementation route and test plan for a future technical build.

## Project history and available evidence

An earlier version was explored in Replit, and a video showing parts of its interface, including the landing page and dashboard, remains available to the project owner. The Replit workspace and downloaded source code were later deleted after the code export became corrupted.

As a result, the earlier source code cannot currently be inspected, run or verified. The video may be used as visual reference for the interface that was explored, but it is not evidence of working backend functionality, AI integration or completed tests.

The current portfolio documents therefore describe the concept and proposed architecture. They do not claim that the earlier prototype is recoverable or that a working MVP exists.

## Safety and scope

The proposed first version keeps a person involved before any action is taken. A future prototype should begin with mock data and test actions, not real payments, external messages or changes to customer records.

## Documentation

- `requirements/` — intended users, needs, requirements and constraints.
- `architecture/` — system structure, component roles and API proposal.
- `workflows/` — proposed user and system workflows.
- `implementation/` — recommended stages for a future build.
- `testing/` — test cases that a future prototype should pass.
- `user-guide/` — instructions to be written if a working prototype becomes available.

## Current status

The strategic concept, initial requirements, architecture proposal, API contract and test plan are documented. Implementation and testing remain future work. The project should only be described as prototyped or tested if a new working version is built and the evidence is recorded.
