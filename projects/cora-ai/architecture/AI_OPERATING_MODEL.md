# CORA AI — AI Operating Model

## Purpose

The AI assistant is the main conversational operating interface inside CORA AI. It helps participants, requesters and administrators understand and navigate the application. It is not an autonomous authority over consent or data access.

## Guided consent conversation

For a participant considering a consent choice, the assistant follows a deliberate sequence:

1. Identify the exact resource/dataset and purpose being discussed.
2. Explain what is being requested, why, and the relevant limits in plain language using approved project information.
3. Invite questions and clarify uncertainty without steering the person towards a grant.
4. Present the available choices: grant, refuse, or—where a current grant exists—withdraw.
5. Read back the exact choice and ask for a separate, unambiguous final confirmation.
6. Submit the confirmed participant action through the authorised application operation; the backend validates identity, role, purpose and state transition, then records the event.
7. Show the recorded result and explain how the person can review or withdraw a grant later.

Silence, general agreement, emotional language, a question, or an ambiguous message is not consent. If the participant changes topic, appears uncertain or does not confirm, no consent mutation is submitted. The assistant must not use persuasion, urgency or dark patterns.

## What the assistant can do

- Explain each defined purpose in plain language.
- Explain the current consent status visible to the signed-in user.
- Guide a participant through the consent interface without recommending a particular choice.
- Help a requester prepare an access request.
- Check whether required request information is missing.
- Invoke the backend access-check operation and explain the returned result.
- Summarise audit events the current user is authorised to view.

## Approved tools

The assistant receives only narrowly scoped tools:

1. Purpose explanation.
2. Authorised consent-status lookup.
3. Request completeness check.
4. Access permission check.
5. Authorised audit-history summary.

Tool inputs are validated by the backend. Role permissions are checked on every request. The assistant cannot query arbitrary database tables or create unrestricted SQL/API calls.

## Actions that remain outside AI authority

The assistant cannot grant, refuse or withdraw consent by itself; approve access; reverse an access denial; change a participant's recorded choice; invent or amend a purpose; make an ethics decision; or reveal information outside the current user's permissions.

A participant's choice must be an explicit, authenticated action in the application. The backend validates and records it. The assistant may guide the person to that action and prepare the exact operation, but an AI-generated suggestion or inferred intent is never a consent record.

## Access decision sequence

The backend receives the access request, checks the caller's permissions, retrieves the current consent state for the exact participant/resource/purpose, applies deterministic rules and returns ALLOW or DENY. The audit service records the request and result. The assistant may explain the result after it is returned, but cannot alter it.

## AI-provider failure

The core application must continue to function when the model provider is unavailable. Forms and API endpoints still support consent, withdrawal, access checks and audit history. AI is an assistant layer, not a dependency for enforcement.

## Privacy and prompt boundaries

Only the minimum authorised information needed for the current task may be sent to the model provider. The MVP uses synthetic records. The static browser demonstration is not a secure channel for sensitive personal information. Secrets remain server-side. The assistant must not be given direct database credentials or unrestricted record access.

Before production, the adopting organisation must assess provider data handling, retention, logging, regional processing, contractual terms and whether any sensitive information may be sent to the selected model provider.

## Evaluation tests

- Assistant explains purposes without changing the participant's choice.
- Assistant cannot call a consent-write operation without an explicit authenticated application action.
- Assistant cannot override a denied access result.
- Assistant cannot retrieve records outside the user's role.
- Assistant clearly communicates missing or ambiguous information.
- Core application works when the AI provider is disabled.
