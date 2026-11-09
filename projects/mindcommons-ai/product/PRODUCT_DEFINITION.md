# Product Definition — MindCommons AI
## Community Data-Use Accountability Ledger

## 1. Product decision

The original proposal—a complete platform with consent management, researcher portal, governance workspace, community dashboard and AI assistant—was too broad and overlapped with substantial SRHIN work already described publicly.

The revised proposal is one narrow workflow: **trace an approved mental-health data use, review a material change to that use, and follow up on community-agreed obligations.**

This is the smallest product hypothesis that could still contribute meaningfully to the host challenge's themes of community governance, privacy and benefit-sharing.

## 2. Problem statement

SRHIN publicly describes Gencurate consent and curation, LEWG, a Data, Ethics & Safety Monitoring Board, a Human Oversight Charter, governance procedures and resources for lived-experience authority and compensation.

What public materials do not clearly establish is whether a community-authorised steward can follow one approved data use across its lifecycle: the authoritative decision, the conditions attached to it, any later change request, and the community-agreed obligations arising from it.

This is a public-documentation gap and a research question—not proof that SRHIN lacks an internal workflow.

## 3. Intended users

- Community-authorised stewards and lived-experience representatives, within their agreed authority.
- Authorised governance / ethics reviewers.
- Researchers submitting a proposed change to an existing approved use.
- Administrators responsible for maintaining the record and permissions.

The product does not create new decision-making authority or presume that all participants need another portal.

## 4. Three capabilities only

### A. Approved-use record
A minimal record containing:
- Data resource or dataset reference (not a copy of participant data).
- Approved purpose and permitted-use summary.
- Conditions and restrictions.
- Decision-making authority and date.
- Authoritative decision / consent-policy reference.
- Review date and current status.

### B. Change-of-use review
A structured request for a material change such as a new purpose, collaborator, AI/model-development activity or other change defined by SRHIN's own policy.

The system:
- Captures the proposed change and supporting evidence.
- Retrieves or links the relevant approved conditions.
- Flags missing information and possible conflicts for human review.
- Routes the request according to an authority map approved by SRHIN and community partners.
- Records the human decision, rationale, conditions and review date.

It does not decide whether the change is ethically or legally permissible.

### C. Community-obligation follow-up
A restricted record of commitments explicitly agreed by the relevant community and authorised parties, such as reporting back, returning findings, access to outputs, contributor recognition or other agreed forms of benefit.

It records owner, due date, status, evidence and update history. It does not define benefits, calculate entitlements or automatically distribute money.

## 5. AI assistant: one assistant, bounded tasks

AI is integrated into these three capabilities. It can:
- Explain an approved condition in plain language with a source link.
- Help a researcher draft a complete change request.
- Identify missing information against a published checklist or approved rule.
- Prepare a concise review brief showing the proposal, relevant conditions and uncertainty.
- Summarise due community commitments for authorised users.

AI cannot grant data access, approve requests, change consent, invent or reinterpret governance rules as binding, decide benefit fairness, or expose restricted information. The application enforces role and record permissions before AI receives context.

## 6. How it complements existing SRHIN work

| Existing SRHIN capability publicly described | What MindCommons will not recreate | Narrow complementary question |
|---|---|---|
| Gencurate consent-before-collection, annotation and clinical review | Collection, consent capture, curation or clinical review | Is a distinct later-use/change record needed after the initial approved workflow? |
| LEWG, Human Oversight Charter and Epistemic Authority Decision Matrix | Governance body, charter or authority model | Can existing decisions be referenced consistently in each use-change record? |
| Data, Ethics & Safety Monitoring Board, escalation procedures and SOPs | Ethics board or review authority | Is it difficult to route a specific change to the already-designated authority and retain its conditions? |
| Public reporting and governance dashboards | Generic organisational KPI dashboard | Is there a missing trace for one data use from decision through obligations? |
| Compensation and governance template | New benefit-sharing policy | Are specific commitments already agreed but difficult to track against the relevant use? |

## 7. Product value if the gap is confirmed

For community stewards: a clearer way to see what was approved, under what conditions, what has changed and what commitments remain.

For authorised reviewers: a concise, traceable change request with the source decisions and missing evidence visible.

For SRHIN: a possible reduction in manual cross-referencing and follow-up effort, without replacing authoritative systems. This benefit must be measured, not assumed.

For researchers: clearer requirements and fewer incomplete submissions.

## 8. Success measures to co-define

Possible measures, subject to baseline and community approval:
- Time required to trace a proposed change to the relevant decision and conditions.
- Percentage of change requests submitted with required information.
- Percentage of decisions with clear authority, rationale and conditions recorded or linked.
- Percentage of community-agreed obligations with an owner, due date and status.
- User-reported clarity and administrative burden.
- Duplicate data entry or records created (target: minimise).

No performance improvement is claimed before evaluation.

## 9. Privacy and authority

- Store references and minimum metadata, not participant-level mental-health records.
- Do not copy consent records when a secure authoritative reference is sufficient.
- Separate individual consent constraints from collective governance decisions.
- Apply role-based access at the application layer.
- Log access and material record changes.
- Use only approved, source-linked rules for AI-assisted comparisons.
- Escalate ambiguity to authorised humans.
- Community partners decide what may appear in any community-facing view.

## 10. Explicit exclusions

No new consent portal, participant data repository, clinical tool, generic research-management portal, governance body, general-purpose chatbot, blockchain, automatic benefit payments, AI approval authority or replacement for GENSCORE/Gencurate.

## 11. Status and dependencies

Research and product specification only. The project must not proceed to implementation until SRHIN and community partners confirm the workflow gap, decision rights, minimum data, privacy requirements, existing system boundaries and value of a new interface. If existing processes already solve the problem, stop or redesign.
