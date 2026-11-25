# Research 04: Applying a Documentation Architecture to a Public AI System — Gemini 3.5 Flash

**Research question:** When a layered documentation architecture is applied to a publicly documented AI system, what information is available, what is missing or difficult to establish, and what would a system-level documentation package need to add?

**Case selected:** Google Gemini 3.5 Flash, using publicly available model documentation and related Google AI guidance.  
**Review date:** 25 November 2026  
**Review type:** Public-source documentation case study (desk review)

## Executive summary

This case study applies the layered documentation architecture proposed in Research 03 to the publicly documented Gemini 3.5 Flash system. The primary source inspected was Google's public model card, published 19 May 2026, alongside Gemini API safety guidance and general documentation principles.

The public model card provides a substantial model-level document, including model identity and description, inputs and outputs, architecture, data, implementation, evaluations, intended usage and limitations, safety, red-teaming and risk-related material. The documentation makes distinctions between automated evaluation and human red teaming and provides evaluation-related information and links. The card also indicates where results may not be directly comparable across earlier evaluations because evaluation updates have occurred.

This review is not an assessment of the model's safety, capability or actual deployed behaviour. It evaluates only the public documentation that could be inspected. It finds that model-level documentation provides useful information, but public documentation alone does not establish every aspect of an individual downstream deployment, such as its exact configuration, application-specific workflow, local monitoring, human oversight, incident processes, decision ownership or user recourse. Those aspects may exist in internal or deployment-specific records but were not established by the sources reviewed.

## 1. Case selection and scope

Gemini 3.5 Flash was selected because a public model card and related guidance provide a concrete documentation set to inspect, and Research 02 previously reviewed the model card at document level. Research 04 extends that earlier work by applying the proposed multi-layer architecture to the documentation available for a model integrated into downstream applications.

**Scope limitation:** The review examines Google's publicly available provider documentation. It does not inspect internal training records, code, datasets, deployment configurations, confidential evaluations or operational telemetry. It does not test Gemini, use it to produce benchmark results, interview Google personnel or examine a particular third-party application built with it.

## 2. Method

The review applied the checklist and layers from Research 03 to publicly available sources:

- Google DeepMind, Gemini 3.5 Flash model card (published 19 May 2026).
- Gemini API Safety Guidance.
- Research 03's proposed seven-layer architecture.
- CLeAR principles as a qualitative lens: Comparable, Legible, Actionable and Robust.

The review distinguishes:
- **Observed:** information explicitly present in the public source.
- **Not established:** information that the source set reviewed does not demonstrate. This does not mean that the information does not exist.
- **Recommendation:** proposed improvement or documentation need, not a claim about Google's actual practices.

## 3. Sources inspected

### Primary documentation
**Gemini 3.5 Flash Model Card**  
https://deepmind.google/models/model-cards/gemini-3-5-flash/

Published 19 May 2026. The model card presents model-related information including identity, inputs/outputs, architecture, data, implementation, evaluation, intended usage and limitations, safety and risk-related information. It includes automated evaluation and human red-teaming material, links to evaluation methods and related documentation, and notes that evaluation updates can affect comparability with earlier results.

### Supporting documentation
**Gemini API Safety Guidance**  
https://ai.google.dev/gemini-api/docs/safety-guidance

Provides guidance relevant to safe use of the Gemini API, including safeguards and developer considerations. It is provider guidance; it does not constitute evidence about the configuration or practices of any particular downstream application.

## 4. Applying the seven layers

### Layer 1 — System overview and context

**Observed:** The model card identifies and describes the model and provides information about model characteristics and usage context.

**Not established by this provider-level source set:** the purpose, users, affected groups, operating context, accountable owner, workflow and system boundaries of any particular application using the model.

**Recommendation:** Downstream developers should publish a separate system record identifying the specific application, its purpose, affected users, owner, context, system boundary, version and review date. The provider model card should be referenced rather than copied as if it were application-specific documentation.

### Layer 2 — Dataset records

**Observed:** The model card includes data-related information and discussion.

**Not established:** complete publicly inspectable dataset-level provenance, composition, consent/licensing details or dataset documentation for every underlying source and processing stage.

**Recommendation:** Provide dataset documentation or a clear disclosure of the scope and limits of data information available. Do not infer specific dataset details from the model card if they are not disclosed.

### Layer 3 — Model records

**Observed:** The model card provides model-level description, architecture/implementation information, evaluation and risk-related sections, intended use and limitations. It distinguishes automated evaluation and human red-teaming material and points to further methodology documentation. Evaluation updates and comparability limitations are discussed.

**Review finding:** This is the most directly represented layer in the provider documentation inspected. Readers can locate model-level information and evaluation context, but must still interpret evidence boundaries and methodology.

**Recommendation:** Where evaluation results are used in downstream decisions, maintain a record of the model version, evaluation date, methodology, metrics, conditions, uncertainty and relevance to the specific application.

### Layer 4 — Application and deployment record

**Observed:** Provider guidance includes API safety considerations relevant to developers.

**Not established:** the settings, prompts, tools, retrieval sources, workflows, safeguards, access controls, fallback behaviour, human oversight and monitoring of a particular downstream application.

**Recommendation:** Create application-specific system documentation. Provider guidance should be treated as an input to, not a substitute for, local risk analysis and operational decisions.

### Layer 5 — Risk and decision register

**Observed:** Model card includes safety and risk-related discussion and evaluation material.

**Not established:** a downstream application's own risk register, risk acceptance decisions, owners, mitigation tracking or residual-risk decisions.

**Recommendation:** Downstream organizations should document application-specific risks, affected parties, supporting evidence, mitigation decisions, owners, review triggers and residual risks. The public provider documentation alone cannot establish that a downstream deployer completed these activities.

