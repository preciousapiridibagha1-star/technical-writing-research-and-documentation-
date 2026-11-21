# CORA AI — Product Experience

## Product promise
Help a participant record separate choices for defined data uses, help a requester check whether a specific use is permitted, and give authorised administrators a clear audit history.

## Main screens
1. Participant consent: clear purpose descriptions with grant, refuse and withdraw actions.
2. Consent status: current choice shown separately for each purpose.
3. Access request: requester selects a synthetic participant/resource and exact purpose.
4. Decision result: clear allow/deny outcome and reason from the backend permission service.
5. Audit history: chronological consent and access events for authorised administrators.
6. AI assistant: contextual conversational guide available throughout the application.

## AI experience
One integrated assistant is the central conversational guide across the application. It explains purposes and consent status, helps users navigate, checks request completeness and explains system results.

For consent, the assistant identifies the exact dataset and purpose, explains the request in plain language, answers questions, presents grant/refuse/withdraw choices, reads back the selected choice and asks for explicit final confirmation. Only then may it submit the participant's action to the backend for authentication, validation and recording. Ambiguous language, silence or general agreement must never be treated as consent. The assistant must not pressure a participant towards granting permission.

The assistant cannot decide for a participant, approve data access or override backend decisions. Core consent and permission functions must remain available if the AI service is unavailable; this preserves the locked MVP's resilience requirement.

## Experience principles
- One application, not multiple portals.
- Plain language and explicit purpose descriptions.
- Consent choices are separate; one purpose never implies another.
- Withdrawal is visible and straightforward.
- Show the reason for an access decision.
- Keep data entry minimal.
- Use synthetic data only in the demonstrator.
- Mobile-friendly and low-bandwidth-conscious without building a native mobile app.

## Demo content
Use fictional participant P001 and dataset D001. Show research granted, AI training refused, research access allowed, AI training denied, research withdrawn and subsequent research access denied. The audit history must show the sequence.

## Boundary
This design describes the locked MVP only. It does not define a future platform expansion or claim production readiness.
