# SRHIN Technical and Governance Gap Assessment

**Research date:** 17 November 2026  
**Target opportunity:** Mozilla Foundation Fellowship 2027–2028, Track I Embedded — Slum & Rural Health Initiative (SRHIN), Nigeria  
**Working project hypothesis under review:** MindCommons AI — Community Data-Use Accountability Ledger  
**Status:** Public-source desk assessment. Not commissioned by SRHIN. No access to internal systems, staff interviews, community consultation, participant data, security testing or legal review has taken place.

---

## Executive assessment

SRHIN is not approaching this challenge as an organisation with no existing governance. Its public materials describe a substantial mental-health AI and lived-experience ecosystem: Gencurate for research-data collection and curation; GENSCORE for culturally grounded AI-assisted mental-health screening; BraveHeart for community-based mental-health support and task-shifting; a Lived Experience Working Group (LEWG); a Data, Ethics & Safety Monitoring Board; a Project Steering Committee; governance and human-oversight charters; escalation procedures; ethics approvals; consent; restricted data access; and multiple public tools for lived-experience participation, decision authority and compensation.

That changes the project hypothesis materially.

**The project must not be framed as building consent from scratch, creating a new ethics board, replacing LEWG, or giving SRHIN a generic mental-health data platform.** Those would overlap with capabilities SRHIN already publicly describes.

The potentially distinctive question is narrower:

> When mental-health data collected with individual consent and governed through existing project structures is proposed for a new purpose, a new recipient, a changed AI-training use or a downstream release, can the relevant community-authorised decision, its restrictions, the data-use history and any agreed community benefits be traced and enforced across the full lifecycle?

Public materials do not answer that question. They may have internal systems, contracts, data-use agreements, registers or manual procedures that already do it well. This is therefore a **gap hypothesis, not a finding**.

The most defensible next step is not to start building MindCommons. It is to validate one real workflow with SRHIN and the people whose data and lived experience are involved. A small synthetic-data prototype should be built only if that validation establishes a specific, material gap that existing processes do not adequately address.

### Assessment confidence

| Area | Current confidence | Reason |
|---|---|---|
| Mozilla's stated SRHIN host challenge | High | Taken directly from the supplied 2027–2028 RFP, page 7. |
| Publicly described SRHIN mission and programme portfolio | High for what the organisation publishes | Official SRHIN pages describe its mission and flagship work; public claims are not an independent impact audit. |
| Publicly described Gencurate and GENSCORE safeguards | Moderate to high for the published descriptions | Gencurate's privacy notice and GENSCORE governance pages are unusually specific, but underlying records and implementation have not been inspected. |
| Actual operating practice and technical architecture | Low | No internal system access, API/schema review, process walk-through or operational audit. |
| Existence of an unmet data-use / benefit-sharing workflow | Unknown | No public evidence establishes either that the gap exists or that it is already solved. |
| Suitability of a new software product | Conditional | Depends on host and community validation; software may be unnecessary or harmful if it duplicates existing processes. |

---

## 1. Organisation and mission

### 1.1 What SRHIN is trying to achieve

SRHIN describes its vision as an Africa where mental-health care is universally accessible through digital and community-based solutions. Its model brings together health professionals, people with lived experience, youth leaders, digital-health and AI innovators, researchers and social scientists to co-create solutions. It also emphasises collaboration with governments, schools, funders, health facilities and communities so models can be institutionalised and scaled.

Its public priorities include:

- Mental health and wellbeing, especially culturally relevant support for underserved populations.
- Digital health, artificial intelligence and data science to improve access, decision-making and scalable health innovation.
- Community organising and local capacity.
- Research and evidence generation.
- Gender equality and lived-experience leadership.

SRHIN says it has led large youth mental-health programmes in underserved communities in Nigeria and Sierra Leone since 2021. BraveHeart is described as a flagship intervention using community-based task-shifting, digital tools and AI to bring mental-health information and services to IDP camps and other underserved communities.

**Implication for this assessment:** the host challenge sits at the intersection of AI, mental-health research, culturally grounded data, community authority and public benefit. It is not simply a software procurement problem.

### 1.2 What the Mozilla host brief asks for

The supplied Mozilla RFP identifies SRHIN as a Track I Embedded host. Its challenge says mental-health data from African communities is increasingly used to build AI, often without meaningful consent, community control or a share of the benefits. It asks applicants to explore community-owned tools for governance, consent, privacy and benefit-sharing, with a pilot involving young people, people with lived experience and community health workers, in pursuit of a mental-health data commons. The stated time-zone preference is Ibadan or Abuja (WAT, UTC+1), and the location preference is Nigeria.

The RFP is the source of the fellowship challenge. It does **not** establish that SRHIN's own GENSCORE programme lacks the controls described on its current public pages. The challenge may be broader than GENSCORE: it may concern a reusable model for other projects, institutions, data custodians, communities or downstream users of African mental-health data.

### 1.3 The key framing distinction

The RFP frames a wider structural problem: communities can provide data while others retain the power to decide how it is used and who benefits. SRHIN's public GENSCORE materials, meanwhile, describe a project attempting to address several of those concerns internally.

These statements are not necessarily contradictory. They can both be true if:

1. GENSCORE has meaningful governance for its own research pipeline, while wider data practices remain extractive;
2. safeguards work for initial collection and model development but do not yet cover later reuse, licensing, external recipients or derivative models;
3. SRHIN has policies and bodies, but lacks a practical way to make some decisions traceable across technical and organisational boundaries; or
4. SRHIN's current procedures already address the relevant workflow, in which case a new tool is not needed.

We must discover which situation applies before deciding what to build.

---

## 2. Existing technology

### 2.1 Gencurate — collection, preparation and research-data workflow

