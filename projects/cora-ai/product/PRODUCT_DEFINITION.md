# Product Definition — CORA AI
## Community-Owned Rights & Access

## 1. Purpose

CORA AI is a small open-source application for recording purpose-specific consent and checking whether a requested data use is permitted by the current consent record. It consists of one web application and a small REST API. The MVP is limited to consent records, access permission checks and audit history.

## 2. Intended users

- Participant: reviews plain-language purposes, grants or refuses permission, and withdraws a previously granted permission.
- Requester: submits a request for a defined data resource and purpose.
- Administrator/data steward: manages synthetic demo records and inspects consent status and audit events.
- Integrator/developer: connects another application's trusted backend to the CORA API.

A requester cannot change participant consent. An administrator cannot silently rewrite a participant's choice. Privileged corrections, if implemented, must be attributable and audited.

## 3. Three capabilities

### A. Purpose-specific consent records

Each record contains a pseudonymous participant ID, resource/dataset ID, purpose, status (granted, refused or withdrawn), consent text/version and timestamp. Choices are stored separately. Granting research permission does not imply permission for AI model training.

### B. Access permission checks

A request identifies the participant, resource and exact purpose. The backend checks the current matching consent record and returns ALLOW or DENY with a reason. Missing, refused, withdrawn or mismatched permission is denied. The default is deny when information is missing or ambiguous.

The check must be called by the system that actually controls access to the data. A consent checker cannot retrieve or delete copies of a dataset already held elsewhere.

### C. Audit history

Record consent grants, refusals, withdrawals, access requests, approvals and denials. Each event includes event type, pseudonymous references, purpose, timestamp, actor/service, outcome and reason. Ordinary users cannot edit or erase historical events through the application. Production tamper resistance requires further engineering.

## 4. AI assistant as operating interface

One integrated AI assistant helps users understand and navigate the application. It can explain purposes and consent status, guide users through forms, help prepare requests, identify missing fields, call approved read/check tools, explain backend decisions and summarise authorised audit events.

It cannot choose or grant consent, withdraw consent without an explicit authenticated action, approve access, override a denial, invent policies or access restricted records.

The assistant invokes a small allow-list of application tools. The backend independently validates every tool call and enforces role permissions. The AI has no direct database credentials or unrestricted write capability. Consequential actions require explicit user action and server-side validation. The core application works without an AI provider.

## 5. Demonstration

Use synthetic participant P001 and dataset D001. Grant research consent; refuse AI-training consent; verify that research access is allowed and AI-training access denied; withdraw research consent; verify that a new research request is denied; inspect the chronological audit history.

## 6. Minimum quality requirements

Clear purpose labels; default-deny checks; server-side validation; role separation; minimal pseudonymous data; no real health data; constrained AI tools; automated tests for consent and access rules; understandable decision reasons; reproducible local setup.

## 7. Exclusions

No clinical functions, screening, diagnosis, therapy, mental-health chatbot, participant health-record repository, general research portal, automatic ethical review, automatic benefit-sharing, blockchain, federated learning, differential privacy, advanced cryptography, native mobile app, multiple agents or production integrations.

## 8. Completion criteria

The synthetic workflow works end to end; all three capabilities are tested; the AI assistant guides operation without authority to grant access or alter consent; the REST API is documented; and another developer can install and run the application from the repository instructions.

## 9. Handover

The deliverable is a documented open-source MVP, not an ongoing hosted service. The adopting organisation is responsible for assigning a maintainer and technical operator before production use.
