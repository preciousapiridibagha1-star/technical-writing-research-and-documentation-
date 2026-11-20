"""HTTP API and browser interface for the synthetic CORA AI prototype."""
import os
from pathlib import Path
import sys

from fastapi import FastAPI, HTTPException
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


@app.get("/audit")
def get_audit_history():
    return {"events": engine.get_audit_history()}
