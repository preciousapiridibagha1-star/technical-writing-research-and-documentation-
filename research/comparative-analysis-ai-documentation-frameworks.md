# Research 03: Comparative Analysis of AI Documentation Frameworks

**Research question:** How do established AI documentation approaches complement one another, and what practical structure could support transparency across datasets, models and AI systems?

**Review type:** Comparative desk research | **Date:** 25 November 2026

## Executive summary

Datasheets for Datasets focus on datasets and their provenance, composition, collection, intended uses and maintenance. Model Cards focus on trained models, evaluation, intended use and limitations. CLeAR offers cross-cutting documentation principles—Comparable, Legible, Actionable and Robust. NIST AI RMF connects risk-management practice through GOVERN, MAP, MEASURE and MANAGE rather than prescribing a documentation template.

These approaches are complementary, not interchangeable. Component documents may not describe how components are integrated into an application, who owns operational decisions, how users are affected, or how incidents and changes are handled. This review proposes a linked, layered documentation set. It is a desk synthesis, not a systematic review, audit, certification or empirical evaluation.

## 1. Scope and method

The review compared published primary descriptions of four approaches qualitatively, focusing on scope, questions addressed, strengths and limitations. It does not rank or score them.

## 2. Frameworks

### Datasheets for Datasets
**Focus:** Dataset.

The proposal responds to the lack of standardized information about how and why datasets are created, their contents, appropriate uses and possible concerns. Suggested documentation covers motivation, composition, collection, uses, distribution and maintenance.

**Strength:** communicates dataset context and provenance to creators and consumers.  
**Boundary:** does not by itself explain model behaviour or application-level deployment.

### Model Cards for Model Reporting
**Focus:** Trained model.

Model Cards propose reporting performance characteristics, evaluation context, intended use, evaluation procedures, relevant subgroup or contextual performance and limitations.

**Strength:** helps users interpret a model and understand its intended context and limitations.  
**Boundary:** cannot fully describe an application’s interfaces, workflows, integration, local operational risks or human processes.

### CLeAR Documentation Framework
**Focus:** Documentation across datasets, models and AI systems.

Four principles:
- **Comparable:** consistent structure and presentation can support comparison.
- **Legible:** understandable to the intended audience.
- **Actionable:** useful in practice and supports decisions.
- **Robust:** maintained and kept relevant over time.

**Strength:** cross-cutting quality principles for documentation.  
**Boundary:** principles need translation into project-specific content, ownership and processes.

### NIST AI Risk Management Framework (AI RMF 1.0)
**Focus:** Organizational AI risk management across the lifecycle.

- **GOVERN:** establish policies, responsibilities, structures and risk-management culture.
- **MAP:** identify risks and contextualize them.
- **MEASURE:** assess, analyse and track risks.
- **MANAGE:** prioritize and respond to risks.

**Strength:** links evidence and documentation to risk decisions and lifecycle practice.  
**Boundary:** it is not a universal dataset/model/system documentation template; organizations must operationalize it.

## 3. Comparison

| Approach | Primary focus | Questions it helps answer | Does not replace |
|---|---|---|---|
| Datasheets | Dataset | Why was data created? How collected? What does it contain? What limitations and uses? | Model and application documentation |
| Model Cards | Model | Intended use? Evaluation context? Performance and limitations? | Dataset and system documentation |
| CLeAR | Documentation quality | Is documentation comparable, legible, actionable and robust? | Project-specific content or risk programme |
| NIST AI RMF | Risk-management process | What is governed, mapped, measured and managed? | Component documentation templates |

## 4. Synthesis and observations

### Different layers require different records
Dataset and model records answer different questions. Neither necessarily documents how a model is integrated into an application. System-level documentation should address context, components, interaction, oversight, operational responsibilities and monitoring.

### Completeness is not the same as usability
A long document may still be hard to use. CLeAR suggests reviewing documentation for clarity, comparability, practical value and maintenance—not merely the presence of headings.

### Documentation should connect to decisions
NIST AI RMF provides a way to connect documentation and evidence with context, assessment, prioritization, response and monitoring. Risk records should connect to actions and accountable owners where appropriate.

### Traceability across documents is a practical need
The reviewed approaches support different documentation levels. A project still needs links between them. A system limitation should ideally connect to relevant component information, evaluation or evidence, mitigation, decision owner and change history. This linkage is a synthesis proposed here, not a requirement shared identically by the frameworks.

## 5. Proposed layered documentation architecture

This structure combines the approaches without claiming endorsement by their authors.

1. **System overview and context:** purpose, intended users, affected people, context, components, boundaries, responsible party and review owner.
2. **Dataset records:** provenance, motivation, collection, composition, processing, permissions, restrictions, limitations, intended uses, maintenance and version.
3. **Model records:** identity, version, dependencies, intended and inappropriate uses, evaluation methods and conditions, results, limitations, risks and mitigations.
4. **Application/deployment record:** integrations, configuration, interfaces, decision pathways, human oversight, failure modes, fallback behaviour and operational dependencies.
5. **Risk and decision register:** context, risk, affected parties, evidence, uncertainty, priority, mitigation, owner, decision and residual risk.
6. **Monitoring, incidents and change log:** signals, incident response, corrective actions, version history, review triggers and ownership.
7. **Audience-specific summaries:** plain-language summary for affected people, technical reference for implementers and governance/risk summary for decision-makers.

## 6. Documentation review checklist

- Can readers identify the system, components, versions and responsible parties?
- Are data sources, context and limitations documented?
- Are model evaluation conditions and evidence described?
- Are intended uses, inappropriate uses and operational boundaries explicit?
- Are risks linked to evidence, actions, owners and review dates?
- Is the content understandable to its intended audience?
- Can readers find linked component and system records?
- Are incidents, changes and updates reflected?
- Are gaps and unavailable evidence explicitly acknowledged?

## 7. Conclusion

Datasheets and Model Cards provide component-level information; CLeAR offers quality principles; NIST AI RMF connects documentation to risk-management activity. A practical approach should preserve these distinctions and link records to decisions, owners, responses and updates. The architecture and checklist proposed here require further refinement and testing; they have not been validated through interviews, deployment or user testing.

## References

1. Gebru, T. et al. (2018; Communications of the ACM, 2021). *Datasheets for Datasets*. https://doi.org/10.48550/arXiv.1803.09010
2. Mitchell, M. et al. (2019). *Model Cards for Model Reporting*. https://doi.org/10.1145/3287560.3287596
3. Chmielinski, K. et al. (2024). *The CLeAR Documentation Framework for AI Transparency*. https://shorensteincenter.org/resource/clear-documentation-framework-ai-transparency-recommendations-practitioners-context-policymakers/
4. Tabassi, E. (2023). *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. NIST. https://doi.org/10.6028/NIST.AI.100-1

## Integrity statement
This is an initial comparative desk synthesis of public sources, not a systematic review, peer-reviewed paper, compliance assessment, audit, empirical study or evidence of field validation. The architecture and checklist are the author's synthesis for further refinement and testing.