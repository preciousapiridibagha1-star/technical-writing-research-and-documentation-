# Open-source upstream candidate audit — 9 November 2026

**Purpose:** Re-check the two prepared Ollama contribution ideas before publishing anything. A previously open issue is not automatically an available contribution: existing pull requests must be checked first.

## Candidate 1 — Ollama issue #18045: Msty README URL

- Issue: [#18045 — update Msty link from .app to .ai](https://github.com/ollama/ollama/issues/18045).
- Existing upstream pull request: [#18050 — README: update Msty link to msty.ai](https://github.com/ollama/ollama/pull/18050).
- Checked status: issue open; PR open, not merged, updated 4 November 2026.
- Decision: **Do not submit the prepared one-line patch as a duplicate.** The requested correction is already represented by another contributor's public PR.

The factual basis remains valid: Msty's official transition announcement says it is moving from `msty.app` to `msty.ai`, and its current site uses `msty.ai`. That verifies the idea, not authorship of the upstream change.

## Candidate 2 — Ollama issue #14260: GPU fallback troubleshooting

- Issue: [#14260 — missing GPU fallback diagnosis and VRAM sizing guidance](https://github.com/ollama/ollama/issues/14260).
- Existing upstream pull request: [#14461 — add GPU-to-CPU fallback troubleshooting section](https://github.com/ollama/ollama/pull/14461).
- Checked status: issue open; PR open, not merged. The PR proposes the same target file and substantially overlapping diagnostic content.
- Decision: **Do not submit the prepared section as a competing duplicate.** The draft remains useful as a technical-writing exercise, but the issue already has an upstream contribution in review.

The current upstream documentation was checked directly. The troubleshooting page explains GPU discovery failures; the FAQ already documents `ollama ps` and the `PROCESSOR` column; and the context-length page warns that larger context windows require more memory. Any later contribution must add a clear improvement beyond the existing PR rather than repackaging the same section.

## Other candidate checks

The following alternatives were also checked and are not clean replacement targets:

| Issue | Existing PR found | Result |
|---|---|---|
| [#18215 — rootless Linux install](https://github.com/ollama/ollama/issues/18215) | [#18234](https://github.com/ollama/ollama/pull/18234) is open; [#19140](https://github.com/ollama/ollama/pull/19140) is closed without merge | Do not duplicate the active proposal. |
| [#17789 — NVIDIA driver guidance](https://github.com/ollama/ollama/issues/17789) | [#17940](https://github.com/ollama/ollama/pull/17940) is open | Already being addressed. |
| [#17155 — update-check identifier disclosure](https://github.com/ollama/ollama/issues/17155) | [#17861](https://github.com/ollama/ollama/pull/17861) is open | Already being addressed. |
| [#2588 — API option descriptions](https://github.com/ollama/ollama/issues/2588) | [#19022](https://github.com/ollama/ollama/pull/19022) is open | Overlaps the unassigned-looking older text-generation documentation request; not a clean new target. |

## GitHub access check

The connected GitHub account has read access to `ollama/ollama` but not push access (`pull: true`, `push: false`). No fork named `preciousapiridibagha1-star/ollama` exists in the connected account's repository list. The connected GitHub actions available in this session do not include a repository-fork operation.

This means I can inspect upstream issues, code, docs and pull requests, and can edit the user's own portfolio repository, but I cannot create a fork or publish an upstream branch from this connection. I have not attempted to write directly to the Ollama upstream repository.

## Current outcome and integrity statement

**No external contribution is claimed. No upstream branch, commit or pull request was created.** The two originally prepared proposals are retained as historical research records but are marked superseded because competing PRs already exist.

To resume Area 7, a fork must first exist under the contributor's GitHub account and be accessible to the connected GitHub integration. Then select two distinct open issues with no existing PR, verify each against current source, make and test focused changes, and submit only the work that adds a demonstrable improvement.
