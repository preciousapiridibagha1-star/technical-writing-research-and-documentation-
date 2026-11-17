# SRHIN Technical and Governance Gap Assessment

**Assessment date:** 17 November 2026  
**Prepared for:** Mozilla Foundation Fellowship 2027–2028 — Track I Embedded, Slum & Rural Health Initiative (SRHIN)  
**Status:** Desk-research assessment and host-validation brief. This is not an SRHIN-commissioned report, an organisational audit, or evidence of a partnership.  
**Working project label:** MindCommons AI (provisional; the product itself is not yet validated).

---

## Executive assessment

SRHIN is not starting from zero. Its public materials describe a substantial mental-health and digital-health ecosystem: Gencurate for spoken research-data collection and curation; GENSCORE for culturally grounded, multilingual AI-supported mental-health screening research; BraveHeart for community-based mental-health education and frontline support; a Lived Experience Working Group (LEWG); a Data, Ethics & Safety Monitoring Board; a Project Steering Committee; governance and human-oversight charters; participant consent and privacy safeguards; and a Knowledge Hub containing practical co-production, compensation and lived-experience authority resources.

That matters because a new consent portal, generic data dashboard, extra lived-experience committee, clinical AI tool or replacement research platform would overlap with capabilities SRHIN already publicly describes.

The most credible potential gap is narrower:

> **Can community-authorised decisions and conditions attached to a mental-health data use be traced through the full life of that use — including a material change of purpose, collaborator or model-development activity — and can community-agreed benefit commitments be followed through without duplicating existing consent, ethics or data-release processes?**

Public documentation does not answer that question. Gencurate says research-data releases are logged. GENSCORE describes formal oversight, charters, reporting and audits. The missing evidence is whether the existing records and workflows connect each data use to the relevant community-authorised decision, conditions, later changes, downstream uses and agreed benefit obligations in a way the appropriate community stewards can inspect and act on.

This is a **validation hypothesis, not a finding that SRHIN has a deficiency**. It may already be handled through internal registers, contracts, data-use agreements, SOPs, committee records or manual processes. If it is already handled adequately, the software project should stop or be redirected.

**Recommended direction:** investigate a thin, community-governed *data-use decision and obligations register* that references authoritative records rather than replacing them. The first prototype should use synthetic data and demonstrate one narrow workflow. Do not include participant-level health data, audio, transcripts, live consent capture, Gencurate integration or autonomous AI decisions. AI is not necessary to prove the core workflow and should be excluded from the first technical demonstration.

---

## 1. Organisation and mission

### 1.1 What SRHIN says it does

SRHIN describes its work as advancing healthcare access and health equity in underserved communities through advocacy, research and technology. Its public account of its work identifies mental health and wellbeing; digital health, artificial intelligence and data science; gender equality; community organising; research and evidence generation; and lived experience as priority areas.

It states that it works with health professionals, people with lived experience, youth leaders, digital-health and AI innovators, researchers and social scientists. It also describes a goal of developing models that governments and institutions can own, institutionalise and scale. Its programmes span Nigeria and Sierra Leone, with a strong emphasis on young people and underserved communities.

### 1.2 Why this matters to the Mozilla host challenge

The Mozilla RFP identifies a specific concern: mental-health data from African communities is increasingly used to build AI, while communities may lack meaningful consent, control over use and a share in resulting benefits. It names SRHIN as a Nigerian Embedded host and describes the challenge as exploring community-owned tools for governance, consent, privacy and benefit-sharing, with a pilot involving young people, people with lived experience and community health workers, in pursuit of a mental-health data commons.

The RFP therefore asks for more than a data-protection interface. It raises questions about who has authority over data use, how individual consent relates to collective governance, who can authorise a use or change, what obligations follow, and how communities participate in the value created from their data.

### 1.3 Working interpretation — not yet host-confirmed

For this assessment, a *community-governed mental-health data commons* is treated as a possible set of governance rules, decision processes, agreements and technical tools through which affected communities can shape and oversee how relevant data is collected, prepared, accessed, reused and used in AI development.

This is deliberately not defined as one central database or a public data marketplace. SRHIN must clarify what it means by *community-owned*, *data commons* and *benefit-sharing* in the context of its challenge.

**Evidence status:** SRHIN's mission and programme descriptions are confirmed as public organisational statements. The exact operating model SRHIN wants the Fellowship project to support remains unconfirmed.

---

## 2. Existing technology and relevant systems

The following inventory reflects public SRHIN/GENSCORE descriptions. A public product description establishes what an organisation says a system is intended to do; it does not independently verify production deployment, technical effectiveness, scale or user adoption.

### 2.1 Gencurate — spoken research-data collection and preparation

**Publicly described purpose:** Gencurate is described as an SRHIN platform for collecting and preparing spoken research data, used in the GENSCORE study. It handles spoken responses to mental-health screening questions in Hausa, Yoruba and Nigerian Pidgin.

**Capabilities described in the Gencurate privacy notice:**
- Contributor and field-officer accounts.
- Capture of participant/recording details and audio answers.
- Recording language and time metadata.
- Manual transcription by a transcription team; the notice says transcripts are not produced by automated speech recognition.
- Review and project-level access controls.
- Role-restricted access: transcribers, reviewers and administrators see different subsets of records according to their work.
- Research-data releases in which names and account details are replaced by codes by default.
- Logging of every research-data release.
- Retention tied to the needs of the GENSCORE study and its ethics approval.
- Participant rights processes including access, correction, deletion, restriction, withdrawal of consent and requests to withdraw recordings from the study.
- Data portability requests.
- A privacy notice stating that Google Cloud services in the United States host servers and recording storage, and Vercel hosts the website.

