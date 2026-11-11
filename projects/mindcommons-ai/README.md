# MindCommons AI
## Community Data-Use Accountability Ledger

**One-line concept:** A small, AI-assisted workspace that helps community-authorised stewards trace approved mental-health data uses, review proposed changes and follow up on community-agreed obligations.

**Project status:** Desk research and product specification only. No prototype, host approval, integration or community validation is claimed.  
**Host context:** SRHIN / Mozilla Foundation 2027–2028 Track I Embedded challenge.  
**Relationship:** Independent project hypothesis; not commissioned, endorsed or operated by SRHIN.

## The problem we are investigating

SRHIN already publicly documents important foundations: Gencurate consent and data curation, lived-experience co-governance through LEWG, independent ethics oversight, governance charters, escalation procedures and public resources on lived-experience authority and compensation.

We should not rebuild those.

The remaining question is narrower: **when an already-governed mental-health data resource is proposed for a new or changed use, can the community-authorised decision, its conditions and any agreed benefit obligations be traced together in a clear, privacy-preserving way?**

Public materials do not establish whether SRHIN already has an internal process for this. This is a gap to validate, not a confirmed deficiency.

## The smallest useful product: three capabilities

1. **Approved-use record** — a plain-language, role-restricted record of the approved purpose, applicable conditions, responsible decision authority, review date and link to the authoritative source. It references existing consent and governance records; it does not collect consent again or store participant-level data.
2. **Change-of-use review** — a structured request when purpose, collaborator, model-development activity or another material use changes. It identifies the relevant existing conditions, routes the proposal to the authority designated by SRHIN/community rules, and records the human decision and conditions.
3. **Community-obligation follow-up** — a traceable record of community-agreed commitments attached to an approved use, including responsible party, due date, evidence/update and status. It does not determine what benefits are fair or promise financial distribution.

### AI is built into the workflow

One contextual AI assistant can explain approved conditions, help complete a change request, identify missing information, prepare a reviewer summary and summarise outstanding obligations. It must cite the source records it used, admit when information is missing and stay within the user's permissions.

**AI never grants access, approves a change, changes consent, invents policy or overrides community decision-makers.** Application permissions and authorised human decisions control all consequential actions.

## Why this is different from existing SRHIN work

- Not Gencurate: no new voice collection, consent capture, annotation or clinical review.
- Not LEWG: no new governance body, charter or authority matrix.
- Not the Data, Ethics & Safety Monitoring Board: no replacement oversight or ethics review.
- Not a generic KPI dashboard: it tracks only the lifecycle of a specific approved use, its conditions and its agreed obligations.
- Not a new research portal: it does not manage research projects generally.

It is a proposed thin accountability layer across existing authoritative records—only if SRHIN confirms that the workflow is not already adequately supported.

## Research-to-design documents

1. [Research and gap analysis](research/RESEARCH_AND_ANALYSIS.md)
2. [Product definition](product/PRODUCT_DEFINITION.md)
3. [Three-capability MVP](product/MVP_SCOPE.md)
4. [Logical system architecture](architecture/SYSTEM_ARCHITECTURE.md)
5. [Product experience](design/PRODUCT_EXPERIENCE.md)
6. [Dashboard layout concept](design/DASHBOARD_LAYOUT.md)
7. [Source register](references/SOURCES.md)

## Validation questions that decide whether to proceed

- Does an internal register already connect each approved data use to its conditions and source decision?
- Is there an established route for new or changed purposes, collaborators or model-development uses?
- Can authorised community stewards trace the decision and its follow-up without requesting multiple manual reports?
- Are community-agreed benefit commitments linked to the relevant data use and tracked already?
- Would a small shared view improve oversight, or duplicate records and add administrative burden?

If SRHIN already does these things well, stop or redirect the concept. Do not build a duplicate system.

## Naming and status

MindCommons AI is a provisional working name, not a cleared brand. The product is a research-backed design hypothesis, not a working application.
