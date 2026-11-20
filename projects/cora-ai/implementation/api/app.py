"""HTTP API for the synthetic CORA AI consent prototype.

The API is a thin interface over the deterministic consent engine.
It uses in-memory state and is not suitable for production deployment.
"""
from pathlib import Path
import sys

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# Allow running this module directly from the implementation folder or project root.
IMPLEMENTATION_DIR = Path(__file__).resolve().parents[1]
if str(IMPLEMENTATION_DIR) not in sys.path:
    sys.path.insert(0, str(IMPLEMENTATION_DIR))

from consent_engine import ConsentEngine  # noqa: E402


app = FastAPI(
    title="CORA AI Consent Prototype API",
    version="0.1.0",
    description=(
        "Synthetic demonstration API. Decisions are made by deterministic "
        "backend rules, not by an AI model. Do not submit real personal data."
    ),
)

engine = ConsentEngine()


class ConsentAction(BaseModel):
    participant_id: str = Field(min_length=1, max_length=40)
    resource_id: str = Field(min_length=1, max_length=40)
    purpose: str = Field(min_length=1, max_length=80)
    action: str


class PermissionRequest(BaseModel):
    participant_id: str = Field(min_length=1, max_length=40)
    resource_id: str = Field(min_length=1, max_length=40)
    purpose: str = Field(min_length=1, max_length=80)


@app.get("/health")
def health():
    return {"status": "ok", "mode": "synthetic-prototype"}


@app.post("/consents")
def record_consent(payload: ConsentAction):
    try:
        record = engine.record_consent(
            payload.participant_id,
            payload.resource_id,
            payload.purpose,
            payload.action,
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
        payload.participant_id,
        payload.resource_id,
        payload.purpose,
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