**What this already covers:** data capture, consent at the collection point, transcription, project review, role-based access, release logging and documented participant rights. A proposed fellowship project must not describe these as absent.

**What remains unclear:** whether the release log records the full purpose, recipient, conditions, community-authorised decision, downstream-use limits and benefit commitments for each release; whether a changed use triggers a structured re-review; the precise relationship between pseudonymisation and irreversible anonymisation; how voice identifiability is managed; how deletion/withdrawal propagates to working copies, backups, released datasets and model derivatives; and how cross-border processors and downstream recipients are governed.

The privacy notice says names and account details are replaced with codes by default in research releases. The GENSCORE governance page separately describes the corpus as fully anonymised before analysis. These statements may describe different processing stages, but the exact technical meaning and sequencing should be clarified rather than assumed.

### 2.2 GENSCORE — culturally grounded mental-health AI research

**Publicly described purpose:** GENSCORE is an SRHIN-led research initiative developing culturally and linguistically grounded mental-health screening approaches for Nigerian languages, including Hausa, Yoruba and Nigerian Pidgin.

Its public-facing descriptions outline a research pipeline involving:
1. Collection of spoken accounts and language through Gencurate.
2. Annotation and contextual interpretation by trained Nigerian contributors, with clinical and language expertise.
3. Clinician review of material before it enters the training corpus.
4. Development of AI-supported assessment items and tools such as GenPHQ and GenGAD.
5. Refinement through workshops involving psychiatrists and people with lived experience.
6. Human review and clinical/psychometric evaluation rather than unrestricted autonomous assessment.

The GENSCORE website currently advertises validation involving 3,600 participants across three states and comparison with blinded SCID-5-CV interviews. A separate SRHIN article describes the project as testing whether culturally adapted assessments can identify depression and anxiety reliably. The exact current validation stage, sample definition and publication status should therefore be confirmed with SRHIN before these figures or milestones are used in an application.

**What this already covers:** a specific AI research use case, local-language data preparation, human and clinical review, lived-experience contribution, assessment development and a stated validation pathway.

**What remains unclear:** the detailed data-use permissions and agreements governing each collaborator; whether external or secondary uses of the corpus are allowed; how model-training and model-derived outputs are covered by consent and governance conditions; whether community authorities can inspect or challenge proposed changes; and what happens when a new partner, purpose, model or commercial pathway is introduced.

### 2.3 BraveHeart — community mental-health support and frontline tools

SRHIN describes BraveHeart as a community-led mental-health initiative using task-shifting, trained community intermediaries, digital tools and local support structures to reach underserved communities and young people, including displaced communities.

Public BraveHeart materials describe several related components:
- **BraveHeart Project / Friendship Tent:** community spaces and trained local champions supporting mental-health literacy, resilience and access to human support.
- **BraveHeart App:** digital learning and support content, including mental-health education, life-skills material and substance-use prevention resources.
- **BraveHeart AI Companion:** a described AI-enabled support/psychoeducation component for young people.
- **BraveHeart AI Clinical Assistant / BraveHeart AI:** described clinical decision support for non-specialist health workers, including screening, guidance and referral.
- **BraveHeart SUD AI:** described decision support for early screening, identification and referral relating to substance-use and mental-health concerns.

The BraveHeart AI clinical product page describes offline-first Android use, culturally adapted assessment workflows, support for English, Yoruba and Nigerian Pidgin, recommendations aligned with clinical protocols, human confirmation of AI recommendations, referral workflows, supervisory review and operational/equity dashboards.

**What this already covers:** mental-health service delivery, community intermediaries, educational resources and human-supervised frontline support. It is not a substitute for a governed mental-health data commons, but it is a relevant source of operational context and existing SRHIN technology.

**Important evidence boundary:** page descriptions, interface examples and displayed activity metrics are not an independent deployment audit. The actual tools in active use, sites, user groups, integrations, data flows and technical maturity need host confirmation.

### 2.4 ALPHA — AI for Low-Resource Public Health Application Centre

SRHIN's public materials identify ALPHA as an application centre for digital health and AI work. Its public catalogue groups or showcases Gencurate, GENSCORE and BraveHeart-related systems alongside other health applications.

**Relevance:** ALPHA appears to be an important technical and programme context for understanding how SRHIN develops and uses AI tools. It may help identify existing infrastructure, technical owners and integration constraints.

**Unknown:** which ALPHA components are production systems, pilots, demonstrations or project pages; whether there is a shared identity, data or audit layer; and what technical governance components are already reusable.

### 2.5 SRHIN Knowledge Hub — existing public governance and co-production resources

The Knowledge Hub publicly lists research publications, guidelines, toolkits, frameworks and policy briefs. The items most relevant to this assessment include:

