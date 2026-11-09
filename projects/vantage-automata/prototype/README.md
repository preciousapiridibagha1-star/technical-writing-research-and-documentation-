# Vantage Automata — Local MVP Demo

**Status:** Locally runnable proof of concept; nine unit tests passed on 9 November 2026.  
**Scope:** Deterministic proposal generation and a mock reminder action. No AI provider or external integration is connected.

## Run

Requires Python 3. Run from this directory:

```bash
python vantage_mvp.py
```

Enter an instruction beginning with `Remind me to ...`, review the proposed mock action, then approve or reject it. The demo appends the decision and outcome to `vantage_audit.jsonl`.

## Tests and verification

Run:

```bash
python -m unittest -v
```

**Verification record (9 November 2026):** The exact committed `vantage_mvp.py` and `test_vantage_mvp.py` contents were retrieved from the repository and executed in an isolated Python 3 test directory. Result: **9 tests passed, 0 failures, 0 errors**.

The nine tests cover valid and invalid input, restricted action types, approval bound to the exact proposal shown, rejection of a changed proposal, wrong proposal identifiers, duplicate-execution blocking, and safe handling of an action failure. This is a local unit-test run, not a continuous-integration result or production validation.

## Safety behaviour demonstrated

- **Narrow scope:** only a reminder-shaped instruction is accepted.
- **Exact approval:** approval is checked against a fingerprint of the proposal content shown to the user. If the proposal changes, approval is invalid.
- **Duplicate protection:** a proposal cannot be executed again in the same process after an execution attempt.
- **Fail-safe outcome:** an action error returns a safe failure and is not automatically retried.
- **Audit trail:** the decision and outcome are appended to a local JSON Lines file.

## Limits

This is a local demonstration, not a production application. The action is a mock; no real reminder is created. Duplicate protection is in-memory and does not survive a restart. The audit file is local and is not tamper-proof. There is no authentication, multi-user permission model, durable transaction store, AI model integration, monitoring or deployment. These controls would need further design and testing before any real-world use.

## Evidence boundary

The prototype demonstrates: instruction → validation → proposal → exact human approval → mock execution or safe stop → local audit record. It does not prove that an AI agent is secure or production-ready. It is a deterministic workflow demonstration rather than an integrated AI agent.
