# User Experience and Workflow Design

## 1. Design principles

The interface should feel clear and approachable to staff who are not software specialists.

- Use plain language.
- Keep navigation predictable.
- Prefer short forms and sensible defaults.
- Show users what will happen before importing or generating information.
- Use tables for records and cards for summaries.
- Keep warnings visible and explain how to resolve them.
- Avoid unnecessary configuration screens.

## 2. Main navigation

A proposed left-hand navigation:

1. Overview
2. Programmes
3. Activities
4. Data Hub
5. Monitoring
6. AI Intelligence
7. Reports
8. Organisation Settings

The demonstration may show only the pages required for its three workflows.

## 3. Overview dashboard

The overview should show:
- Active programmes.
- Activities completed, in progress and overdue.
- Progress against selected targets.
- Recent programme updates.
- Data issues requiring attention.
- Quick actions such as Create Programme, Add Activity and Upload Data.

Avoid displaying a large number of decorative metrics that do not help users make decisions.

## 4. Forms and modal windows

Use modal pop-ups for short actions. Use full pages for complex tasks such as reviewing a large import or editing a report.

### Create Programme modal
Fields:
- Programme name.
- Sector configuration.
- Description.
- Objectives.
- Start date.
- End date.
- Programme owner or team.

Actions: Save Programme / Cancel.

### Add Activity modal
Fields:
- Activity name.
- Programme.
- Description.
- Responsible person or team.
- Planned start and end dates.
- Status.
- Expected output.

Actions: Save Activity / Cancel.

### Create Indicator modal
Fields:
- Indicator name.
- Description.
- Measurement unit.
- Target value.
- Reporting period or frequency.
- Data source.

Actions: Save Indicator / Cancel.

### Upload Data flow
1. Select file.
2. Select programme and data category.
3. Preview the data.
4. Review suggested field mapping.
5. Review validation warnings.
6. Confirm import.

Do not use a single confirmation button that hides unresolved warnings.

### Record Progress modal
Fields:
- Programme or activity.
- Indicator.
- Reporting period.
- Actual value.
- Evidence or source.
- Notes.

Actions: Save Update / Cancel.

### Generate Report flow
Fields:
- Programme.
- Reporting period.
- Report type.
- Sections to include.

Show a preview before the user exports or copies the report.

## 5. AI Intelligence experience

Provide a clear question box with example questions.

Examples:
- Which activities are overdue?
- How many people were reached in this reporting period?
- Which indicators are missing updates?
- Summarise progress against the programme targets.
- What evidence supports this result?
- Draft a quarterly programme summary.

The answer should show its reporting period, supporting records and limitations. If the system cannot answer from the available information, it should say so.

## 6. Three primary user journeys

### Journey A: Upload and review programme information
User opens Data Hub → selects programme → uploads spreadsheet → previews rows → reviews field mapping and warnings → confirms import → sees imported records.

### Journey B: Monitor a programme
User opens Programmes → selects programme → reviews activities and indicators → records progress → sees updated target-versus-actual status → identifies overdue activities or missing updates.

### Journey C: Ask a question and prepare a report
User opens AI Intelligence → asks a question → receives an answer supported by records → opens Reports → selects programme and period → reviews draft report → edits and exports.

## 7. Sector experience

The same screens should adapt to the selected sector.

For example:
- Public health may use community outreach and intervention indicators.
- A health organisation may use facility support, training and service-delivery indicators.
- Education may use schools supported, teachers trained and learners reached.

The interface should not expose irrelevant sector fields to every organisation.
