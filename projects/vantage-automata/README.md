# Vantage Automata

**Project status: Specification and MVP planning**

Vantage Automata is a proposed AI-assisted task system. The idea is to let a person describe a task, have an AI model interpret the instruction and suggest an action, and then let the person review that suggestion before anything is carried out.

The first version will be deliberately small. It is not intended to connect to every business tool or operate as an autonomous employee. The aim is to build and test one complete, understandable workflow.

## The first MVP workflow

1. A user enters a task or instruction.
2. The backend receives the request.
3. An AI model returns a structured interpretation and a proposed action.
4. The system checks that the response follows the expected format.
5. The user sees the proposal and can approve or reject it.
6. Rejection stops the workflow. Approval allows only a safe test action to run.
7. The system records the request, proposal, decision and result, then shows the outcome to the user.

## What the MVP needs to demonstrate

- A simple frontend form communicating with a backend endpoint.
- A real AI call or a clearly labelled mock response.
- A defined JSON response structure.
- Validation and useful error handling.
- Human approval before execution.
- A safe action adapter, initially using a mock action or test environment.
- An audit log showing what happened.
- Tests for a successful run, rejection, malformed AI output and failed action.

## Safety and scope

The first version will use mock data and safe test actions. It will not send real messages, make payments or change important external records. Those capabilities would require separate permission checks, safeguards and testing.

A diagram or written workflow is not proof of a working implementation. Each feature will be labelled according to its actual status.

## Planned documentation

- `requirements/` — user needs, functional requirements and constraints.
- `architecture/` — system design and component responsibilities.
- `workflows/` — step-by-step workflow descriptions and diagrams.
- `implementation/` — setup and implementation notes as the build progresses.
- `testing/` — test cases, results and known issues.
- `user-guide/` — instructions for using the working MVP.

## Current next step

Define the MVP requirements and choose one implementation route before writing code. The first route should be either a backend/API-first build or an automation-platform-first build, not both at once.

This project is being developed as a practical learning and portfolio project. Features will only be described as working after they have been implemented and tested.
