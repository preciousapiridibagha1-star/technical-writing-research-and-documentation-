# Research and Analysis

**Research status:** Expanded public-source review, 9 November 2026  
**Purpose:** Identify the actual problem in the SRHIN host challenge, map what SRHIN already has, and avoid proposing a duplicate system.  
**Evidence standard:** Public descriptions establish what SRHIN says it has built or operates. They do not independently verify every claim or reveal internal workflows. Gaps below are hypotheses until confirmed with SRHIN and affected communities.

## 1. The host challenge

Mozilla's official 2027–2028 call confirms SRHIN as a Track I Embedded host and points applicants to the full RFP for the host-specific challenge. The challenge wording reproduced by a third-party guide describes the concern that mental-health data from African communities may be used to develop AI without meaningful consent, community control or fair benefit-sharing. It calls for community-owned tools for governance, consent, privacy and benefit-sharing, piloted with young people, people with lived experience and community health workers, toward a mental-health data commons.

**Source caution:** The official RFP PDF is linked from Mozilla's call page, but its SRHIN section was not independently extracted in this review. The reproduced wording is a discovery aid, not a substitute for checking the original PDF before an application is submitted.

## 2. SRHIN's existing work is substantial

Public SRHIN and GENSCORE materials show that this is not an organisation starting from zero.

### GENSCORE and Gencurate

GENSCORE describes a culturally grounded mental-health AI initiative working across Hausa, Yorùbá and Nigerian Pidgin. Gencurate is presented as the data-curation pipeline through which voice notes, interviews and narratives pass before possible use in model development.

Its public platform description says the process includes:
- Consent before collection, in the speaker's own language.
- Contextual annotation by trained people.
- Clinician review and sign-off before material joins the training corpus.
- Monitoring representation across language, gender, age and region.

### Existing governance and lived-experience structures

The GENSCORE Governance & Ethics page publicly describes:
- A Lived Experience Working Group (LEWG).
- An independent Data, Ethics & Safety Monitoring Board.
- A project steering committee and institutional collaborators.
- A written governance charter and human-oversight charter.
- An escalation protocol and standard operating procedures.
- Monthly governance/performance dashboards, quarterly reports and annual external audits.
- Ethics approval, informed consent, de-identification, encryption and restricted access.

The GENSCORE lived-experience page goes further: it describes LEWG members as co-applicants who share responsibility for decisions, outputs and governance; it describes compensated participation, co-design, co-authoring the Human Oversight Charter, research dissemination and a 12-member working group across three language communities.

### Public governance resources

SRHIN's Knowledge Hub publicly lists practical resources, including:
- The LEEF Checklist for pre-launch review of digital mental-health tools.
- A template for lived-experience compensation and governance.
- The Co-Production Readiness Self-Assessment.
- The Epistemic Authority Decision Matrix, designed to clarify which decisions lived-experience contributors hold authority over.
- A plain-language guide for people with lived experience to participate in AI mental-health tool design.

These materials materially change the product analysis. It would be inaccurate to claim that SRHIN lacks community participation, lived-experience governance, compensation guidance, consent safeguards, ethics oversight or accountability structures.

## 3. What this means: the broad original product would duplicate existing work

The first MindCommons AI concept was too broad. A general platform containing consent management, a researcher request portal, community governance, audit dashboards and benefit tracking could duplicate or repackage capabilities and structures SRHIN already publicly describes.

In particular:
- A new consent collection tool would overlap with Gencurate's consent-before-collection process.
- A new lived-experience governance framework would overlap with LEWG, the Human Oversight Charter and SRHIN's published decision-making resources.
- A generic governance dashboard would risk duplicating GENSCORE's stated monthly KPI dashboards and reporting.
- A generic AI assistant would add little value unless it addresses a specific operational task not already served by existing tools.

**Decision:** Do not present the original broad MindCommons AI platform as a confirmed gap or proceed as if SRHIN needs a replacement governance system.

## 4. The narrower opportunity worth validating

The strongest remaining hypothesis is not "SRHIN has no governance". It is whether SRHIN and its community partners need a **community-facing data-use stewardship and accountability layer that connects existing governance decisions to the later lifecycle of data**.

