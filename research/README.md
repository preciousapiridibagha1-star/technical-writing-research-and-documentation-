# Research Portfolio

This section contains research projects and the methods used to produce them. Each published document identifies its question, scope, sources, method, findings, limitations and practical implications.

## AI Documentation Accountability Research Collection

This is a connected four-paper research sequence, not four unrelated essays. It examines how AI documentation can support accountability, how existing documentation approaches fit together, and how a layered review structure can be applied to public model documentation.

### Research sequence

1. **[Research 01 — AI System Documentation as an Accountability Mechanism](ai-system-documentation-accountability.md)** establishes the problem and research framing. It distinguishes dataset, model, system, deployment, safeguards, oversight and change information, and proposes initial documentation-quality criteria.
2. **[Research 02 — Documentation Review: Gemini 3.5 Flash Model Card](documentation-review-gemini-3-5-flash.md)** applies the initial quality criteria to a public model card. It tests document-level review and identifies the boundary between model documentation and downstream application documentation.
3. **[Research 03 — Comparative Analysis of AI Documentation Frameworks](comparative-analysis-ai-documentation-frameworks.md)** compares Datasheets for Datasets, Model Cards, CLeAR and the NIST AI RMF. It synthesises these approaches into the seven-layer architecture used by the later case studies.
4. **[Research 04 — Applying a Documentation Architecture to a Public AI System: Gemini 3.5 Flash](case-study-documentation-review-gemini-3-5-flash.md)** applies the seven-layer architecture to the publicly available Gemini documentation set and identifies what provider documentation does and does not establish about a downstream application.

### Practical tool and second application

- **[AI System Documentation Review Tool](tools/ai-system-documentation-review-tool.md)** turns the seven-layer architecture into a reusable review worksheet. It defines evidence statuses, source recording, layer-specific questions, a findings register and a cross-layer traceability check. It is a working research tool, not a validated standard.
- **[Case Study 02 — Claude Sonnet 5.5](case-study-documentation-review-claude-sonnet-5-5.md)** applies the same tool to a second provider's public documentation. This is a consistency check across two documentation sets, not a ranking or safety assessment.

### How the pieces connect

The sequence moves from **problem framing → initial criteria → cross-framework synthesis → first application → reusable tool → second application**. Research 02 and Research 04 both examine Gemini documentation but answer different questions: Research 02 reviews a model card against initial quality criteria; Research 04 applies a system-level, seven-layer architecture to a broader provider documentation set. The Claude case study then tests whether that same architecture remains usable with a different provider's sources.

### Shared limitations

All six documents are self-directed public-source desk research or working research tools. They are not peer-reviewed publications, a systematic review, field research, interviews, user testing, model testing, safety audits, certification or evidence that any provider's internal processes are complete. “Not established” means not demonstrated by the sources inspected; it does not mean that the information does not exist elsewhere. The review tool has not been validated through inter-reviewer testing or formal usability research.

## Other published research

- [The Talent Paradox: Skilled Migration, Remittances and Digital Work in Nigeria](talent-paradox-skilled-migration-digital-work-nigeria.md) — revised Nigeria-focused desk-research brief distinguishing emigration, remittances and web-based platform work.
- [AI Job-Search Platforms: Updated Comparison, November 2026](ai-job-search-platforms/updated-comparison-november-2026.md) — source-checked desk-research comparison of Jobright, Sonara, LoopCV and Sorce, including an explicit correction on conflicting Sorce Android information.
- [Audit of the June 2026 AI Job-Search Platforms Report](ai-job-search-platforms/2026-report-audit-and-corrections.md) — documents unsupported rankings, source issues, pricing corrections and evidence limitations.
- [Applied Analysis: Human Oversight in AI-Assisted Job Applications](ai-assisted-decision-making-human-oversight.md) — examines applicant authority, eligibility checks, truthful self-representation, privacy and human review; desk-based analysis, not a live platform evaluation.

- [CORA AI MVP specification](../projects/cora-ai/README.md) — product scope, AI operating boundaries, architecture and handover plan; this is project documentation, not a research report.

## Research methodology

- [Research Methodology](research-methodology/research-methodology.md) — source selection, evidence checking, analytical approach and limitations.

## Research standards

Research should:
1. Start with a clear question.
2. Define geography, timeframe and key terms.
3. Prefer primary sources for policy, eligibility, programme rules and official claims.
4. Record publication dates and access dates.
5. Cross-check important claims.
6. Separate evidence from interpretation.
7. Identify gaps, bias and uncertainty.
8. Avoid presenting correlation as causation.
9. State what the research cannot establish.
10. Update findings when the underlying information changes.

A source appearing in a bibliography does not automatically support every claim. Claims should be traceable to the relevant evidence. Desk research, qualitative studies and national statistics must be described according to their actual scope; none should be presented as nationally representative unless the method supports that conclusion.
