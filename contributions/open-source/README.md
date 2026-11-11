# Open-Source Contributions

This directory records external contributions with links to the upstream issue, pull request and verified status. An investigation or prepared patch is not a submitted contribution; a submitted pull request is not merged until maintainers merge it.

## Contribution record standard

For every contribution, record the upstream project, issue addressed, problem, exact change, verification performed, pull request or commit, maintainer feedback and final status. Never claim tests passed unless they were run and the output is recorded.

## 1. uniunihan-db — Correct Mandarin pinyin in README

- **Upstream repository:** [garfieldnate/uniunihan-db](https://github.com/garfieldnate/uniunihan-db)
- **Issue:** [#9 — typo in README](https://github.com/garfieldnate/uniunihan-db/issues/9)
- **Pull request:** [#10 — Correct Mandarin pinyin for 電話 in README](https://github.com/garfieldnate/uniunihan-db/pull/10)
- **Contribution type:** Focused documentation correction.
- **Status:** Submitted; open and awaiting maintainer review. Not merged.
- **Change:** Corrected the Mandarin pinyin for 電話 from `diǎn huà` to `diànhuà` in the README example.
- **Work completed:** Reviewed the reported text, checked the language-specific correction, created a fork and working branch, made the change, committed it and opened a pull request against the upstream repository.
- **Skills evidenced:** Careful reading, factual checking, narrow issue scope, documentation correction and the basic fork/branch/commit/pull-request workflow.

**Evidence boundary:** This is a small documentation correction. It demonstrates an initial upstream contribution workflow, not software engineering expertise or a substantial code contribution. It has not been accepted or merged.

## 2. Second contribution — in progress

A second upstream issue has not yet been selected or submitted. Selection criteria:

1. The issue is open and its scope is clear.
2. No existing pull request already addresses the same change.
3. The repository's contribution guide and licence/attribution requirements are understood.
4. The work is realistic and can be verified with available skills and access.
5. The contribution adds a distinct skill or evidence dimension; it should not be another cosmetic typo.
6. The issue has a credible connection to AI governance, public-interest technology, humanitarian/nonprofit systems or technical documentation.

No candidate will be described as a contribution until a real change is submitted.

## Contribution workflow

1. Read the upstream README, contribution guide and code of conduct.
2. Confirm the issue is open; check assignees, related branches, discussions and duplicate PRs.
3. Read the relevant source documentation and verify the underlying facts.
4. Prepare a focused change matching project conventions.
5. Run applicable checks and review the complete diff.
6. Submit the pull request and respond to maintainer feedback.
7. Record the verified outcome and lessons.

## 2. Contribution selection note

A candidate in `pydata/pydata-sphinx-theme#1629` was reviewed but not selected: an earlier PR (#2476) was closed after maintainers found its documentation change insufficiently contextualised, and a new contributor had already asked maintainers to clarify the remaining scope. Repeating that work without a distinct, confirmed scope would risk duplication.

## Earlier proposals and investigations

- [Ollama — Msty URL correction (#18045)](proposal-01-ollama-msty-link.md) — an existing upstream PR [#18050](https://github.com/ollama/ollama/pull/18050) already proposed this change.
- [Ollama — GPU fallback troubleshooting (#14260)](proposal-02-ollama-gpu-troubleshooting.md) — an existing upstream PR [#14461](https://github.com/ollama/ollama/pull/14461) already proposed substantially overlapping documentation.
- [Shipley issue #24 investigation](shipley-issue-24-investigation.md) — a focused change was prepared on the personal fork, but upstream submission was withheld because two open PRs already proposed the same correction.
- [Upstream candidate audit](upstream-candidate-audit-2026-11-09.md) — records earlier candidate checks and duplicate-PR findings.

These records are retained as research and process evidence, not represented as available upstream contributions.
