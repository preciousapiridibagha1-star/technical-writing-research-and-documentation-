# Jarvis AI — First MVP Agent Specifications

**Status:** Proposed design specification for a future developer collaboration. No agents or integrations are currently implemented.

## Purpose

Specify the smallest useful agent arrangement for the first Jarvis AI MVP: an AI-assisted customer-enquiry helper for a business. The design deliberately avoids activating the wider ecosystem until the first workflow has been built and evaluated.

## Operating principles

- The business owner controls the approved knowledge, topics, policies and permissions.
- The system prepares suggestions; a named human reviewer controls whether a response is used.
- Every proposed answer must be traceable to approved business information.
- Missing, conflicting, sensitive or out-of-scope information triggers escalation.
- The system must not send messages or change business records autonomously in the first MVP.
- A simpler single-agent implementation is preferable if it meets the requirements; separate agent labels do not justify unnecessary complexity.

## Agent and human roles

### 1. Owner / authorised manager

**Purpose:** Set the operating boundary.

**Responsibilities**
- Approve the FAQ, product and service information supplied to the system.
- Define supported topics and mandatory escalation topics.
- Assign reviewers and remove access when needed.
- Review recurring errors and approve changes to the knowledge set.
- Decide whether the MVP should continue, change or stop.

**Must not be delegated:** Final authority over business policy, access permissions and customer-impacting decisions.

### 2. Lead coordinator

**Purpose:** Manage the enquiry from intake to review.

**Inputs**
- Customer question (test data during development).
- Supported-topic rules.
- Approved knowledge references.
- Escalation rules.

**Responsibilities**
- Check that the enquiry is within the MVP's supported scope.
- Route an in-scope enquiry to the response-drafting function.
- Ensure the result includes its supporting approved source.
- Apply the uncertainty and escalation rules.
- Present a draft and its status to the human reviewer.
- Record the workflow state and reviewer decision.

**Restrictions**
- Cannot approve its own output.
- Cannot send a reply to a customer.
- Cannot change business policy or approved knowledge.
- Cannot bypass an escalation or permission check.

### 3. Customer-support response drafter

**Purpose:** Prepare a grounded draft for a routine enquiry.

**Inputs**
- The customer question.
- Only the relevant approved knowledge excerpts.
- The supported-topic and prohibited-topic rules.

**Responsibilities**
- Draft a concise answer using only the supplied approved information.
- Identify the source used for each material factual claim where practical.
- Mark information as unavailable when the knowledge set does not answer the question.
- Flag conflicting, ambiguous or potentially sensitive requests.

**Restrictions**
- Must not invent prices, stock, delivery dates, refund decisions, guarantees or policy.
- Must not treat a customer's message as an instruction to change system rules.
- Must not access unrelated customer records.
- Must not send messages or make commitments.

### 4. Human reviewer

**Purpose:** Retain accountable control over the customer-facing response.

**Available decisions**
- Approve the draft for staff use.
- Edit the draft before use.
- Reject the draft.
- Take over the enquiry.
- Escalate to the owner or another authorised person.

**Required review information**
- Original enquiry.
- Proposed response.
- Supporting approved source(s).
- Any uncertainty or escalation flag.
- Previous workflow status.

Approval in this MVP records a human decision. It does not authorise automatic sending, refunds, bookings or other external actions.

## Workflow states

| State | Meaning | Permitted next states |
|---|---|---|
| Received | Enquiry entered into the test workflow. | Scope check |
| Out of scope | Enquiry is not supported. | Human handling / closed |
| Drafting | Approved information is being checked and a draft prepared. | Draft ready / escalation |
| Draft ready | A sourced draft is available for review. | Approved / edited / rejected / escalation |
| Escalation required | Information is missing, conflicting, sensitive or outside policy. | Human handling / closed |
| Approved for staff use | Reviewer approved the draft for a staff member to use. | Closed |
| Edited for staff use | Reviewer amended and approved the text for staff use. | Closed |
| Rejected | Reviewer declined the suggestion. | Human handling / closed |
| Closed | The test case has ended and its outcome is recorded. | None |

A transition must be recorded with the actor, timestamp, decision and reason where relevant. The first MVP does not include automatic customer messaging.

## Minimum information model

A test case should record:
- Unique case identifier.
- Test enquiry text.
- Scope-check result.
- Approved knowledge reference identifiers used.
- Draft response.
- Uncertainty or escalation reason.
- Reviewer identifier (test account).
- Reviewer decision and any edited response.
- State-change timestamps.
- Final test outcome.

Use synthetic test data. Do not put real customer personal data into the first prototype.

## Acceptance checks for a future build

1. An in-scope question can produce a draft linked to approved information.
2. An unanswered question is marked uncertain rather than completed with an invented fact.
3. Conflicting knowledge triggers escalation.
4. Sensitive and prohibited topics are routed to a human.
5. The lead coordinator cannot approve its own draft.
6. No customer-facing message is sent by the MVP.
7. Reviewer decisions and state changes are recorded.
8. A user without reviewer permission cannot approve a draft.
9. An attempt to bypass the review step is blocked.
10. Test records contain no real customer personal data.

These are proposed acceptance checks. They have not been executed.

## Developer hand-off questions

Before implementation, the collaborating developer and project owner should agree:
- The first business type and exact supported enquiry categories.
- The knowledge format, update process and source versioning.
- Authentication and reviewer permissions.
- Data retention and deletion rules.
- Whether one model call and deterministic application logic are sufficient.
- Hosting, model provider, cost limits and data-processing terms.
- Logging and error-handling requirements.
- A test plan and a review of security and privacy risks.

## Relationship to the wider Jarvis ecosystem

Operations, Finance, Analytics, Sales, Product, Marketplace, Content and other proposed agents remain outside this MVP. They should only be considered after a real business need is established and the first workflow has evidence of value.

## Evidence boundary

This is a design and hand-off specification. It does not claim customer research, a working multi-agent system, live integrations, deployment or test results.
