"""HTTP API and browser interface for the synthetic CORA AI prototype."""
import os
from pathlib import Path
import sys
import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

IMPLEMENTATION_DIR = Path(__file__).resolve().parents[1]
API_DIR = Path(__file__).resolve().parent
UI_DIR = API_DIR / "ui"
if str(IMPLEMENTATION_DIR) not in sys.path:
    sys.path.insert(0, str(IMPLEMENTATION_DIR))

from consent_engine import ConsentEngine  # noqa: E402

DEFAULT_DB_PATH = API_DIR / "data" / "cora_demo.sqlite3"
DB_PATH = Path(os.environ.get("CORA_DB_PATH", str(DEFAULT_DB_PATH))).expanduser()

app = FastAPI(
    title="CORA AI Consent Prototype API",
    version="0.3.0",
    description=(
        "Synthetic demonstration API. Decisions are deterministic backend "
        "rules, not AI decisions. Do not submit real personal data."
    ),
)
allowed_origins = [origin.strip() for origin in os.environ.get(
    "CORA_ALLOWED_ORIGINS",
    "https://preciousapiridibagha1-star.github.io",
).split(",") if origin.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)
engine = ConsentEngine(db_path=DB_PATH)


class ConsentAction(BaseModel):
    participant_id: str = Field(min_length=1, max_length=40)
    resource_id: str = Field(min_length=1, max_length=40)
    purpose: str = Field(min_length=1, max_length=80)
    action: str


class PermissionRequest(BaseModel):
    participant_id: str = Field(min_length=1, max_length=40)
    resource_id: str = Field(min_length=1, max_length=40)
    purpose: str = Field(min_length=1, max_length=80)


class AssistantMessage(BaseModel):
    message: str = Field(min_length=1, max_length=4000)
    conversation: list[dict[str, str]] = Field(default_factory=list, max_length=12)


@app.get("/", include_in_schema=False)
def browser_app():
    return FileResponse(UI_DIR / "index.html")


app.mount("/assets", StaticFiles(directory=UI_DIR), name="assets")


@app.get("/health")
def health():
    return {
        "status": "ok",
        "mode": "synthetic-prototype",
        "storage": "sqlite",
    }


@app.post("/consents")
def record_consent(payload: ConsentAction):
    try:
        record = engine.record_consent(
            payload.participant_id, payload.resource_id, payload.purpose, payload.action
        )
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    return {
        "participant_id": record.participant_id,
        "resource_id": record.resource_id,
        "purpose": record.purpose,
        "status": record.status,
        "updated_at": record.updated_at,
    }


@app.post("/permissions/check")
def check_permission(payload: PermissionRequest):
    return engine.check_permission(
        payload.participant_id, payload.resource_id, payload.purpose
    )


@app.get("/consents/{participant_id}/{resource_id}/{purpose}")
def get_consent(participant_id: str, resource_id: str, purpose: str):
    record = engine.get_consent(participant_id, resource_id, purpose)
    if record is None:
        raise HTTPException(status_code=404, detail="No consent record found.")
    return record


@app.post("/assistant/chat")
def assistant_chat(payload: AssistantMessage):
    """Gemini-powered explanation assistant; never records consent or grants access."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=503, detail="AI assistant is not configured on this server.")

    system_instruction = (
        "You are CORA's consent and data-rights guide. Explain dataset purposes, "
        "consent choices, permission outcomes and audit history in clear, neutral language. "
        "Research and AI model training are separate purposes. Never infer, request or "
        "treat ambiguous language as consent. Never choose for a participant, record or "
        "change consent, approve data access, or override a deterministic DENY. Explain "
        "that only CORA's backend can validate and record an explicit participant action. "
        "Do not provide medical advice or ask for real personal, health or sensitive data. "
        "This is a synthetic prototype. If asked to grant/refuse/withdraw, explain how "
        "to use the consent controls; do not claim you performed the action."
    )
    model = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
    contents = []
    for item in payload.conversation[-10:]:
        role = item.get("role", "")
        text = item.get("text", "")
        if role in ("user", "model") and isinstance(text, str) and text.strip():
            contents.append({"role": role, "parts": [{"text": text[:4000]}]})
    contents.append({"role": "user", "parts": [{"text": payload.message}]})
    body = json.dumps({
        "systemInstruction": {"parts": [{"text": system_instruction}]},
        "contents": contents,
        "generationConfig": {"temperature": 0.25, "maxOutputTokens": 700},
    }).encode("utf-8")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    request = Request(url, data=body, headers={
        "Content-Type": "application/json",
        "x-goog-api-key": api_key,
    }, method="POST")
    try:
        with urlopen(request, timeout=20) as response:
            result = json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        if exc.code in (400, 401, 403, 404, 429):
            raise HTTPException(status_code=502, detail="The AI provider rejected the request or the configured quota is unavailable.") from exc
        raise HTTPException(status_code=502, detail="The AI provider is temporarily unavailable.") from exc
    except (URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise HTTPException(status_code=502, detail="Could not reach the AI provider.") from exc
    candidates = result.get("candidates", [])
    parts = candidates[0].get("content", {}).get("parts", []) if candidates else []
    answer = " ".join(part.get("text", "") for part in parts if isinstance(part.get("text"), str)).strip()
    if not answer:
        raise HTTPException(status_code=502, detail="The AI provider returned no text response.")
    return {"reply": answer, "provider": "Google Gemini", "model": model}


@app.get("/audit")
def get_audit_history():
    return {"events": engine.get_audit_history()}