| Resource | Publicly described purpose | What it means for this assessment |
|---|---|---|
| *A Basic Guide for People with Lived Experience to Get Involved in AI Mental Health Tool Design* | Plain-language guidance for people with lived experience who want to participate in AI mental-health tool design; drawn from GENSCORE. | Do not design a new basic participation guide without first establishing a specific unmet training need. |
| *The LEEF Checklist: A Pre-Launch Check for Digital Mental Health Tools* | A pre-launch check asking whether knowledge held by people with lived experience has shaped a digital mental-health tool. | A lived-experience review mechanism is already publicly available. |
| *A Template for Lived Experience Compensation and Governance in Digital Health Projects* | A policy template covering payment, credit, protection and meaningful say over contributors' material. | Compensation and contributor governance are already addressed in a public resource; any proposed extension must identify what is not covered. |
| *The Co-Production Readiness Self-Assessment* | A checklist to assess whether a project is ready to involve people with lived experience well. | Do not invent a new co-production readiness checklist. |
| *The Epistemic Authority Decision Matrix* | A planning grid for deciding which decisions lived-experience contributors hold real authority over. | Any new workflow should refer to existing authority-setting work, not replace it. |

The Knowledge Hub describes its resources as free to read and use, and the listed items are presented under a Creative Commons Attribution 4.0 licence.

**What remains unclear:** whether each resource has been formally adopted in every GENSCORE workflow; how compliance or use is monitored; and whether these resources are operationally linked to technical data-release and secondary-use records.

---

## 3. Existing governance, consent and community participation

### 3.1 LEWG — Lived Experience Working Group

GENSCORE's public materials describe the LEWG as a central part of the project. The lived-experience page states that members are involved as co-applicants and share responsibility for decisions, outputs and governance. It describes a 12-member group organised across Hausa-English, Yoruba-English and Pidgin-English, with members who have lived experience of depression and anxiety.

The same page describes participation across four stages:
- **Compose:** membership, language coverage and lived-experience representation.
- **Design:** refinement of questionnaires, co-generation and validation of assessment items, and co-authorship of a Human Oversight Charter.
- **Deliver:** Delphi validation, think-aloud sessions, stigma and acceptability reviews, co-facilitated interviews, data co-creation and interpretation.
- **Disseminate:** lead/first authorship, community workshops, policy dialogues and public storytelling.

It also states that contributors are compensated.

**Existing capability:** there is a named lived-experience group with ongoing project responsibilities, rather than a proposal to add lived experience only at the end of technical development.

**Validation needed:** the exact decision rights attached to co-applicant status; which decisions the LEWG can approve, reject, pause or veto; how representatives are selected and refreshed; how dissent is recorded; and how its authority interacts with the Project Steering Committee and independent oversight board.

The governance page labels the LEWG as an advisory body in its governance structure, while the lived-experience page describes co-applicant status and shared responsibility for decisions, outputs and governance. These descriptions may be compatible in practice, but the practical decision rights should be clarified before modelling the governance workflow in software.

### 3.2 Data, Ethics & Safety Monitoring Board

The GENSCORE governance page describes an independent Data, Ethics & Safety Monitoring Board with expertise in AI ethics, global mental health and Nigerian law. It says the board meets every two months, reviews governance and data-integrity reporting, commissions recurring model-bias audits across language, gender, age and region, and reports findings to the funder as well as the project team.

**Existing capability:** independent oversight is publicly described. A new fellowship tool must not purport to replace this board or conduct ethics review.

**Validation needed:** its formal terms of reference, independence safeguards, exact remit, relationship with research ethics committees, and whether it reviews individual data-use requests or only project-level safety, ethics and performance.

### 3.3 Project Steering Committee and institutional oversight

The governance page identifies a Project Steering Committee as the executive-control body, SRHIN as lead institution, and academic/clinical collaborators including the University of Ibadan, Imperial College London and the Federal Neuropsychiatric Hospital, Yaba.

It describes a governance charter, conflict-of-interest declarations, escalation levels, SOPs, monthly KPI dashboards, quarterly progress reports and annual external audits.

**Existing capability:** SRHIN publicly describes a multi-level governance structure and recurring accountability processes.

**Validation needed:** which body owns each class of decision; which records are authoritative; how committee decisions translate into operational access/use conditions; how decisions are communicated to communities; and whether external audit findings or corrective actions are tracked to closure.

### 3.4 Consent, privacy and data protection

The Gencurate privacy notice describes:
- Consent for use of contributor information and explicit consent before mental-health recordings.
- Consent before each recording session.
- Consent in relevant participant languages, also described in GENSCORE governance materials.
- Restricted, role-based staff access.
- De-identification or coding of research releases.
- Release logging.
- A retention period tied to study need and ethics approval.
- Rights to access, correct, delete, restrict use, withdraw consent and request withdrawal of recordings from the study.
- Data portability.
- A stated use of Google Cloud services in the United States and Vercel hosting.

The GENSCORE governance page additionally describes ethics approvals before collection, encryption, data minimisation, de-identification before analysis and support/referral pathways for participants who need care.

**Critical distinction:** individual consent, ethics approval, collective/community governance and benefit-sharing are related but different controls. Evidence that a recording was collected with consent does not by itself establish who may authorise later uses on behalf of a community, how downstream uses are constrained, or how benefits are distributed. Conversely, a community decision should not be treated as a replacement for the rights of an individual participant.

### 3.5 Compensation and benefit-sharing

SRHIN publicly states that LEWG contributors are compensated and provides a template on lived-experience compensation and governance. This is evidence of existing work on contributor payment, recognition, protection and authority.

