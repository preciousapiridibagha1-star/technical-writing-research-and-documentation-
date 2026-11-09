# Technical Writing Sample Review — Evidence and Revision Record

**Review date:** 9 November 2026  
**Scope:** Existing cloud AI assistant overview, FAQ, user guide and research brief, plus the Vantage documentation samples.  
**Method:** Read the repository files, compare their claims with established documentation principles and identify which instructions can actually be verified. This is a self-review, not an independent certification.

## Overall finding

The original four cloud-AI samples were readable and well organised, but they described a broad product category as though it were one identifiable product. They included broad claims about security, privacy, integrations, hardware and local deployment without a named product or cited evidence. The user guide was a general usage outline rather than a task-based guide.

The Vantage samples are more specific, but they describe a proposed experience. They must remain labelled as illustrative unless the interface and behaviour are tested.

## Sample-by-sample review

| Sample | What worked | Main issue found | Improvement required |
|---|---|---|---|
| Software overview | Clear audience and feature headings | No named product, scope boundary or source trail | Label as a category overview; distinguish common capabilities from product-specific features |
| FAQ | Addresses relevant beginner questions | General answers about encryption, integrations and enterprise security can imply universal guarantees | Attribute security claims to a named provider and link to its current documentation; otherwise explain that controls vary |
| User guide | Logical basic sequence | Reader cannot complete a specific real task from the instructions | Choose a named product and verify every step, or label it as a general illustrative workflow |
| Research brief | Useful comparison topic | Treats proprietary cloud and open-weight/local models as two uniform categories; overstates privacy and customisation | Compare named models and deployments; explain that open weights, open-source software and local hosting are different concepts |
| Vantage user guide | Approval/rejection journey is easy to follow | It describes a proposed UI, not a verified live interface | Keep illustrative label; align steps with the local prototype and state clearly that its action is mocked |

## Before → after examples

### 1. Security claims

**Before:** “Local models provide complete privacy and absolute data sovereignty.”

**After:** “Running a model locally can reduce the need to send prompts to an external model provider, but privacy and security still depend on the application, device, network, logs, backups and access controls. Local hosting is not, by itself, a security guarantee.”

### 2. Integrations

**Before:** “Most modern platforms offer APIs, browser extensions or direct integrations.”

**After:** “Integration options vary by product and plan. Check the provider's current documentation for supported APIs, connectors, access limits and required permissions before describing an integration as available.”

### 3. User instructions

**Before:** “Access the platform, formulate your instruction, review and refine.”

**After:** “Before using a named product, confirm the supported sign-in method and the task you intend to complete. Enter only information you are authorised to share. Review the output against the original source before using it. Do not treat generated text as verified fact.”

The revised version is safer and more useful, but a full product-specific guide still requires a selected product and a verified walkthrough.

## External standard applied

Google's Developer Documentation Style Guide recommends writing for the reader, using clear and consistent language and structuring information so readers can find and complete tasks. The review applies those principles as a practical checklist, not as a claim of formal compliance.

Source: [Google Developer Documentation Style Guide](https://developers.google.com/style/).

## Reusable quality checklist

- Is the intended reader identified?
- Is the product or concept clearly named?
- Are facts separated from assumptions and examples?
- Are security, privacy and capability claims linked to authoritative sources?
- Can a reader complete the stated task using the instructions?
- Are prerequisites, expected results and failure paths included where relevant?
- Are version-sensitive details dated?
- Are proposed features clearly labelled as proposed?
- Are links and file paths valid?
- Does the document avoid claiming tests or implementation that did not happen?

## What remains incomplete

- The FAQ source file with the expected root filename was not found under that exact path during this review; locate the actual FAQ file before editing it.
- The four original cloud-AI samples still need a product decision: select a named product for a verified guide, or consistently label all four as category-level illustrative samples.
- No live vendor product walkthrough was performed in this review.
- No accessibility or usability testing with external readers was performed.

## Evidence boundary

This record demonstrates a structured self-review and concrete corrections to unsupported generalisations. It does not establish professional certification, independent peer review or product testing.
