# Vantage Automata — Local MVP Demo

**Status:** Working local proof of concept; five unit tests passed locally.  
**Scope:** Deterministic proposal generation and a mock reminder action. No AI provider or external integration is connected.

## Run

Requires Python 3. Run from this directory:

```bash
python vantage_mvp.py
```

Enter an instruction beginning with `Remind me to ...`, review the proposed mock action, then approve or reject it. The demo appends the decision and outcome to `vantage_audit.jsonl`.

## Tests

```bash
python -m unittest -v
```

The test suite covers a valid proposal, empty input, an out-of-scope request, an overlong instruction and rejection of an unauthorised action type.

## Safety boundary

This is a local demonstration, not a production application. It does not send messages, create real reminders, connect to accounts, call an AI model or change external data. Proposal generation is deterministic so that the approval flow can be tested without model variability.

## Evidence

The prototype demonstrates the first technical slice: instruction → validated proposal → human decision → mock action or stop → audit record. It does not yet demonstrate model integration, authentication, multi-user permissions, persistence hardening or deployment.
