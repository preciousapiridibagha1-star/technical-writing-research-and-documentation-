# System Architecture and Design Methodology

**Opportunity context:** Mozilla Foundation Fellowship 2027–2028 — Track I Embedded, SRHIN  
**Status:** A practical design method prepared independently for the portfolio. It is not an SRHIN-approved architecture, a confirmed set of host requirements or evidence of a deployed system.  
**How it fits:** This document follows the [Problem Discovery & Co-Design Framework](PROBLEM_DISCOVERY_AND_CO_DESIGN_FRAMEWORK.md) and the [Problem-to-System Engineering Framework](PROBLEM_TO_SYSTEM_ENGINEERING_FRAMEWORK.md).

---

## 1. Purpose

This document explains how I would turn a validated need into a clear, practical system design.

I do not start by choosing a programming language, database, AI model or website framework. I first need to understand what the system is expected to help people do, what already exists, and what constraints the design must respect.

**My basic approach is:**

1. Confirm the problem and the people involved.
2. Understand the existing process and tools.
3. Write down what the proposed system must and must not do.
4. Break the system into a small number of understandable parts.
5. Decide how information moves between those parts and who can access it.
6. Check how it may connect to existing tools.
7. Record important design choices and their reasons.
8. Test the design against the original requirements.

The design should be only as complicated as the problem requires.

## 2. Start with requirements, not technology

Before drawing an architecture, I would make sure the requirements are clear enough to guide a design.

For each important requirement, I would record:

- **What is needed?** The capability or outcome.
- **Who needs it?** The intended user or responsible role.
- **Why is it needed?** The problem or evidence behind it.
- **What should happen?** The expected system behaviour.
- **How will we check it?** A simple acceptance test.
- **What must be protected?** Any privacy, safety, access or operational constraint.

I would separate requirements into two practical groups:

**Functional requirements** describe what the system does. For example, it may allow an authorised user to submit a request, show its status or record a decision.

**Quality and operating requirements** describe the conditions under which it must work. These may include privacy, security, reliability, accessibility, ease of use, maintainability and cost.

I would not treat an example in this document as a confirmed SRHIN requirement. Actual requirements would need to be validated with the host and relevant stakeholders.

## 3. Describe the system in simple parts

A system architecture is a map of the main parts of a system and how they work together. It helps people understand the design before implementation begins.

For a small software system, I would normally consider these parts:

| Part | What it is responsible for |
|---|---|
| User interface | The screen, form or other way a person interacts with the system |
| Application logic | The rules that determine what happens when a user takes an action |
| Data storage | The information the system needs to keep |
| Access control | Checks that determine which users can perform which actions |
| Integrations | Approved connections to other tools or services |
| Logs and monitoring | Records needed to understand important actions, errors and system operation |

Not every project needs all these parts as separate services. In a small project, several responsibilities may live in one application. I would separate them only when there is a clear reason, such as security, maintainability or a real integration requirement.

For a non-software intervention, the same thinking can be used to describe the people, responsibilities, information and steps in the process.

## 4. Map how information moves

I would describe the information flow from the moment it enters a process until it is used, stored, shared or deleted.

A simple data-flow description should answer:

1. Who or what provides the information?
2. What information is actually needed?
3. Where does it go next?
4. Which part of the system processes or stores it?
5. Which people or services can access it?
6. Is it sent to another system or organisation?
7. How long is it kept, and how is it corrected or deleted where applicable?

For sensitive information, I would pay particular attention to unnecessary collection, copies, exports and external services.

A data-flow diagram can make this easier to review. It should show the main systems, information moving between them and the points where access or trust changes. The diagram should be based on confirmed information, with unknowns clearly marked.

**Important:** I would not use real participant or mental-health data to create a portfolio diagram or demonstration. Synthetic data is sufficient to explain a proposed design.

## 5. Design permissions around responsibilities

Access should be based on what a person needs to do, not simply on their job title or general membership of an organisation.

I would begin by listing the user roles and the actions each role genuinely needs. For example, a system might distinguish between someone who submits a request, someone who reviews it and someone who administers the software. These are illustrative roles, not a proposed SRHIN permission model.

A simple permissions table helps make the rules visible:

| Role | View relevant records | Submit a request | Review or decide | Manage system settings |
|---|---:|---:|---:|---:|
| Requester | Limited | Yes | No | No |
| Authorised reviewer | As required | If permitted | Within assigned authority | No |
| System administrator | Only as operationally necessary | No, unless separately authorised | No | Yes |

The actual roles and permissions must be agreed with the organisation and any legitimate community decision-making bodies.

I would also consider:

- Giving users only the access they need.
- Preventing users from approving their own requests where separation of duties is required.
- Removing access when a person's role ends.
- Protecting administrator accounts.
- Recording important actions where an audit trail is necessary.
- Avoiding the exposure of sensitive information in notifications, logs or reports.

A software permission must never be mistaken for legal, ethical or community authority. The system can enforce an approved decision process; it cannot decide who ought to have that authority.

## 6. Decide whether integration is necessary

An integration allows two systems to exchange information. It may be useful when people otherwise have to enter the same information repeatedly or when an existing system needs to receive an approved update.

Before proposing an integration, I would ask:

- Is there already an approved way to exchange this information?
- Is the connection genuinely necessary?
- Which system is the authoritative source?
- What exact information needs to move?
- Who has permission to authorise the connection?
- What happens if the connection fails?
- How will access, errors and changes be recorded?

Where an integration is justified, an API may provide a controlled way for systems to communicate. But I would not add an API or connect to an external service just because the technology is available.