It does not, by itself, establish the complete benefit-sharing model contemplated by the Mozilla host challenge. Payment for a person's work in a co-design or research role is distinct from benefits that a community may expect when data contributes to model development, research outputs, licensing, commercial partnerships or institutional value.

Questions still open include:
- What benefits are agreed with participants and communities, separately from contributor compensation?
- Are benefits financial, non-financial, collective, individual or mixed?
- Who negotiates and approves them?
- Are agreements attached to each data use or partner?
- Who monitors delivery and handles disputes?
- What happens if a partner does not meet an agreed commitment?
- Are community benefits considered when data is reused or a model is commercialised?

No particular benefit model should be assumed or prescribed by the prototype.

---

## 4. Existing capabilities: consolidated inventory

| Component or process | Publicly described capabilities already present | Do not rebuild | Important unknowns |
|---|---|---|---|
| Gencurate | Spoken data capture, consent steps, transcription, review, role-scoped access, coded research releases, release logs and participant-rights procedures. | Consent portal, audio collection system, transcription queue, generic access-control dashboard. | Whether each release log carries the complete decision, conditions, purpose, downstream-use and benefit-sharing history. |
| GENSCORE pipeline | Local-language corpus development, human annotation, clinician review, assessment generation/refinement and human/clinical validation. | Another mental-health AI screener, generic annotation tool or clinical evaluation platform. | Data-use scope across partners and purposes; model/data derivative governance; approval route for changed uses. |
| LEWG | Lived-experience participation in design, validation, interpretation and dissemination; public description of compensation and co-applicant role. | Another lived-experience committee or generic co-design guide. | Exact decision powers, veto/appeal rights, representation rules and operational link to data-use decisions. |
| Data, Ethics & Safety Monitoring Board | Independent oversight, risk/bias monitoring and reporting, as publicly described. | Replacement ethics/safety board or a duplicate high-level oversight dashboard. | Terms of reference, remit over secondary data use, corrective-action follow-up and access to operational records. |
| Project Steering Committee / charters / SOPs | Executive oversight, written roles, conflict declarations, escalation, monthly KPIs, quarterly reporting and annual audits, as publicly described. | New generic governance charter, generic SOP library or generic KPI dashboard. | Whether current records connect individual uses, conditions, changes and community commitments. |
| Knowledge Hub | Public resources on co-production, lived-experience authority, contributor compensation and digital mental-health tool readiness. | New basic guides/checklists that reproduce these resources. | Adoption, version control, enforcement and integration into operational workflows. |
| BraveHeart | Community mental-health support, task-shifting, digital learning and described AI-supported frontline workflows. | A new clinical screening or community mental-health service product under this fellowship's data-governance scope. | Actual production footprint, data flows, integration with GENSCORE and how governance controls apply across tools. |
| ALPHA | Publicly presented as an AI/public-health application centre and home for related tools. | A broad replacement application platform. | Shared infrastructure, identity/data services, technical ownership, APIs and actual deployment status. |

---

## 5. Unresolved questions — what public documentation cannot establish

Public sources are not internal system diagrams, data-sharing agreements, committee minutes, technical audits or interviews. The following points cannot responsibly be inferred from the public material reviewed.

### 5.1 Actual operating workflow
- Is there already a register for data assets, approved uses, recipients, purpose limitations, authorising decisions and review dates?
- Is the Gencurate release log sufficient for the purpose, or does another internal system contain additional context?
- Are changes in purpose, model, partner, location, retention or onward sharing handled through a formal re-approval workflow?
- Which tool or document is the authoritative record?

### 5.2 Scope of the proposed data commons
- Does SRHIN intend to govern only GENSCORE data, a broader SRHIN data portfolio, or community data contributed to multiple independent projects?
- Is the intended model centralised, federated, cooperative, stewarded or something else?
- What does community ownership mean in practical and legal terms?
- Which communities are represented, and how are their boundaries defined?

### 5.3 Authority and accountability
- What exact decisions can the LEWG make or veto?
- Which decisions belong to participants, community representatives, SRHIN, the Steering Committee, the ethics board, research ethics committees or data custodians?
- Who resolves disagreement between individual consent restrictions and collective decisions?
- How are appeals, conflicts of interest and dissent handled?

### 5.4 Data lifecycle, reuse and model derivatives
- What data is shared, with whom, for what purposes and under what agreements?
- Can data be used for new model training, fine-tuning, benchmarking, evaluation, publication or commercial activity?
- Are downstream recipients allowed to pass data or derivatives to others?
- How are model checkpoints, embeddings, synthetic data, derived labels and evaluation artefacts treated?
- What does withdrawal mean before release, after release, after training and after model deployment?
- Can voice recordings or other content be re-identifiable even where names have been removed?

### 5.5 Benefit-sharing
- Which benefits are promised or negotiated for data contribution, not just for paid contributor labour?
- How are commitments recorded, funded, monitored and enforced?
- Who can see their status and challenge non-delivery?

### 5.6 Privacy, security and technical implementation
- What encryption, key-management, backup, deletion and incident-response controls are implemented?
- What is the exact data-flow map, including processors, hosting locations and partner systems?
- What APIs, data schemas and identity/access services exist?
- What audit information is retained and for how long?
- What operational constraints apply to low-bandwidth access, mobile devices and community workflows?

