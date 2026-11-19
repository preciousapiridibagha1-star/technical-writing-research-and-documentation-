# CORA AI — System Architecture

## 1. Objective

Build one small web application that records purpose-specific consent, checks data-use requests against that consent and records an audit history. Include one AI assistant as the conversational operating interface while keeping consent and access authority in deterministic backend rules.

The first implementation is a local synthetic-data demonstrator, not a production deployment.

## 2. Components

**Web application:** React interface with participant, requester and administrator screens. The AI assistant appears in the same application.

**AI assistant service:** One configurable model provider accessed through a server-side adapter. The assistant can invoke a small allow-list of application tools, including explaining purposes, retrieving authorised consent status, checking access permission, validating request completeness and summarising authorised audit events. It has no direct database credentials.

**Application API:** Python/FastAPI backend. It validates input, checks roles and permissions, and calls the domain services.

**Consent service:** Records grant, refusal and withdrawal separately for each participant/resource/purpose combination.

**Permission service:** Retrieves the current matching consent state and returns ALLOW or DENY with a reason. Missing, refused, withdrawn or mismatched consent returns DENY. This service—not the AI model—makes the final technical access decision.

**Audit service:** Records consent and access events and provides an authorised chronological history.

**Database:** SQLite for the local demonstrator. It stores pseudonymous synthetic participants, resources, purpose definitions, consent records, access requests and audit events.

## 3. Main flows

### Consent update
1. Participant selects a purpose and grant/refuse/withdraw action.
2. Frontend sends the explicit action to the backend.
3. Backend validates role, purpose and input.
4. Consent service records the new state.
5. Audit service records the event.
6. Interface displays the updated status.

AI may explain or guide, but does not choose for the participant.

### Access check
1. Requester submits participant, resource and exact purpose.
2. Backend validates the request.
3. Permission service checks current matching consent.
4. Service returns ALLOW or DENY and reason.
5. Audit service records the request and result.
6. Interface displays the result.

AI can explain the result; it cannot change it.

### AI interaction
1. User asks a question in the assistant panel.
2. Backend checks the user's role and permitted context.
3. AI receives only minimum authorised information.
4. AI may invoke an allow-listed tool.
5. Backend independently validates the tool call.
6. Consequential actions require explicit user confirmation and server-side validation.
7. Assistant explains the result.

## 4. Proposed technology

React frontend; Python and FastAPI backend; SQLite local database; REST/JSON API; configurable AI provider through environment variables; pytest backend tests; GitHub for version control and documentation. These are proposed implementation choices, not completed work.

## 5. API outline

Illustrative routes; final schemas are documented alongside implementation:

- POST /api/consents — record grant or refusal.
- POST /api/consents/{consent_id}/withdraw — withdraw a granted purpose.
- GET /api/participants/{participant_id}/consents — retrieve authorised consent status.
- POST /api/access-checks — check a requested purpose and record the result.
- GET /api/audit-events — retrieve audit events for an authorised administrator.
- POST /api/assistant/message — send a message to the bounded assistant.

The access-check endpoint must be called by the system that actually controls the protected resource. A browser display alone does not enforce access to a dataset.

## 6. Minimum data model

Participants: pseudonymous ID and demo flag.  
Resources: resource ID, label and demo flag.  
Purposes: stable purpose key, description and consent-text version.  
Consents: participant/resource/purpose, status, version and decision timestamp.  
Access requests: requester, participant/resource/purpose, result, reason and timestamp.  
Audit events: event type, actor/service, references, timestamp, outcome and reason.

Avoid direct identifiers and mental-health content.

## 7. Security boundaries

For the demonstrator: synthetic data only; backend input validation; server-side role checks; AI credentials stored only on the server; no direct AI database access; allow-listed tools; no AI override of consent or permission results; default deny when state is uncertain; no logging of secrets or unnecessary personal information.

Before real-world use, qualified engineering and security review must address authentication, authorisation, threat modelling, encryption, key management, database hardening, secure hosting, backups, monitoring, incident response, retention, deletion, audit integrity and applicable privacy/legal requirements.

## 8. Integration boundary

CORA is a standalone application with an API. An adopting platform can call the access-check endpoint from its trusted backend before releasing data. A developer must map identities and resource identifiers and ensure every relevant data-release path is protected.

CORA cannot prevent use of a dataset already copied outside the system it controls. No SRHIN integration is included or claimed.

## 9. AI-provider independence

Consent and permission logic must work without an AI provider. If AI is unavailable, participants can still use forms, requesters can still submit access checks and administrators can still inspect audit events.

## 10. Architecture decision

AI is the central conversational operator, but not the policy authority or access-control engine. This prevents uncertain language-model output from becoming a consent or data-access decision.
