# Case Study 1: Governance of an AI Recruitment System

**Workstream:** AI governance and policy understanding  
**Status:** Initial learning exercise — requires source-based development  
**Scenario:** A company uses an AI system to screen and rank job applicants.

## 1. Problem statement

An employer uses an AI recruitment system to assess applications and recommend candidates for shortlisting. The system may improve the speed and consistency of recruitment, but its design and use can also create risks for applicants.

For example, the system might apply nationality or location filters. Some eligibility restrictions may be justified by law, security requirements or the genuine conditions of a role. However, an arbitrary or poorly justified restriction could exclude qualified applicants without a fair assessment of their abilities.

The governance question is:

> What rules, safeguards, responsibilities and review mechanisms should govern the use of an AI recruitment system so that decisions are lawful, fair, secure and appropriately accountable?

## 2. Stakeholders

The initial stakeholder analysis identifies:

- **Applicants:** People whose personal information is processed and whose employment opportunities may be affected.
- **Recruiters and hiring managers:** People who use the system's recommendations and make or approve recruitment decisions.
- **The employer:** The organisation deploying the system and setting the recruitment criteria.
- **AI developers and vendors:** Parties involved in designing, supplying, configuring or maintaining the system.
- **Data protection and employment regulators:** Public bodies that may oversee relevant legal obligations.
- **The wider workforce:** Existing employees and teams affected by hiring outcomes.

Stakeholder interests may differ. The employer may prioritise efficiency, while applicants need fair treatment, privacy, understandable decisions and a way to challenge errors.

## 3. Initial risk analysis

| Risk | How it could arise | Potential impact |
|---|---|---|
| Unfair exclusion or discrimination | Criteria, training data or proxies may disadvantage applicants on grounds unrelated to legitimate role requirements. | Qualified applicants may be unfairly screened out. |
| Privacy and data security failures | CVs and other personal information may be collected, retained, accessed or shared inappropriately. | Exposure of personal data and loss of trust. |
| Over-reliance on automated recommendations | Recruiters may accept AI rankings without meaningful scrutiny. | Errors or unfair outcomes may pass unchecked. |
| Lack of explainability | The employer may be unable to give a clear account of why an applicant was rejected. | Applicants may struggle to understand or challenge decisions. |
| Poorly defined eligibility rules | The system may apply nationality, location or other restrictions without a valid, role-related basis. | Applicants may be excluded for reasons unrelated to their suitability. |
| Weak accountability arrangements | The employer, vendor and staff may not have clearly allocated responsibilities. | Complaints and failures may not be properly investigated or remedied. |

These are potential risks for analysis, not findings about a particular real-world system.

## 4. Accountability: initial position

Responsibility should not automatically be assigned to software engineers alone. Different parties have different roles and obligations.

- **Employer/deployer:** Should take responsibility for the recruitment process, the criteria it chooses, its use of the system and the decisions made through that process.
- **AI developer or vendor:** Should address responsibilities associated with system design, testing, documentation, security and contractual or legal obligations.
- **Recruiters and hiring managers:** Should carry out meaningful reviews within their authority rather than treating automated recommendations as unquestionable.
- **Relevant oversight personnel and regulators:** May provide internal assurance or enforce applicable legal requirements.

The precise allocation depends on the system, contractual arrangements, jurisdiction and applicable law. This case study does not make a legal determination.

## 5. Proposed safeguards

1. **Meaningful human oversight:** Provide trained reviewers with enough information, authority and time to question or override AI recommendations. Human review should not become a rubber stamp.
2. **Defined system permissions and decision authority:** Limit the system to the data and actions needed for its assigned function. For example, it may assist with screening or ranking without independently making final hiring decisions.
3. **Regular testing and audits:** Examine system performance, possible discriminatory effects, data security and reliability before deployment and throughout use. Document problems and corrective action.

Additional safeguards to investigate include clear notices to applicants, explanations of relevant decisions, accessible routes for human reconsideration, data minimisation, retention limits and incident-response procedures.

## 6. Human oversight concepts to investigate

The initial discussion raised the idea of a human reviewing AI decisions. The next stage will distinguish:

- **Human-in-the-loop:** A person participates in the decision or approval process before a specified action is completed.
- **Human-on-the-loop:** A person supervises the system and can intervene when necessary.
- **Human-in-command:** People retain broader authority over the system's purpose, use and operating boundaries.

These labels are useful working concepts, but their precise meanings can vary between frameworks. The next research stage will examine how authoritative sources define human oversight and what makes it effective in practice.

## 7. Questions for further research

