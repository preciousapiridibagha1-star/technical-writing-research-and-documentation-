# Locked MVP Scope — CORA AI

**Status:** Locked.  
**Demonstrator target:** 28 November 2026.  
**Data:** Synthetic only.  
**Product:** One web application plus REST API.

## Product statement

CORA AI is an AI-assisted open-source consent and access-control application. It records consent separately for each defined purpose, checks requested use against the current consent record and maintains an audit history.

## The only three core capabilities

### 1. Consent records
- Create a pseudonymous demo participant.
- Show separately defined purposes, initially research and AI model training.
- Record grant or refusal for each purpose.
- Allow explicit withdrawal of a previously granted purpose.
- Store purpose, resource reference, status, timestamp and consent-text version.
- Display current purpose-by-purpose status.

### 2. Access permission checks
- Accept a request for a defined participant, resource and purpose.
- Check the current matching consent on the backend.
- Return ALLOW or DENY with a reason.
- Deny by default if permission is missing, refused, withdrawn or mismatched.
- Record the request and outcome.
- Expose the check through the web interface and a documented REST endpoint.

### 3. Audit history
- Record consent grants, refusals and withdrawals.
- Record access requests, approvals and denials.
- Include timestamp, event type, pseudonymous reference, purpose, actor/service, outcome and reason.
- Show chronological history to an authorised administrator.
- Do not provide ordinary edit/delete controls for historical events.

## AI assistant requirements

One integrated assistant supports all three capabilities. It explains, guides, prepares requests, checks completeness, invokes approved read/check tools and summarises authorised events.

It cannot make consent choices, grant access, override a denial, rewrite policy or directly mutate the database. Consequential actions require explicit user action and backend validation. The AI is the central conversational operating interface; it is not the source of authority. The deterministic permission service returns the final access decision.

Core functions must remain available without an AI API key.

## Required screens

1. Welcome and role entry.
2. Participant consent.
3. Consent status.
4. Access request.
5. Allow/deny result.
6. Audit history.
7. Contextual AI assistant panel.

## Minimal data objects

- Participant: pseudonymous ID and demo metadata.
- DataResource: synthetic resource/dataset ID and description.
- Purpose: stable purpose key and plain-language definition.
- ConsentRecord: participant, resource, purpose, status, version and timestamp.
- AccessRequest: requester, participant/resource, purpose, timestamp and outcome.
- AuditEvent: event type, references, actor/service, timestamp, outcome and reason.

No names, phone numbers, clinical notes, diagnoses, voice recordings or actual health datasets are needed.

## Required API operations

Record a consent choice; withdraw a consent choice; retrieve current consent status for an authorised caller; submit an access permission check; retrieve audit history for an authorised administrator; send a message to the bounded assistant.

Every endpoint validates inputs and permissions on the server. Exact route names and schemas are documented in the architecture document.

## Acceptance tests

- Participant can grant research consent.
- Participant can refuse AI-training consent independently.
- Research access is allowed when matching research consent is granted.
- AI-training access is denied when AI-training consent is refused.
- Research access is denied after research consent is withdrawn.
- Missing consent is denied.
- A request for a different purpose is denied.
- Every consent and access event appears in audit history.
- Unauthorised roles cannot view restricted records or perform another role's action.
- AI cannot override a denied result or change consent without an explicit authorised action.
- Core functions work when the AI provider is unavailable.

## Explicitly out of scope

Real personal, mental-health or clinical data; production identity verification; production hosting and operations; live SRHIN or other platform integration; mobile-native apps; multiple AI agents; autonomous background operations; AI-generated consent decisions; AI approval of access; blockchain; federated learning; differential privacy; advanced cryptography; bulk migration; complex analytics; multi-language translation in the first demonstrator; legal or security certification.

## Build order

1. Backend data model and consent rules.
2. Access-check service and audit events.
3. Automated tests.
4. Simple web screens.
5. AI assistant with limited tools and no direct database access.
6. Synthetic end-to-end demonstration.
7. Setup, API, limitations and handover documentation.

## Definition of done

The synthetic demonstration passes, automated tests pass, AI boundaries are enforced in code, API and local setup are documented, and the repository clearly labels the product as a synthetic-data demonstrator—not a production health-data system.