**Publicly described purpose:** Gencurate is SRHIN's platform for collecting and preparing spoken research data. Its current privacy notice identifies its use in the GENSCORE study, which records adults answering mental-health screening questions in Hausa, Yoruba and Nigerian Pidgin.

The 16 November 2026 privacy notice says Gencurate processes several categories of information:

- Account information for contributors and field officers, including contact and profile information.
- Details entered about recorded participants, which may include a name or label, age, gender, language, dialect and location.
- Audio recordings and the language and time of each answer. The notice explicitly recognises mental-health answers as sensitive personal data.
- Transcripts prepared by a transcription team. The notice states that transcripts are typed by that team and that automated speech recognition is not used for this workflow.
- Activity records, including platform actions and server logs.

The notice says the information is used to collect, transcribe, check and prepare research data for building and testing mental-health screening tools in Nigerian languages.

**Controls publicly described in the privacy notice:**

- Consent is the stated basis for processing; explicit consent is required for recordings about mental health.
- Consent is obtained at account creation and before each recording session.
- Access is role-limited: transcribers see recordings in their organisation awaiting transcription; reviewers see transcripts for their project; administrators see their own organisation's data.
- Research data released from the platform has names and account details replaced by codes by default; each release is logged.
- Recordings, transcripts and participant details are retained for as long as the study needs them and as ethics approval requires, then deleted or anonymised.
- People can request access, correction, deletion, cessation of use, portability, and withdrawal of consent, including withdrawal of recordings from the study.
- The notice states that withdrawing consent does not affect processing that occurred before withdrawal.
- Gencurate says its servers and recording storage are provided by Google Cloud in the United States; the website is hosted by Vercel. It therefore discloses transfers outside Nigeria to service providers.
- The notice says Gencurate is for people aged 18 or older and that only adults may be recorded.

**Assessment:** Gencurate already describes consent capture, research-data preparation, role-based access, release logging and participant rights. Any proposal to recreate those functions would be duplicative unless SRHIN identifies a specific limitation.

**What the public notice does not establish:** the full data schema, encryption configuration, key custody, identity-to-code separation, data-release approval workflow, recipient agreements, onward-transfer restrictions, model-training lineage, process for handling a withdrawal after a dataset has been exported, or what happens to model weights and derived artefacts after a withdrawal request.

The privacy notice is a meaningful source, but it is not a technical security audit or a complete data-governance manual.

### 2.2 GENSCORE — culturally grounded AI-assisted mental-health screening

**Publicly described purpose:** GENSCORE is an SRHIN research initiative developing culturally grounded mental-health screening approaches for Hausa, Yoruba and Nigerian Pidgin speakers. Public descriptions refer to adapted depression and anxiety assessments, including GenPHQ and GenGAD, and work combining voice and self-reported text.

The GENSCORE website describes a workflow with four broad stages:

1. **Listen:** collect local-language voices and stories through lived-experience groups and curate them through Gencurate.
2. **Learn:** fine-tune an open-source model using the corpus and clinician-written clinical and ethical rules.
3. **Score:** generate locally meaningful assessment items and refine them in consensus workshops with psychiatrists and people with lived experience.
4. **Prove:** benchmark adapted tools against established clinical interviews.

The site also describes human review: clinicians rank or correct model outputs, people with lived experience test the resulting items, and the project reports that screening outputs should not be released without human sign-off. A separate SRHIN article explains that AI is intended to support screening and early identification, not replace mental-health professionals.

The Wellcome grant page describes a 2026-funded project to develop and validate culturally grounded multimodal AI software for depression and anxiety screening in Pidgin, Hausa and Yoruba. It describes GENSCORE-DATA v2.0, GENSCORE-LLM v2.0, culturally adapted screening tools and a validation plan involving 990 participants at language-specific sites in Lagos, Abuja and Oyo State, benchmarked against SCID-5-CV interviews.

**Important source reconciliation:** the GENSCORE website currently states that validation involved 3,600 participants across three states, while the Wellcome grant summary describes a 990-participant validation plan. These may refer to different phases, cohorts, versions or updated targets. They should not be collapsed into one figure. SRHIN should confirm what each number represents, what has been completed, and which dataset/model version the fellowship pilot would touch.

**Assessment:** GENSCORE already demonstrates substantial work on local-language data, lived-experience input, clinician oversight, fairness and validation. It is a likely practical context for understanding the host challenge, but we cannot assume it is the only system in scope or that the proposed fellowship project should integrate directly with its production environment.

### 2.3 BraveHeart — community-based mental-health support and task-shifting

SRHIN describes BraveHeart as a community-led, digitally driven programme serving young people in displaced and underserved communities. Public materials describe:

- Community safe spaces, including the Friendship Tent.
- Trained community members and local champions delivering mental-health information and basic support through a task-shifting model.
- Digital mental-health information and services, including the historically described SimbiHealth mobile application.
- An AI companion offering culturally relevant mental-health support and psychoeducation.
- A newer BraveHeart innovation page describing an AI clinical assistant for non-specialist primary-healthcare workers, intended to support screening, management and referral for conditions such as depression, anxiety, PTSD and substance-use disorders.
- Offline-capable tools and low-cost Android devices in the newer product description.
- Mental-health and substance-use-disorder learning curricula.

**Assessment:** BraveHeart provides the programme and community context from which SRHIN's lived-experience and mental-health work has developed. It also means the challenge is not limited to research datasets: data, user interactions, community workflows and AI-assisted care may exist across multiple programmes.

**Boundary:** public descriptions of BraveHeart must not be treated as proof that all listed tools are currently deployed, integrated with GENSCORE, or sharing one data store. The technical relationships between BraveHeart, SimbiHealth, Gencurate and GENSCORE are not established by the pages reviewed.

