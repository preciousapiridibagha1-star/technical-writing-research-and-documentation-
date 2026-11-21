# Configure the CORA Gemini API key

This file explains where to configure the Gemini key for the CORA backend.

## Important

Do not paste a real API key into this public GitHub repository. The `.env.example` file is a blank template only. Keep the real key private as a backend environment secret.

## If deploying the backend to a hosting provider

1. Open the backend service's **Environment Variables** or **Secrets** settings.
2. Add a variable named `GEMINI_API_KEY`.
3. Paste your Gemini API key as its value and save.
4. Add `GEMINI_MODEL` with value `gemini-2.5-flash` (optional; this is the current default).
5. Redeploy or restart the backend service.
6. Set the website's `window.CORA_API_BASE_URL` to the deployed backend's HTTPS origin so the chat interface can reach `/assistant/chat`.

## Local setup

1. Copy `.env.example` to `.env` in this API folder.
2. Put the key after `GEMINI_API_KEY=` in `.env`.
3. Keep `.env` out of Git. Never upload it or share screenshots containing the key.

## Current integration status

The FastAPI backend contains `POST /assistant/chat`. The GitHub Pages site is static hosting and cannot safely store provider secrets. The API endpoint must be deployed to a backend host and the website configured with that backend URL before live Gemini chat will work. The assistant explains consent and system behaviour only; it cannot grant consent, record a participant's choice, or override a backend DENY.
