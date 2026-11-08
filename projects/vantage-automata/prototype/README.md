# Vantage Automata — Local Approval Demo

**Evidence type:** Working local demonstration using Python's standard library.  
**Scope:** Mock action only. No AI provider, external account, network service or real-world action is connected.

This small demo makes one principle tangible: an instruction can be turned into a proposed action, but the action handler is called only after an explicit approval. Rejection stops the workflow. Each decision is written to a local JSON Lines audit file.

## Run it

Requires Python 3.9 or later.

```bash
python prototype.py
```

Choose approve or reject when prompted. The demonstration uses a fixed, harmless mock task and records the result in `audit.jsonl` in the current directory.

## What it demonstrates

- A proposal is shown before an action.
- Approval is explicit.
- Rejection does not call the mock action.
- The action is deliberately harmless and local.
- A record is written for later inspection.

## What it does not demonstrate

It does not connect to an AI model, authenticate users, provide production security, store data in a database, prevent every possible duplicate request, or integrate with email, payments or customer systems. The proposal is pre-written mock data. This is a learning prototype, not a deployable product.

## Next validation

Run the script, inspect the audit record, then add automated tests for approval, rejection and invalid decisions before expanding the scope.
