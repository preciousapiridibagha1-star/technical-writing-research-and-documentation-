# Contribution Proposal 2 — Ollama GPU fallback troubleshooting

**Upstream repository:** [ollama/ollama](https://github.com/ollama/ollama)
**Issue:** [#14260 — Troubleshooting docs missing GPU fallback diagnosis and VRAM sizing guidance](https://github.com/ollama/ollama/issues/14260)
**Target file:** `docs/troubleshooting.mdx`

## Problem verified

The troubleshooting page covers GPU discovery failures but does not provide a short diagnostic path for the case where a GPU is detected and the model is only partly loaded onto it. The current FAQ already documents `ollama ps` and its `PROCESSOR` column. The context-length page explains that increasing context length increases memory requirements. The issue is open, unassigned and shows no linked branch or pull request in the checked metadata.

## Proposed documentation improvement

Add a concise section for a GPU detected but slow model. It should:

1. Ask the user to run `ollama ps` while the model is loaded.
2. Explain `100% GPU`, `100% CPU` and mixed CPU/GPU values using the FAQ's existing terminology.
3. Explain that a split can be consistent with insufficient available GPU memory, while avoiding a claim that the split proves one cause.
4. Link to context-length documentation and explain that larger contexts require more memory.
5. Suggest closing other GPU-intensive applications and trying a smaller model or lower-memory quantised variant where available.
6. Ask the user to rerun `ollama ps` after each change.

## Model-size and VRAM table: accuracy safeguards

A parameter-count-to-VRAM table can mislead because actual use depends on architecture, quantisation, context length, runtime allocations, concurrent workloads and partial offloading. A safer table should show specific current Ollama model artifacts and their published download sizes, explicitly stating that download size is not the same as a guaranteed VRAM minimum.

Examples checked in the Ollama model library:

| Model artifact | Published variant | Download size |
|---|---|---:|
| `qwen2.5:3b` | Q4_K_M | 1.9 GB |
| `llama3.1:8b` | Q4_K_M | 4.9 GB |
| `qwen2.5:14b` | Confirm exact tag variant before submission | 9.0 GB |
| `qwen2.5:32b` | Confirm exact tag variant before submission | 20 GB |
| `llama3.1:70b` | Confirm exact tag variant before submission | 43 GB |

Do not label all listed models Q4 without verifying their individual tag detail pages. Explain that runtime allocations and the context/KV cache consume additional memory. The table is a reference for published artifact size, not a compatibility guarantee.

## Candidate text for the new section

### The GPU is detected, but the model is slower than expected

A detected GPU does not necessarily mean that the entire model is running on it. While the model is loaded, run `ollama ps` and check the `PROCESSOR` column:

- `100% GPU`: the model is loaded entirely into GPU memory.
- `100% CPU`: the model is running in system memory.
- A CPU/GPU percentage split: the model is split between system memory and GPU memory.

If the model is partly or fully on the CPU, check whether the model and requested context fit in the available GPU memory. Other applications may also be using GPU memory. Increasing the context length increases memory use; see [Context length](./context-length.mdx).

For diagnosis, close other GPU-intensive applications and try a smaller model or a lower-memory quantised variant where one is available. Load the model again and check `ollama ps`. Change one variable at a time so that you can identify which change affects the processor split.

The published download size of a model is only a starting point, not a VRAM requirement. Runtime allocations and the context/KV cache need additional memory, and the amount varies by model, quantisation, context length and workload. Use the model's own details and observed system memory use rather than treating a model-size table as a compatibility guarantee.

## Verification plan

- Compare `ollama ps` terminology against the current FAQ.
- Check the context-length explanation and link against the current page.
- Confirm all Markdown/MDX links resolve.
- Build/render documentation following the Ollama contributor workflow.
- Verify each model tag's current quantisation and published size before including it.
- Ensure the table clearly separates download size from VRAM requirements.

## Contributor guidance

Ollama's contributor guide welcomes small documentation corrections and asks contributors to keep documentation additions maintainable. Keep the proposed section focused on this issue.

## Status

**Superseded as a submission target — not submitted.** Another contributor has already opened [upstream PR #14461](https://github.com/ollama/ollama/pull/14461), which targets the same file and proposes substantially overlapping GPU-fallback guidance. Do not submit a competing duplicate. Retained as a research and technical-writing exercise.