### 5.7 Population and age
The Mozilla challenge refers to young people. The Gencurate privacy notice says Gencurate is for adults aged 18 or older and that only adults may be recorded. This may be entirely compatible if the intended pilot participants are young adults, but the intended age range and any plans involving minors must be clarified. No assumption should be made that the current data-collection platform is approved for minors.

### 5.8 Deployment and performance
Public pages include descriptions of technical features and certain scale/validation claims. They do not provide the complete evidence needed to independently verify current deployment, performance, data quality, model validation, real-world outcomes or adoption. These should be checked directly with the host and relevant published studies.

---

## 6. Potential gap — a hypothesis, not a conclusion

### 6.1 The candidate gap

The strongest candidate gap is **end-to-end traceability of community-authorised data-use decisions and obligations when a governed mental-health data resource is accessed, released, reused or materially repurposed**.

More specifically, the question is whether the organisation can connect the following objects in one auditable chain:

1. **Data resource:** what governed dataset or data asset is involved, described without exposing participant identities.
2. **Proposed use:** the research, model-development, evaluation, publication or other purpose requested.
3. **Authority:** the individual, committee or community body authorised to decide that type of use.
4. **Decision and conditions:** what was approved, declined or returned for revision, including the applicable restrictions and source documents.
5. **Change event:** whether a material change requires review and who has authority to decide.
6. **Community commitments:** any benefits, reporting, acknowledgement, capacity-building or other obligations explicitly agreed by the relevant parties.
7. **Follow-through:** whether the obligations were fulfilled, disputed, revised or left outstanding.

This hypothesis is narrower than a new data-governance platform. It is not a replacement for individual consent, Gencurate, ethics approval, LEWG, the independent board, existing charters or existing release logs.

### 6.2 Why the hypothesis is plausible

Public documentation already explains how data is collected, reviewed, protected and released, and it describes governance structures and contributor participation. It is less explicit about whether the record of a specific community-authorised decision remains connected to the conditions and obligations governing that data use over time, especially when a purpose, recipient or model-development activity changes.

That absence from public documentation is a reason to ask a question, not evidence that the workflow does not exist.

### 6.3 What would invalidate the hypothesis

The project should not build this software if SRHIN confirms that:
- An existing tool or register already links each relevant use to the authorising decision, conditions, change history and benefit obligations.
- Existing staff and community stewards can access and use that information without substantial friction.
- The remaining problem is primarily a policy, agreement, resourcing or representation issue rather than an information-system problem.
- A new application would create duplicate data entry, split accountability or introduce additional privacy risk.
- The relevant communities do not want this form of software or do not consider the workflow a priority.

### 6.4 Refined problem statement for validation

> When a mental-health data resource is proposed for a new, changed or downstream AI-related use, can the authorised community and institutional decision-makers see the relevant request, the applicable conditions, the decision record and any agreed community obligations together — and can they verify what happened afterwards?

This wording intentionally asks whether the process works. It does not claim that SRHIN currently fails to do it.

---

## 7. Software requirements — only if the gap is confirmed

### 7.1 Product boundary

A small **Data-Use Decision and Obligations Register** would be the most that should be considered initially. It would reference existing authoritative decisions and data systems. It would not become a new data lake, consent manager, research platform, clinical application or autonomous governance system.

### 7.2 Minimum functional requirements

**A. Governed data-resource reference**
- Assign a non-identifying reference ID to a data resource.
- Record only safe metadata needed for governance: description, data category/modality, language or population scope where appropriate, sensitivity classification, responsible steward and reference to the authoritative source.
- Link to current governance terms and applicable approval documents.
- Do not store participant names, recordings, transcripts, clinical answers or copies of sensitive datasets.

**B. Data-use request**
- Record requesting organisation/team, purpose, proposed method, intended model/data activity, collaborators, recipients, jurisdiction, duration, retention and onward-sharing proposal.
- Capture the evidence and approvals required by the host's existing rules.
- Identify whether the request is new, renewal or a material change.
- Flag missing information; do not make an ethics or community decision.

**C. Human decision and conditions**
- Route a complete request to the authority identified by SRHIN's existing decision-rights framework.
- Record the decision outcome, decision-maker/body, date, rationale, conditions, review/expiry date and authoritative source.
- Support approval, approval with conditions, request for revision or rejection if those outcomes match the host's real process.
- Prevent the requester from approving their own request where separation of duties is required.
- Preserve previous decisions and versions.

**D. Change-of-use review**
- Link a proposed change to the existing approved use.
- Show what has changed: purpose, recipient, partner, model activity, data fields, retention, transfer location or other host-defined trigger.
- Route the change for human review.
- Keep the previous approval and its conditions visible.
- Do not silently treat a new use as covered by an old approval.

**E. Community-obligation follow-up**
- Record only obligations explicitly agreed by authorised parties.
- Link each obligation to the relevant decision/use.
- Record responsible party, due/review date, progress, evidence and dispute/escalation status.
- Support non-financial and financial obligations only as the host and community define them.
- Do not calculate what benefit is fair, negotiate terms or automatically distribute funds.

**F. Audit and export**
- Keep an append-only history of key actions and changes.
- Show who did what, when, under which role and against which record version.
- Allow authorised users to export a human-readable decision history.
- Provide a machine-readable export only if the host confirms a real interoperability need.
- Make clear that a system log does not replace legal agreements, committee minutes or ethics records.

### 7.3 Non-functional requirements

