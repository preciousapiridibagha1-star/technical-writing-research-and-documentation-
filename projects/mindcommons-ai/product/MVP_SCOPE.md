# Minimum Viable Product (MVP)

## MVP goal

Define the smallest useful version of MindCommons AI that demonstrates the core community-governed data-use journey without attempting to replace SRHIN's existing platforms.

The MVP is a product scope document. It is not a prototype or implementation commitment.

## 1. Core modules

### A. Participant Centre — consent and permissions

Participants can:
- Read plain-language explanations of how their information may be used.
- Review purpose-specific permissions.
- See the status and scope of their choices.
- Find out how to ask questions or request a change.
- Understand any limits on changing or withdrawing permission after data has been used.

AI assistance: explain approved consent text, answer questions from approved materials and guide participants through the available options. The participant makes the choice.

### B. Researcher Workspace — data-use requests

Researchers can:
- Describe their organisation and research purpose.
- Specify the data or data category requested.
- Explain intended use, duration and whether AI model development or commercial use is involved.
- Provide required ethics and privacy information.
- Submit a request and track its status.

AI assistance: guide form completion, identify missing information, explain request requirements and prepare a readable request summary.

### C. Governance & Community Workspace — review and decisions

Authorised reviewers can:
- View incoming requests.
- See relevant consent conditions and community rules.
- Review AI-generated summaries and flagged issues.
- Request clarification.
- Refer a request for ethics or community review.
- Record an approval, rejection or conditional decision with reasons.

AI assistance: compare the request with approved, structured rules; flag conflicts and missing evidence; prepare a review brief. Human and community authorities retain decision-making power.

### D. Transparency & Community Benefits

Authorised users can:
- Review request and decision histories.
- See who reviewed a request and why it was decided.
- Monitor changes to permissions and governance rules.
- Record agreed community benefit commitments, responsible parties and progress.
- Produce public-safe, aggregated summaries.

AI assistance: answer authorised questions about records, summarise activity and prepare benefit progress reports. Private participant information is never exposed in public reports.

## 2. AI assistant in the MVP

The MVP includes one coordinated AI assistant with role-aware capabilities. It appears as a chat panel or assistant button inside the relevant dashboard.

The assistant uses approved platform information and only retrieves records the signed-in user is allowed to see. It can prepare information and suggest next steps, but it cannot bypass application permissions or perform high-impact actions without the required human confirmation.

## 3. Core end-to-end journey

1. A participant receives an understandable explanation and makes a specific data-use choice.
2. The platform records the participant's choice and the applicable community governance rules separately.
3. A researcher submits a request for a defined use.
4. The application checks the request against relevant permissions and rules.
5. The AI assistant prepares a summary and flags missing information or possible conflicts.
6. The request is routed to the appropriate human or community review.
7. An authorised decision-maker records the decision and reasons.
8. The platform records the event and updates the request status.
9. Appropriate community representatives can review permitted transparency information and track agreed benefits.

## 4. What is included in the MVP

- Role-based workspaces for participants, researchers and authorised reviewers/community representatives.
- Plain-language consent and permission information.
- A structured data-use request form.
- A rule-based permission and policy check.
- An AI assistant for explanations, form guidance, summaries and review support.
- Human approval and escalation workflow.
- Decision and activity records.
- Basic benefit commitment tracking.
- Privacy-aware reporting.

## 5. What is not included in the MVP

- A new mental-health screening or diagnosis tool.
- A general-purpose therapy or wellbeing chatbot.
- Training a new foundation model.
- AI making final access or ethics decisions.
- A public database of participant records.
- Automatic payments or distribution of benefits.
- Blockchain or token-based governance.
- Complex multi-agent infrastructure.
- Replacing GENSCORE, Gencurate or other SRHIN systems.
- Unverified integrations with existing SRHIN platforms.

## 6. MVP design rules

- Keep the first release to the four core modules and one coordinated AI assistant.
- Use structured rules for permissions; do not ask a language model to invent or interpret access authority on its own.
- Keep individual consent separate from collective/community governance.
- Show why a request was flagged and what human review is required.
- Use minimum necessary information.
- Make AI-generated summaries visibly identifiable and reviewable.
- Provide a non-chat route for every essential task, so people are not forced to use AI.
- Design for mobile screens, low bandwidth and clear language.

## 7. Questions before the MVP can be finalised

- Which parts of this scope are already supported by SRHIN's systems?
- What community governance model will be used?
- Who can define and change permitted data-use rules?
- Which users and communities should be involved in the first pilot?
- What local languages and accessibility needs must be supported first?
- What integrations are technically and institutionally possible?
- What legal, ethics, safeguarding and privacy requirements must be built into the design?

The MVP scope should be revised after these questions are answered with SRHIN and community partners.
