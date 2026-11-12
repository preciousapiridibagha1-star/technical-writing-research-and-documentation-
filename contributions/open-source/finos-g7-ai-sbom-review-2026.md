# Review Note: G7 Minimum Elements for an AI Software Bill of Materials

**Prepared by:** Precious Apiri Dibagha  
**Research checked:** 12 November 2026  
**Upstream discussion:** [FINOS AI Governance Framework #424](https://github.com/finos/ai-governance-framework/issues/424)  
**Document reviewed:** [Software Bill of Materials for AI - Minimum Elements (G7/BSI PDF)](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/KI/SBOM-for-AI_minimum-elements.pdf)

## Executive summary

The G7 guidance is a useful starting point for making AI supply chains more visible. Its central contribution is to adapt the software bill of materials (SBOM) idea to AI systems, whose relevant components can include models, datasets, supporting software and infrastructure, as well as security-related information. This can help an organisation ask better questions when it procures, develops, integrates or operates an AI-enabled system.

An AI SBOM should, however, be treated as a structured transparency and evidence input—not as proof that an AI system is safe, accurate, fair, lawful, secure or suitable for a particular use. The value of the inventory depends on its scope, freshness, provenance, completeness and the organisation's ability to verify important claims.

For the FINOS AI Governance Framework, the most practical opportunity is to connect AI SBOM information to existing technology onboarding, third-party risk, change management, security review and ongoing monitoring processes. The SBOM can inform these controls; it should not replace them.

## 1. Scope and status of the guidance

The G7 Cybersecurity Working Group's *Software Bill of Materials for AI - Minimum Elements* was released on 12 May 2026 by CISA and G7 international partners. CISA describes the guidance as recommendations for additional AI-related SBOM elements to be considered alongside general SBOM minimum elements. CISA also states that the supplemental elements are not exhaustive or mandatory and are expected to evolve.

That status matters. The guidance is a voluntary baseline and a practical transparency aid. It should not be presented as a certification scheme, a complete AI risk assessment, or a legal compliance checklist.

The distinction between the general SBOM baseline and AI-specific information is also important. AI systems remain software systems and need ordinary component and dependency visibility. AI-specific documentation can add context that a conventional software inventory may not adequately express, such as model and dataset information, model lineage, intended use and relevant safeguards.

## 2. Why AI supply-chain visibility needs additional context

An AI-enabled service is often assembled from more than one model or software package. Depending on the system, its lifecycle may involve:
- one or more models, including externally hosted models;
- training, fine-tuning, validation or evaluation datasets;
- application code, orchestration components and third-party libraries;
- infrastructure and external services;
- safety and security controls; and
- updates to models, datasets, prompts, dependencies or service configurations.

A conventional component list can identify software dependencies, but it may not by itself explain how data moves through an AI system, which model is used for a particular function, what data was used in development, or which safeguards are claimed to be in place.

An AI SBOM can improve the visibility of these relationships. It gives procurement, security, engineering and governance teams a more structured basis for asking what is inside a system and what has changed. It does not, by itself, establish that the information supplied is accurate or that the listed controls work.

## 3. Governance implications and practical review

### 3.1 Treat the SBOM as an evidence input, not an assurance verdict

A completed inventory is not equivalent to a verified system. A supplier can provide a detailed SBOM while important statements remain unverified, incomplete or out of date.

A receiving organisation should distinguish at least four things during intake:
1. **Declared information:** what the supplier or SBOM author states.
2. **Corroborated information:** what can be checked against a trusted independent source or artifact.
3. **Unknown information:** information the author does not know.
4. **Withheld information:** information known to the author but not disclosed to the recipient.

The last two categories should not be collapsed. The G7/BSI material distinguishes information that is unknown from information that is intentionally withheld. That distinction helps a recipient decide whether to request clarification, seek an alternative evidence source, apply a contractual restriction or record a residual risk.

These four labels are a proposed intake practice for discussion, not a claim that the G7 document mandates this exact status vocabulary.

### 3.2 Interpret hashes and signatures narrowly

A component or model hash can help identify a particular artifact. If a hash matches a trusted reference generated from the artifact being assessed, it supports the conclusion that the compared bytes match. If it differs, the artifacts do not match under that comparison. If the relevant hash is unknown or withheld, identity has not been established by that check.

A hash match does not prove that the artifact is safe, unbiased, high quality, correctly trained or appropriate for the intended use. It also does not establish provenance unless the reference value and the chain connecting it to the claimed producer are trustworthy.

Similarly, a digital signature can support verification of origin and integrity when the signing identity, certificate or key-management process is trusted. It does not independently prove that the SBOM is complete or that every statement in it is true. Reviewers should therefore check the trust basis for both the artifact and the evidence used to describe it.

### 3.3 Make lifecycle updates part of governance

AI components and dependencies can change after initial onboarding. A model can be replaced, a dataset corrected, a hosted service updated, or an application dependency changed. An SBOM that accurately described an earlier release may no longer describe the system in operation.

Organisations should therefore connect SBOM refreshes to meaningful change events, including:
- a new system or model release;
- a model or dataset replacement or material revision;
- changes to external model providers or APIs;
- dependency or infrastructure changes that alter the system's attack surface; and
- corrections to previously supplied component information.

The organisation should define who is responsible for providing updates, how quickly they are expected, how version history is retained and how material changes trigger renewed risk review. A timestamp alone is not a change-management process.

### 3.4 Link inventory information to actual control decisions

The strongest governance use is not simply storing an AI SBOM. It is using relevant fields to inform specific decisions:
- **Procurement and onboarding:** identify suppliers, models, datasets, dependencies and missing information before approval.
- **Security review:** support vulnerability triage, component identification and investigation of affected releases.
- **Privacy and data governance:** identify dataset references and data flows that require separate purpose, lawful-basis, retention or access review.
- **Model and use-case risk review:** connect intended use, model limitations and system context to the organisation's own impact and risk assessment.
- **Change management:** detect material changes and decide whether previous approvals remain valid.
- **Incident response:** use versioned component information to narrow the scope of investigation and communicate with suppliers.

These are proposed operational uses. An SBOM does not itself complete a privacy assessment, determine an AI system's risk classification, validate a supplier's security controls or decide whether a use case should be approved.

## 4. Suggested implementation approach for a financial-services organisation

A proportionate adoption path could be:

1. **Set the intake scope.** Identify which AI-enabled systems and suppliers require an AI SBOM, considering business criticality, data sensitivity, external exposure and potential customer impact.
2. **Request a machine-readable inventory.** Accept recognised, interoperable formats and define the minimum information required for the organisation's use case.
3. **Record evidence status.** Distinguish supplier-declared claims from independently corroborated facts, unknowns and withheld information.
4. **Validate priority identifiers.** Where feasible, check component identifiers, versions and hashes against trusted artifacts or authoritative supplier records. Record what could not be verified.
5. **Connect to existing governance.** Link the inventory to technology onboarding, third-party risk, security, privacy, model risk and change-management workflows rather than creating a disconnected parallel process.
6. **Set update and escalation rules.** Define update triggers, ownership, review cadence and what happens when important information is missing, withheld or contradicted.
7. **Monitor usefulness.** Evaluate whether the information improves decisions—for example, time to identify affected systems after a vulnerability disclosure, percentage of high-risk suppliers with current inventories, or time taken to resolve material evidence gaps.

The metrics above are illustrative. Each organisation should define measures that reflect its operating model and should avoid treating document completion as proof of risk reduction.

## 5. Questions worth discussing in the FINOS project

1. What minimum AI SBOM information should be requested at onboarding for different classes of AI use case?
2. How should an organisation distinguish supplier declarations from information verified against a trusted artifact or independent source?
3. What update events should trigger a refreshed AI SBOM and a renewed governance review?
4. How should organisations handle model or dataset information that is unknown, commercially sensitive or withheld?
5. How can AI SBOM data be connected to existing technology-risk and third-party-risk processes without duplicating established controls?
6. Which evidence fields are sufficiently actionable to support incident response and vulnerability management, and which require additional context?

## 6. Limitations of this review

This is an independent desk-based review of publicly available guidance and project discussion. It does not test an actual supplier SBOM, inspect a deployed AI system, validate a model or dataset, conduct a security assessment, or provide legal or regulatory advice. The proposed intake statuses and implementation steps are analytical recommendations for discussion, not official G7 requirements or adopted FINOS policy.

## Sources

1. CISA, **CISA & G7 Partners Release Joint Guidance on the Minimum Elements of a Software Bill of Materials for Artificial Intelligence**, 12 May 2026.  
   https://content.govdelivery.com/accounts/USDHSCISA/bulletins/416bd74
2. Germany's Federal Office for Information Security (BSI), **Software Bill of Materials for AI - Minimum Elements** (G7 guidance PDF, linked in FINOS issue #424).  
   https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/KI/SBOM-for-AI_minimum-elements.pdf
3. ANSSI, **Software bill of materials (SBOM) for artificial intelligence**, 13 May 2026.  
   https://cyber.gouv.fr/en/publications/jointly-led-international-publications/software-bill-of-materials-sbom-for-artificial-intelligence/
4. CISA and international partners, **2026 Minimum Elements for a Software Bill of Materials (SBOM)**, published 29 July 2026.  
   https://content.govdelivery.com/accounts/USDHSCISA/bulletins/422a7eb

---
**Research note:** Source status checked on 12 November 2026. The G7 AI-specific document is treated as voluntary and non-exhaustive; the general SBOM update is cited separately and is not conflated with the AI-specific guidance.
