# Product Requirements

## 1. Purpose

Define the intended product behaviour for a modular organisational intelligence platform. This document describes the broader product direction; it is not a statement that all requirements have been implemented.

## 2. Intended users

Depending on the organisation, users may include:

- Programme managers.
- Monitoring, Evaluation and Learning (MEL/M&E) officers.
- Health programme coordinators.
- Education programme coordinators.
- Project officers.
- Data and research officers.
- Organisation administrators.
- Senior managers reviewing organisational performance.

The platform should accommodate different levels of digital confidence.

## 3. Core user needs

Users need to:

1. Bring relevant programme information into an organised workspace.
2. Create programmes, activities, targets and indicators.
3. Record and review implementation progress.
4. Identify missing, inconsistent or duplicated information.
5. Understand what the available records say.
6. Prepare reports from traceable evidence.
7. Configure the workspace for their sector and organisation.

## 4. Functional requirements

### 4.1 Organisation workspace
- Create an organisation profile.
- Configure sector and programme categories.
- Invite users and assign roles.
- Separate one organisation's information from another's.
- Configure basic reporting preferences.

### 4.2 Data Hub
- Accept CSV and Excel files in the demonstration.
- Support document uploads such as PDF and Word in the broader design.
- Let users choose the programme and data category for an upload.
- Preview imported records before confirmation.
- Map source columns to recognised fields.
- Flag missing or unrecognised fields.
- Retain source-file and import information for traceability.
- Allow users to correct or reject questionable imports.

### 4.3 Programme and activity management
- Create a programme with name, sector, description, objectives and dates.
- Create projects or workstreams under a programme where needed.
- Add activities with owners, dates, status and expected outputs.
- Record progress updates.
- Link activities to indicators and supporting evidence.

### 4.4 Monitoring and evaluation
- Define indicators, units and reporting frequency.
- Set targets for a defined period.
- Record actual values and the source of each value.
- Calculate progress using explicit formulas.
- Distinguish activities, outputs, outcomes and impact.
- Flag overdue activities and missing updates.
- Display the period and denominator used in calculations.

### 4.5 AI intelligence
- Extract relevant information from supported uploaded files.
- Summarise selected programme records.
- Answer natural-language questions using available records.
- Identify possible inconsistencies and missing information.
- Explain why a programme or activity has been flagged.
- Provide references to source records for material claims.
- State when information is unavailable or insufficient.

### 4.6 Analytics
- Show active programmes and activity status.
- Show target-versus-actual progress.
- Show trends where sufficient time-series data exists.
- Display data completeness and unresolved issues.
- Filter by programme, sector and reporting period.

### 4.7 Reporting
- Generate draft programme summaries.
- Prepare periodic progress reports.
- Include indicator tables and evidence references.
- Allow users to review and edit before export.
- Identify unsupported statements and missing evidence.
- Support export to a common document format in a later implementation phase.

### 4.8 Security and privacy
- Use authentication and role-based access.
- Restrict access to organisation and programme records.
- Minimise personal data collection.
- Apply stronger protections to sensitive health and beneficiary information.
- Record important changes and access events where appropriate.
- Define retention, deletion and incident-handling procedures before any real-data pilot.

## 5. Non-functional requirements

- Clear, responsive and accessible interface.
- Understandable forms and validation messages.
- Reliable import and error handling.
- Traceability for important data and generated findings.
- Maintainable modular code.
- Secure handling of credentials and uploaded files.
- Performance appropriate to the expected pilot scale.
- Documentation of limitations and known risks.

## 6. Explicit exclusions from the initial concept

The platform is not intended to become:
- A hospital electronic medical record system.
- A clinical diagnosis or treatment recommendation tool.
- A payment processor or accounting ledger.
- A replacement for every CRM, survey or field-data application.
- A full enterprise resource planning system.
- An autonomous decision-maker about beneficiaries or services.

Fundraising and donor management are not the product's central use case.

## 7. AI reliability rules

- AI-generated text is a draft for human review.
- Financial and indicator calculations use explicit code and validated data.
- The system must not infer missing values as if they were facts.
- Conflicting records must be surfaced, not silently reconciled.
- Answers should identify source records and reporting periods.
- Sensitive personal information should not be sent to an AI provider unless the use is justified, authorised and appropriately protected.

## 8. Acceptance criteria for the demonstration

The demonstration should allow a reviewer to:
- Select one of the three initial sector scenarios.
- Upload or load clearly labelled synthetic data.
- Review imported records.
- Create or inspect a programme, activities and indicators.
- See target-versus-actual progress.
- Ask a question answered from the loaded records.
- See missing information or a data-quality warning.
- Generate and review a draft report.
- Understand that this is a limited demonstration, not a production deployment.
