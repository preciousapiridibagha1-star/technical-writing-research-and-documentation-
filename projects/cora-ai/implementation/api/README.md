# CORA AI API and browser prototype

FastAPI exposes the deterministic consent engine and serves a small browser
workspace for the synthetic demonstration. The interface does not make
permission decisions; it sends requests to the backend.

## Run locally

Use Python 3.10 or newer. From this `api` directory:

```bash
python -m venv .venv
```

Activate the environment, then install dependencies:

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

Open **http://127.0.0.1:8000/** for the browser workspace or
**http://127.0.0.1:8000/docs** for interactive API documentation.

## Browser workflow

1. Keep the fictional defaults P001 and D001, or enter other synthetic IDs.
2. Select Research or AI model training.
3. Record Grant, Refuse or Withdraw. Withdrawal is accepted only for a current grant.
4. Select the same purpose and run Check permission.
5. Refresh Audit history to inspect the recorded events.

The browser workspace currently calls the API directly. State remains in memory
and resets when the server restarts. SQLite persistence is a separate next
milestone and is not yet implemented.

## API endpoints

- `GET /health` — confirms the prototype is running.
- `POST /consents` — records `grant`, `refuse` or `withdraw`.
- `POST /permissions/check` — returns deterministic `ALLOW` or `DENY`.
- `GET /consents/{participant_id}/{resource_id}/{purpose}` — reads current consent.
- `GET /audit` — returns audit events.

Example consent request:

```json
{"participant_id":"P001","resource_id":"D001","purpose":"research","action":"grant"}
```

## Tests

From this directory:

```bash
pytest -v
```

The API test suite includes a check that the browser workspace is served.

## Limitations and safety

- Synthetic identifiers and data only. Never submit real participant or health data.
- State is in memory and resets when the server restarts.
- No authentication, authorisation, database, encryption, rate limiting or production monitoring.
- The audit log is not tamper-resistant.
- The API does not enforce access to external datasets; an adopting system must
  enforce every permission decision at every relevant data-release point.
- This is not a legal consent mechanism, privacy certification or production-ready
  access-control service.
- No security, legal, privacy or community review has been completed.

This is a development demonstration, not a deployable service for real people.
