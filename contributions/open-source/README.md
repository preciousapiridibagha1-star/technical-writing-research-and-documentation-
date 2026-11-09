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

## Previously prepared proposals — now superseded as submission targets

1. [Ollama — Msty URL correction (#18045)](proposal-01-ollama-msty-link.md) — an existing upstream PR [#18050](https://github.com/ollama/ollama/pull/18050) already proposes this change.
2. [Ollama — GPU fallback troubleshooting (#14260)](proposal-02-ollama-gpu-troubleshooting.md) — an existing upstream PR [#14461](https://github.com/ollama/ollama/pull/14461) already proposes substantially overlapping documentation.

The [9 November upstream candidate audit](upstream-candidate-audit-2026-11-09.md) records these checks and other alternatives. The original drafts are retained as research records, not represented as available issues to submit against.

## Current status

**Area 7 remains in progress. No accepted or merged external contribution is claimed.** A focused change for [Shipley Integrations issue #24](shipley-issue-24-investigation.md) was prepared and committed to the personal fork, but upstream submission was withheld because two open PRs already proposed the same correction. The record documents the investigation, AI assistance, human review, duplicate check and limits of verification.