# Jarvis AI — Proposed Agent Catalogue

**Status:** Conceptual roles only. No agents are currently verified as configured or operational.

## Purpose

This catalogue defines possible responsibilities for agents in the proposed Jarvis AI ecosystem. An agent should exist only where a real business need justifies it. The catalogue is not a recommendation to deploy every role.

## 1. Owner / Human Decision-Maker

- **Purpose:** Set business direction and retain authority over consequential decisions.
- **Inputs:** Business goals, priorities, constraints and reports.
- **Outputs:** Approved objectives, decisions and delegated authority.
- **Boundaries:** Does not delegate unrestricted financial, legal, employment or other consequential authority to an AI system.

## 2. Lead / Orchestrator Agent

- **Purpose:** Interpret an approved goal, break it into bounded tasks, coordinate specialist work and present consolidated results.
- **Inputs:** Owner-approved objectives, task context and specialist outputs.
- **Outputs:** Task plans, assignments, consolidated reports and escalation requests.
- **Boundaries:** Cannot expand its own permissions, approve high-impact actions or conceal uncertainty. It should request human direction when instructions conflict or scope is unclear.

## 3. Operations Agent

- **Purpose:** Assist with defined operational workflows and identify incomplete or delayed tasks.
- **Inputs:** Approved process documentation, task status and permitted operational data.
- **Outputs:** Status summaries, exception reports and proposed next steps.
- **Boundaries:** No changes to critical operational records without explicit authority and appropriate controls.

## 4. Customer Support Agent

- **Purpose:** Assist with routine customer enquiries using approved business information.
- **Inputs:** Approved FAQs, product/service information and the customer's enquiry within permitted data boundaries.
- **Outputs:** Draft or routine responses, information references and escalation recommendations.
- **Boundaries:** Escalate complaints, sensitive cases, policy exceptions, low-confidence answers and requests requiring human judgement. Do not invent policy or promise unauthorised outcomes.

## 5. Sales Support Agent

- **Purpose:** Help organise incoming enquiries and prepare relevant product or service information.
- **Inputs:** Approved product details, sales criteria and enquiry information.
- **Outputs:** Enquiry summaries, qualification suggestions and draft follow-ups.
- **Boundaries:** No misleading claims, unauthorised discounts, binding commitments or contact without applicable consent and business approval.

## 6. Finance Support Agent

- **Purpose:** Organise approved financial information and prepare summaries for review.
- **Inputs:** Authorised records and defined reporting instructions.
- **Outputs:** Draft summaries, categorisation suggestions and exception flags.
- **Boundaries:** No independent payments, transfers, accounting sign-off or financial advice. Authorised humans retain control.

## 7. Analytics Agent

- **Purpose:** Summarise defined business metrics and identify patterns for investigation.
- **Inputs:** Approved datasets, metric definitions and reporting periods.
- **Outputs:** Reports, charts or questions for further analysis.
- **Boundaries:** Must identify missing data, avoid unsupported causal claims and distinguish observed patterns from interpretation.

## 8. Research Agent

- **Purpose:** Gather and organise information relevant to a defined business question.
- **Inputs:** Research brief, source criteria and permitted sources.
- **Outputs:** Source log, evidence summary, comparison and unresolved questions.
- **Boundaries:** Must distinguish primary from secondary sources, record dates, flag uncertainty and never fabricate citations.

## 9. E-commerce Operations Agent

- **Purpose:** Assist with bounded catalogue, product-information and order-enquiry tasks.
- **Inputs:** Approved catalogue information, process rules and permitted order data.
- **Outputs:** Draft product updates, enquiry summaries and workflow recommendations.
- **Boundaries:** No unapproved price, stock, refund, order or customer-record changes.

## Agent governance requirements

Every agent specification should define:
- Business purpose and owner.
- Permitted tasks and prohibited tasks.
- Approved knowledge and data sources.
- Inputs and outputs.
- Tools and access permissions.
- Human approval and escalation conditions.
- Error handling and logging.
- Performance measures and review owner.

## Architecture note

The roles above are a proposed catalogue. A practical MVP should select one business problem and only the minimum agent responsibilities required to address it. Multiple agents should not be introduced merely to make the architecture appear sophisticated.