### 2.4 Other relevant systems and infrastructure

| System or resource | Publicly described role | Relevance to the challenge | What is not established |
|---|---|---|---|
| **SRHIN Knowledge Hub** | Public library of research, guidelines, frameworks, toolkits and policy resources. | Existing governance and lived-experience resources should be reused, not recreated. | Whether internal staff use these resources as mandatory operating procedures, and how implementation is monitored. |
| **ALPHA Centre** | SRHIN's public innovation portfolio lists Gencurate, GENSCORE and other digital-health products such as MamaWell. | Shows that mental-health AI and data collection sit within a broader digital-health portfolio. | Whether projects share infrastructure, data, identity systems or governance processes. |
| **SimbiHealth** | Older SRHIN project materials describe a conversational AI/chatbot for sexual and mental-health information. | Relevant historical example of AI-enabled health information and a potential source of legacy data or operational learning. | Current maintenance status, active deployment, data flows and relationship to current systems. |
| **SRHIN research and clinical partnerships** | GENSCORE pages list SRHIN, University of Ibadan, Imperial College London and Federal Neuro-Psychiatric Hospital, Yaba among institutional participants; other technical collaborators are also named. | Indicates a multi-institutional environment where agreements, responsibility boundaries and data access may matter. | The exact legal roles, contracts, data-controller/processor allocation and project-specific access rights of each partner. |

---

## 3. Existing governance

### 3.1 Lived Experience Working Group (LEWG)

GENSCORE's public lived-experience page says the LEWG has worked with SRHIN for nearly a decade, from BraveHeart to GENSCORE. It describes LEWG members as co-applicants who share responsibility for decisions, outputs and governance—not merely as consultation participants.

The page describes a 12-member panel organised across Hausa-English, Yoruba-English and Pidgin-English language groups, including people with lived experience of depression and anxiety. It also says members choose how they are named publicly and that privacy choices belong to the members.

The published co-production model covers four stages:

- **Compose:** recruit a diverse group through trusted community networks and compensate contributors.
- **Design:** refine questionnaires for clarity, stigma sensitivity and cultural resonance; co-generate and validate locally meaningful assessment items; co-author the Human Oversight Charter.
- **Deliver:** contribute to validation, think-aloud sessions, acceptability reviews, interviews, annotated text/audio datasets and interpretation.
- **Disseminate:** contribute as lead or first authors, present in community workshops and policy dialogues, and lead public storytelling.

**Assessment:** this is a substantial public commitment to lived-experience participation and leadership. A new project should work through existing representative structures where appropriate, rather than set up a parallel advisory panel.

**Unresolved:** the public summary does not provide the full terms of reference, voting rules, quorum, delegated powers, veto rights, appeal routes, conflict-resolution process, succession arrangements or the exact decisions over which LEWG has final authority. The phrase “co-owns it” is a strong organisational statement; the practical decision rights should be examined in the underlying charter and operating procedures.

### 3.2 Independent Data, Ethics & Safety Monitoring Board

GENSCORE's governance page describes an independent board spanning AI ethics, global mental health and Nigerian law. It says the Board:

- Has no reporting line into the project team.
- Meets every two months, with additional escalation when needed.
- Receives reports and meeting minutes from oversight bodies.
- Commissions recurring bias audits across language, gender, age and region.
- Reports findings to both the funder and project team.

The same page describes a wider governance arrangement with:
- LEWG as an advisory/lived-experience body.
- A Data, Ethics & Safety Monitoring Board as the independent board.
- A Project Steering Committee for executive control.
- SRHIN as lead institution coordinating administrative and technological workflows.
- Academic and clinical co-applicant institutions and technical collaborators.

**Assessment:** the public architecture already separates community input, independent oversight and executive project control. The fellowship should not propose replacing this architecture.

**Unresolved:** the public page does not provide the board's terms of reference, appointment process, attendance records, actual audit reports, findings, remediation tracking or the boundary between the Board's authority and formal research ethics committees.

### 3.3 Governance charter, Human Oversight Charter and operating procedures

GENSCORE publicly describes the following governance instruments:

- A written Governance Charter defining roles, responsibilities, decision rights and conflict-of-interest declarations.
- A Human Oversight Charter co-authored with LEWG, defining ethical standards for use of adapted assessments.
- An escalation protocol with risk levels 1–3 and defined responses.
- Standard operating procedures for day-to-day activity.
- Monthly KPI dashboards for governance performance, data integrity and ethical compliance.
- Quarterly reports to oversight bodies and the funder, with minutes.
- Annual external audits.

These descriptions demonstrate that formal governance mechanisms are intended to be part of the project design.

**Unresolved:** the actual documents and evidence of their execution are not available in the public materials reviewed. Before proposing software, the host should identify the authoritative version of each charter/SOP and show how a real decision moves from policy into operational action.

### 3.4 Research ethics, consent and data protection

GENSCORE's governance page states that no data is collected before required approvals. It names the Nigerian National Health Research Ethics Committee (NHREC), the Health and Human Services Secretariat in Abuja and the institutional review boards of collaborating institutions.

It also describes:

- Written informed consent or assent in a participant's preferred language.
- De-identification before analysis.
- Encryption and restricted access.
- Data minimisation.
- Responsiveness and referral pathways established before data collection.
- Fairness commitments grounded in beneficence, non-maleficence and justice.

The separate Gencurate privacy notice gives more operational detail about explicit consent, roles, activity logs, data releases, retention, rights and cross-border storage.

**Important distinction:** formal research ethics approval, individual consent, data-protection compliance and community governance are related but not interchangeable. An ethics approval does not by itself decide every future secondary use or establish collective benefit-sharing. Equally, a community governance agreement does not replace legally required participant rights or ethics review.

