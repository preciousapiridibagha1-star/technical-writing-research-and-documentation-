# Jarvis AI — Agent Catalogue Based on the Supplied Architecture

**Status:** Proposed roles transcribed and organised from the user's Jarvis AI architecture outline and diagrams. No agents are verified as configured or operational.

## Purpose

This catalogue follows the roles identified in the existing Jarvis AI architecture baseline. It does not add new agent categories. The ecosystem diagram and AI Business System MVP diagram are related architecture views, and some labels differ between them.

## 1. Owner

- **Role shown:** Supplies business goals and instructions, reviews results and retains final approval in the MVP view.
- **Inputs:** Business objectives, priorities, constraints and instructions.
- **Outputs:** Approved goals, clarifications and decisions.
- **Boundary:** The owner retains authority over consequential decisions. The system must not infer approval from an instruction alone.

## 2. Jarvis CEO Agent / Lead Agent

- **Role shown:** Receives the owner's instruction, interprets it, decomposes it into tasks, delegates to specialist agents, reviews outputs and reports results.
- **Inputs:** Owner instruction, business context and defined operating constraints.
- **Outputs:** Task plan, delegated assignments, reviewed results and owner-facing report.
- **Boundary:** It coordinates work but does not create its own authority or bypass approval requirements. Ambiguity, conflicts and consequential actions must be escalated.

## 3. Executive / Management agents

### COO / Operations Agent
- **Role shown:** Monitors workflows and automations, triggers or supervises tasks, and checks completion.
- **Inputs:** Approved operational goals, workflow status and permitted business data.
- **Outputs:** Task status, exception reports and operational recommendations.
- **Open specification:** Define which workflows it may initiate, which are read-only and which require owner approval.

### CFO / Finance Agent
- **Role shown:** Tracks revenue, fees, commissions, expenses and profit.
- **Inputs:** Authorised financial records and agreed calculation rules.
- **Outputs:** Financial summaries, calculations and exception flags for review.
- **Boundary:** The diagram's tracking role does not authorise transfers, payments, accounting sign-off or independent financial decisions. Data access and prohibited actions must be specified.

### Analytics Agent
- **Role shown:** Tracks revenue, traffic, sales, conversion and product performance.
- **Inputs:** Approved datasets, metric definitions and reporting periods.
- **Outputs:** Performance summaries, trends and questions for investigation.
- **Open specification:** Define authoritative data sources, metric calculations, refresh frequency and treatment of missing data.

### Customer / Customer Support Agent
- **Role shown:** Handles FAQs, installation help, download issues and customer queries.
- **Inputs:** Approved product/service knowledge and permitted customer enquiry information.
- **Outputs:** Routine answers, support guidance and escalation requests.
- **Boundary:** Define approved knowledge, privacy limits, confidence thresholds and human escalation for complaints, unusual cases or policy exceptions.

### Sales Agent — Jarvis ecosystem diagram
- **Role shown:** Supports the buyer journey, WhatsApp, deployment offer and custom-project conversion.
- **Inputs:** Approved offer information, customer enquiry and agreed sales criteria.
- **Outputs:** Buyer guidance, enquiry summaries and proposed next steps.
- **Boundary:** Must not make unauthorised promises, discounts or binding commitments.

### Automation Agent — AI Business System MVP diagram
- **Role shown:** Triggers next tasks and automations and keeps business processes running.
- **Inputs:** Approved task plan, defined triggers and permitted workflow state.
- **Outputs:** Workflow triggers, status updates and automation results.
- **Open decision:** Do not assume this is identical to the Sales Agent. The architecture owner must decide whether these remain separate roles, are renamed, or are scoped differently in the MVP.

## 4. Business / Execution agents

### Product Agent
- **Role shown:** Researches niches and creates or improves products, templates and assets.
- **Example outputs shown:** Product assets, templates and packaged files.
- **Open specification:** Define quality checks, intellectual-property review, source verification and approval before publication.

### Marketplace Agent
- **Role shown:** Manages storefronts, uploads, pricing, descriptions and optimisation.
- **Example outputs:** Published or updated marketplace listings.
- **Boundary:** Live publishing, price changes and catalogue modifications require explicit permissions and appropriate approval.

### Content Agent
- **Role shown:** Creates traffic-oriented content ideas and social content.
- **Example outputs:** Content calendar, captions and post ideas.
- **Boundary:** Define brand rules, fact checking, platform requirements and human review before publication.

### Video Agent
- **Role shown:** Turns screenshots or recordings into promotional or showcase videos.
- **Example output:** Ready-to-post video.
- **Open specification:** Define asset rights, brand requirements, quality review and approval before publishing.

### Affiliate Agent
- **Role shown:** Finds or recruits promoters and tracks performance.
- **Example outputs:** Affiliate database and performance information.
- **Boundary:** Define permitted data, consent, outreach rules, tracking methods and approval of commercial terms.

## 5. Shared requirements for every agent

Before implementation, each role needs:
- A named business owner.
- A defined purpose and trigger.
- Permitted and prohibited tasks.
- Approved inputs and data sources.
- Expected outputs and quality criteria.
- Tool access and permissions.
- Human approval and escalation conditions.
- Error handling and logging.
- Performance measures and review process.

## 6. Architecture discrepancies to resolve

| Topic | Current evidence | Decision still required |
|---|---|---|
| Sales vs Automation | Sales appears in the broader Jarvis diagram; Automation appears in the MVP diagram. | Decide whether separate roles, a renamed role or a scoped split is intended. |
| Customer naming | The diagrams use Customer Agent / Customer Support labels. | Select one canonical name and define the scope. |
| Delegation | The Lead Agent delegates to executive and business agents. | Define exact hand-offs and whether specialist agents may delegate further. |
| Autonomy | The diagrams include automation and execution concepts. | Define permission levels, approval thresholds and stop controls. |
| Dashboard metrics | Illustrative business metrics appear in the diagrams. | Label sample figures as illustrative until connected to verified data. |

## Evidence boundary

This catalogue is a structured interpretation of the supplied architecture outline. It is not proof that any agent, tool or integration exists in a running system. The detailed permissions and behaviours remain to be specified and technically validated.
