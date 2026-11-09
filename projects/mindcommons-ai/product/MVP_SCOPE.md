# Minimum Viable Product — Validation-First Scope

## Purpose

This document defines the smallest product scope worth validating. It is **not a decision to build a prototype**.

The original four-module concept was too broad and risked duplicating Gencurate, LEWG, the Human Oversight Charter, existing governance procedures and SRHIN's reporting arrangements. The MVP hypothesis is now deliberately narrower.

## 1. Core workflow to investigate

**A proposed change or new use of an existing mental-health data resource → relevant governance conditions are identified → authorised review takes place → the decision and follow-up commitments are traceable.**

This workflow is worth pursuing only if SRHIN confirms that current systems do not already support it adequately.

## 2. Candidate MVP components

### A. Data-use register
A role-restricted, plain-language record of:
- Approved data-use purposes or categories.
- Applicable conditions and restrictions.
- Responsible governance body or decision authority.
- Approval status and review date.
- Links to the authoritative source record.

The application should reference existing records where possible rather than copy sensitive datasets or participant details.

### B. New-use / change request
An authorised researcher can submit:
- Research purpose and public benefit.
- Data category requested.
- Intended collaborators and recipients.
- Whether AI training, model evaluation or commercial activity is involved.
- Proposed duration, safeguards and ethics approvals.
- What has changed from a previously approved use.

### C. Governance review workspace
Authorised reviewers can:
- See the request and the applicable documented conditions.
- View missing information and potential conflicts.
- Route the proposal to the appropriate community, lived-experience or ethics authority.
- Record a human decision, conditions, rationale and review date.

### D. Community accountability view
Appropriately authorised community representatives can:
- See privacy-preserving summaries of approved uses.
- Review outstanding conditions and follow-up actions.
- Monitor agreed benefit commitments and their status.
- See the responsible party and evidence of progress, where disclosure is appropriate.

Benefit arrangements must be defined by the community and host partners. The application only records and reports them.

## 3. AI assistant

One coordinated AI assistant is a core capability within the workflow. It can:
- Explain an approved governance condition.
- Help complete a new-use request.
- Identify missing fields or documents.
- Compare a proposal against structured, approved conditions.
- Prepare a concise review summary with links to source records.
- Explain status and follow-up actions to authorised users.

The assistant must show its sources and distinguish confirmed rules from missing or ambiguous information. It must say when it cannot determine an answer.

AI cannot:
- Approve, reject or grant access.
- Change consent or governance rules.
- Decide whether a proposal is ethically acceptable.
- Override LEWG, ethics boards or community authority.
- reveal sensitive records to a user without permission.

## 4. What is deliberately excluded

- Replacing Gencurate's consent and data-curation workflow.
- Creating a new lived-experience governance group or ethics board.
- Replacing SRHIN's charters, SOPs, escalation process or audit arrangements.
- Collecting or storing raw participant mental-health data.
- Clinical screening, diagnosis or treatment.
- Automatic benefit payments.
- Blockchain, tokens or complex multi-agent architecture.
- Any unverified integration.

## 5. Validation gates before an MVP can be approved

1. **Workflow confirmation:** SRHIN maps how new and changed data uses are handled today.
2. **Gap confirmation:** community stewards and relevant reviewers identify a specific pain point, not just a feature preference.
3. **Non-duplication:** the proposed interface is shown to complement existing systems and not create a parallel source of truth.
4. **Authority mapping:** SRHIN and community partners identify who can view, recommend, approve, reject and appeal.
5. **Data minimisation:** agree which metadata is needed and what must remain in existing secure systems.
6. **AI suitability:** confirm which tasks benefit from AI and which should remain ordinary forms, rules or human decisions.
7. **Evaluation:** agree a baseline and measures such as review traceability, completeness, turnaround time, user understanding and administrative burden.

If these gates show that current processes already work well, do not build the proposed application. A research or documentation contribution may be more useful.

## 6. Status

Validation-first product scope only. No prototype or implementation is underway. No SRHIN workflow, API, partnership or community requirement is assumed.
