# Jarvis AI

**Project status: Strategic concept and proposed architecture documented; implementation not verified.**

Jarvis AI is a self-directed concept for an AI-enabled business operating ecosystem. It explores how a business owner, organisation or individual building a venture could coordinate work through a lead AI agent and specialised agents for defined business functions.

It is not designed only for CEOs or large companies. The system would need to be adapted to the size, operating model and actual needs of each business. A small e-commerce brand may need a focused customer-support workflow; a larger organisation may need several coordinated specialist functions.

## Strategic principle: problem before technology

The project starts with the business problem, not with a tool. The first task is to understand what is going wrong, why it is happening, who is affected and what outcome needs to improve. Only then should possible AI tools, agent platforms and integrations be evaluated.

For example, slow customer-service responses may be caused by understaffing, fragmented enquiry channels, unclear processes or hard-to-find information. An AI support agent may help with some of these issues, but the right solution depends on the diagnosis. The agent would need approved knowledge, clear boundaries and a reliable route to human staff.

## Proposed system model

1. **Owner and lead agent** — the owner sets direction and retains authority; the lead agent interprets goals, coordinates specialist work, reviews outputs and reports back.
2. **Executive or management agents** — proposed functions such as Operations, Finance, Analytics, Customer Support and Sales/Automation oversee defined business areas.
3. **Business or execution agents** — proposed specialists perform bounded tasks across areas such as product research, marketplace work, content and other business activities.
4. **Infrastructure layer** — proposed interface, orchestration, automation, data and model services.

The broader ecosystem diagram and the simplified AI Business System MVP diagram are related views of the same direction. The MVP should validate one narrow workflow before attempting the wider ecosystem.

## Human oversight, permissions and accountability

The owner or authorised staff member remains accountable for business decisions. An agent may prepare information or a draft, but it should not grant itself authority or expand its own access.

| Situation | Agent behaviour | Human responsibility |
|---|---|---|
| Routine question supported by approved information | Prepare a draft and show the source used. | Review and decide whether to use it. |
| Information missing, outdated or conflicting | State the uncertainty and stop short of inventing an answer. | Check the source or provide corrected information. |
| Complaint, refund, payment, account change or sensitive matter | Escalate without taking the consequential action. | Handle the case through the business's authorised process. |
| Request outside the approved topics | Explain that it is out of scope and route to a person. | Decide whether the scope should change. |
| Proposed change to knowledge or permissions | Do not apply the change automatically. | Approve, document and periodically review the change. |

The first MVP should use least-privilege access, approved knowledge, test data and human review. External sending and consequential actions remain disabled unless separately scoped, authorised, tested and reviewed.

These are proposed governance requirements. They are not evidence that the system currently enforces them.

## Strategic and systems-design contribution

The project documents work in:
- Business-problem framing and root-cause analysis.
- Understanding users, customers and business requirements.
- Identifying suitable and unsuitable AI use cases.
- Designing the proposed system architecture and agent responsibilities.
- Evaluating tools and explaining how components may fit together.
- Defining human oversight, escalation, permissions and risk boundaries.
- Prioritising an MVP and sequencing implementation.
- Preparing requirements, workflows, technical specifications and developer hand-off documentation.

This is strategic and systems-design work. It is not a claim that the author independently coded, configured, integrated or deployed the proposed platform.

## Project documentation

- [Strategic Contribution and Business Application](strategic-contribution.md)
- [Proposed Agent Catalogue](agent-documentation/agent-catalogue.md)
- [Lead-Agent Coordination Workflow](system-workflows/lead-agent-coordination.md)
- [Technology Evaluation Framework](technical-specifications/technology-evaluation.md)
- [First MVP Definition](requirements/first-mvp-definition.md)
- [First MVP Agent Specifications](agent-documentation/first-mvp-agent-specifications.md)
- [First MVP Use-Case Decision Record](decision-records/first-mvp-use-case-decision.md)
- [Proposed System Architecture](architecture/system-overview.md)

The original ecosystem and AI Business MVP diagrams will be added as the final visual assets. Short explainer-video production briefs are in [Portfolio Demonstration Video Briefs](../../media/portfolio-demonstration-video-briefs.md).

## Technology and evidence boundaries

The architecture outline names Open WebUI, CrewAI, n8n, PostgreSQL and Ollama as proposed components. Their roles, compatibility, costs, data boundaries and operational suitability still require validation. A tool appearing in an architecture does not mean it has been configured or integrated.

The diagrams and documents describe a proposal. They do not prove that agents, APIs, integrations or infrastructure are operational. Implementation and testing claims will only be added when supported by evidence.

## Relationship to Vantage Automata

Vantage Automata is a separate, bounded task-approval concept and remains the first practical MVP priority. Jarvis AI documents the broader business ecosystem vision; it should not be presented as an already implemented extension of Vantage Automata.
