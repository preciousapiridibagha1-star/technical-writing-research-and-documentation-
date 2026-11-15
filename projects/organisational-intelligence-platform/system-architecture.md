# Proposed System Architecture

## 1. Architecture objective

Create a maintainable platform with one shared foundation and configurable sector experiences. The architecture should be understandable and proportionate to the first demonstration rather than over-engineered for hypothetical scale.

## 2. Main components

### User interface
- Organisation dashboard.
- Programme and activity pages.
- Data upload and review screens.
- Indicator and progress views.
- AI question-and-answer panel.
- Report preview and review.

### Application layer
- Organisation and user management.
- Programme and activity management.
- Import workflow.
- Indicator and progress calculations.
- Search and retrieval of organisational records.
- Report generation workflow.

### Data layer
- Organisation records.
- Programmes and activities.
- Indicators, targets and actual values.
- Uploaded file metadata.
- Extracted and reviewed records.
- Evidence references.
- User roles and audit events.

### AI services
- Document extraction where supported.
- Classification and field suggestions.
- Summarisation.
- Retrieval-grounded question answering.
- Draft report generation.
- Explanation of data-quality warnings.

### Sector configuration
- Sector-specific labels and forms.
- Indicator templates.
- Activity categories.
- Report templates.
- Optional fields and validation rules.

## 3. Conceptual data relationships

An organisation can have multiple programmes. Each programme can contain activities and indicators. Activities can have progress updates and evidence. Indicators have targets, actual values, units and reporting periods. Uploaded source files can support multiple extracted records, but the source relationship must remain traceable.

A simplified relationship:

Organisation → Programmes → Activities  
Programme → Indicators → Targets and actual results  
Activity / Indicator → Evidence records  
Uploaded source → Imported records → Reviewed programme data  
Reviewed programme data → Analytics and report drafts

## 4. Import and review flow

1. User selects a programme and uploads a file.
2. The system checks file type and basic validity.
3. The system previews rows or extracted content.
4. Field mapping is suggested where possible.
5. The user reviews the mapping and warnings.
6. The user confirms or rejects the import.
7. Accepted records are stored with source and import metadata.
8. The system updates relevant programme views.

The system should not silently overwrite existing information or automatically merge uncertain matches.

## 5. AI and deterministic processing

Use AI for:
- Reading and classifying supported documents.
- Suggesting mappings between source columns and platform fields.
- Summarising programme narratives.
- Answering questions from retrieved records.
- Drafting reports for review.

Use deterministic application logic for:
- Totals and counts.
- Target-versus-actual calculations.
- Percentages and date comparisons.
- Duplicate candidate rules.
- Validation rules.
- Indicator aggregation.

When data is incomplete or contradictory, show the issue and ask for review instead of inventing a resolution.

## 6. Evidence and traceability

Important generated statements should link to:
- The source file or record.
- The relevant programme and reporting period.
- The calculation or aggregation rule, where applicable.
- Any caveat or missing information.

A report should make clear which statements are verified from records and which are AI-generated interpretation.

## 7. Security and privacy design

- Separate organisation data logically and enforce access checks server-side.
- Apply role-based permissions.
- Encrypt data in transit and use appropriate protection at rest.
- Keep secrets out of source control.
- Minimise collection of sensitive personal data.
- Use synthetic data for development and demonstration.
- Apply additional review before processing health or other sensitive records.
- Define retention and deletion procedures before a real-world pilot.

This document is a proposed architecture, not evidence of a completed security review.

## 8. Demonstration architecture boundary

The first demonstration may use a simplified application and a limited data model. It should prove the workflow, not attempt to implement every production requirement.

External integrations, complex multi-tenant administration, advanced analytics, full document-processing coverage and production-grade deployment can remain future work, subject to validation and resources.
