# CORA AI Prototype — Verification Results

**Verification date:** 20 November 2026  
**Environment:** GitHub Actions, Ubuntu 26.04, Python 3.11.18  
**Workflow:** [CORA AI Prototype Tests — run #2](https://github.com/preciousapiridibagha1-star/technical-writing-research-and-documentation-/actions/runs/44698932087)  
**Commit tested:** `b7d1b15dd946d84d69b0c110997776e1ec046b3f`  
**Overall workflow result:** SUCCESS

## Test summary

| Verification | Result |
|---|---:|
| Deterministic consent engine unit tests | 8 passed |
| Synthetic demonstration script | Executed successfully |
| API endpoint tests | 6 passed |
| Total automated tests | **14 passed** |

## Behaviour observed in the synthetic demonstration

Using fictional participant `P001` and resource `D001`:

1. Research consent was granted.
2. Model-training consent was refused.
3. Research permission check returned **ALLOW**.
4. Model-training permission check returned **DENY**.
5. Research consent was withdrawn.
6. A subsequent research permission check returned **DENY**.
7. The audit history showed consent changes and permission checks.

This confirms the intended purpose-specific, default-deny behaviour in this prototype test environment.

## API behaviours tested

- Health endpoint responds successfully.
- Granting research consent followed by a matching permission check returns ALLOW.
- Refused model-training consent returns DENY.
- Withdrawn research consent returns DENY.
- An invalid consent action is rejected with HTTP 422.
- The audit endpoint returns recorded events.

## Warning observed

The API test run completed with one dependency deprecation warning: Starlette's test client reports that using `httpx` through `starlette.testclient` is deprecated and recommends `httpx2`. This did not fail the tests, but should be reviewed during dependency maintenance.

The GitHub runner also emitted Node.js action-runtime deprecation notices for the workflow actions. These were not test failures.

## What this evidence does — and does not — establish

**Established:** the current in-memory engine's tested consent rules behave as expected, the demonstration script executes, and the tested HTTP API routes communicate with the engine correctly in the CI environment.

**Not established:** persistent storage, authentication, production authorisation, tamper-resistant audit records, secure handling of real personal data, legal validity of consent, enforcement across external data systems, deployment readiness, usability, or community acceptance.

No real participant or health data was used. The prototype remains a development demonstration and must not be used to control access to real sensitive datasets.
