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
