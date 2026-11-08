# Evidence Challenge & Improvement Record

**Portfolio:** Applied Technology Research & Documentation  
**Purpose:** Test the current portfolio work against credible external guidance and evidence.  
**Approach:** Keep what is useful, identify what does not yet stand up, and make a practical improvement plan.  
**Research checked:** 8 November 2026.

This is a focused portfolio review, not a formal audit, systematic review or legal opinion. The sources below challenge and strengthen the work; they do not certify it.

## 1. AI Systems & Practical Implementation

### What the current work says
Vantage Automata proposes a controlled flow: instruction → proposal → validation → human approval/rejection → action → audit record. The new local demo uses deterministic logic and a mock reminder action.

### What external guidance challenges
- OWASP advises least-privilege permissions, input validation, structured-output validation, separation of decision and execution, human approval for high-risk actions, audit metadata and adversarial testing. It warns against relying on model output as authorisation. [OWASP AI Agent Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html).
- Microsoft’s agent safety guidance says approval should be considered according to side effects, data sensitivity, reversibility and scope of impact. [Microsoft Agent Safety](https://learn.microsoft.com/en-us/agent-framework/agents/safety).
- NIST's Generative AI Profile provides a broader lifecycle risk-management approach, rather than treating a single approval button as sufficient. [NIST AI 600-1](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence).

### Before → after
**Before:** “The user approves the action, so the system is safe.”

**After:** “Approval is one control. The application must also restrict what can be proposed, validate the proposal independently, bind approval to the exact proposal, prevent duplicate execution, limit permissions, handle failures safely and keep an audit record.”

### What changes next
Keep the existing small demo. Add only three practical checks next: (1) reject a modified proposal after approval, (2) prevent the same approval from running twice, and (3) show a clear failure state without claiming success. Later, test malicious or misleading instructions before connecting any real tools. Jarvis remains a design concept until a single agent workflow can be demonstrated and evaluated.

**Evidence boundary:** the current Python demo is a deterministic local proof of concept, not an AI agent, production system or security-tested application.

## 2. AI Governance & Responsible Technology

### What the current work says
The recruitment case study identifies bias, privacy, automation bias, explainability and accountability, and proposes human review.

### What external evidence adds or challenges
- UK government guidance identifies risks across sourcing, screening, interviewing and selection, including biased historical data, digital exclusion and the need to evaluate system performance in the organisation's own context. It is written for non-specialists. [Responsible AI in Recruitment](https://www.gov.uk/government/publications/responsible-ai-in-recruitment-guide/responsible-ai-in-recruitment).
- The UK Information Commissioner's Office reports scrutiny of recruitment automation and identifies transparency, discrimination and misuse of personal information as regulatory concerns. Its work draws on engagement with more than 30 employers. [ICO: Recruitment Rewired](https://ico.org.uk/about-the-ico/what-we-do/recruitment-rewired/).
- The Dutch data protection authority explains that meaningful human intervention requires a competent assessor with real authority to change or override the result—not a person who simply confirms a score. [Dutch DPA: meaningful human intervention](https://autoriteitpersoonsgegevens.nl/en/themes/employment-and-benefits/job-applications/online-and-game-based-assessments-in-recruitment-and-selection-rules-for-automated-decision-making).

### Before → after
**Before:** “A human should review AI recruitment decisions.”

**After:** “A trained reviewer must understand the system's relevant limits, see enough evidence to assess the recommendation, have authority to disagree, consider relevant information the system missed, record the decision and provide an escalation route.”

### What changes next
Revise the case study around the recruitment lifecycle, not only final rejection. Add a compact evidence table: risk, source, affected person, control, owner and evidence that the control works. Keep legal statements jurisdiction-specific. Do not present UK or EU rules as Nigerian law.

## 3. Research & Analytical Writing

### What the current work says
The job-platform comparison is desk research and explicitly does not claim successful Nigerian account testing. The Talent Paradox report needs a full source and argument audit.

### What external guidance challenges
University College London describes critical appraisal as checking trustworthiness, relevance, methodology and potential bias—not simply collecting links. [UCL: Appraising studies](https://library-guides.ucl.ac.uk/systematic-reviews/appraising). The University of Texas guide describes systematic reviews as requiring a clear question, explicit reproducible methods, a systematic search and critical appraisal. [UT Austin: Evidence synthesis methods](https://guides.lib.utexas.edu/systematicreviews).

### Before → after
**Before:** “I compared four platforms and identified the best option.”

**After:** “I compared the public claims of four platforms against a defined Nigeria-based use case. I recorded the date and type of each source, separated vendor claims from independent evidence, and marked signup, payment and job eligibility as untested.”

### What changes next
For each research report, add a one-page source and claim table. Check whether each conclusion is supported by the evidence cited. Include contrary evidence and missing information. For The Talent Paradox, do not polish the conclusion until the argument and sources have been checked.

## 4. Internet Governance & Digital Policy

### What the current work says
The brief argues that internet participation depends on more than coverage: affordability, devices, skills, safety and access to relevant services matter.

### What external evidence adds
- ITU's Global Connectivity Report 2025 defines universal and meaningful connectivity through six interdependent dimensions: quality, availability, affordability, devices, skills and security. It also discusses the role of national data ecosystems in evidence-based policy. [ITU Global Connectivity Report 2025](https://www.itu.int/itu-d/reports/statistics/global-connectivity-report-2025/).
- GSMA's 2025 research distinguishes coverage from adoption and examines affordability, knowledge, skills, safety and relevant content as barriers to meaningful mobile internet use. [GSMA State of Mobile Internet Connectivity 2025](https://www.gsmaintelligence.com/research/the-state-of-mobile-internet-connectivity-2025-overview-report).

### Before → after
**Before:** “More people need internet access so they can get online jobs.”

**After:** “Digital participation should be assessed across availability, quality, affordability, suitable devices, skills and safety. For online work, also examine platform eligibility, payment access and whether opportunities are genuinely open across borders.”

### What changes next
Narrow the brief to Nigeria and one practical issue: access to cross-border digital work. Use ITU and GSMA for the connectivity context, then add Nigerian primary sources for local prices, connectivity, regulation and payment access. Clearly separate measured facts from proposed policy options.

## 5. Technical Writing & Documentation

### What the current work says
The portfolio now includes a before-and-after system description and user instructions, plus a README guide, FAQ, user-guide sample and review checklist.

### What external guidance challenges
Google's developer documentation style guide stresses clarity and consistency for the intended technical audience, while recognising that project-specific needs and reader context matter. [Google Developer Documentation Style Guide](https://developers.google.com/style/).

### Before → after
**Before:** “Vantage Automata is an AI-powered platform that automates tasks.”

**After:** “Vantage Automata is a proposed task-approval system. It prepares a structured action proposal from a user's instruction and waits for approval before running a harmless mock action.”

### What changes next
Use one small review checklist across all samples: who is the reader, what task are they trying to complete, what must they know first, what should happen at each step, what can go wrong, and has every instruction been tested? Keep conceptual examples visibly labelled. Do not add screenshots that do not match a real interface.

## 6. Project & Programme Delivery

### What the current work says
The Vantage plan has a narrow first milestone, exclusions, risks, acceptance evidence and tests.

### What external practice challenges
The strongest challenge is whether each milestone has observable completion evidence, whether risks are reviewed as work changes, and whether the plan records what actually happened—not just what was intended. The current portfolio has a plan, but not yet a completed delivery record.

### Before → after
**Before:** “Build the MVP, test it and finish the project.”

**After:** “Complete one end-to-end mock approval journey; attach the source code, test output, known defects, fixes and a short demonstration; mark the milestone complete only when the agreed acceptance checks pass.”

### What changes next
Keep a simple delivery log with five columns: date, task, result/evidence, issue or decision, next action. Update it when real work happens. Do not create fictional progress, stakeholder interviews or project outcomes.

## Consolidated next-work list

| Priority | Work | Completion evidence |
|---|---|---|
| 1 | Strengthen Vantage demo controls | Tests for changed proposal, duplicate approval and failure handling |
| 2 | Upgrade recruitment governance case study | Source-backed risk/control table and jurisdiction limits |
| 3 | Audit existing research reports | Claim-to-source check, counter-evidence and transparent conclusion |
| 4 | Narrow digital policy brief to Nigeria | Local primary sources and clearly scoped policy options |
| 5 | Review technical writing samples | Tested instructions, consistent terminology and reader-focused edits |
| 6 | Start a real delivery log | Dated decisions, test results, issues and fixes |
| 7 | Open-source and community contribution | A real public issue, contribution and verifiable repository record; intentionally last |

## Source-use note

The sources above are authoritative guidance or research publications, but they serve different purposes and jurisdictions. A framework, regulator's guidance, industry report and technical cheat sheet are not interchangeable. This record uses them to challenge the portfolio's assumptions and identify better questions; it does not claim that the portfolio is certified, legally compliant or independently validated.
