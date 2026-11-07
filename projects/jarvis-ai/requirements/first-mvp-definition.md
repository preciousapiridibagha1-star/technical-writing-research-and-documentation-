# Jarvis AI — First MVP Definition

**Status:** Proposed scope for discussion; not implemented or user-validated.

## The first problem to test

The wider Jarvis idea covers many parts of a business. Building all of them at once would make the project too large and difficult to test. The first version should focus on one common problem:

**Small businesses receive customer questions repeatedly, but answers may be slow or inconsistent because useful information is spread across different documents or messages.**

This is a starting problem hypothesis, not a proven finding. It should be checked with real business owners before development.

## Proposed first use case

An AI-assisted customer enquiry helper that uses a small set of business-approved information to prepare answers to routine questions and sends uncertain or sensitive questions to a person.

The system should help staff respond more consistently. It should not pretend to replace the business owner or support team.

## Who would use it?

- **Business owner or manager:** approves the information and sets the rules.
- **Customer-support staff:** reviews suggested answers and handles escalations.
- **Customer:** asks a question through the business's chosen channel.

## What the first version should do

1. Receive a customer question through one agreed test interface.
2. Check the question against a small, approved set of business information.
3. Prepare a suggested answer and show which approved information supports it.
4. Mark the answer as uncertain when the information is missing, unclear or conflicting.
5. Send uncertain, sensitive or complaint-related questions to a human.
6. Let a staff member approve, edit or reject the suggested answer.
7. Keep a basic record of the question, suggested response, review decision and outcome, using test data during the first build.

## What the first version must not do

- Send replies to real customers without staff approval.
- Make refunds, payments, bookings or account changes.
- Invent prices, policies, delivery dates or product details.
- Use private customer information that is not needed for the task.
- Learn new business policies from unapproved conversations.
- Give itself wider access or permissions.
- Run a large group of agents simply because the wider architecture contains them.

## Minimum roles

| Role | First-version responsibility |
|---|---|
| Owner / authorised manager | Approves the knowledge and operating rules. |
| Lead agent | Receives the question, coordinates the response process and presents the result. |
| Customer Support agent | Drafts a response using approved information and flags uncertainty. |
| Human reviewer | Approves, edits, rejects or takes over the case. |

Other roles in the wider Jarvis catalogue are outside this first MVP.

## Basic workflow

1. A customer question arrives.
2. The system checks whether the question fits the supported topics.
3. The support agent looks for relevant approved information.
4. It prepares a suggested answer with the supporting source.
5. A confidence or uncertainty check decides whether the case can be shown as a routine suggestion or must be escalated.
6. A staff member reviews the suggestion.
7. The staff member approves, edits or rejects it.
8. The system records the decision and closes or escalates the case.

**Important:** In this first version, approval means a staff member may use the suggested reply. It does not mean the system can perform other business actions.

## Information and access needed

- A small, owner-approved FAQ or product/service information set.
- Test customer questions that do not contain real personal data.
- A list of topics the helper may answer.
- A list of topics that must always go to a person.
- Staff accounts with clear reviewer permissions.
- A record of decisions and errors for testing.

## How success could be measured

These are proposed measures. Targets should be agreed after a baseline is collected.

- Percentage of test questions matched to the correct approved information.
- Percentage of suggested answers accepted without major edits.
- Number of unsupported or invented details in responses.
- Percentage of uncertain cases correctly sent to a person.
- Average time taken by a reviewer to handle a test enquiry.
- Number of cases where the system acts outside its permitted scope.

Safety matters as much as speed. A fast answer that gives the wrong policy is not a successful result.

## Main risks and controls

| Risk | First-version control |
|---|---|
| Made-up answer | Require support from approved information; otherwise escalate. |
| Old or incorrect business information | Owner reviews and approves the knowledge set. |
| Sensitive customer question | Route to a person; do not draft a final decision. |
| Accidental message sent | Keep external sending disabled until separately reviewed and approved. |
| Unnecessary personal data | Use fictional test data and collect only what is needed. |
| Staff over-trusts the suggestion | Label it clearly as a draft and show its supporting source. |

## Decisions required before development

1. Which real business type will be used for the first test?
2. Which five to ten question types are in scope?
3. Where will test questions be entered?
4. Who approves the knowledge and reviews answers?
5. What information must never be processed?
6. What result would make the business owner say the test is useful?

## Relationship to the wider Jarvis system

This MVP tests a narrow customer-support workflow. It does not prove that the wider Jarvis multi-agent ecosystem is necessary or working. If the test shows value, the architecture can be expanded carefully. If a simpler single-agent workflow is enough, the project should use the simpler design.

## Evidence boundary

This document is a proposed product and systems-design specification. No customer interviews, live integrations, working agents or measured results are claimed.
