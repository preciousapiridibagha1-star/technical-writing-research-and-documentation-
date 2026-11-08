# 2. AI Governance & Responsible Technology

## Case study: Governance of AI-assisted recruitment

**Status:** Structured hypothetical case study; source-based legal and policy verification remains outstanding.  
**Scenario:** An employer uses an AI system to extract information from CVs, rank applicants and support shortlisting.

### Governance question

How should an organisation use AI in recruitment while protecting applicants, maintaining accountability and ensuring that automated recommendations receive appropriate scrutiny?

### People affected

Applicants are directly affected by screening and ranking. Recruiters use the recommendations. The employer chooses the criteria and remains responsible for its recruitment process. Vendors design or supply the system. Regulators and oversight teams may have relevant supervisory roles.

### Main risks

- **Discrimination:** Data, proxies or poorly designed criteria may disadvantage groups for reasons unrelated to the role.
- **Privacy:** CVs and related personal data may be collected or retained beyond what is necessary.
- **Automation bias:** Recruiters may accept a ranking without checking the underlying evidence.
- **Weak explanations:** Applicants may not understand or be able to challenge an adverse outcome.
- **Unclear accountability:** Employer and vendor responsibilities may be poorly allocated.
- **Eligibility errors:** Nationality, location or work-authorisation rules may be applied inaccurately or without a role-related basis.

These are risks to investigate, not findings about a named product or employer.

### Proposed controls

1. Define the recruitment purpose and document which decisions the system may support.
2. Review input data and criteria for relevance, accuracy and potential discriminatory effects.
3. Give reviewers sufficient information, training, time and authority to challenge recommendations.
4. Keep final consequential decisions under an appropriately accountable human process.
5. Provide applicants with clear information and an accessible route to request review or correct data.
6. Maintain access controls, retention rules, audit records and an incident-response process.
7. Monitor outcomes after deployment and investigate unexpected patterns.

### Before → after

**Before:** “A human should be in the loop.” This sounds reassuring but does not explain what the person sees, what authority they have or how an error is corrected.

**After:** “A trained recruiter receives the relevant evidence and system limitations, can override the recommendation, records the reason for the decision, and can refer disputed or unusual cases for review. The employer monitors outcomes and investigates patterns of exclusion.” This makes oversight operational and auditable.

### Decision boundaries

| Activity | Initial governance position |
|---|---|
| CV data extraction | May be assisted by automation with accuracy checks and restricted access |
| Applicant ranking | Treat as decision support; examine criteria and group-level outcomes |
| Interview scheduling | May be automated within approved rules and correction routes |
| Applicant rejection | Require a defined, meaningful review and escalation process |
| Recruitment record changes | Restrict permissions and keep traceable records |

The appropriate controls depend on jurisdiction, the role, the system and the consequences. This case study is not legal advice and does not determine that a particular practice is lawful or unlawful.

### Evidence needed to complete the case study

The next research pass must use primary legal texts and regulator guidance for the selected jurisdiction(s), plus authoritative AI risk-management guidance. Record the source, relevant provision, publication/update date, access date and the specific claim it supports. Do not infer legal requirements from general commentary.

### What this demonstrates

The work shows an ability to identify affected stakeholders, distinguish risks, propose proportionate controls and translate an abstract principle—human oversight—into a practical review process. The current document remains a learning case study until its legal and policy claims are verified against authoritative sources.