### 3.5 Compensation and community participation resources

The SRHIN Knowledge Hub currently lists public resources that directly overlap with common proposed fellowship features:

- **A Template for Lived Experience Compensation and Governance in Digital Health Projects:** described as a policy template covering payment, credit, protection and meaningful say over contributors' material.
- **The Co-Production Readiness Self-Assessment:** a pre-recruitment checklist for deciding whether a team is ready to involve people with lived experience well.
- **The Epistemic Authority Decision Matrix:** a planning tool requiring teams to decide in advance which decisions lived-experience contributors hold real authority over.
- **The LEEF Checklist:** a pre-launch check asking whether knowledge held by people with lived experience has shaped a digital mental-health tool.
- **A Basic Guide for People with Lived Experience to Get Involved in AI Mental Health Tool Design.**
- A prompt bank and a Nigerian Pidgin glossary of expressions of mental distress.

The Knowledge Hub lists these materials as free resources, with the compensation template, co-production checklist and decision matrix described as CC BY 4.0 resources.

**Assessment:** the existence of these resources is important. A project should first test whether SRHIN's current challenge is implementation, operational traceability, adaptation to other organisations, or a need beyond what the resources already cover. Publishing another generic compensation policy or decision matrix would add little.

**Unresolved:** public listings do not establish whether compensation rates, payment schedules, credit decisions, contributor contracts, grievance channels and follow-up obligations are implemented consistently across every programme or partner.

---

## 4. Existing capabilities — consolidated map

| Capability | Existing SRHIN component or process | What public materials say is already handled | Do not rebuild |
|---|---|---|---|
| Initial research-data capture | Gencurate | Structured voice research collection and participant/account records. | A new generic data-collection portal. |
| Individual consent | Gencurate and GENSCORE research process | Consent in preferred language; explicit consent for sensitive mental-health recordings; consent before recording. | A replacement consent checkbox or generic e-consent form. |
| Data preparation | Gencurate and GENSCORE workflow | Transcription, review/curation, annotation and research-data preparation are described. | A duplicate transcription and curation queue. |
| Role-restricted access | Gencurate | Transcriber, reviewer and administrator visibility is limited by role and organisation/project scope. | A generic user-and-role management product without a confirmed gap. |
| Data-release traceability | Gencurate privacy notice | Research releases replace names/account details with codes by default and are logged. | A second release log unless the existing one is insufficient for a defined purpose. |
| Cultural/clinical review | GENSCORE | Lived-experience input, linguist/researcher work and clinical review of language and assessment items. | Another generic annotation or clinical review tool. |
| Model oversight | GENSCORE | Human review, clinical rules, model bias audits and safety escalation are publicly described. | An AI system that approves clinical outputs autonomously. |
| Community decision input | LEWG | Co-production through design, delivery, interpretation and dissemination; co-applicant status is claimed. | A parallel lived-experience committee. |
| Independent oversight | Data, Ethics & Safety Monitoring Board | Independent oversight, bimonthly meetings and regular bias audits are described. | A substitute ethics/safety board. |
| Project accountability | Governance Charter, SOPs, KPI dashboards, reports and audits | Defined roles, escalation, monitoring and periodic reporting are described. | A generic governance dashboard before checking existing reporting. |
| Compensation and contributor authority | Knowledge Hub templates and LEWG practice | Resources address payment, credit, protection, readiness and decision authority; LEWG members are described as compensated. | Another generic compensation or co-production policy. |
| Community mental-health support | BraveHeart | Safe spaces, trained community members, task-shifting, digital information and AI-assisted support are described. | A generic community mental-health chatbot. |

---

## 5. Unresolved questions — what public documentation cannot establish

This is the most important section for determining whether a project is needed. The questions below are not claims of deficiency.

### 5.1 The boundaries of community authority

1. Which community or communities are represented when a dataset is described as community-owned: individual contributors, LEWG, language communities, programme participants, local organisations or a combination?
2. What decisions can LEWG make directly, and which decisions are advisory, delegated or reserved for SRHIN, ethics bodies, institutions or funders?
3. Can the community-authorised body refuse a proposed secondary use, commercial collaboration, model-training use or onward data transfer? Under what process?
4. How are disagreements between individual participant preferences, community-level decisions, research ethics requirements and institutional obligations resolved?
5. How are people who are not members of LEWG represented, including people from communities or language groups not currently represented in the panel?

### 5.2 Consent scope, secondary use and withdrawal

6. Do current consent materials explicitly distinguish collection, transcription, annotation, model training, validation, publication, open data release, external research use, commercial use and onward transfer?
7. How are changes in purpose, model, recipient, collaborator, geographic location or intended deployment assessed?
8. When a participant withdraws, what can be removed from raw recordings, transcripts, curated corpora, exported datasets, embeddings, fine-tuned model weights and deployed systems?
9. Which outputs cannot practically be withdrawn once derived or made anonymous, and how is that limitation explained before consent?
10. Who decides whether a proposed new use is compatible with the original consent and governance conditions?

### 5.3 Data lineage, release and downstream accountability

11. Is there a data-use register connecting dataset versions to purpose, approved users, recipients, conditions, agreements and release events?
12. Are external recipients contractually prohibited from onward transfer, re-identification, unauthorised model training or uses outside the approved purpose?
13. Can SRHIN or authorised community representatives see where each dataset version has gone and which downstream models or products used it?
14. Is there a process for notifying participants or community representatives about material new uses?
15. Are data, model versions, release events and downstream outputs connected through durable identifiers or provenance records?

### 5.4 Benefit-sharing and accountability

