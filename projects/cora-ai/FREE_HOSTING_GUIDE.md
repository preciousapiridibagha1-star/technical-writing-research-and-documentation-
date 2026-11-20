# CORA AI — Free public demonstration

## Stage 1: GitHub Pages

The static demonstration is in `docs/index.html`. GitHub Pages can publish this browser interface from the repository using GitHub Actions. The browser-only mode uses localStorage and synthetic IDs; it is **not** the Python backend and records stay in the visitor's browser.

The workflow is `.github/workflows/deploy-pages.yml`. After this branch is merged, enable Pages in repository Settings → Pages → Build and deployment → Source: GitHub Actions. The workflow then publishes the site. No custom domain or paid plan is required for this public repository.

Expected URL:
`https://preciousapiridibagha1-star.github.io/technical-writing-research-and-documentation-/`

## Stage 2: free Python API hosting (prepared, not yet deployed)

The FastAPI + SQLite API remains the authoritative permission engine. A candidate zero-cost host is a Hugging Face Docker Space on its free CPU tier. Free Space storage is ephemeral: SQLite records may be lost when the Space restarts or is rebuilt. Do not treat this as durable storage or use real participant data.

Before connecting the static site to a remote API:
1. Create a public Docker Space with no paid hardware.
2. Copy the API deployment package in `hosting/huggingface/` into the Space repository root.
3. Set the Space's port to 7860 (Dockerfile does this).
4. Set the GitHub Pages origin in the API CORS allow-list.
5. Add the resulting Space URL to the site's `cora-api-base` meta tag and redeploy Pages.
6. Verify health, grant/refuse/withdraw, permission checks and audit history.

This repository change does not create a Hugging Face account/Space or claim that the API is publicly live. Free hardware availability and current limits should be checked in the account before use. Do not enable paid hardware, persistent storage, or any paid add-on.

## Security boundary

This is a shared synthetic demonstration only. It has no authentication, participant identity verification, rate limiting, backup, tamper-resistant audit log or external dataset enforcement. Visitors may change demo records. Never enter real personal, health or mental-health data.
