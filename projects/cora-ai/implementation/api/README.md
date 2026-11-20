# CORA AI API — Synthetic Prototype

This FastAPI application exposes the deterministic consent engine through HTTP
endpoints. It is an interface layer only: it does not make consent decisions
itself and does not use an AI model.

## Setup

Use Python 3.10 or newer. From this `api` directory:

```bash
python -m venv .venv
```

Activate the environment, then install dependencies:

```bash
pip install -r requirements.txt
```

Start the local API:

```bash
uvicorn app:app --reload
```

Open the interactive API documentation at `/docs` on the local server.

## Endpoints

- `GET /health` — confirms the local prototype is running.
- `POST /consents` — records `grant`, `refuse` or `withdraw`.
- `POST /permissions/check` — returns deterministic `ALLOW` or `DENY`.
- `GET /consents/{participant_id}/{resource_id}/{purpose}` — reads the current consent state.
- `GET /audit` — returns the in-memory audit events.

Example consent request:

```json
{
  "participant_id": "P001",
  "resource_id": "D001",
  "purpose": "research",
  "action": "grant"
}
```

Example permission request:

```json
{
  "participant_id": "P001",
  "resource_id": "D001",
  "purpose": "research"
}
```

## Run API tests

From this directory:

```bash
pytest -v
```

## Limitations and safety

- Synthetic identifiers and data only. Never submit real participant or health data.
- State is in memory and resets when the server restarts.
- No authentication, authorisation, database, encryption, rate limiting or production monitoring.
- The audit log is not tamper-resistant.
- The API does not enforce access to external datasets; an adopting system would
  need to enforce every permission decision at every relevant data-release point.
- This is not a legal consent mechanism, privacy certification or production-ready
  access-control service.
- No security, legal, privacy or community review has been completed.

The API is a development demonstration, not a deployable service for real people.
