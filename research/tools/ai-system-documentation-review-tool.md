# AI System Documentation Review Tool

**Version:** 1.0  
**Derived from:** [Research 03 — Comparative Analysis of AI Documentation Frameworks](../comparative-analysis-ai-documentation-frameworks.md)

**Purpose:** A repeatable desk-review instrument for examining whether a public documentation set makes an AI system understandable, traceable and reviewable across seven connected layers.

> **Status and limits:** This is an independent working tool derived from this portfolio's research. It is not an MLCommons, NIST, CLeAR or other official standard; it is not validated, a certification checklist, a legal assessment or a safety audit. It evaluates the documentation made available within a defined review scope, not the complete internal practices or actual behaviour of an organisation or system.

## 1. How to use the tool

1. Define the exact system, model/version, deployment boundary, review date and intended audiences.
2. List the sources actually inspected. Record publication or update dates and the exact section used.
3. Review each layer below. Do not mark a question as documented merely because a nearby topic is mentioned.
4. Separate what the source explicitly states from reviewer interpretation, recommendations and information that the inspected sources do not establish.
5. Record evidence gaps and limitations without assuming that information absent from public sources is absent internally.
6. Complete the cross-layer traceability check and write a short conclusion with practical next steps.

### Evidence status

| Status | Meaning |
|---|---|
| **Documented** | The inspected source explicitly provides relevant information at a usable level of detail. |
| **Partly documented** | Some relevant information is present, but important details, context or evidence boundaries remain unclear. |
| **Not established** | The inspected source set does not demonstrate the information. This is not proof that the information does not exist elsewhere. |
| **Not applicable** | The question does not apply to the defined system boundary. Explain why. |
| **Not reviewed** | The source or evidence was not inspected, could not be accessed or was outside the review time available. |

Do not convert these statuses into a numerical score or an overall safety/compliance rating.

## 2. Review record

- **System / application name:**
- **Provider / developer:**
- **Model and version(s):**
- **Review date:**
- **Reviewer:**
- **System boundary:** What is included? What is excluded?
- **Use context:** What is the system intended to do, and in which setting?
- **Intended users:**
- **Potentially affected people:**
- **Review purpose:**
- **Review type:** Public-source desk review / other (specify).
- **Important exclusions:** For example, no direct testing, internal access, interviews or deployment observation.

### Source inventory

| ID | Document / source | Publisher | Publication or update date | Date accessed | Sections inspected | Source type / boundary |
|---|---|---|---|---|---|---|
| S1 |  |  |  |  |  |  |
| S2 |  |  |  |  |  |  |
| S3 |  |  |  |  |  |  |

Use stable links where possible. If a page changes over time, record the access date and version or snapshot if available.

## 3. Seven-layer review

For each layer, record: **status, evidence references, observed information, unresolved questions/boundaries, and reviewer recommendation.**

### Layer 1 — System overview and context

**Purpose:** Establish what the system is, why it exists, who it serves or affects, and where its boundary lies.

Review questions:
- Is the system identified by name, version and responsible organisation?
- Is its purpose and intended use described clearly?
- Are the context, intended users and potentially affected groups identified?
- Are system components and external dependencies described?
- Are exclusions, boundaries and material assumptions stated?
- Is a responsible contact or documentation owner identified?

Evidence to seek: system overview, product or deployment description, version/release information, architecture or component descriptions, intended-use statements.

**Layer status:**  
**Evidence references:**  
**Observed information:**  
**Unresolved questions / boundaries:**  
**Reviewer recommendation:**

### Layer 2 — Dataset records

**Purpose:** Understand what data is involved and what is publicly documented about its provenance, composition, processing, restrictions and limitations.

Review questions:
- Are relevant datasets or data sources identified at an appropriate disclosure level?
- Are collection, selection, labelling, filtering, preprocessing and update processes described?
- Is dataset composition or coverage explained where it matters?
- Are known imbalances, biases, missingness or representational limits documented?
- Are permissions, licences, consent conditions or usage restrictions described where relevant?
- Are privacy-sensitive or personal data considerations explained without unnecessary disclosure?
- Are synthetic, third-party, user-provided or internally generated data distinguished where possible?

Evidence to seek: datasheets, dataset cards, data-governance statements, provenance records, public descriptions of data sources and processing.

**Important boundary:** A broad statement such as “trained on diverse data” is not a dataset inventory. Do not infer sources, consent, demographic composition or representativeness when the inspected sources do not establish them.

**Layer status:**  
**Evidence references:**  
**Observed information:**  
**Unresolved questions / boundaries:**  
**Reviewer recommendation:**

### Layer 3 — Model records

**Purpose:** Understand the model component and how its capabilities, limitations and evaluations are documented.

Review questions:
- Are the model name, version or snapshot and relevant dependencies identified?
- Are inputs, outputs and supported modalities described?
- Is architecture or training methodology explained to the extent publicly disclosed?
- Are intended uses, inappropriate uses and known limitations stated?
- Are evaluation methods, test conditions, metrics and results described?
- Are comparisons qualified by differences in versions, test sets, harnesses or methodology?
- Are automated evaluations distinguished from human review or red-teaming?
- Are mitigations and their stated limits described?

Evidence to seek: model cards or system cards, evaluation reports and methodology documents, release notes, model identifiers and version history.

**Layer status:**  
**Evidence references:**  
**Observed information:**  
**Unresolved questions / boundaries:**  
**Reviewer recommendation:**

### Layer 4 — Application and deployment record

**Purpose:** Determine whether the documentation explains how a model is integrated into a particular application or operational workflow.

