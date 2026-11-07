# Jarvis AI — First MVP Decision Record

**Decision status:** Proposed scope decision for future developer collaboration.  
**Project status:** Design documentation only; no implementation or customer validation is claimed.

## Decision

Prioritise a narrow, human-reviewed customer-enquiry assistant as the first Jarvis AI MVP. Keep the wider multi-agent business ecosystem as a longer-term architecture direction, not part of the first build.

## Why this use case comes first

The wider Jarvis concept spans many business functions. Attempting to build Operations, Finance, Analytics, Customer Support, Sales, Product, Marketplace and Content agents together would create a large, expensive system before there is evidence that the overall architecture is needed.

A customer-enquiry workflow is a more bounded starting point:
- It has a clear input: a customer question.
- It has a constrained information source: business-approved FAQs and service information.
- It has a visible output: a suggested response with supporting information.
- It has an understandable human control point: staff review the draft.
- It can be evaluated with synthetic questions before any real customer data or external messaging is introduced.

This is a product-design rationale, not a claim that business owners have been interviewed or that this problem has been validated in the market.

## Alternatives considered

| Option | Reason not selected for the first MVP |
|---|---|
| Build the complete Jarvis ecosystem | Too broad for an initial test; creates multiple dependencies before the value of the core workflow is known. |
| Start with Finance or payment agents | Higher consequence of errors and greater need for permissions, financial controls and specialist validation. |
| Start with autonomous Sales or outreach | External actions and customer impact increase risk; human review should be established first. |
| Start with a general-purpose assistant for every business function | Scope and success criteria would be difficult to define and test. |
| Start with a customer-enquiry helper | Selected because the workflow can be bounded, grounded in approved information and reviewed by a person. |

## Conditions for reconsidering the decision

The first use case should be changed if conversations with prospective users show that:
- customer enquiries are not a meaningful problem for the intended business;
- another problem is more frequent, costly or suitable for a safe first test;
- the business cannot provide reliable approved information;
- a simpler non-AI process would solve the problem better.

Before committing to development, validate the problem with a small number of relevant business owners or support staff. Record what they say, distinguish observations from assumptions and revise the scope accordingly.

## Build boundary

The first prototype should use synthetic test enquiries and an approved sample knowledge set. It should not send real customer messages, process payments, change bookings, issue refunds or make commitments. A human must review each suggested response.

The design should begin with the simplest architecture that meets the acceptance checks. Separate agents should only be introduced where they provide a clear, testable benefit over a single agent plus ordinary application logic.

## Success measures for a future test

Agree a baseline and targets before testing. Candidate measures include:
- correctness against approved source information;
- rate of unsupported statements;
- accuracy of escalation;
- proportion of drafts accepted or edited by reviewers;
- reviewer handling time;
- unauthorised or out-of-scope actions (target: zero).

No results are available because no test has been run.

## Next decision gate

Proceed to a developer-scoping session only after the first business context, enquiry categories, approved knowledge source, reviewer role, data boundaries and test criteria have been agreed.

## Evidence boundary

This record explains the current design choice. It is not evidence of user research, market demand, implementation or measured performance.