16. What does benefit-sharing mean in the SRHIN challenge: compensation to individual contributors, collective community benefits, infrastructure, capacity-building, co-authorship, access to tools, revenue-sharing or some combination?
17. Who defines what counts as an acceptable benefit, and can the community renegotiate terms?
18. Are benefits recorded as enforceable commitments in agreements, or as programme intentions?
19. Who monitors delivery, reports delays and resolves disputes?
20. What happens when a recipient does not fulfil an agreed benefit or reporting obligation?

### 5.5 Technical and institutional architecture

21. What systems currently hold the authoritative consent, governance decision, data-release and benefit-sharing records?
22. Are Gencurate, GENSCORE, BraveHeart and other SRHIN systems technically integrated, or are they separate projects with separate data stores and governance?
23. Which institution is the data controller for each processing activity, and which partners act as processors, joint controllers, recipients or independent researchers?
24. What contracts or data-sharing agreements govern Google Cloud and other service providers, research partners, model collaborators and external data recipients?
25. What transfer mechanism and safeguards support the disclosed storage of Gencurate data in the United States under the Nigeria Data Protection Act?
26. Are current workflows burdensome, fragmented or difficult for community-authorised stewards to inspect—or do existing registers and reports already make them clear?

### 5.6 Pilot population and scope

27. The Gencurate privacy notice says only adults may be recorded, while the Mozilla host brief refers to a pilot with young people. Does the proposed pilot involve adults aged 18–24, or is another approved process intended for minors?
28. Which programme, community, language group, dataset or data-use scenario is the intended pilot context?
29. What role would community health workers play: users of the governance tool, data contributors, decision participants or beneficiaries?
30. What would SRHIN consider a successful project outcome after 12 months?

---

## 6. Potential gap — what may remain unaddressed

### 6.1 Working hypothesis: lifecycle governance after initial collection

The public evidence is strongest for initial collection and internal GENSCORE research governance. Gencurate documents consent and data preparation. GENSCORE documents LEWG involvement, ethics and safety oversight, human review, governance charters and reporting. The Knowledge Hub provides resources on contributor compensation, readiness and authority.

The possible gap is therefore not “there is no consent” or “communities have no voice.”

The possible gap is **whether community authority and agreed conditions remain operationally visible and enforceable after the initial collection and within future data-use decisions**.

A candidate workflow would cover:

1. A dataset or data resource has already been collected under a defined consent and governance arrangement.
2. A researcher, partner or model team proposes a new or changed use.
3. The proposed use is checked against the relevant consent, data-use conditions and community governance decisions.
4. The request is routed to the authority that is actually empowered to decide.
5. The decision and any conditions are recorded against the specific data resource and its version.
6. Any community-agreed benefit, reporting or accountability commitment is tracked to completion.
7. The history remains available to authorised community stewards without exposing participant-level information.

### 6.2 Why this is only a hypothesis

Public websites are not internal operating manuals. The existing process may already be handled through data access committees, research agreements, institutional systems, Gencurate logs, governance dashboards, project managers or manual registers.

A new ledger could make matters worse if it creates duplicate records, introduces a second authority system, exposes sensitive relationships, or suggests that software can determine who owns data or what benefit is fair.

**Go/no-go rule:** if SRHIN already has a reliable workflow that links approved purposes, conditions, changes, recipients and community obligations, do not build MindCommons as currently conceived. Redirect to a different problem only if SRHIN and affected communities identify one.

### 6.3 A broader possibility: a reusable mental-health data commons model

The host challenge may be asking for more than an internal GENSCORE workflow. It may seek a model that other African communities and organisations can use when their mental-health data is collected, processed, licensed or used to develop AI.

A reusable model could combine:
- Community-defined decision rights.
- Individual rights and consent constraints.
- Dataset provenance and permitted-use metadata.
- Agreements covering access, onward transfer and model development.
- Benefit-sharing commitments.
- Plain-language explanations and community reporting.
- Open documentation and interoperable standards.

However, this is too broad for a first prototype. It should not be assumed that SRHIN wants a regional platform or that it has authority to define governance for other communities. Start with one validated workflow.

---

## 7. Software requirements — what genuinely needs to be built

No production software requirement has yet been confirmed. If SRHIN validates the lifecycle-traceability gap, the smallest useful product would be a **Community Data-Use Governance Register** that links existing authoritative records rather than replacing them.

### 7.1 Core user roles

The actual roles must be confirmed with SRHIN, but a test model might include:

- **Community-authorised steward:** views and reviews requests within the authority delegated by the community.
- **Research/data steward:** submits a proposed use and supplies the required documentation.
- **Ethics or governance reviewer:** checks the request against applicable approvals and conditions.
- **SRHIN administrator:** manages records and system access without gaining authority to approve on behalf of the community.
- **External recipient:** receives only the approved conditions and information needed to comply, if SRHIN determines such a role is appropriate.

Role names must reflect actual authority, not software convenience.

### 7.2 Minimum functional requirements

**A. Data-resource reference**

Store metadata only:
- Unique resource and version identifier.
- Resource description and provenance.
- Responsible data steward.
- Collection purpose and applicable consent/approval references.
- Permitted and prohibited use categories, where defined by the authoritative source.
- Review date, expiry or conditions.
- Links to the original authoritative document or system.

Do not store raw audio, transcripts, names, participant-level records or mental-health responses in the prototype.

**B. New-use or change request**

A requester submits:
- Proposed purpose.
- Proposed recipient or collaborator.
- Intended AI/model-development activity.
- Data categories and version required.
- Proposed storage/processing location.
- Retention and onward-transfer plan.
- Expected public, commercial or institutional benefit.
- Risk and safeguard documents.

The system may flag missing fields or apparent conflicts with recorded conditions. It must not decide whether the use is ethically acceptable.

