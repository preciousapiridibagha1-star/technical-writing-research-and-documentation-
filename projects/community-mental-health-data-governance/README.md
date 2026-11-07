# Community Mental Health Data Governance Demonstrator

**Status:** Proposed self-directed prototype — work not yet started  
**Purpose:** Explore how community-centred consent, data-use permissions and accountability could be represented in a small, inspectable software demonstration.  
**Relationship to SRHIN:** This is an independent learning and portfolio project inspired by the SRHIN challenge description reproduced in the applicant's research dossier. It is not an SRHIN-approved project, partnership, commissioned deliverable or representation of SRHIN's internal systems.

## 1. Problem being explored

Mental-health data can be valuable for research and the development of AI-supported services. However, people and communities need meaningful ways to understand and influence how information about them is collected, accessed and reused.

This project explores a narrow technical question:

> Can a small software demonstrator make consent choices, permitted data-use purposes and access decisions visible and auditable?

The prototype will not claim that software alone creates community ownership or legitimate consent. Those require appropriate governance, community participation, legal and ethical review, and accountable institutions.

## 2. Intended users in the demonstration

All users and records in the prototype will be fictional:

- **Participant:** reviews a plain-language data-use notice and makes a purpose-specific choice.
- **Researcher:** submits a request to use a fictional record for a stated purpose.
- **Governance reviewer:** reviews requests where a policy or consent rule requires human review.
- **Auditor:** inspects a history of consent changes and access decisions.

These are demonstration roles, not claims about SRHIN's actual staffing or operating model.

## 3. First prototype workflow

1. A fictional participant is shown a clear explanation of a proposed data use.
2. The participant grants or declines permission for a specific purpose.
3. A fictional researcher requests access and states the intended purpose.
4. The application checks the request against the recorded permission.
5. The application allows, rejects or flags the request for human review according to the prototype rules.
6. The application records the decision and relevant event in an audit history.
7. The participant can review or withdraw a permission in the demonstration.

## 4. Initial technical scope

The first version should remain deliberately small:

- A simple web interface.
- Synthetic participant and research records only.
- Purpose-specific consent records.
- A basic role and permission model.
- A request-and-decision workflow.
- An append-only-style event history for demonstration purposes.
- Automated tests for the key permission rules.
- Clear setup instructions so another person can run the project.

The implementation technology will be selected after checking what can be built, tested and maintained reliably within the available time. External AI APIs are not required for the first version; adding AI without a genuine need would distract from the governance problem.

## 5. What this prototype will not do

- It will not collect, store or process real patient or participant data.
- It will not diagnose, screen, treat or provide mental-health advice.
- It will not claim legal compliance, production security or clinical validation.
- It will not claim that a participant's click alone establishes meaningful community consent.
- It will not represent itself as a complete data commons or production data-trust platform.
- It will not claim to be built for, endorsed by or deployed at SRHIN.

## 6. Safety, privacy and governance principles

- Use synthetic data and clearly labelled fictional identities.
- Collect the minimum information needed for the demonstration.
- Make each proposed data-use purpose understandable and distinct.
- Make permission changes and withdrawal visible in the workflow.
- Record why an access request was allowed, rejected or escalated.
- Keep human review visible where a rule is ambiguous or consequential.
- Document limitations and unresolved ethical, legal and security questions.
- Do not treat an audit log as proof that an organisation behaved ethically.

## 7. Evidence to publish

As work progresses, this repository should contain:

- Source code and reproducible setup instructions.
- A system architecture and data-flow diagram.
- A concise requirements specification.
- A threat, privacy and misuse review appropriate to the prototype's scope.
- Tests and their actual results.
- Screenshots or a short demonstration recording.
- A changelog of implemented features and known limitations.

Only completed and verified work will be labelled implemented or tested.

## 8. Questions for expert and community review

Before any real-world use, the concept would need review with relevant community representatives, people with lived experience, qualified mental-health practitioners, data-protection/privacy specialists and the host organisation if a collaboration were ever agreed.

Questions include:

- Who defines acceptable data-use purposes?
- How are collective/community decisions represented alongside individual choices?
- What happens when individual preferences and community governance decisions conflict?
- Who can authorise access, and how can that authority be challenged?
- What does meaningful withdrawal mean after data has already been used?
- What benefit-sharing arrangements are appropriate and who decides?
- What legal, safeguarding and data-protection requirements apply?

## 9. Current status

At the time of this README, this is a project specification, not a working application. The prototype, tests, diagrams and demonstration remain to be built. This status will be updated only when there is verifiable implementation evidence.

## 10. Licence

A suitable open-source licence will be added when the initial code and dependency choices are established. Until then, do not assume that the project has already been released under an open-source licence.