Review questions:
- Are the deployed model version and configuration identified?
- Are prompts, tools, retrieval sources, APIs, external services and data flows described at an appropriate level?
- Are the application purpose, workflow and decision points clear?
- Are access controls, security boundaries, privacy controls and dependencies documented?
- Are failure modes, fallback behaviour and service limitations described?
- Is human review or intervention explained where relevant?
- Are provider instructions distinguished from controls implemented by the deployer?

Evidence to seek: application/system card, architecture, API and integration documents, operating procedures and deployment-specific evaluation.

**Important boundary:** Provider model documentation does not automatically describe every downstream application. Do not treat general developer guidance as evidence that a particular deployer implemented it.

**Layer status:**  
**Evidence references:**  
**Observed information:**  
**Unresolved questions / boundaries:**  
**Reviewer recommendation:**

### Layer 5 — Risk and decision register

**Purpose:** Establish whether risks are connected to evidence, mitigations, accountable decisions and residual uncertainty.

Review questions:
- Are relevant risks and potentially affected parties identified?
- Are risk claims linked to evidence, test results or clearly labelled assumptions?
- Are mitigation measures described, including their scope and limitations?
- Is responsibility for decisions or risk acceptance identified?
- Are residual risks, unresolved questions and trade-offs visible?
- Are review triggers or escalation routes described?
- Can readers distinguish provider-level risk decisions from deployer-level decisions?

Evidence to seek: risk assessments, safety reports, policy documents and decision records; ownership or governance roles where disclosed; mitigation and residual-risk statements.

Do not infer that a risk has been accepted, mitigated or independently reviewed unless the source says so.

**Layer status:**  
**Evidence references:**  
**Observed information:**  
**Unresolved questions / boundaries:**  
**Reviewer recommendation:**

### Layer 6 — Monitoring, incidents and change log

**Purpose:** Determine how documentation addresses system changes, operational signals, incidents and corrective action over time.

Review questions:
- Is the release, version or revision history visible?
- Are important changes and their dates summarised?
- Are monitoring responsibilities, metrics or review signals described?
- Are incident reporting, investigation and corrective-action processes explained?
- Are documentation update triggers defined?
- Can readers connect a change or incident to the system/model version it affected?
- Are stale links or inherited documents clearly identified?

Evidence to seek: release notes, changelogs, incident disclosures and policy revision histories, monitoring/escalation documentation and version-specific evaluation updates.

**Layer status:**  
**Evidence references:**  
**Observed information:**  
**Unresolved questions / boundaries:**  
**Reviewer recommendation:**

### Layer 7 — Audience-specific summaries

**Purpose:** Check whether the information is understandable and actionable for the people who need it.

Review questions:
- Is there a concise plain-language explanation of the system and its purpose?
- Are limitations and appropriate reliance explained for non-specialists?
- Do developers and operators have technical guidance relevant to implementation?
- Do decision-makers have risk and governance information?
- Are affected people told what the system may mean for them?
- Are support, complaint, challenge or recourse routes described where relevant?
- Is the information navigable, accessible and kept current?
- Has audience comprehension been tested, or is it only assumed?

Evidence to seek: summary pages, help materials, user notices, developer guidance, governance summaries and accessibility or user-testing evidence.

**Layer status:**  
**Evidence references:**  
**Observed information:**  
**Unresolved questions / boundaries:**  
**Reviewer recommendation:**

## 4. Cross-layer traceability check

Select one important system claim, limitation or risk and test whether a reader can follow it through related documentation.

| Traceability step | Evidence / link | Status |
|---|---|---|
| Claim, limitation or risk is stated |  |  |
| Relevant dataset or model component is identified |  |  |
| Evaluation or supporting evidence is linked |  |  |
| Application/deployment context is identified |  |  |
| Mitigation or operational response is described |  |  |
| Responsible owner or decision role is identified |  |  |
| Version/change or review date is visible |  |  |
| Affected-user explanation or recourse is available where relevant |  |  |

A break in this chain is a documentation finding, not automatic proof of unsafe system behaviour.

## 5. Findings register

| ID | Layer | Finding | Evidence reference | Evidence status | Impact on reader / decision | Suggested improvement |
|---|---|---|---|---|---|---|
| F-01 |  |  |  |  |  |  |
| F-02 |  |  |  |  |  |  |
| F-03 |  |  |  |  |  |  |

For every finding, keep these categories separate:
- **Observation:** What the source explicitly says or shows.
- **Interpretation:** What that means for the defined review question.
- **Recommendation:** What could make the documentation more useful.
- **Not established:** What the reviewed sources do not demonstrate.

## 6. Closing assessment

1. **Most clearly documented layers:**
2. **Layers partly covered:**
3. **Important information not established by the reviewed sources:**
4. **Information not reviewed or inaccessible:**
5. **Most useful documentation improvements:**
6. **One cross-layer traceability strength or break:**
7. **Who would benefit from the improvements and why:**

### Quality and integrity checks

- [ ] Review boundary and exclusions are explicit.
- [ ] Each substantive finding has a source reference.
- [ ] Publication, revision and access dates are recorded where available.
- [ ] Observations are separated from interpretations and recommendations.
- [ ] “Not established” is not presented as “does not exist”.
- [ ] Provider-level and application-level responsibilities are distinguished.
- [ ] No safety, compliance or certification verdict is inferred from documentation alone.
- [ ] No numerical rating is presented as a validated measure.
- [ ] Links and references have been checked before publication.

## 7. Method note

The seven layers are a synthesis developed in this portfolio from the comparison of Datasheets for Datasets, Model Cards, the CLeAR documentation framework and the NIST AI Risk Management Framework. The tool is intended for repeatable public-source documentation reviews. It requires further independent testing, user feedback and revision before it could be treated as a validated instrument.
