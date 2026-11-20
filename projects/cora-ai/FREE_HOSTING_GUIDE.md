# CORA AI — zero-cost public demonstration

## Stage 1: GitHub Pages (static frontend)

The browser interface is in `docs/index.html`. It is designed to publish as a static site from this public GitHub repository. The deployment workflow is `.github/workflows/deploy-pages.yml`.

Expected public URL after Pages is enabled and deployment succeeds:

`https://preciousapiridibagha1-star.github.io/technical-writing-research-and-documentation-/`

To activate it after merging this branch: repository Settings → Pages → Build and deployment → Source: **GitHub Actions**. No domain purchase or paid plan is required.

If no backend URL is configured in the page's `cora-api-base` meta tag, the interface runs a clearly labelled browser-only demonstration using localStorage. Those records exist only in that visitor's browser and are not shared with other visitors.

## Stage 2: Python API on Render Free

The FastAPI + SQLite implementation remains the authoritative deterministic permission engine. `render.yaml` now explicitly selects Render's **Free** web-service plan. It does not request a paid persistent disk, paid compute, or a paid database. The service uses an ephemeral SQLite file at `/tmp/cora_demo.sqlite3`.

Render's official free-service documentation says Python web services can run on its Free instance. The service sleeps after 15 minutes without traffic and can take about a minute to wake. Its local filesystem is ephemeral: SQLite records are lost when the service spins down, restarts or redeploys. Render may also restart free services. This is suitable only for a temporary synthetic demonstration, not production or durable records.

Official details: https://render.com/docs/free

### Deploy steps

1. Merge the hosting branch into the repository's default branch after reviewing the changes.
2. Sign in to Render and connect the GitHub repository.
3. Choose **New → Blueprint** and select this repository's `render.yaml`.
4. Before creating anything, inspect the plan. It must say **Free**. Do not select Starter, paid compute, persistent disk, paid database, or an add-on. Do not enter payment details or approve an upgrade.
5. Create the service only if the dashboard confirms the Free plan and $0 service cost.
6. Wait for deployment and test `/health`. Expected response includes `"status":"ok"` and `"storage":"sqlite"`.
7. Copy the service's public `onrender.com` base URL into the `cora-api-base` meta tag in `docs/index.html`, commit and deploy Pages again.
8. Test grant, refuse, withdraw, permission checks and audit history from the GitHub Pages interface. The first request after idle may take about a minute.

If Render asks for a payment method, paid upgrade or any amount above $0, stop. Do not proceed. The browser-only GitHub Pages demo remains available without the backend.

## Important limitations

- This is a shared synthetic demonstration. Do not enter real participant, health or mental-health data.
- Free Render service data is temporary and may reset after idle spin-down, restart or redeployment.
- The service may be unavailable while it wakes from idle.
- No authentication, authorisation, rate limiting, backups, tamper-resistant audit log, production monitoring or external dataset enforcement is implemented.
- A public demo does not establish SRHIN approval, partnership, consultation or integration.
- This is not a legal consent mechanism or a production service.

## Hugging Face hosting note

Hugging Face Static Spaces are free, but the current official documentation says Docker/Gradio Spaces running on compute require a paid plan for ordinary accounts (with a limited ZeroGPU exception for eligible Gradio apps). Therefore this Python FastAPI backend is **not** being assigned to a Hugging Face Docker Space as a zero-cost solution.
