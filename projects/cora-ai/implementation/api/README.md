# CORA AI API, SQLite storage and browser prototype

FastAPI exposes the deterministic consent engine and serves the browser workspace.
Consent records and audit events are stored in SQLite. The interface does not
make permission decisions; it sends requests to the backend.

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

## SQLite database

The API creates a SQLite database automatically at:

`api/data/cora_demo.sqlite3`

Set `CORA_DB_PATH` to choose another writable file path. For example:

```bash
CORA_DB_PATH=/path/to/cora.sqlite3 uvicorn app:app --reload
```

Consent records and audit events are committed to the same SQLite database.
They survive API process restarts when the database file remains on persistent
storage. The local `data/` directory is ignored by Git; never commit database
files.

The consent table uses participant ID, resource ID and purpose as a composite
key. Audit events are appended with an increasing database ID. Consent changes
and their corresponding audit event are written in one transaction.

## Browser workflow

1. Keep the fictional defaults P001 and D001, or enter other synthetic IDs.
2. Select Research or AI model training.
3. Record Grant, Refuse or Withdraw. Withdrawal is accepted only for a current grant.
4. Select the same purpose and run Check permission.
5. Refresh Audit history to inspect the recorded events.
6. Restart the API and reload the page: the SQLite-backed consent state and audit history remain.

## API endpoints

- `GET /health` — confirms the prototype is running and reports SQLite storage.
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

The API suite uses an isolated temporary SQLite file for each test and checks
that records and audit events survive closing and reopening the database.

## Public synthetic demonstration deployment

A Render Blueprint is provided at the repository root in `render.yaml`.
It configures a Python web service with a mounted persistent disk and sets
`CORA_DB_PATH=/var/data/cora_demo.sqlite3`.

Deployment requires a Render account, connecting this GitHub repository and
creating the Blueprint service. The configured Starter web service and 1 GB
persistent disk are paid resources; review Render's current pricing before
creating the service. Do not deploy without approving the expected cost.
Once deployed, the public URL will be shown in the Render service dashboard.

## Limitations and safety

- Synthetic identifiers and data only. Never submit real participant or health data.
- SQLite persistence is suitable for this small single-instance demonstration,
  not a claim of production database architecture.
- The public demo is a shared writable sandbox. Visitors can create, change and
  inspect synthetic records in the same demo database.
- No authentication, authorisation, encryption, rate limiting, backups,
  tamper-resistant audit log or production monitoring.
- The API does not enforce access to external datasets; an adopting system must
  enforce every permission decision at every relevant data-release point.
- A persistent disk protects against ordinary service restarts, but it is not
  a backup or disaster-recovery plan.
- This is not a legal consent mechanism, privacy certification or production-ready
  access-control service.
- No security, legal, privacy or community review has been completed.

This is a public learning demonstrator, not a service for real people or real data.
