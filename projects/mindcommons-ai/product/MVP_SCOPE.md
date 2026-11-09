# Minimum Viable Product — Three-Capability Scope

**Status:** Proposed scope for validation and fellowship planning. This is not an instruction to build a prototype now.

## One workflow

**Approved data use → proposed material change → authorised human decision → traceable conditions and community-agreed follow-up.**

The MVP is deliberately limited to three connected capabilities.

## 1. Approved-use record

Minimum fields:
- Reference to the data resource (no participant-level records).
- Plain-language approved purpose.
- Conditions / restrictions.
- Authorising body and decision date.
- Link to the authoritative approval / consent-policy record.
- Current status and next review date.

**Acceptance test:** An authorised steward can identify the approved purpose, conditions, decision authority and source record without searching across disconnected documents.

## 2. Change-of-use review

Minimum fields:
- Existing approved-use reference.
- Description and reason for the proposed change.
- New purpose, collaborators, AI/model-development involvement and duration, where relevant.
- Supporting documents / ethics references.
- Missing-information checklist.
- Assigned decision authority.
- Human decision, rationale, conditions and review date.

AI assistance: prepare a structured summary, flag missing fields and compare the proposal with approved, machine-readable conditions. All flags are advisory and source-linked.

**Acceptance test:** A reviewer can see what is changing, which approved conditions may apply, what evidence is missing and which human authority must decide.

## 3. Community-obligation follow-up

Minimum fields:
- Commitment wording as agreed by authorised community/host parties.
- Linked approved data use and decision.
- Responsible owner.
- Due date / review date.
- Status and update.
- Evidence or source link.

Examples could include returning findings in an agreed format, community feedback sessions, contributor recognition or other locally agreed benefits. These are examples only; the community defines the actual commitments.

**Acceptance test:** An authorised community steward can identify each agreed commitment, its owner, progress and source decision.

## AI across the workflow

One role-aware assistant:
- Explains the approved record and links its source.
- Helps prepare a change request.
- Identifies missing information and potential condition conflicts.
- Drafts reviewer summaries.
- Summarises overdue or upcoming obligations.

No independent access decision, ethics decision, consent decision, policy creation or benefit allocation.

## Out of scope

- New consent capture or participant portal.
- Data collection, storage or curation.
- Clinical screening, diagnosis or therapy.
- Full research project management.
- Replacement ethics / governance process.
- Generic KPI or organisational dashboard.
- Public participant-level data.
- Automatic payment or benefit distribution.
- Blockchain, tokens or complex multi-agent architecture.
- Unapproved integration with Gencurate or any SRHIN system.

## Validation gates before implementation

1. SRHIN confirms whether an approved-use register already exists.
2. SRHIN and community partners explain how material use changes are reviewed today.
3. They confirm whether benefit commitments are already tracked and what is missing.
4. They identify authoritative systems, record owners and permitted data.
5. Community partners approve what transparency means and what may be shown.
6. Privacy, ethics and security specialists review the proposed minimum data and AI boundary.
7. A small workflow test demonstrates reduced effort without duplicate records.

If these gates show no meaningful unmet need, do not build the MVP.
