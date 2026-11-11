# Research and Gap Analysis
**Review date:** 9 November 2026  
**Method:** Desk research of publicly available Mozilla, SRHIN, GENSCORE and Knowledge Hub materials.  
**Status:** No internal system access, staff interviews or community consultation.

## 1. Host challenge

Mozilla's official 2027–2028 call lists Slum & Rural Health Initiative (SRHIN), Nigeria, as a Track I Embedded host. The official call directs applicants to the full RFP for the host-specific challenge. The detailed challenge wording available in a third-party reproduction describes community-owned approaches to mental-health data governance, consent, privacy and benefit-sharing, with young people, people with lived experience and community health workers involved.

**Verification note:** The host-specific wording must be checked against the original Mozilla RFP before final application use. The third-party reproduction is not treated as the official source.

## 2. Existing SRHIN capabilities — significant and directly relevant

The public GENSCORE materials describe:
- Gencurate as the data engine through which voice notes, interviews and narratives pass before model use.
- Informed consent before recording, in the speaker's preferred language.
- Human annotation and clinician review before material joins the training corpus.
- Monitoring representation across language, gender, age and region.
- A Lived Experience Working Group (LEWG).
- A Data, Ethics & Safety Monitoring Board.
- A written Governance Charter and Human Oversight Charter.
- Escalation protocols, SOPs, monthly governance/performance dashboards, quarterly reports and annual external audits.
- Ethics approvals, de-identification, encryption and restricted access.

The SRHIN Knowledge Hub adds practical public resources:
- A Basic Guide for People with Lived Experience to Get Involved in AI Mental Health Tool Design.
- The LEEF Checklist for pre-launch review of digital mental-health tools.
- A Template for Lived Experience Compensation and Governance.
- The Co-Production Readiness Self-Assessment.
- The Epistemic Authority Decision Matrix.

These are concrete evidence that SRHIN is already working on consent, privacy, lived-experience participation, governance and accountability. It would be inaccurate to claim those capabilities are absent.

## 3. What must not be proposed again

The broad original idea included a consent portal, researcher portal, new governance workspace, community dashboard and general AI chatbot. This is too large and overlaps with public SRHIN work.

Do not propose:
- Rebuilding consent collection or Gencurate.
- Creating another lived-experience governance body or authority framework.
- Replacing the ethics board, charter, SOPs or escalation routes.
- A generic organisational performance dashboard.
- A new research-management portal.
- A chatbot without a specific, validated workflow.

## 4. Narrow gap hypothesis

The narrowest potentially useful gap is **traceability for an approved data use across a material change and its community-agreed obligations**.

The public pages reviewed explain collection consent, curation, clinical review, governance bodies, charters, SOPs and reporting. They do not clearly show whether a community-authorised steward can follow a specific approved data use through:
1. Its approved purpose and conditions.
2. A later proposed change in purpose, collaborator or model-development use.
3. The authority that reviews the change and the conditions attached to the decision.
4. Any community-agreed benefit or accountability commitments linked to that use.

This is not proof that SRHIN lacks the process. It may exist in internal registers, contracts, Gencurate, SOPs or manual practice. The proposed tool should only proceed if the workflow is currently difficult, fragmented or insufficiently visible to authorised community stewards.

## 5. The focused product

**MindCommons AI — Community Data-Use Accountability Ledger**

Three capabilities only:
1. Approved-use record: reference approved purpose, conditions, authority, date and source.
2. Change-of-use review: capture a material change, surface relevant approved conditions, route it to the correct human authority and record the decision.
3. Community-obligation follow-up: track commitments that the community and authorised parties have actually agreed to.

One integrated AI assistant supports explanations, request completeness, source-linked comparisons and summaries. It does not make decisions.

The design stores minimal metadata and source references, not participant-level mental-health records. It does not collect consent again.

## 6. Why this may be valuable

The host challenge is about community control over mental-health data used in AI and fair distribution of benefits. If existing systems already handle initial consent and governance, a narrow traceability layer could help preserve community authority as proposed uses change over time and keep agreed obligations visible.

Potential value:
- Community stewards can see what was approved, by whom, under what conditions and what follow-up is due.
- Reviewers receive a structured change request linked to the existing source decisions.
- Researchers see what information is required before submission.
- SRHIN may reduce manual cross-referencing and follow-up work, if this is a current burden.

These are expected benefits, not demonstrated outcomes.

## 7. Questions that decide go / no-go

Ask SRHIN and community representatives:
- Is there already a register linking each approved use to the relevant consent constraints, decision and conditions?
- How are new purposes, new collaborators, commercial use or model-development changes handled?
- Can the relevant community-authorised stewards see the status and rationale they are entitled to see?
- Are conditions attached to the use and checked at the point of a later change?
- Are community-agreed benefits linked to a specific data use and followed up?
- Which current tool, register, contract, SOP or manual process is authoritative?
- What is the real administrative or community oversight pain point?
- Would a small ledger solve it or create duplicate administration?

## 8. Privacy, governance and AI boundaries

- Individual consent and collective governance are distinct; one does not replace the other.
- No unnecessary copy of participant-level information.
- Application-level role and record permissions.
- AI only receives authorised context.
- AI comparisons reference approved, structured conditions and show source links.
- Conflicts, ambiguity and missing records go to authorised humans.
- No AI approval, access grant, consent modification, policy creation or benefit allocation.
- Community partners determine which information is safe and useful to share.

## 9. Research limitations

This review has not examined internal SRHIN systems, data schemas, contracts, APIs, operating procedures or access controls. It has not independently audited public claims, interviewed SRHIN staff or community members, or conducted legal, clinical, ethics or security review. Public documentation cannot prove that an internal process is absent.

## 10. Conclusion

The broad platform should be dropped. The only concept worth carrying forward at this stage is a **Community Data-Use Accountability Ledger** with three tightly connected capabilities: approved-use record, change-of-use review and community-obligation follow-up.

This is a focused, potentially complementary answer to the host challenge—but it is still conditional. Validate the workflow with SRHIN and the affected communities. If it is already adequately supported, stop or redirect the project rather than building a duplicate.