**C. Human decision and conditions**

The system records:
- Which authorised body or person reviewed the request.
- The source of their authority.
- The decision and date.
- Conditions, limitations, review points or reasons.
- Links to the relevant governance and ethics documents.
- Any required re-consent or additional review action.

The system must distinguish community governance decisions from research ethics approval, institutional legal approval and individual consent. One approval must not be represented as a substitute for another.

**D. Obligation follow-up**

Where a community has actually agreed to a benefit or accountability commitment, record:
- The commitment and its source agreement.
- The responsible party.
- Due date or reporting interval.
- Evidence of progress or completion.
- Status and escalation route.

The software must not decide what benefit is fair, create obligations that have not been agreed, or calculate a community's entitlement.

**E. Audit and export**

- Version the record and preserve a traceable decision history.
- Record who created, changed, reviewed or accessed an entry.
- Provide a human-readable decision summary.
- Export a minimal record for authorised review.
- Support a documented correction and dispute process.

### 7.3 Minimum non-functional requirements

- Data minimisation by default.
- Role-based, least-privilege access.
- Separation of duties between request submission and approval.
- Strong authentication for privileged users.
- Encrypted transport and secure storage for any real deployment.
- Append-only or otherwise tamper-evident audit history.
- Clear retention and deletion rules for governance records.
- Accessibility and plain-language usability.
- Support for the language and connectivity realities of the actual pilot.
- No dependency on an AI model to enforce permissions or make approvals.

### 7.4 AI requirement: optional, not foundational

An AI assistant is not required to prove the core workflow. It may add risk and complexity before the governance process is agreed.

If later justified, AI may:
- Explain a recorded condition in plain language.
- Help a requester complete a form.
- Identify missing documentation.
- Summarise a request for reviewers.
- Compare a proposed use with recorded restrictions and cite the source clauses.

AI must not:
- Grant access.
- Approve or reject a use.
- Modify consent.
- Decide who represents a community.
- Determine what benefit is fair.
- Infer permission from silence.
- Override LEWG, ethics or other authorised decision-makers.

The first prototype should be deterministic and human-governed. AI can be considered after the workflow is proven.

---

## 8. Non-software requirements — what governance, policy and participation must do

Software cannot create legitimate community authority. The following work must happen through people, policies, agreements and accountable institutions.

### 8.1 Define community governance in practice

SRHIN and the affected communities must define:
- Who constitutes the relevant community for a given data resource.
- How representatives are selected and replaced.
- Which decisions are delegated and which require wider consultation.
- Which uses can be refused.
- How decisions are documented and communicated.
- How conflicts of interest, disagreements and appeals are handled.
- How individual rights interact with collective governance.

“Community-owned” should not be reduced to a software field labelled owner. The governance meaning and legal arrangements must be defined by the relevant people.

### 8.2 Consent, withdrawal and derivative data policy

The project needs a clear explanation of what consent covers at each stage, including:
- Collection and recording.
- Transcription and annotation.
- Research analysis.
- Model training and validation.
- Publication and data release.
- External research or commercial use.
- Onward transfer.
- Use in derived datasets, embeddings or model weights.

It also needs a transparent withdrawal policy explaining what can be withdrawn, what has already been irreversibly anonymised or aggregated, and what may not be technically removable from a trained model. This must be written and approved by the appropriate research, legal and community authorities—not invented by the software team.

### 8.3 Data-use and benefit-sharing agreements

Where appropriate, agreements should identify:
- Permitted purposes and prohibited uses.
- Data recipients and onward-transfer rules.
- Security and confidentiality obligations.
- Publication, attribution and acknowledgement.
- Model-training and derivative-artifact conditions.
- Reporting and audit rights.
- Benefit-sharing commitments.
- Breach, suspension, dispute and termination procedures.
- Return, retention or deletion obligations.

Benefits may include payment, training, infrastructure, access to tools, co-authorship, community services or other collectively selected forms. The community—not a default software template—must determine what counts as meaningful.

### 8.4 Compensation and capacity-building

Existing SRHIN resources should guide the work. Participation must be properly compensated, accessible and supported. Contributors should understand the work, have enough information to make decisions, and receive credit or privacy according to their preferences.

Capacity-building should not be used as a substitute for payment or decision authority.

### 8.5 Legal, ethics, privacy and security review

Before any real data is used, the host should confirm:
- The data-controller and processor roles for each activity.
- Current ethics approvals and whether the proposed activity requires an amendment or new review.
- The relevant Nigeria Data Protection Act 2023 requirements.
- Lawful grounds and safeguards for any cross-border data transfer.
- Data-sharing, processor and research agreements.
- Privacy impact and security risk assessments.
- Incident response and participant/community notification procedures.

The Nigeria Data Protection Commission's General Application and Implementation Directive describes lawful grounds for cross-border transfer, including an adequacy decision, a Commission-approved cross-border data transfer instrument or other lawful bases. The Gencurate notice discloses US-based cloud storage. This makes the applicable transfer mechanism and safeguards a legitimate validation question; it does **not** establish non-compliance.

---

## 9. Prototype specification — the smallest useful technical demonstration

### 9.1 Proposed prototype name

**MindCommons — Data-Use Decision and Commitment Trace**

This is a provisional name for a research prototype, not a product approved by SRHIN.

### 9.2 Demonstration scenario

Use one fictional mental-health research dataset and one fictional proposed secondary use.

Example:
- A fictional dataset has been collected for a defined research purpose.
- A fictional research partner requests to use a specified version for a new AI-model evaluation.
- The request is checked against fictional consent and governance conditions.
- The request is routed to a fictional community-authorised decision-maker and a separate ethics reviewer.
- A human records approval, rejection or a request for changes.
- If approved with conditions, the system records those conditions and a fictional community benefit commitment.
- The system shows whether the obligation is pending, completed or overdue.