### Layer 6 — Monitoring, incidents and change log

**Observed:** The model card describes evaluation information and notes changes relevant to interpretation and comparison.

**Not established:** real-time or application-specific monitoring, incident response, change control, downstream release records or incident reporting for any chosen application.

**Recommendation:** Downstream developers should maintain versioned operational logs, incident records, monitoring plans and change history. Public provider documentation should be reviewed at major version changes, but local application changes also require their own record.

### Layer 7 — Audience-specific summaries

**Observed:** The model card is a structured provider document with technical and safety-related material. The safety guidance addresses developers.

**Not established:** a plain-language explanation for affected users of a particular downstream application, user-specific recourse mechanisms or local support and escalation pathways.

**Recommendation:** Downstream deployers should produce audience-specific documentation, including a plain-language system explanation, appropriate use and limitations, how outputs are checked, and where affected people can seek help or challenge a consequential decision.

## 5. Documentation assessment

This is a qualitative assessment of the inspected documents, not a score or compliance verdict.

| Layer | Public documentation observed | Boundary / unresolved information in this review | Proposed downstream documentation |
|---|---|---|---|
| System context | Model identity and model description | Application purpose, users, context and owner not established | System card |
| Dataset | Data-related model-card discussion | Dataset provenance/composition detail not fully established | Dataset records/disclosure |
| Model | Description, evaluations, intended usage, limitations, safety and related material | Methodology and applicability must be interpreted; not a local evaluation | Version-specific model record and local evaluation |
| Deployment | Developer safety guidance | Particular app's integration, workflow, configuration and oversight not established | Deployment/system record |
| Risk | Model safety/risk-related information | Local risk ownership, decision and residual risk not established | Local risk register |
| Monitoring/change | Evaluation updates and comparability notes | Particular app's monitoring, incidents and releases not established | Local operational/change records |
| Audience summary | Structured provider documentation | Affected-user explanation and local recourse not established | Plain-language summary and support route |

## 6. CLeAR-based observations

### Comparable
The structured model card makes information easier to locate. Downstream system records could adopt a consistent structure, but comparison of evaluation results still requires attention to methodology, context and version.

### Legible
The card organizes technical and safety-related content. Different audiences may nevertheless require additional plain-language explanations and application-specific summaries. This review does not conduct reader testing, so it cannot establish comprehension.

### Actionable
Evaluation and limitations can inform downstream decisions, but usefulness depends on whether readers understand the conditions, evidence and relevance to their use case. A provider document does not replace application-specific safeguards or accountability.

### Robust
The card notes evaluation updates and comparability considerations. Downstream applications need their own change histories and review processes because provider documentation updates alone do not capture local application changes.

## 7. Principal findings

1. **Provider-level documentation and application-level documentation answer different questions.** A model card is not a complete system card for every application built with the model.
2. **Evaluation disclosure needs context.** Methodology, version and comparability notes are important to interpreting published results.
3. **Transparency has boundaries.** Public documentation does not establish the completeness of internal records or the actual behaviour of a particular deployment.
4. **Responsibility shifts in part to deployers.** Application-specific configuration, workflow, oversight, risk decisions and recourse need local documentation.
5. **Traceability is an improvement opportunity.** A downstream record should connect model version and provider evidence to the local configuration, evaluation, decisions, monitoring and change history.

## 8. Proposed system-documentation template for a downstream Gemini application

This template is proposed, not a record of any real deployment.

- **System name and version:** 
- **Purpose and context:** 
- **Users and affected people:** 
- **Owner and contact:** 
- **Provider model and version:** 
- **Integration details:** prompts, tools, retrieval, data inputs, workflow and settings (appropriate disclosure level)
- **Intended and inappropriate use:** 
- **Local evaluation:** methods, conditions, results, limitations and dates
- **Risks and mitigations:** 
- **Human oversight and fallback:** 
- **Privacy and security:** 
- **Monitoring and incident process:** 
- **Change history and review date:** 
- **User explanation and recourse:** 
- **Evidence gaps and assumptions:** 

## 9. Limitations

- Public documentation review only.
- No direct model testing or application testing.
- No access to internal datasets, training procedures, code or logs.
- No interviews, user comprehension tests or deployment observation.
- Findings about information not established are not claims that information is absent internally.
- No certification, compliance verdict or safety conclusion.

## 10. Conclusion

The public model card provides a substantial model-level documentation resource. Applying the Research 03 architecture highlights the need to distinguish provider information from application-specific system documentation. A downstream deployment would still need to document its context, configuration, local evaluation, risk decisions, oversight, monitoring, incidents, change history and user recourse.

This case study demonstrates how a documentation architecture can be applied to a public documentation set to identify visible evidence, boundaries and downstream documentation needs. It does not demonstrate that the model or any application is safe, unsafe, compliant or non-compliant.

## References

1. Google DeepMind. *Gemini 3.5 Flash Model Card*. Published 19 May 2026. https://deepmind.google/models/model-cards/gemini-3-5-flash/
2. Google AI. *Gemini API Safety Guidance*. https://ai.google.dev/gemini-api/docs/safety-guidance
3. Chmielinski, K. et al. (2024). *The CLeAR Documentation Framework for AI Transparency*. https://shorensteincenter.org/resource/clear-documentation-framework-ai-transparency-recommendations-practitioners-context-policymakers/
4. UC Berkeley Center for Responsible AI. *Transparency in Generative AI Systems: A Playbook*. https://ucb-responsibleai.github.io/TransparencyPlaybook/playbook.html

## Research integrity statement

This case study is an independent public-source documentation review. It is not a safety evaluation, audit, certification, systematic review, field study or empirical validation. Findings describe the public documentation inspected and identify information not established by that source set; they do not assert that the information is absent from internal or other records.