If an integration is not necessary, a documented manual process may be simpler, safer and easier to maintain.

## 7. Make technology choices for clear reasons

I would compare technology options against the requirements rather than choose tools because they are popular.

The decision should consider:

- Whether the tool solves the required problem.
- Whether the team can understand and maintain it.
- Security and privacy implications.
- Compatibility with existing systems.
- Accessibility and the users' operating environment.
- Hosting, licensing and ongoing costs.
- Availability of documentation and support.
- How difficult it would be to change or replace later.

I would record important choices in a short decision note:

| Question | What I would record |
|---|---|
| What decision was made? | The selected approach or technology |
| Why was it needed? | The requirement it addresses |
| What alternatives were considered? | Other reasonable options, including no new tool |
| Why was this option selected? | The practical advantages and trade-offs |
| What are the limitations? | Risks, dependencies and things it does not solve |

I would keep the first design as simple as possible. The specific programming language, database, hosting provider or AI model should only be selected when the requirements and operating context justify that choice.

## 8. Treat AI as an optional component, not the centre of every system

AI should only be included when it provides a clear benefit that a simpler method cannot provide as well.

Possible bounded uses include helping a user find information, explaining a process, drafting a summary or identifying missing information for a human reviewer.

If AI is included, I would define:

- What information it is allowed to use.
- What task it is allowed to perform.
- What it must not decide or do.
- When a human must review the result.
- How incorrect or uncertain output is handled.
- How users can report a problem or request human assistance.

AI should not independently approve access to sensitive data, change consent conditions, determine community benefits or replace an authorised decision-maker. Those decisions belong to the people and governance processes with legitimate authority.

If AI does not improve the validated workflow, I would leave it out.

## 9. Consider failure and safe operation

A design should consider not only what happens when everything works, but also what happens when something goes wrong.

I would ask:

- What if a user enters incorrect information?
- What if someone tries to access a record they are not permitted to see?
- What if an integration or external service is unavailable?
- What if a request is submitted twice?
- What if a system update fails?
- What if a user leaves the organisation?
- What happens if the system needs to be paused or retired?

The response may be a validation check, an error message, a manual fallback, an escalation route or a recovery procedure. The appropriate response depends on the system and its risks.

For any system handling sensitive information, security and privacy review should involve suitably qualified people. A portfolio design document is not a security audit or certification.

## 10. Keep the design understandable and testable

Before implementation, I would review the design with the people responsible for the requirements and ask:

- Does each part have a clear purpose?
- Can we explain where information comes from and where it goes?
- Are permissions consistent with agreed responsibilities?
- Are external connections necessary and authorised?
- Have we considered failure and human review?
- Can the intended team operate and maintain the design?
- Can each important requirement be tested?

I would then connect requirements to tests. For example:

| Example requirement | Possible check |
|---|---|
| Only authorised reviewers can make a decision | Test that a requester cannot access the decision action |
| Users can see the status of their own request | Test that the correct status is shown to the requester |
| Important decisions are traceable | Check that the required action record is created |
| The workflow handles an unavailable integration | Simulate a failed connection and check the error or fallback |

These are illustrative tests. A real project would need its own agreed requirements and acceptance criteria.

## 11. What I would produce before building

I would keep the design package small and useful. Depending on the size of the project, it may contain:

1. **Requirements summary** — what the system needs to do and the constraints it must respect.
2. **System diagram** — the main parts and how they connect.
3. **Data-flow diagram or description** — how information moves and where it is stored or shared.
4. **Roles and permissions table** — who can do what, based on agreed authority.
5. **Integration notes** — which existing systems need to connect and why.
6. **Decision notes** — the main technology choices, alternatives and trade-offs.
7. **Test outline** — how we will check that the design meets the requirements.

A small project may not need seven separate documents. I would combine them where that makes the work easier to understand.

## 12. A simple example of how I would explain the method

Imagine an organisation has a validated need to track requests that require review by an authorised person. This is a generic example for explaining the design method; it is not a claim about SRHIN's current systems or a confirmed host requirement.

I would approach it like this:

- **Understand the need:** Find out who submits requests, who reviews them and what information is necessary.
- **Map the current process:** Understand how requests are received, assigned, reviewed and followed up today.
- **Define requirements:** Agree what a requester should be able to do, what the reviewer needs and what records must be kept.
- **Sketch the system:** Show the user interface, the rules that manage the workflow, the records stored and the access controls.
- **Map information and permissions:** Identify what information is collected, who can see it and who is authorised to take each action.
- **Consider integration:** Check whether the workflow needs to connect to another system or whether it can operate independently.
- **Plan tests:** Check that requests move through the correct steps and that users cannot perform actions outside their permissions.
- **Review before implementation:** Confirm that the design is useful, safe, affordable and maintainable.

That is the level of architecture I would start with. More detail should be added only when the real requirements demand it.

## 13. What this document demonstrates—and what it does not

This document demonstrates a structured approach to thinking about system design. It provides a method for discussing requirements, components, information flows, permissions, integrations, technology choices and testing.

It does **not** claim that:

- A system has been designed or built for SRHIN.
- SRHIN has approved these example roles, requirements or design choices.
- Any integration with SRHIN systems has been investigated or authorised.
- A security audit, production deployment or user evaluation has taken place.
- A particular technology stack has been selected.

The next step is to use this method in a small, clearly labelled technical demonstration with synthetic data. The demonstration should be chosen because it illustrates a real engineering capability—not because it is being presented as the solution SRHIN must adopt.

**My design principle:** Understand the need. Keep the architecture simple. Make information and authority clear. Choose technology for a reason. Test what the system is supposed to do.