All records must be synthetic. No actual participant information, recordings, consent forms, agreements or confidential SRHIN records should be copied into this demo.

### 9.3 Minimum screens

1. **Resource register:** list of fictional data resources, versions and source-document references.
2. **Use request:** form for a proposed purpose, recipient, model activity, data scope and safeguards.
3. **Review queue:** role-specific view of requests awaiting human review.
4. **Decision record:** decision-maker, authority source, decision, conditions and document references.
5. **Commitment tracker:** agreed benefit/accountability commitments, responsible party, due date and status.
6. **Audit view:** chronological history of submission, review, decision and follow-up.

### 9.4 What the demo must prove

- A proposed use can be linked to the relevant resource and version.
- The system can distinguish the authorities involved.
- A request cannot be marked approved by an unauthorised role.
- A recorded condition can be carried forward into the decision record.
- A benefit commitment can be linked to the use and tracked.
- The history is inspectable and exportable.
- No participant-level health data is required.

### 9.5 What the demo must not claim

The demo must not claim:
- SRHIN has adopted it.
- It is integrated with Gencurate or GENSCORE.
- It is legally compliant or security-certified.
- It has been tested with communities.
- It proves fair benefit-sharing.
- It governs real data access.
- It can reverse model training or guarantee withdrawal from derived models.

### 9.6 Proposed evaluation measures

For the prototype stage, measure only software behaviour:
- Percentage of requests with all required metadata.
- Whether the correct role can submit, review and decide.
- Whether unauthorised approvals are blocked.
- Whether conditions and obligations remain attached to the relevant resource version.
- Whether the audit history can reconstruct the sequence of events.
- Whether a reviewer can identify missing information.

If a later host-led pilot is approved, community-defined measures may include time required to understand a proposed use, ability to locate the source decision, clarity of restrictions, confidence in the process and the visibility of agreed benefits. These require co-design; the developer must not choose the success criteria alone.

---

## 10. Host validation — what SRHIN must confirm before proceeding

A respectful discovery conversation should focus on the host's real workflow, not a pitch for a predetermined solution.

### 10.1 Priority questions for SRHIN

1. **Challenge scope:** Is the Mozilla challenge intended to strengthen GENSCORE's own governance, create a reusable model for other African mental-health data projects, or address a different SRHIN programme?
2. **Existing workflow:** Which system, register, committee, contract or SOP currently connects a dataset's approved purpose to subsequent uses, recipients and conditions?
3. **Change of use:** How are new purposes, new partners, model training, commercial use and onward transfer currently reviewed?
4. **Community authority:** What decision rights do LEWG and other affected communities hold in these cases? Which decisions can they refuse or condition?
5. **Benefit-sharing:** What benefit-sharing arrangements already exist, how are they documented, and who tracks fulfilment?
6. **Withdrawal:** How does withdrawal work after data has been transcribed, coded, released, used in research or incorporated into a model?
7. **Data lifecycle:** Can SRHIN trace the relationship between source recordings, coded data, dataset versions, external releases and downstream model versions?
8. **System boundaries:** How do Gencurate, GENSCORE, BraveHeart and other programmes relate technically and operationally?
9. **Legal and ethics:** What approved protocols, data-sharing agreements, privacy assessments and cross-border transfer safeguards apply to the proposed pilot?
10. **Pilot group:** Which community and which people would participate? How does the “young people” description in the Mozilla brief relate to Gencurate's adult-only recording notice?
11. **Operational pain:** Which part of the current process creates material friction, weak accountability or lack of visibility for community-authorised stewards?
12. **Definition of success:** What specific improvement would SRHIN and the participating communities want to see at the end of 12 months?

### 10.2 Evidence to request only if SRHIN is willing and it is appropriate to share

Do not request sensitive participant data or privileged documents in an introductory message. If a formal discovery relationship is established, ask whether SRHIN can provide safe, appropriately redacted versions of:

- Gencurate data lifecycle and release workflow diagrams.
- Relevant consent language and participant information sheets.
- Governance Charter and Human Oversight Charter.
- LEWG terms of reference and decision-authority matrix.
- Data, Ethics & Safety Monitoring Board terms of reference.
- Data-use, data-sharing and material-transfer agreement templates.
- Benefit-sharing and contributor-compensation procedures.
- Data retention, withdrawal and model-change procedures.
- A redacted example of a request, decision and follow-up record.
- A system inventory showing which tool is authoritative for each record.

SRHIN should decide what may be shared and under what conditions.

### 10.3 Go / no-go criteria

**Proceed to prototype only if all are true:**
- SRHIN identifies a specific workflow that matters to the host and affected community.
- Existing systems and agreements do not already support it adequately.
- The relevant community-authorised people help define the problem and the decision rights.
- A software component is genuinely needed; a policy, agreement or process change alone will not solve the problem.
- The host can identify a realistic pilot context and a responsible supervisor.
- A synthetic-data demonstration can be built without access to sensitive data.
- A path exists for ethics, legal, privacy and security review before any real pilot.

**Stop or redirect if any are true:**
- The workflow is already handled adequately.
- The proposed tool would create a parallel governance authority.
- The community does not want another system.
- The need is primarily a policy, agreement, compensation or institutional-accountability issue.
- The host challenge is focused on a different population, system or workflow.
- The project would require access to sensitive data before appropriate authorisation and safeguards exist.

---

## 11. Source reconciliation and research cautions

Several public descriptions need to be reconciled with SRHIN before any technical specification is treated as accurate:

