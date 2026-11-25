# Case Study 02: Applying the Seven-Layer Documentation Review Tool to Claude Sonnet 5.5

**System examined:** Anthropic Claude Sonnet 5.5  
**Review date:** 25 November 2026  
**Review type:** Public-source desk review  
**Tool applied:** [AI System Documentation Review Tool](tools/ai-system-documentation-review-tool.md)  
**Research connection:** This is a second application of the architecture developed in Research 03 and first applied in Research 04. It tests whether the same review structure can be used with a different provider's public documentation set.

## Executive summary

This case study applies the portfolio's seven-layer review tool to Anthropic's public documentation for Claude Sonnet 5.5. The inspected source set includes Anthropic's model system-card index, its Transparency Hub, the Claude Platform model overview, the model announcement, the Responsible Scaling Policy page and developer guidance on prompt injection.

The reviewed materials provide substantial provider-level information. The Transparency Hub summarises model characteristics, modalities, training-data categories, selected evaluation results and deployment safeguards. Anthropic also publishes a dedicated system card and a versioned Responsible Scaling Policy with public risk-report references. The Platform model page provides technical identifiers, modality, context and output specifications, release/lifecycle information and links to the system card.

Applying the seven layers again exposes the same important boundary identified in the Gemini case study: detailed model/provider documentation is not the same as documentation for a particular downstream application. The public source set does not establish the local configuration, data flows, decision workflow, risk ownership, monitoring, incident response or recourse of any specific third-party deployment.

The tool was usable across a second provider. It separated explicit public evidence from information not established by the inspected source set, and highlighted where provider documentation and deployment-specific records need to be linked. This is a consistency check, not validation of the tool or a comparison of provider quality or model safety.

## 1. Scope and method

### Review boundary

The review covers public Anthropic documentation about Claude Sonnet 5.5 and related platform/developer guidance. It does not examine a particular customer's deployment or application.

The review does not include:
- direct model testing or benchmark reproduction;
- independent verification of Anthropic's evaluation results;
- inspection of internal datasets, training records, source code, telemetry or incident systems;
- interviews with Anthropic staff, downstream deployers or users;
- user-comprehension testing;
- legal or regulatory assessment;
- certification or safety audit.

The system card is linked from Anthropic's official system-card index. The findings below use the publicly accessible model summary, model-platform page and policy/developer pages for the stated observations. The full linked system-card PDF was not independently exhaustively extracted for this review; detailed claims are therefore limited to information surfaced in the official public summaries and page references.

### Evidence labels

- **Observed:** explicit information found in the inspected public sources.
- **Partly documented:** some relevant information is present, but important detail or scope remains unclear.
- **Not established:** the reviewed source set does not demonstrate the information; this does not mean it does not exist.
- **Recommendation:** a proposed improvement or downstream documentation need.

## 2. Sources inspected

