# CORA AI — SQLite-backed consent prototype

This folder contains the deterministic consent engine, synthetic demonstration,
automated tests and FastAPI browser application. The API stores consent and
audit records in SQLite so they survive process restarts.

## What this prototype demonstrates

- A participant can grant or refuse consent for a specific purpose.
- A participant can withdraw a current grant.
- Access is allowed only when a current grant matches the exact participant,
  resource and purpose.
- Missing, refused, withdrawn or mismatched consent results in **DENY**.
- Consent changes and permission checks are recorded in an SQLite audit table.

The demonstration uses fictional identifiers only: `P001` and `D001`.

## Run the engine demonstration

You need Python 3.10 or newer. From this folder:

```bash
python demo.py
python -m unittest -v
```

The standalone engine defaults to an in-memory SQLite database for isolated
demonstration runs. The API configures a persistent SQLite file.

## Run the browser application

From the `api/` folder:

```bash
python -m venv .venv
pip install -r requirements.txt
uvicorn app:app --reload
```

Open `http://127.0.0.1:8000/`. See [api/README.md](api/README.md) for
database configuration, API endpoints, tests and deployment details.

## Persistence design

- SQLite database path is configured with `CORA_DB_PATH`.
- Default local path: `api/data/cora_demo.sqlite3`.
- Consent primary key: participant ID + resource ID + purpose.
- Consent state and its audit event are written in one transaction.
- Audit events are appended in database order.
- Tests use temporary database files and verify state after reopening.

## Important limitations

This is an early synthetic demonstration, not a production application.

- Use fictional identifiers and synthetic data only.
- No authentication, authorisation, encryption, rate limiting or production monitoring.
- The audit log is not tamper-resistant and the database has no automated backup.
- The public demonstration is a shared writable sandbox.
- The prototype does not connect to real datasets or enforce access at external data-release points.
- It does not establish that consent was informed, freely given or legally valid.
- It has not undergone security, privacy, legal or community review.
- Permission decisions are deterministic; AI does not make them.

Never enter real participant, health or other sensitive personal data.

## Evidence status

SQLite persistence is implemented in the API. Automated tests cover consent rules,
audit recording and state recovery after reopening the database. GitHub Actions
is the verification environment; see the workflow associated with the current
SQLite persistence pull request for its exact results.

Persistence does not establish production security, legal compliance, backup
resilience, deployment readiness or suitability for real participant data.