The public material reviewed explains data collection, consent, annotation, clinician sign-off, oversight bodies and governance documentation. It does not clearly show, in the public-facing descriptions, a shared operational interface for community members and authorised stewards to:

1. View a plain-language register of approved data-use purposes and the rules attached to them.
2. Trace how an approved dataset or data category may be reused beyond its original collection or project.
3. Review and record new or changed data-use proposals against existing community decisions.
4. See which governance body or community authority approved a use, under what conditions, and when it should be reviewed again.
5. Monitor the delivery of community benefits attached to a specific data-use arrangement, where such arrangements exist.
6. Access understandable, privacy-preserving explanations of data-use history without exposing participant-level records.

This is a **public-evidence gap**, not proof of an operational gap. SRHIN may already have internal tools, procedures or contractual arrangements for these tasks that are not described publicly.

## 5. Refined problem statement

SRHIN has publicly documented important foundations for responsible mental-health data and AI: informed consent, data curation, clinical review, lived-experience co-governance, ethics oversight and accountability processes.

The question worth investigating is how those existing safeguards and community decision rights are carried forward and made visible when data is considered for new, changing or secondary uses over time. The practical challenge may be connecting governance decisions, authorised data-use purposes, review conditions and community benefit commitments in a way that community stewards can understand and oversee.

The product should therefore be considered only as a possible **complementary stewardship interface**, not a replacement for GENSCORE, Gencurate, LEWG or SRHIN's governance bodies.

## 6. What would prove the gap is real?

Before confirming the product, ask SRHIN and community representatives:
- Is there already a system or register for approved data-use purposes and subsequent/secondary use requests?
- How are changes in purpose, new collaborators, model-training use or commercial use reviewed?
- Can community representatives see the status and rationale of data-use decisions at an appropriate level of detail?
- How are conditions imposed by LEWG, the ethics board or other governance bodies attached to the relevant data-use workflow?
- How are benefit-sharing commitments linked to a particular use, monitored and reported?
- Which parts are already handled by Gencurate, internal databases, agreements, SOPs or manual processes?
- What is difficult for participants or community stewards in practice?
- Would a new interface reduce friction, or would it add another system and administrative burden?

If these workflows are already handled effectively, the proposed application should be narrowed further or abandoned rather than built for its own sake.

## 7. Product principles and boundaries

- Preserve SRHIN's existing governance bodies and community authority.
- Do not collect consent again if an existing approved process already does so.
- Do not copy or centralise sensitive participant data unnecessarily.
- Treat individual consent and collective governance as related but distinct.
- Keep policy enforcement in application rules and approved human decisions, not in free-form model judgement.
- AI can explain approved records, identify missing information, compare a proposal with documented conditions and prepare summaries.
- AI must not approve data access, change consent, overrule LEWG or ethics decisions, or decide what benefits are fair.
- Any integration must be based on documented need, permission, technical feasibility and security review.

## 8. Research limitations

This remains desk research. We have not:
- Reviewed SRHIN's internal systems, contracts, APIs, databases or SOPs.
- Independently audited GENSCORE's claimed technical or governance performance.
- Interviewed SRHIN staff, LEWG members, young people or community health workers.
- Verified how data-use requests, secondary use or benefit-sharing are handled in daily operations.
- Conducted legal, clinical, ethics or security review.

The public website and Knowledge Hub are unusually informative, but public documentation cannot establish the absence of private operational tools.

## 9. Research conclusion and go/no-go position

**There is a real problem in the host challenge:** communities need meaningful control over mental-health data and the benefits of AI development.

**There is also substantial existing SRHIN work addressing that problem:** GENSCORE, Gencurate, LEWG, the Data, Ethics & Safety Monitoring Board, the Human Oversight Charter, governance procedures and public co-production resources.

Therefore, the original broad MindCommons AI platform is not sufficiently differentiated and should not be presented as filling a verified gap.

A narrower community-facing data-use stewardship and accountability layer is worth exploring because the public materials reviewed do not clearly show how governance decisions and community benefit commitments are operationally connected across later data uses. This remains a hypothesis. The next decisive step is validation with SRHIN and community stewards. If existing systems already do this well, do not build a duplicate.