- When may nationality or location be a legitimate eligibility condition for a role, and how should such criteria be justified?
- What information should an employer provide to applicants about AI-assisted screening?
- What makes human review meaningful rather than merely formal?
- How should responsibilities be allocated between an employer and an AI vendor?
- What testing, documentation and appeal mechanisms are appropriate?
- Which legal requirements apply in the relevant jurisdictions?

## 8. Current limitations

This is an introductory learning exercise based on a hypothetical scenario and an initial analysis. It is not legal advice, empirical research or an audit of a real recruitment product. The risks and safeguards must be tested against authoritative sources and applicable law before this document is treated as a finished analytical brief.

## 9. Next development steps

1. Build a source register using relevant laws, regulator guidance and authoritative AI governance frameworks.
2. Verify and refine the stakeholder, risk and accountability analysis.
3. Compare human oversight approaches and identify practical implementation requirements.
4. Revise this document into a sourced analytical brief.
5. Add it to the portfolio evidence register only after review and completion.


## 10. Applied analysis: human oversight and control

### 10.1 Activities and approval boundaries

The exercise considered five capabilities: reading CVs, contacting applicants, scheduling interviews, rejecting applicants and updating recruitment records.

The initial position is that **final rejection decisions should require meaningful human review**, particularly where the decision could significantly affect an applicant. The AI may identify possible mismatches or recommend an outcome, but a qualified recruiter should be able to inspect the evidence, challenge the recommendation and correct errors.

Other activities do not necessarily require the same level of approval in every organisation:

- **Reading and extracting CV information:** May be automated for a defined purpose, provided access is authorised, data use is transparent and accuracy is checked.
- **Contacting applicants:** Routine, pre-approved messages may be automated within strict templates and rules. Sensitive, unusual or consequential communications should be escalated for human review.
- **Scheduling interviews:** May be automated within approved availability and communication rules, with a way for applicants or recruiters to correct mistakes.
- **Rejecting applicants:** Should have a clearly defined human-review and escalation process. The level of review required will depend on the decision's significance, applicable law and system design.
- **Updating recruitment records:** May be automated when changes are authorised, traceable and reversible where appropriate. The system should not be able to alter or erase records without controls and audit logs.

The right approach is therefore not to prohibit all autonomous activity. It is to match the level of autonomy to the potential impact, reversibility and risk of each action.

### 10.2 Investigating repeated rejection patterns

If the system repeatedly rejects qualified applicants from Nigeria, India or another group, correcting individual decisions is not enough.

The organisation should investigate the system and recruitment process to identify the cause. Possible causes include:

- Explicit nationality or location filters.
- Proxy variables that correlate with nationality or location.
- Biased or unrepresentative training or evaluation data.
- Incorrectly configured job eligibility criteria.
- Errors in CV parsing or qualification matching.
- Recruiter practices that reinforce automated recommendations.

The organisation should preserve relevant logs, assess the scale and impact of the problem, pause or restrict the affected function where necessary, correct affected decisions and test the system again before resuming use.

Nationality or location restrictions are not automatically improper in every situation; some roles may have genuine legal, contractual or security-related eligibility requirements. The employer should be able to identify and justify the relevant requirement rather than allowing an unexplained technical filter to decide.

### 10.3 Permissions and restrictions

The AI agent should operate under the principle of least privilege: it should receive only the access and authority needed for its assigned tasks.

Possible controls include:

- Read-only access to specified applicant information where editing is unnecessary.
- Permission to send only approved categories of messages.
- Scheduling access limited to authorised calendars and available time slots.
- No authority to make final rejection decisions unless a properly governed process explicitly permits the action and applicable requirements are met.
- Restrictions on exporting, sharing, deleting or retaining applicant data.
- Authentication, role-based access, audit logs and monitoring.
- Escalation to a human when information is incomplete, contradictory or outside the agent's approved rules.

### 10.4 Authority to intervene or suspend

The organisation should designate accountable human owners with authority to restrict, pause or suspend the system. This may include the hiring-process owner and relevant senior operational, risk, compliance or data-protection personnel, according to the organisation's structure.

Developers and vendors may be responsible for technical investigation and remediation within their roles, but the employer deploying the system should not assume that responsibility can simply be transferred to the engineers.

A documented incident process should specify who can stop the system, how affected decisions are reviewed, how applicants are treated during the interruption and what evidence is required before the system is restarted.

### 10.5 Key learning

Human oversight is not meaningful merely because a person is present somewhere in the workflow. Reviewers need sufficient information, competence, time and authority to challenge the AI. The organisation also needs clear intervention rights, access controls, monitoring and accountability.

These are initial design recommendations for the hypothetical case. They require further validation against relevant law, standards and authoritative guidance before being treated as a formal compliance assessment.
