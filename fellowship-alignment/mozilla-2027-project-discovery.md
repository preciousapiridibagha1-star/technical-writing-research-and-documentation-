# Mozilla Foundation Fellowship 2027–2028 — Project Discovery Brief

**Status:** Opportunity and project discovery; no track or final project selected.  
**Last reviewed:** 17 November 2026  
**Purpose:** Turn the current portfolio into evidence of a real problem, identifiable users, a credible intervention and a testable result before drafting a Letter of Interest.

## 1. Decision context

The applicant is interested in two Mozilla focus areas:

1. **Raising p(bloom):** technology that supports human flourishing, agency and wellbeing.
2. **Business models for a post-agentic web:** economic and institutional models for a web increasingly shaped by AI agents.

A separate possible route is the **Track I Embedded** challenge hosted by Slum & Rural Health Initiative (SRHIN), which concerns community-owned governance, consent, privacy and benefit-sharing for mental-health data used in AI.

These are not interchangeable project descriptions. They have different users, problems, evidence requirements and routes into the fellowship.

**Important distinction:** Track I is not automatically easier to enter because the applicant is based in Nigeria. Nigeria is relevant to geographic eligibility for the SRHIN host, but selection still depends on fit, technical ability, a credible project, host needs and community relevance. Track II is designed for applicants with a stronger record of independent leadership and field recognition. The track decision must be based on the actual eligibility and evidence, not on stipend size or perceived ease.

## 2. What a credible Mozilla project must make visible

A reviewer should be able to answer, without guessing:

- **Who experiences the problem?** Name the actual user group and distinguish primary users, affected people, decision-makers and beneficiaries.
- **What are they trying to do?** Describe a real task or decision, not a broad aspiration.
- **Where does the current process fail or create friction?** Support this with public evidence, direct user research or documented host input.
- **What happens today?** Identify existing tools, workarounds, organisations and systems. Do not propose a duplicate.
- **What will the project change?** Specify the smallest useful intervention and the mechanism by which it changes the workflow or outcome.
- **What can be demonstrated?** Provide a working prototype, deployment, dataset, research paper, field-tested process or other inspectable artefact appropriate to the project.
- **Who has used or reviewed it?** State what is verified, by whom, and under what conditions. Do not invent users, consultation, endorsement or impact.
- **How will we know it helped?** Define observable measures and limits before claiming success.

A large folder of architecture diagrams and concept documents is not a substitute for these answers. Documentation should make the product and its evidence inspectable, not merely make the repository look substantial.

## 3. Three routes to investigate — keep them separate

### Route A — Track I Embedded: SRHIN (Nigeria)

**Host challenge as described in Mozilla's RFP:** community-owned governance, consent, privacy and benefit-sharing for mental-health data used in AI, with a pilot involving young people, people with lived experience and community health workers.

**Potential user groups named in the challenge context:**
- People with lived experience of mental-health conditions.
- Young people participating in relevant programmes or research.
- Community health workers.
- Community-authorised stewards and governance bodies.
- Researchers or programme teams who request or use data, as accountable actors rather than the primary beneficiaries.

**Existing work to respect:** The current MindCommons AI note records public SRHIN materials on Gencurate, lived-experience co-governance through LEWG, independent ethics oversight, governance charters and escalation procedures. It explicitly says that public material does not establish whether an internal workflow gap exists.

**Current hypothesis—not a finding:** There may be a narrow coordination or traceability problem around a particular approved data use, changed purpose, decision condition or follow-up obligation. This must be tested against SRHIN's actual tools and operating practices. If existing systems already handle it, do not build a duplicate.

**Do not proceed to build until we have:**
1. A current map of SRHIN's publicly documented tools, services, governance mechanisms and workflows.
2. A comparison showing what each existing component already does.
3. A clearly bounded, evidence-supported unmet need—or a decision to stop this route.
4. Host and community input before representing any proposed workflow as appropriate.
5. A small prototype scope using synthetic data only until authorised data access and safeguards are established.

**Potential demonstration if a genuine gap is validated:** a narrow, role-based workflow that makes one community-authorised process easier to understand, carry out or audit. The exact workflow is deliberately undecided.

### Route B — Independent focus area: Raising p(bloom)

**Interest:** human flourishing and wellbeing, not simply adding another chatbot or claiming that AI makes people happier.

**Potential user groups to investigate:** choose one bounded group only after research—for example, people navigating a specific high-friction information or decision task, or practitioners supporting that group. These are research candidates, not confirmed target users.

**Questions that must be answered:**
- What specific aspect of human flourishing is being addressed: agency, learning, connection, access to opportunity, decision quality, creativity or another defined outcome?
- What concrete situation causes difficulty for the target group?
- What do people currently use, and why are those approaches insufficient?
- What role should AI play, and where should it not be used?
- How could the intervention preserve user agency rather than maximise engagement or dependence?
- What observable outcome could be tested ethically and realistically?

**Minimum credible evidence:** a defined user group, source-grounded problem statement, review of existing solutions, explicit theory of change, working or testable artefact, and a realistic evaluation plan. Claims about wellbeing require appropriate measures and care; a demo alone cannot establish improved mental health or flourishing.

### Route C — Independent focus area: Business models for a post-agentic web

**Interest:** how value, control, compensation and sustainability might work as AI agents increasingly discover, access, summarise and transact across web services.

**Potential user groups to investigate:** independent publishers, small web businesses, creators, open-web service providers or users whose content/services are accessed by agents. Select one group and one transaction or workflow; do not attempt to redesign the entire web.