- Least-privilege access at role and record level.
- Strong authentication appropriate to the risk.
- Encryption in transit and at rest, with key management defined by the host's technical/security team.
- Defined backup, retention, deletion and incident-response rules.
- Accessible plain-language interface and language support chosen with community partners.
- Low-bandwidth operation appropriate to actual users.
- Clear separation between public, community-restricted, internal and confidential information.
- Exportability and maintainability; avoid vendor lock-in.
- Open-source code and documentation where safe and agreed.
- No live integration until the host approves architecture, data flows, permissions and security review.

### 7.4 Explicitly out of scope

- New participant consent capture.
- Raw audio, transcripts or participant-level health records.
- Rebuilding Gencurate.
- Clinical screening, diagnosis, treatment, referral or mental-health chatbot functions.
- Replacing LEWG, the Data, Ethics & Safety Monitoring Board, Project Steering Committee or research ethics committees.
- A generic monitoring dashboard.
- General research project management.
- Blockchain, tokenisation or a speculative data marketplace.
- AI approval, access decisions, consent decisions, policy interpretation as authority, benefit allocation or automated ethics judgements.
- Production connection to Gencurate or GENSCORE before written host approval.

**AI decision:** exclude AI from the first prototype. The primary problem is likely a governance workflow and evidence trail. Deterministic forms, permissions, versioning and audit records are sufficient to test whether the proposed workflow is useful. An AI summarisation feature should only be considered later if users identify a specific need and the host can define safe inputs, evaluation and human review.

---

## 8. Non-software requirements — governance must lead the product

Software cannot create legitimate community authority by itself. The following must be defined or confirmed by SRHIN and affected communities before implementation.

### 8.1 Community representation and decision rights
- Define which communities are represented and why.
- Confirm whether existing LEWG structures are appropriate for the proposed data commons or whether other groups must participate.
- Define selection, tenure, renewal, compensation, accessibility and conflict-of-interest procedures.
- Specify which decisions community representatives can approve, reject, pause or appeal.
- Record how dissent and disagreement are handled.
- Avoid creating a new committee unless existing governance genuinely cannot serve the purpose.

### 8.2 Consent and data-use policy
- Distinguish participant-level permission from collective governance.
- Define permitted and prohibited data uses in plain language.
- Define which changes trigger renewed consent, ethics review, community review or multiple reviews.
- Clarify the treatment of withdrawal after data release and after model training.
- Define how onward sharing and derivatives are handled.
- Explain what cannot technically be withdrawn or erased and how that limitation is communicated.

### 8.3 Benefit-sharing agreements
- Define what counts as a benefit for the relevant community.
- Separate payment for contributor labour from community-level benefit-sharing.
- Agree how benefits are proposed, negotiated, approved and revised.
- Specify responsible parties, budgets, timeframes, evidence and dispute routes.
- Ensure agreements can be enforced or escalated; a software status field alone is not enforcement.

### 8.4 Ethics, privacy and security
- Clarify the roles of research ethics committees, the Data, Ethics & Safety Monitoring Board, the Steering Committee, LEWG and data custodians.
- Review cross-border data transfers, processors, storage and access.
- Define anonymisation/pseudonymisation, voice-identification risks, retention and deletion.
- Establish incident response and communication to affected participants/communities.
- Obtain legal, ethics, clinical and security advice from qualified people; this assessment is not a legal or security audit.

### 8.5 Participation and capacity
- Fund meaningful participation, not just attendance.
- Provide accessible information and support for language, literacy, disability and connectivity needs.
- Return research findings to participants and communities in formats they can use.
- Support community members to understand data use, AI development, risk and governance options.
- Ensure participation is continuous across scoping, design, testing, review and dissemination.

---

## 9. Prototype specification — smallest useful technical demonstration

**Prototype status:** proposed only. Build only after host validation confirms a real unmet workflow and identifies who should use it.

### 9.1 Demonstration objective

Show that a single proposed or changed use of a fictional mental-health dataset can be submitted, reviewed by an authorised human role, recorded with conditions and linked to agreed follow-up obligations — without importing participant-level data or replacing existing governance systems.

### 9.2 Demonstration actors

Use synthetic accounts for:
1. **Research requester:** submits a proposed use or material change.
2. **Community-authorised reviewer/steward:** sees the request and records a decision within a fictional, predefined authority model.
3. **Ethics/oversight reviewer:** records whether a required external review reference is present; does not replace or simulate the real ethics committee.
4. **System custodian/auditor:** manages permissions and inspects the history, without acquiring authority to override a community decision.

The exact real-world roles and separation of powers must come from SRHIN.

### 9.3 Synthetic scenario

Create one fictional data asset, for example: **DEMO-MH-001 — Synthetic multilingual mental-health speech research dataset**.

The dataset is only a label and metadata record. It contains no real audio, transcript, diagnosis, participant identity or sensitive personal information.

A fictional university research team requests to use the synthetic asset for a new model-evaluation purpose. The request changes one material condition, such as the intended recipient or model-development activity. The reviewer sees the original approved purpose, the proposed change and missing documents. A human decision is recorded. If approval is conditional, the system creates linked follow-up items based on fictional commitments.

### 9.4 Minimum screens

1. **Data resource:** description, steward, governance-term version and source references.
2. **Use request:** purpose, requester, proposed activity, partners, location, duration and supporting references.
3. **Review:** change summary, required evidence, authority, human decision and conditions.
4. **Obligations:** agreed commitment, owner, due date, progress and evidence.
5. **History:** time-ordered record of submissions, reviews, decisions and changes.

