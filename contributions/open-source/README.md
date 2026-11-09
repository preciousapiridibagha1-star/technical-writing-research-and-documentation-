# Open-Source Contributions

This section records evidence for external open-source contribution work. It distinguishes issue investigation and patch preparation from a change that has actually been submitted.

## Contribution record standard

For every contribution, record the upstream project, issue addressed, problem, exact change, verification performed, pull request or commit, maintainer feedback, and final status.

An issue investigation or draft patch is not an upstream contribution. A pull request is not merged until the upstream repository confirms it. Never claim tests passed unless they were run and the output is recorded.

## Contribution workflow

1. Read the upstream README, contribution guide and code of conduct.
2. Confirm the issue is open and check assignees, related branches and duplicate PRs.
3. Read the relevant implementation or documentation source.
4. Prepare a focused change that matches project conventions.
5. Run project-specified checks and verify factual claims and links.
6. Review the complete diff.
7. Obtain approval before creating a public upstream branch or pull request.
8. Submit and respond to maintainers' review.
9. Record the verified outcome and lessons.

## Prepared contribution proposals

1. [Ollama — update the Msty URL in README (#18045)](proposal-01-ollama-msty-link.md) — one-line external-link correction, checked against Msty's official domain.
2. [Ollama — add GPU fallback troubleshooting guidance (#14260)](proposal-02-ollama-gpu-troubleshooting.md) — practical `ollama ps` diagnostic workflow, context-length guidance and carefully qualified model-artifact-size information.

Both issues were open and unassigned, with no linked branch or pull request in the issue metadata at the time checked. Recheck immediately before submission.

## Current status

**Two candidate changes have been investigated and drafted. Neither has been submitted upstream.** This index does not claim an external contribution or merged pull request.