**Questions that must be answered:**
- What specific economic problem is emerging or already visible for the chosen group?
- How do agent-mediated discovery, access or transactions change traffic, attribution, consent, payment or bargaining power?
- Which existing business models and technical protocols already address part of the problem?
- Who pays, who receives value, who bears infrastructure costs and who can opt out?
- What is the smallest mechanism that could be prototyped and evaluated?
- What would count as evidence that the model is fairer or more sustainable?

**Minimum credible evidence:** a well-sourced market/system analysis, a clearly identified participant group, an explicit value-flow model, comparison with existing approaches, and a prototype or testable mechanism. A speculative token or marketplace concept without participants, incentives and validation is not enough.

## 4. Portfolio audit: what existing work can and cannot support

| Existing project | What it can evidence | What it does not yet prove |
|---|---|---|
| Vantage Automata | A narrow deterministic approval workflow; recorded passing unit tests; thinking about human control and bounded actions | Agentic-web economics, wellbeing outcomes, external deployment or production readiness |
| Jarvis AI | Systems thinking and architecture documentation for an AI-enabled business ecosystem | A working product, actual users, integrations or market validation |
| Organisational Intelligence Platform | A defined organisational workflow concept and limited backend proof of concept using synthetic data | A complete MVP, customer demand, real organisational use or Mozilla-specific fit |
| MindCommons AI | Desk research and a clearly stated hypothesis about community data-use accountability in the SRHIN context | A confirmed SRHIN gap, host approval, community validation or implemented product |
| Open-source contributions | Experience submitting a documentation PR and a source-based governance discussion upstream | Maintainer acceptance, merged code or evidence of sustained technical leadership |

These projects must remain separate. They may demonstrate transferable skills, but they must not be combined into a fictional single product or presented as if one validates another.

## 5. Evidence work plan before selecting the project

### Workstream 1 — SRHIN ecosystem and gap investigation
- Review the latest official SRHIN website, product/service pages, governance documents, publications and public demonstrations.
- Build a feature-and-workflow matrix: existing component, intended user, task supported, data handled, governance role, evidence source, known limitation and unanswered question.
- Compare the current MindCommons hypothesis against this matrix.
- Record which statements are directly evidenced, inferred or unknown.
- Decide: pursue a genuinely distinct gap, reshape the idea around an existing workflow, or stop the route.

### Workstream 2 — Raising p(bloom) opportunity scan
- Select two or three concrete problem domains, not a broad theme.
- Review relevant research and existing products/projects.
- Identify a specific user group and a testable task.
- Draft a problem statement and theory of change for the strongest evidence-backed candidate.

### Workstream 3 — Post-agentic-web opportunity scan
- Map one narrow value flow involving a defined web participant.
- Review current standards, platforms, payment/attribution mechanisms and published research.
- Identify where value or control is lost or misallocated.
- Formulate one testable mechanism rather than a general vision.

### Workstream 4 — Comparative decision
Score each viable route against the same questions:
1. Fit with Mozilla's published focus and track.
2. Specificity and importance of the problem.
3. Evidence that the intended users experience it.
4. Distinctness from existing tools and initiatives.
5. Feasibility within the fellowship period.
6. Applicant's demonstrated ability to lead the work.
7. Access to users, host support and ethical validation.
8. Strength of the demonstrable artefact and evaluation plan.

Do not give a route a high score merely because the applicant is geographically eligible or personally excited by it.

## 6. Communication and relationship-building principles

For the SRHIN route, initial communication should be a short, respectful request to understand the host's current work and priorities—not a pitch claiming to have found a gap or proposing that SRHIN adopt an unvalidated product.

A first contact should:
- Introduce the applicant accurately and link to the relevant portfolio evidence.
- State interest in the Mozilla Embedded challenge and why the public challenge is relevant.
- Acknowledge the existing SRHIN tools and governance work already identified.
- Ask whether the host is open to a brief conversation or can point to public materials that clarify current workflows and unmet needs.
- Make clear that no solution or partnership is being assumed.
- Avoid asking for sensitive data, privileged documents or access to vulnerable participants.

For Independent-track routes, communication should focus on research, public-interest networks and potential collaborators or users appropriate to the chosen project. Do not imply that SRHIN is the host for an Independent proposal unless Mozilla's process and SRHIN explicitly establish that relationship.

No message should be sent until the current official contact route and the factual claims in the message have been checked.

## 7. Current decision

**No final project or track is selected in this document.**

The next action is research, not a pitch and not another large architecture package:

1. Verify the SRHIN ecosystem and identify whether a genuinely unmet workflow exists.
2. Investigate Raising p(bloom) and post-agentic-web business models as the applicant's two stated Independent-track interests.
3. Compare the three routes using evidence, track criteria, feasibility and access.
4. Select one route only after this comparison.
5. Then write the project specification around real users, a verified pain point, a defined workflow, a demonstrable artefact and an evaluation plan.

## 8. Source and claim discipline

- Mozilla programme and track requirements must be checked against the official 2027–2028 RFP and eligibility guidance before submission.
- SRHIN capabilities must be described from current, attributable public sources or direct host confirmation.
- User needs must not be inferred from an organisation's public website alone.
- Public documentation is not proof of how an internal system is operated.
- No host relationship, community consultation, user testing, deployment or impact is claimed until it occurs.
- Any prototype should use synthetic data unless appropriate authorisation, consent, security and governance arrangements are in place.
