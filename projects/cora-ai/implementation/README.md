# CORA AI — Deterministic Consent Prototype

This folder contains the first runnable implementation milestone: a small Python
engine that records purpose-specific consent, checks permission, and records an
audit history.

## What this prototype demonstrates

- A participant can grant or refuse consent for a specific purpose.
- A participant can withdraw a current grant.
- Access is allowed only when a current grant matches the exact participant,
  resource and purpose.
- Missing, refused, withdrawn or mismatched consent results in **DENY**.
- Consent changes and permission checks are recorded in an in-memory audit log.

The demonstration uses fictional identifiers only: `P001` and `D001`.

## Run it

You need Python 3.10 or newer. No third-party packages are required.

From this folder, run:

```bash
python demo.py
```

Run the automated checks:

```bash
python -m unittest -v
```

## Important limitations

This is an early learning prototype, not a production application.

- Data is held in memory and disappears when the program exits.
- There is no database, user login, authentication or API yet.
- The audit log is not tamper-resistant.
- The prototype does not connect to real datasets or external systems.
- It does not establish that consent was informed, freely given or legally valid.
- It does not prevent copies or data uses outside a system that enforces its decisions.
- It has not undergone security, privacy, legal or community review.
- It does not use AI to make permission decisions. Permission decisions are deterministic.

Never enter real participant, health or other sensitive personal data.

## Next development steps

1. Review the rules and test cases.
2. Add a persistent local database and API boundary.
3. Add a minimal user interface for the synthetic demonstration.
4. Add a bounded AI assistant that explains system information but cannot grant
   consent, change permission or override a denial.
5. Conduct technical, privacy, security and community review before any real use.

## Evidence status

**Implemented:** in-memory consent state, exact-purpose permission checks,
default-deny behaviour, audit events, demonstration script and automated tests.

**Verified in GitHub Actions (20 November 2026):** all 8 consent-engine tests
passed, the synthetic demonstration executed successfully, and all 6 API tests
passed. See [TEST_RESULTS.md](TEST_RESULTS.md) for the run record.

This verification does not establish persistence, production security,
deployment readiness or suitability for real participant data.

## HTTP API

A FastAPI interface has also been added under `api/`. It exposes consent
recording, permission checks, current consent lookup, audit history and a health
endpoint. See [api/README.md](api/README.md) for setup and request examples.

**API implementation status:** source code and API test cases are committed.
They have not yet been executed in a local Python environment, so API test
results are not claimed.
