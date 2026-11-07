# Vantage Automata — Learning Notes 01

These notes explain the project documents in plain English. The aim is to understand the decisions and be able to discuss them naturally, not memorise technical phrases.

## Lesson 1: What problem is Vantage Automata exploring?

Vantage Automata explores a simple question:

**How can AI prepare a digital action for someone while leaving the final decision with that person?**

Imagine asking an assistant to prepare a reminder. Instead of silently doing something, the system first explains what it understood and what it proposes to do. You review that proposal. If you reject it, nothing happens. If you approve it, the first version performs only a safe demonstration action.

The important idea is not simply “AI automation”. It is controlled AI assistance.

## Lesson 2: The difference between an instruction, a proposal and approval

These are three different things:

- **Instruction:** what the user asks the system to do.
- **Proposal:** what the AI says it understood and intends to do.
- **Approval:** the user's explicit permission for that specific proposal to proceed.

An instruction must not automatically count as approval. The AI's proposal must not count as approval either.

For example:
- Instruction: “Prepare a reminder for me to review the sales report.”
- Proposal: “Create a mock reminder to review the weekly sales report.”
- Approval: the user selects Approve after reading the proposal.

If the proposal is wrong, the user can reject it.

## Lesson 3: What is a frontend and a backend?

The **frontend** is the part the person sees and uses: forms, buttons, screens and status messages.

The **backend** is the application logic behind the interface. It receives requests, checks them, manages the task's status and decides whether the action handler may be called.

Why does that matter? A button in a browser is not a security boundary. A person or script could send a request without using the screen. The backend must independently check whether approval is valid.

## Lesson 4: What is an API contract?

An API contract is an agreed description of how two parts of a software system communicate.

For Vantage Automata, the frontend may send an instruction to an endpoint such as `POST /api/tasks`. The backend responds with a task identifier, status and proposal.

The contract documents:
- The request fields.
- The response fields.
- The endpoint's purpose.
- What errors may occur.
- What rules the backend must enforce.

The API contract in this portfolio is proposed. It does not mean those endpoints have been implemented.

## Lesson 5: What is a workflow?

A workflow is the sequence of steps and decisions needed to complete a process.

The Vantage workflow is:

1. User submits an instruction.
2. Backend validates it.
3. AI prepares a structured proposal.
4. Backend validates the proposal.
5. User reviews it.
6. User rejects or approves.
7. Rejection stops the process; approval permits one mock action.
8. The system records and displays the result.

The workflow helps a developer understand what must happen and in what order.

## Lesson 6: What is an audit record?

An audit record is a history of important events. In this project it should show what instruction was submitted, what proposal was produced, what decision the user made and what result followed.

It helps answer: “What happened, and why does the system say this task was completed?”

It should not contain passwords, API keys or unnecessary personal information.

## Lesson 7: What is a mock action?

A mock action imitates an operation without changing a real external service.

For example, the system might report that a test reminder was created, while only saving a demonstration result inside the prototype. It does not send an actual message or change a real business account.

This lets a developer test the approval logic before introducing real-world consequences.

## Explain the project in an interview

A natural answer could be:

“Vantage Automata is a self-directed AI task-system concept I developed around controlled execution. I wanted to explore how an AI system could interpret a user's instruction and prepare an action without automatically carrying it out. My work has focused on defining the problem, narrowing the first version, mapping the architecture and workflow, and documenting requirements and test cases. The key design principle is that the AI proposes, the application enforces the approval rules, and the user makes the decision. The earlier prototype is no longer available for verification, so I present the current work as a documented concept rather than a working product.”

## Questions to practise

1. What problem is Vantage Automata trying to solve?
2. Why should an instruction not automatically authorise an action?
3. What is the difference between the frontend and backend?
4. Why does the backend need to check approval?
5. What does the API contract describe?
6. Why does the first MVP use a mock action?
7. What evidence would you need before saying the system works?

## Your own contribution

Be precise. You can say that you framed the problem, developed the concept, defined the proposed workflow and requirements, considered safeguards, and prepared technical documentation for a future implementation.

Do not say that you built the backend, integrated an AI model, configured the infrastructure or tested a working system unless you later complete those activities and retain evidence.