### 9.5 Core acceptance tests

- A requester cannot approve their own request if the role model requires separation.
- A user without permission cannot see restricted records.
- A request cannot proceed to decision while required fields are missing.
- A material change is linked to the existing record and triggers the configured review route.
- The previous decision and conditions remain visible after a new decision is recorded.
- Each obligation is linked to the decision that created it.
- The history shows the actor, action, timestamp and version.
- No participant-level information is collected or stored.
- AI does not approve, deny or modify a decision.
- The demonstration clearly labels all people, records and data as synthetic.

### 9.6 Evaluation

Do not measure clinical outcomes. Evaluate the governance workflow:
- Can an authorised reviewer reconstruct the purpose, decision, conditions and obligations from one place?
- Does the workflow reduce time or manual cross-referencing compared with the current process?
- Can community reviewers understand what they are being asked to decide?
- Are permissions and decision boundaries understood?
- Does the workflow create duplicate entry or extra administration?
- Are required conditions and obligations consistently recorded?

Baseline and target values must be agreed after observing the real current workflow. No improvement claim should be made from a synthetic demonstration alone.

### 9.7 Definition of done for the prototype

A reviewer can complete the synthetic request-to-decision-to-obligation journey, inspect its history, understand the authority boundaries and see precisely what the software does not do. The prototype is a workflow demonstration, not a live data commons or production-ready governance system.

---

## 10. Host validation — what SRHIN must confirm

The questions below should be asked respectfully and without presuming that a gap exists.

### 10.1 Priority questions

1. **Challenge scope:** Is Mozilla's challenge intended to support GENSCORE specifically, a broader SRHIN portfolio of mental-health datasets, or a community data-governance model that can extend beyond SRHIN?
2. **Meaning of data commons:** What does SRHIN mean by community-owned data commons in practical terms — governance, stewardship, data access, licensing, cooperative ownership, benefit-sharing or a combination?
3. **Current workflow:** How is a new data-use request, research partner, purpose change, model-training use or onward-sharing request handled today?
4. **Existing records:** Which systems, registers, contracts, release logs, committee minutes or SOPs already record the request, authorisation, conditions and follow-up?
5. **LEWG authority:** Which decisions can LEWG make or veto, and how does that authority interact with the Steering Committee, Data/Ethics/Safety Monitoring Board and research ethics committees?
6. **Community scope:** Which young people, people with lived experience and community health workers should participate in the pilot, and how are they represented?
7. **Age and consent:** Does the intended pilot involve adults only, or also minors? How does that align with Gencurate's published adults-only notice?
8. **Data lifecycle:** What happens when consent is withdrawn, a dataset is reused, a model is retrained, data is shared with a new partner or a model-derived asset is released?
9. **Benefit-sharing:** How does SRHIN distinguish contributor compensation from wider community benefit-sharing, and how are agreed benefits currently tracked?
10. **Technical boundary:** What existing platforms, APIs, identity services, data schemas and logs would a small tool need to work with — if any?
11. **Real burden:** Which part of the current process is hardest for community stewards, researchers or administrators? How often does it happen and what workarounds exist?
12. **Pilot success:** What would SRHIN and the participating communities consider a useful result after a short pilot?

### 10.2 Documents or demonstrations to request — only if SRHIN is comfortable sharing

- A non-sensitive, redacted example of the current data-use or release workflow.
- A high-level data-flow diagram showing systems and organisations, without credentials or participant details.
- Relevant public or shareable governance charter, human-oversight charter and SOP summaries.
- A redacted example of a data-sharing/use agreement or benefit-sharing schedule.
- A demonstration of the current Gencurate release log or equivalent record, if appropriate.
- A description of the roles and decision rights for LEWG, the Steering Committee and the independent oversight board.

Do not request raw recordings, participant-level records, credentials, private committee deliberations or confidential legal documents. A high-level walkthrough may be enough to decide whether a software prototype is justified.

### 10.3 Go/no-go gates

**Gate 1 — Problem confirmation:** SRHIN and community representatives identify a specific recurring workflow problem, not merely a broad aspiration.

**Gate 2 — Existing-system comparison:** the team identifies which current system or process is authoritative and why it does not fully solve the problem.

**Gate 3 — Community legitimacy:** the relevant community decision-makers agree that the problem matters and define the authority model.

**Gate 4 — Non-duplication:** the proposed tool adds a capability rather than re-creating consent, ethics, data collection, dashboards or existing registers.

**Gate 5 — Safe prototype scope:** SRHIN confirms that a synthetic-data demonstration is appropriate and identifies what must remain out of scope.

**Gate 6 — Pilot pathway:** there is a realistic route to test the workflow with the right people, with fair compensation, accessibility and ethical safeguards.

If a gate fails, revise, pause or stop. Do not build merely to have a software artefact for an application.

---

## 11. Recommended project direction and immediate next actions

### 11.1 Recommended working direction

Continue investigating a **Community Data-Use Decision and Benefit-Obligations Register** as a possible contribution to SRHIN's broader community-governance challenge.

This name is descriptive, not final. MindCommons AI remains a provisional repository label. The project should not be pitched as a complete solution or as a confirmed SRHIN need.