| ID | Source | Publisher / date | Use in this review |
|---|---|---|---|
| S1 | [Anthropic Model System Cards](https://www.anthropic.com/system-cards) | Anthropic; page lists Claude Sonnet 5.5, September 2026 | Establishes that system cards document capabilities, safety evaluations and responsible deployment decisions; identifies the Sonnet 5.5 card. |
| S2 | [Anthropic Transparency Hub](https://www.anthropic.com/transparency) | Anthropic; Model Report dated 2 October 2026 | Public summary of model identity, modalities, training-data description, selected evaluations and deployment safeguards. |
| S3 | [Claude Sonnet 5.5 — Claude Platform model overview](https://platform.claude.com/docs/en/models/sonnet-5-5/overview) | Anthropic; current model reference, accessed 25 November 2026 | Model identifier, technical specifications, modalities, release/lifecycle status, supported platforms and system-card link. |
| S4 | [Introducing Claude Sonnet 5.5](https://www.anthropic.com/claude-sonnet-5-5) | Anthropic; 28 September 2026 | Release context and selected capability and safety statements. |
| S5 | [Responsible Scaling Policy](https://www.anthropic.com/responsible-scaling-policy) | Anthropic; page last updated 14 August 2026 | Policy revision history and public risk-report information. |
| S6 | [Mitigate jailbreaks and prompt injections](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks) | Anthropic Platform documentation | Developer guidance on input screening, system prompts and untrusted tool content. |
| S7 | [Claude Sonnet 5.5 system card](https://www.anthropic.com/claude-sonnet-5-5-system-card) | Anthropic; September 2026 | Dedicated provider system-card document, linked from the official system-card index and model page. |

## 3. Applying the seven layers

### Layer 1 — System overview and context

**Observed**

- Anthropic's model system-card index states that system cards document model capabilities, safety evaluations and responsible deployment decisions.
- The Transparency Hub describes Sonnet 5.5 as a model for well-scoped everyday tasks, including coding, agentic tasks and creating documents, slides and spreadsheets.
- The Platform page identifies the model as claude-sonnet-5-5, lists text and image inputs with text output, gives a release date of 28 September 2026 and identifies supported access platforms.

**Partly documented / not established**

- Provider-level identity, purpose and access routes are publicly described.
- The reviewed provider sources do not define the system boundary, owner, users, affected groups or operational context of any one downstream application.
- A list of access platforms does not establish how a particular deployer configured or uses the model.

**Recommendation**

A deployer should publish a separate application/system record naming the application, its purpose, users and affected people, responsible owner, workflow, model identifier, integrations, version and review date. The provider model card should be linked as a component source, not treated as a full application description.

**Layer status:** Partly documented.

### Layer 2 — Dataset records

**Observed**

- The Transparency Hub describes the training data at a broad category level: a proprietary mix of publicly available internet information, public and private datasets, synthetic data generated by other models and potentially some user data from feedback or bug reports or data users explicitly permitted for training.
- It also describes data cleaning and filtering methods, including deduplication and classification.
- The same hub summarises the model's pretraining and post-training approach.

**Partly documented / not established**

- This is a provider-level summary, not an itemised dataset inventory.
- The inspected public summary does not establish the complete source list, dataset-level provenance, composition, licensing/permission details, representation characteristics or the contribution of each source.
- This review does not infer that such records do not exist internally.

**Recommendation**

Where detailed disclosure is not possible, documentation should state the level of detail being disclosed, relevant restrictions and known limitations. A downstream application should separately document its own user inputs, retrieval sources, uploaded materials, retention settings and other data flows; those application data are distinct from the model's training data.

**Layer status:** Partly documented.

### Layer 3 — Model records

**Observed**

- Anthropic provides a dedicated Sonnet 5.5 system card through its official model system-card index and Platform model page.
- The Transparency Hub presents a model summary, supported modalities, a training-method description, selected capability and safety evaluations, and deployment-safeguard information.
- The Platform page supplies the API model identifier, context window, output limit, input/output specifications, knowledge and training-data cutoff, release date, active status and supported platforms.
- The Transparency Hub's evaluation summaries describe particular test designs and conditions, including a distinction between direct API access and the claude.ai setting, where standing system instructions are applied.
- The hub notes that some evaluation results for earlier models may vary from prior system cards because of routine evaluation updates.

**Partly documented / not established**

- The model layer is the most strongly represented layer in the inspected source set.
- The public summary provides selected results and links to fuller evaluation material. It is not itself a complete reproduction package for each evaluation.
- This review does not reproduce tests or independently establish the validity or generalisability of the reported results.

**Recommendation**

Downstream evaluation records should preserve the exact model identifier/snapshot, date, prompt and tool configuration, evaluation method, sample or task coverage, results, uncertainty and known limits. Avoid using a provider-level benchmark as a substitute for testing the particular application and user context.

**Layer status:** Documented at provider level, with evaluation boundaries.

### Layer 4 — Application and deployment record

**Observed**

- The model documentation lists multiple access routes, including the Claude API and supported cloud platforms.
- Anthropic's developer guidance addresses jailbreaks and prompt injection. It recommends input screening, hardened system prompts and safe handling of untrusted tool content, and distinguishes direct user prompt attacks from indirect prompt injection through third-party content.

**Not established**

- The reviewed materials do not describe any particular downstream application's prompts, retrieval corpus, enabled tools, data routing, permissions, workflow, access controls, user interface, human review, fallback behaviour or local monitoring.
- General developer advice does not establish that a specific deployer implemented those controls.

**Recommendation**

For a real integration, create a deployment record that describes model ID and configuration, prompt/tool versions, data sources, external systems, access permissions, untrusted input handling, fallback behaviour, user-facing disclosures and human escalation points. Include verification evidence for locally implemented controls.

**Layer status:** Partly documented at provider-guidance level; downstream deployment is not established.

### Layer 5 — Risk and decision register

**Observed**

- The Transparency Hub links model-specific evaluation and safeguard summaries to the system card.
- Anthropic maintains a Responsible Scaling Policy page with a revision history; the page identifies version 3.4 as effective 8 July 2026 and lists public risk reports, including an August 2026 report.
- The public policy page describes the Risk Reports as covering assessed risks, mitigations and forward-looking plans.
- The model summary states a provider-level deployment decision and describes safeguards for selected risk areas.

**Not established**

- These are provider-level policy and deployment materials. They do not establish risk acceptance decisions, mitigation effectiveness, accountable owners or residual-risk judgements for any specific downstream application.
- This desk review does not independently verify the provider's internal risk processes or reproduce the assessments.

**Recommendation**

Downstream deployers should keep a local risk and decision register that connects each material risk to affected users, evidence, mitigation, owner, decision date, residual uncertainty and review trigger. Reference provider materials as evidence inputs, while keeping local decisions distinct.

**Layer status:** Documented at provider-policy level; local decisions not established.

### Layer 6 — Monitoring, incidents and change log

**Observed**

- The Platform model page identifies release date and lifecycle status and links to model versioning and deprecation documentation.
- The Responsible Scaling Policy page lists dated policy revisions and public risk reports.
- The Transparency Hub provides a dated Model Report and links to model-specific system cards.

**Partly documented / not established**

- These materials show public documentation and policy change visibility at provider level.
- The reviewed sources do not establish an individual deployer's production monitoring thresholds, incident records, corrective actions, release approvals or update responsibilities.
- A public model or policy revision history is not a substitute for an application-specific change log.

**Recommendation**

A deployment should maintain its own versioned record of model IDs, prompts, tools, connected data sources, configuration changes, evaluation results, incidents, mitigations and review dates. Define which provider updates trigger reassessment.

**Layer status:** Partly documented at provider level; downstream operations not established.

### Layer 7 — Audience-specific summaries

**Observed**

- The Transparency Hub is explicitly designed as an accessible summary of model capabilities, safety evaluations and deployment safeguards.
- The model overview links technical readers to model details, system card, migration guidance and API resources.
- The separate Responsible Scaling Policy page makes policy versions and public risk-report information discoverable.

**Not established**

- The reviewed provider materials do not supply a plain-language explanation, support route or appeal/recourse procedure for every downstream application using the model.
- This review did not test whether different audiences understand the Transparency Hub or technical model documents.

**Recommendation**

Downstream applications should provide concise, context-specific explanations for users and affected people. Explain what the application does, when AI output is involved, what human review is available, the limitations of relying on outputs, and how users can report errors or challenge consequential decisions.

**Layer status:** Documented for provider-level summaries; downstream audience needs remain application-specific.

## 4. Findings register

| ID | Layer | Finding | Evidence status | Practical implication |
|---|---|---|---|---|
| F-01 | System context | The provider documents model identity, intended task categories, modalities and access routes, but not the context of every downstream application. | Partly documented | A deployer needs a separate system overview and boundary. |
| F-02 | Dataset | Training-data categories and selected processing methods are summarised, but the public summary is not a full dataset inventory. | Partly documented | State the limits of disclosure and document application data separately. |
| F-03 | Model | A dedicated system card, model reference and public summary are linked; selected evaluation methods and results are described. | Documented at provider level | Preserve exact model version and evaluation conditions in local records. |
| F-04 | Deployment | The provider gives API access routes and prompt-injection guidance, but local implementation is not demonstrated. | Partly documented | Document and test the actual integration. |
| F-05 | Risk | Provider policy, selected safeguards and risk-report references are public. | Documented at provider-policy level | Keep downstream risk ownership and acceptance decisions separate. |
| F-06 | Monitoring/change | Provider model lifecycle and policy revision information are available. | Partly documented | Maintain local change, incident and monitoring records. |
| F-07 | Audience | A public model-summary hub and technical materials exist, but local user recourse and comprehension are not established. | Partly documented | Add application-specific notices, help and challenge routes. |

## 5. Cross-layer traceability check

A downstream reviewer should be able to follow an identified model limitation or provider-reported risk through:

1. the relevant system-card or Transparency Hub statement;
2. the specific model identifier and version;
3. the downstream application configuration in which the model is used;
4. local evaluation evidence and relevant failure modes;
5. the deployer's safeguard or human-review response;
6. the person accountable for the decision;
7. the monitoring, incident and change history;
8. the explanation and recourse route available to affected users.

The reviewed provider sources support parts of this path, but they do not establish the remaining application-specific records for an unspecified deployment.

## 6. What this second application shows about the tool

The tool was applied without changing its seven layers. It was able to identify:
- strong provider-level model documentation and public safety-evaluation summaries;
- dataset transparency that is meaningful but intentionally high-level in the Transparency Hub;
- distinctions between provider policy and downstream deployment responsibility;
- version and policy update information;
- the continued need for deployment-specific risk, monitoring and user-recourse records.

This is a limited consistency check: the same categories helped organise a second public documentation set from a different provider. It does not show inter-reviewer reliability, completeness across all AI systems, user comprehension or predictive value for system safety. Further reviews and independent feedback are required before the tool could be described as validated.

## 7. Conclusion

The Claude Sonnet 5.5 documentation set shows how a provider can connect a model summary, a dedicated system card, technical platform documentation, developer guidance and a public risk policy. This makes more provider-level information discoverable than a single model page would provide.

The seven-layer review still identifies an application boundary: no provider documentation set can, by itself, establish the configuration, data flows, human oversight, local risk decisions, incident handling and recourse of every downstream deployment. Those records need to be created and maintained by the relevant deployer.

Together with the Gemini case study, this second application supports keeping the architecture as a practical documentation-review structure while treating it as an unvalidated research tool. It also confirms the importance of precise evidence labels and clear limits on conclusions.

## References

1. Anthropic. [Model system cards](https://www.anthropic.com/system-cards).
2. Anthropic. [Transparency Hub](https://www.anthropic.com/transparency).
3. Anthropic. [Claude Sonnet 5.5 Platform model overview](https://platform.claude.com/docs/en/models/sonnet-5-5/overview).
4. Anthropic. [Introducing Claude Sonnet 5.5](https://www.anthropic.com/claude-sonnet-5-5), 28 September 2026.
5. Anthropic. [Responsible Scaling Policy](https://www.anthropic.com/responsible-scaling-policy), page last updated 14 August 2026.
6. Anthropic. [Mitigate jailbreaks and prompt injections](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks).
7. Anthropic. [Claude Sonnet 5.5 system card](https://www.anthropic.com/claude-sonnet-5-5-system-card), September 2026.

## Research integrity statement

This is an independent desk review of publicly accessible provider documentation. It is not a model test, safety assessment, compliance review, systematic review, audit, field study or empirical validation. Statements about information not established are bounded to the sources inspected. No conclusion is made about internal records, the actual behaviour of every deployment or the safety of the model.