| Topic | Publicly visible statements | Why host clarification is needed |
|---|---|---|
| GENSCORE validation size | Wellcome grant summary describes a 990-participant validation plan; GENSCORE website states 3,600 participants across three states. | May refer to different study phases or versions. Confirm target, completed recruitment and dataset version. |
| Gencurate transcription | Current privacy notice says transcripts are typed by a transcription team and automated speech recognition is not used in that workflow; product pages describe broader speech/transcription capabilities. | The exact Gencurate product functions used by GENSCORE must be confirmed. |
| Anonymisation terminology | Gencurate notice says names/account details in research releases are replaced with codes by default; GENSCORE governance page says data are anonymised/de-identified before analysis and the corpus is fully anonymised by design. | Confirm whether and where data are pseudonymised, anonymised, linked, or irreversibly anonymised; who holds any linkage key; and what withdrawal remains possible. |
| Participant age | Gencurate notice says only adults may be recorded; Mozilla host brief mentions a pilot involving young people. | Confirm whether the pilot population is adults aged 18–24 or a different approved process. |
| Cross-border infrastructure | Gencurate notice discloses Google Cloud storage in the United States; NDPC guidance sets out grounds and safeguards for cross-border transfers. | Confirm the applicable lawful transfer basis, processor contracts and safeguards without presuming a compliance failure. |
| Governance implementation | GENSCORE pages describe charters, monthly dashboards, quarterly reports, bimonthly independent oversight and annual external audits. | Request underlying policy and implementation evidence before designing software around these processes. |

Public product pages are not substitutes for technical documentation, signed governance instruments or an independent audit. Website claims should be attributed as SRHIN's or GENSCORE's published descriptions, not presented as independently verified facts.

---

## 12. Recommended decision and immediate next step

### Decision

Retain the SRHIN Embedded route as the current fellowship target, but narrow the project claim:

**Do not pitch “a new consent and governance platform for SRHIN.”**

Carry forward this conditional direction instead:

**A community-governed workflow for tracing approved mental-health data uses, changes of use and agreed benefit obligations—only if SRHIN and affected communities confirm that this workflow is not already adequately supported.**

The initial MindCommons concept is a useful design hypothesis, not a validated product. Its three proposed capabilities—approved-use record, change-of-use review and community-obligation follow-up—remain candidates, not final requirements.

### Immediate next deliverable

Before coding, produce a one-page workflow map of the current SRHIN process using only information the host is willing to confirm:

**data resource → consent and governance conditions → proposed use → authorised review → decision and restrictions → data release/use → benefit and accountability follow-up.**

Mark each step as:
- Existing system or document.
- Responsible authority.
- Evidence available.
- Open question.
- Confirmed pain point, if any.

Only the confirmed pain point should become the prototype's problem statement.

---

## Sources

### Primary fellowship source
- Mozilla Foundation, *Fellowships 2027–2028: Imagining a Future Worth Building*, supplied 16-page RFP, especially page 7 (SRHIN challenge), pages 8–9 (track profiles and fit), pages 11–12 (selection, timeline and AI-use policy), and pages 13–16 (LOI questions).

### SRHIN and GENSCORE
- [SRHIN — Our Work](https://srhin.org/our-work/)
- [SRHIN — BraveHeart Intervention Program](https://srhin.org/our-project/braveheart-project/)
- [SRHIN — BraveHeart Innovation Tools](https://srhin.org/braveheart-innovation-tools/)
- [SRHIN — ALPHA Centre](https://srhin.org/alpha-center/)
- [SRHIN — Mental Health Innovation, Leadership and Entrepreneurship Centre](https://srhin.org/mental-health-innovation-leadership-and-entrepreneurship-centre/)
- [GENSCORE — Governance & Ethics](https://www.genscore.io/governance.html)
- [GENSCORE — Lived Experience Working Group](https://www.genscore.io/lived-experience.html)
- [GENSCORE — Project website](https://www.genscore.io/)
- [Gencurate — Privacy Notice, version 16 November 2026](https://app.gencurate.com/privacy)
- [Gencurate — Platform](https://app.gencurate.com/)
- [SRHIN — How SRHIN Is Advancing AI Innovation in Mental Health Screening in Nigeria](https://srhin.org/how-srhin-is-advancing-ai-innovation-in-mental-health-screening-in-nigeria/)

### SRHIN Knowledge Hub
- [SRHIN Knowledge Hub](https://resources.srhin.org/)
- [Template for Lived Experience Compensation and Governance](https://resources.srhin.org/item/lived-experience-compensation-governance-template)
- [Epistemic Authority Decision Matrix](https://resources.srhin.org/item/epistemic-authority-decision-matrix)
- [Co-Production Readiness Self-Assessment](https://resources.srhin.org/item/coproduction-readiness-self-assessment)
- [LEEF Checklist](https://resources.srhin.org/item/leef-checklist)

### Independent funder and Nigerian governance sources
- [Wellcome — GENSCORE Project grant summary (award year 2026)](https://wellcome.org/research-funding/funding-portfolio/funded-grants/genscore-project-leveraging-generative-ai-adapt)
- [Nigeria Data Protection Commission — Nigeria Data Protection Act General Application and Implementation Directive (GAID)](https://ndpc.gov.ng/wp-content/uploads/2025/07/NDP-ACT-GAID-2025-MARCH-20TH.pdf)
- [National Health Research Ethics Committee of Nigeria](https://nhrec.gov.ng/)
- [NHREC — Proposal Guidance](https://nhrec.gov.ng/services/proposal-guidance/)

**Research limitation:** this assessment is based on the public documents and pages listed above as reviewed on 17 November 2026. It is not an audit, legal opinion, clinical assessment, security review or confirmation of SRHIN's internal operating practice.