### 11.2 What to do next

1. Prepare a short, respectful host inquiry grounded in the documented existing systems.
2. Ask whether SRHIN is open to a conversation about current workflows and the specific data-commons challenge.
3. Map the workflow from data collection to release, reuse, changed purpose, model development and community benefit obligations.
4. Compare the workflow map with Gencurate, GENSCORE governance materials, LEWG and the Knowledge Hub resources.
5. Decide whether there is a genuine software gap, a non-software governance gap, both or neither.
6. Only then finalise a prototype specification and build a small synthetic-data demonstration.

### 11.3 Fellowship fit and evidence discipline

The Mozilla RFP expects an Embedded applicant to respond to the host's identified issue, then refine the project with the host if selected. It asks applicants to show an inspectable artefact and explain who uses it and how that is known. It also explicitly rejects projects designed about a community rather than with it, and technology looking for a problem.

The applicant's repository can demonstrate research, product definition, documentation and a bounded technical proof of concept. It must not present MindCommons as implemented, validated, deployed, host-approved or community-endorsed. The assessment itself is desk research. It is a foundation for asking better questions, not a substitute for host and community input.

---

## 12. Evidence register and sources

**Source rule:** Organisational websites and product pages are treated as evidence of what the organisation publicly describes, not as independent verification of implementation, performance or outcomes. The Mozilla RFP is the source of truth for the Fellowship challenge and track rules.

### Mozilla Foundation
1. [Official 2027–2028 Fellowship RFP (PDF)](https://assets.mofoprod.net/network/documents/PUBLIC_2027_2028_Fellowship_RFP-3.pdf) — track definitions, host challenge, eligibility, applicant qualities, output expectations, open-work requirements and application questions.
2. [2027 Call for Applications](https://www.mozillafoundation.org/en/what-we-do/grantmaking/fellowship/2027-call-for-applications/) — public programme overview and application dates.

### SRHIN / GENSCORE — technology and governance
3. [SRHIN — Our Work](https://srhin.org/our-work/) — organisational mission, priority areas and flagship programmes.
4. [Gencurate — Privacy Notice](https://app.gencurate.com/privacy) — data categories, consent, purpose, role-based access, release logging, hosting, retention and participant rights.
5. [GENSCORE — Governance & Ethics](https://www.genscore.io/governance.html) — governance structure, LEWG, independent oversight, charters, reporting, audits and stated privacy safeguards.
6. [GENSCORE — Lived Experience](https://www.genscore.io/lived-experience.html) — LEWG membership description, co-production stages, compensation and dissemination.
7. [GENSCORE — Main public description](https://www.genscore.io/) — data-to-model pipeline and public validation claims. Current page/indexed descriptions should be checked with SRHIN because public page versions and stated project stages are not fully consistent.
8. [SRHIN — GENSCORE project update](https://srhin.org/how-srhin-is-advancing-ai-innovation-in-mental-health-screening-in-nigeria/) — description of the research objective, local languages, Gencurate, clinical and lived-experience input.
9. [SRHIN — BraveHeart Project](https://srhin.org/our-project/braveheart-project/) — community-based programme, Friendship Tent, app, curriculum and related tools.
10. [SRHIN — BraveHeart AI](https://srhin.org/braveheartai/) — publicly described frontline clinical decision-support workflow, offline operation and human oversight.
11. [SRHIN — ALPHA Centre](https://alpha.srhin.org/) — public catalogue of AI/public-health applications.

### SRHIN Knowledge Hub — co-production and governance resources
12. [SRHIN Knowledge Hub](https://resources.srhin.org/) — public research, policy, toolkits and frameworks.
13. [A Basic Guide for People with Lived Experience to Get Involved in AI Mental Health Tool Design](https://resources.srhin.org/item/ai-co-design-guide).
14. [The LEEF Checklist: A Pre-Launch Check for Digital Mental Health Tools](https://resources.srhin.org/item/leef-checklist).
15. [A Template for Lived Experience Compensation and Governance in Digital Health Projects](https://resources.srhin.org/item/lived-experience-compensation-governance-template).
16. [The Co-Production Readiness Self-Assessment](https://resources.srhin.org/item/coproduction-readiness-self-assessment).
17. [The Epistemic Authority Decision Matrix](https://resources.srhin.org/item/epistemic-authority-decision-matrix).

---

## 13. Limitations and final conclusion

This assessment is based on the Mozilla RFP and publicly accessible SRHIN/GENSCORE materials reviewed on 17 November 2026, plus the applicant's own repository documents. It does not include internal system access, staff interviews, LEWG consultation, participant research, legal advice, clinical review, cybersecurity testing or independent verification of product metrics.

The evidence shows that SRHIN already publicly describes meaningful technical and governance work around consent, privacy, data collection, clinical review, lived-experience participation, oversight, co-production and compensation. Any project that ignores those capabilities would be poorly researched and likely duplicative.

The remaining question is not “How do we build a consent platform?” It is whether there is a specific, unresolved workflow connecting community-authorised data-use decisions, conditions, changed uses and agreed benefit obligations across the data lifecycle.

**Current decision: investigate; do not yet build.** The next milestone is host validation of the workflow and decision rights. If the gap is real, build the smallest synthetic-data register that helps authorised people trace one request, one decision and the obligations that follow. If it is not real, stop or redirect. The project must be shaped with the community, not merely described on its behalf.
