# Contribution Proposal 1 — Ollama README link correction

**Upstream repository:** [ollama/ollama](https://github.com/ollama/ollama)
**Issue:** [#18045 — README: update Msty link from .app to .ai](https://github.com/ollama/ollama/issues/18045)
**Target file:** `README.md`

## Problem verified

The upstream README still points the Msty entry to `https://msty.app`. Msty's official communications describe a transition to `msty.ai`, and its current product site uses the `.ai` domain. The upstream issue is open, unassigned and shows no linked branch or pull request in the checked metadata.

## Proposed change

Replace only the affected destination:

- Old: `https://msty.app`
- New: `https://msty.ai`

Keep the surrounding description and categorisation unchanged.

## Verification plan

1. Search the upstream README for `msty.app` and confirm the exact entry.
2. Confirm `msty.ai` is the official destination.
3. Check the final diff contains no unrelated changes.
4. Verify the README entry no longer points to the old domain and the destination loads.

## Contributor guidance

Ollama's contribution guide welcomes small documentation corrections, requests focused commits and asks for tests where relevant. A destination check and minimal diff are appropriate for this link change.

## Status

**Superseded as a submission target — not submitted.** Another contributor has already opened [upstream PR #18050](https://github.com/ollama/ollama/pull/18050) for this exact change. Do not submit a duplicate. Retained as an issue-research and link-verification exercise.