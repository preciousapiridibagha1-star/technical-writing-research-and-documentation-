# Backend Proof of Concept

**Status:** Early local API demonstration. Synthetic data only. Not production-ready.

This small FastAPI service demonstrates a limited backend foundation for the organisational intelligence platform. It is intentionally separate from the complete product vision and does not claim to be a complete MVP.

## What it demonstrates

- Three sample sector configurations: Public Health, Health Organisation Programmes and Education.
- Programme and activity records.
- Indicator targets and actual progress.
- Deterministic progress calculations.
- Basic data-quality flags for missing updates.
- A simple report draft generated from the sample records.

The data is held in memory and resets when the server restarts. There is no database, authentication, file upload, external integration or live AI model in this proof of concept.

## Run locally

From this directory:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

On Windows, activate the environment with:

```bash
.venv\Scripts\activate
```

Open the interactive API documentation at `http://127.0.0.1:8000/docs`.

## Example endpoints

- `GET /health`
- `GET /api/v1/sectors`
- `GET /api/v1/programmes?sector=public-health`
- `GET /api/v1/dashboard/public-health`
- `GET /api/v1/data-quality/public-health`
- `GET /api/v1/reports/draft/public-health`

## Important limitations

- All organisations and programme records are fictional.
- The service does not accept uploaded files yet.
- The report is a deterministic template, not an AI-generated report.
- The question endpoint uses simple rules, not a language model.
- No authentication or organisation-level access control is implemented.
- Do not use real beneficiary, patient, student or other sensitive information.
- Do not deploy this service for real organisational use.

## Next engineering steps

1. Review the data model with prospective users.
2. Add automated tests and persistent storage.
3. Implement secure authentication and organisation-level permissions.
4. Add a reviewed CSV import workflow.
5. Build the frontend against the API.
6. Add retrieval-grounded AI only after data access, privacy and evidence controls are designed.
