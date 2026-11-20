"""API-level tests for the synthetic CORA AI prototype."""
from fastapi.testclient import TestClient

from app import app, engine

client = TestClient(app)


def setup_function():
    # Each test starts with a fresh in-memory engine.
    engine._consents.clear()
    engine.audit_log.clear()


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_grant_then_permission_allow():
    grant = client.post("/consents", json={
        "participant_id": "P001",
        "resource_id": "D001",
        "purpose": "research",
        "action": "grant",
    })
    assert grant.status_code == 200
    assert grant.json()["status"] == "granted"

    check = client.post("/permissions/check", json={
        "participant_id": "P001",
        "resource_id": "D001",
        "purpose": "research",
    })
    assert check.status_code == 200
    assert check.json()["decision"] == "ALLOW"


def test_refused_purpose_is_denied():
    client.post("/consents", json={
        "participant_id": "P001",
        "resource_id": "D001",
        "purpose": "model_training",
        "action": "refuse",
    })
    check = client.post("/permissions/check", json={
        "participant_id": "P001",
        "resource_id": "D001",
        "purpose": "model_training",
    })
    assert check.json()["decision"] == "DENY"


def test_withdrawn_consent_is_denied():
    base = {
        "participant_id": "P001",
        "resource_id": "D001",
        "purpose": "research",
    }
    client.post("/consents", json={**base, "action": "grant"})
    client.post("/consents", json={**base, "action": "withdraw"})
    check = client.post("/permissions/check", json=base)
    assert check.json()["decision"] == "DENY"


def test_invalid_action_is_rejected():
    response = client.post("/consents", json={
        "participant_id": "P001",
        "resource_id": "D001",
        "purpose": "research",
        "action": "approve",
    })
    assert response.status_code == 422


def test_audit_endpoint_returns_events():
    client.post("/consents", json={
        "participant_id": "P001",
        "resource_id": "D001",
        "purpose": "research",
        "action": "grant",
    })
    response = client.get("/audit")
    assert response.status_code == 200
    assert len(response.json()["events"]) == 1
