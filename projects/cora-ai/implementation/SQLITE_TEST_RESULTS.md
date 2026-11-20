# CORA AI SQLite Persistence Test Results

**Date:** 20 November 2026  
**Pull request:** #10 — Persist CORA consent and audit records with SQLite  
**Tested commit:** `c1ed952b98126de08cf438028a669a69326d40ee`  
**Environment:** GitHub Actions, Ubuntu runner, Python 3.11.18, pytest 8.4.2

## Outcome

**All workflow steps passed.**

| Check | Result |
|---|---:|
| Consent-engine unit tests | 9 passed |
| Synthetic demonstration | Completed successfully |
| FastAPI tests | 8 passed |
| Overall workflow | Success |

The new persistence tests verify that consent state and audit events remain available after closing the database connection and opening the same SQLite file again. The API tests use a separate temporary database for each test.

## Behaviour covered

- Missing consent defaults to DENY.
- A grant allows only the exact participant, resource and purpose.
- Refused and withdrawn consent deny access.
- Withdrawal without a current grant is rejected.
- Invalid consent actions are rejected.
- Consent changes and permission checks are recorded in audit history.
- Consent and audit records survive database reopen.
- Browser workspace is served by the API.
- API state survives database reopen.

## Warning

The API test run emitted one Starlette deprecation warning: its TestClient integration currently uses `httpx`, and the installed Starlette version recommends `httpx2`. This warning did not fail the tests. GitHub Actions also emitted a Node.js 20 action-runtime deprecation notice for the existing checkout/setup actions; it did not fail the workflow.

## Important limitations

Passing automated tests proves only the tested prototype behaviours. It does not establish:

- production security or privacy;
- authentication or authorisation;
- encryption, rate limiting, backup or disaster recovery;
- tamper-resistant audit history;
- legal validity of consent;
- integration with, or enforcement at, external dataset release points;
- suitability for real participant, mental-health or other sensitive data.

The public demonstration configuration is a shared writable synthetic sandbox. It must not be used with real personal data.
