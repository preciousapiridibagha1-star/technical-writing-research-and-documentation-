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

## 2. FINOS AI Governance Framework — Review of G7 AI SBOM guidance

- **Upstream repository:** [finos/ai-governance-framework](https://github.com/finos/ai-governance-framework)
- **Issue:** [#424 — Review and discuss the G7 guidance on SBOM for AI](https://github.com/finos/ai-governance-framework/issues/424)
- **Contribution type:** Independent source-based research and governance analysis, submitted as an issue discussion comment.
- **Status:** Discussion contribution submitted on 12 November 2026; awaiting maintainer/community response. No upstream pull request or code change is claimed.
- **Upstream contribution:** [Issue comment with findings and practical discussion questions](https://github.com/finos/ai-governance-framework/issues/424#issuecomment-6818628176).
- **Portfolio evidence:** [Full review note](finos-g7-ai-sbom-review-2026.md); portfolio PR #3 is open and unmerged.
- **Work completed:** Reviewed the G7 AI SBOM minimum-elements guidance and public CISA/ANSSI summaries; distinguished a transparency inventory from assurance; analysed evidence provenance, unknown versus withheld information, hashes and signatures, lifecycle updates and integration with existing governance controls; documented limitations and discussion questions.
- **Skills evidenced:** Public-source research, critical reading, AI supply-chain governance analysis, evidence qualification, technical writing and communicating practical recommendations.

**Evidence boundary:** This is independent desk research, not a supplier SBOM assessment, technical validation, security audit, legal opinion or adopted FINOS policy. The contribution is an issue discussion response; it is not a merged pull request and does not imply endorsement by FINOS or the maintainers.

## Contribution workflow

1. Read the upstream README, contribution guide and code of conduct.
2. Confirm the issue is open; check assignees, related branches, discussions and duplicate PRs.
3. Read the relevant source documentation and verify the underlying facts.
4. Prepare a focused change matching project conventions.
5. Run applicable checks and review the complete diff.
6. Submit the pull request or issue discussion contribution and respond to maintainer feedback.
7. Record the verified outcome and lessons.

## Earlier contribution selection notes

A candidate in `pydata/pydata-sphinx-theme#1629` was reviewed but not selected: an earlier PR (#2476) was closed after maintainers found its documentation change insufficiently contextualised, and a new contributor had already asked maintainers to clarify the remaining scope. Repeating that work without a distinct, confirmed scope would risk duplication.

### Additional candidate checks — 12 November 2026

- **pydata/pydata-sphinx-theme#1629:** not selected. The issue remains open, but maintainers' discussion shows unresolved scope around version-switcher and warning-banner behaviour. PR #2476 was previously closed after review feedback that its documentation was insufficiently contextualised, and a new contributor has asked maintainers to clarify the remaining work. A second attempt without a distinct, confirmed scope would risk duplication.
- **strands-agents/harness-sdk#2572:** not selected. A maintainer offered the missing Galileo integrations-catalog entry to another contributor, who had already asked to take the work.
- **strands-agents/harness-sdk#2584:** not selected. Although open and labelled ready for contribution, the requested cross-provider LiteLLM hook examples require implementation and technical validation beyond the current verified skill scope.

These checks are evidence of issue screening, not submitted contributions.

## Earlier proposals and investigations

- [Ollama — Msty URL correction (#18045)](proposal-01-ollama-msty-link.md) — an existing upstream PR [#18050](https://github.com/ollama/ollama/pull/18050) already proposed this change.
- [Ollama — GPU fallback troubleshooting (#14260)](proposal-02-ollama-gpu-troubleshooting.md) — an existing upstream PR [#14461](https://github.com/ollama/ollama/pull/14461) already proposed substantially overlapping documentation.
- [Shipley issue #24 investigation](shipley-issue-24-investigation.md) — a focused change was prepared on the personal fork, but upstream submission was withheld because two open PRs already proposed the same correction.
- [Upstream candidate audit](upstream-candidate-audit-2026-11-09.md) — records earlier candidate checks and duplicate-PR findings.

These records are retained as research and process evidence, not represented as available upstream contributions.
