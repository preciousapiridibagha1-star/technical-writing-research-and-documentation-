# Technical Writing Sample Review — Evidence and Revision Record

**Review date:** 9 November 2026  
**Scope:** Cloud AI assistant overview, FAQ, usage guide and research brief, plus Vantage documentation.  
**Method:** Repository-file review against reader-focused documentation practice and external style guidance. This is a self-review, not independent certification.

## Overall finding

The original samples had readable structures but described a broad category as if it were one identifiable product. Security, privacy, integration and hardware claims were too general; the user guide was not tied to a tested interface; and the research brief treated open weights and local deployment as if they guaranteed privacy and cost advantages.

The revised set deliberately remains category-level rather than pretending to document a vendor product that has not been selected or tested. Each file now labels its scope, avoids universal claims and explains what evidence would be required for product-specific documentation.

## Sample-by-sample review

| Sample | Existing strength | Challenge found | Improvement made |
|---|---|---|---|
| Software overview | Clear audience and capability structure | Broad category presented like one product | Rewritten as a category overview; uses task-based examples and explicit scope limits |
| FAQ | Covers beginner questions | Blanket claims about security, integrations and compatibility | Rewritten as questions to ask; distinguishes provider-specific facts from general cautions |
| Usage guide | Logical basic workflow | Not enough to guide a reader through one real product interface | Rewritten as a task-based generic workflow with prerequisites, expected results, troubleshooting and a strong non-vendor-specific label |
| Research brief | Relevant cloud/local deployment topic | Confuses open-source, open-weight, local and offline; overclaims privacy and cost | Rebuilt with definitions, decision criteria, qualified findings and primary technical/standards sources |
| Vantage guide | Approval/rejection flow is clear | The interface is a proposed experience, not a fully tested UI | Kept illustrative and aligned to the local prototype; mock action and known limitations remain explicit |

## Before → after examples

### Security and privacy
**Before:** “Local models provide complete privacy and absolute data sovereignty.”

**After:** “Running a model locally can reduce the need to send prompts to an external inference provider, but security still depends on the application, device, network, logs, backups and access controls. Local hosting is not, by itself, a privacy guarantee.”

### Integrations
**Before:** “Most modern platforms offer APIs, browser extensions or direct integrations.”

**After:** “Integration options vary by product, region and plan. Check current provider documentation for supported connectors, API access, limits and permissions before describing an integration as available.”

### User instructions
**Before:** “Access the platform, formulate your instruction, review and refine.”

**After:** The revised usage guide establishes prerequisites, a bounded instruction, source checking, export review and troubleshooting, while warning readers to follow the chosen provider's own interface documentation.

## Research and writing standards applied

- [Google Developer Documentation Style Guide](https://developers.google.com/style/) — clarity, consistency, reader context and task-oriented structure.
- [Open Source Initiative — Open Source AI Definition](https://opensource.org/ai/open-source-ai-definition) — precise distinction between open-source AI systems and the availability of model weights.
- [Ollama documentation](https://github.com/ollama/ollama/blob/main/docs/faq.mdx) and [Meta Llama model access/licensing](https://dev.meta.ai/llama/docs/getting-the-models/meta) — examples of runtime and model-specific requirements/terms; not universal rules.

## Reusable quality checklist

- Is the intended reader identified?
- Is the document scope clear: named product, product category or illustrative workflow?
- Are facts separated from assumptions and examples?
- Are security, privacy, licence and capability claims linked to authoritative sources?
- Can a reader complete the stated task using the instructions?
- Are prerequisites, expected results and failure paths included where relevant?
- Are version-sensitive details dated?
- Are proposed features clearly labelled as proposed?
- Are links and file paths valid?
- Does the document avoid claiming tests or implementation that did not happen?

## What remains incomplete

- The samples are not product-specific because no named vendor has been selected for a verified walkthrough.
- No live vendor product walkthrough was performed.
- No accessibility or usability testing with external readers was performed.
- The Vantage command-line demo has been unit-tested, but that does not constitute user-interface usability testing.

## Evidence boundary

This record demonstrates a documented self-review, concrete revisions and use of external standards. It does not establish professional certification, independent peer review, live product testing or formal accessibility conformance.
