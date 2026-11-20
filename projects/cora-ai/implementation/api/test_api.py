"""API tests using an isolated temporary SQLite database per test."""
import pytest
from fastapi.testclient import TestClient

import app as api_module
from consent_engine import ConsentEngine


@pytest.fixture
def client(tmp_path, monkeypatch):
    test_engine = ConsentEngine(tmp_path / "api-test.sqlite3")
    monkeypatch.setattr(api_module, "engine", test_engine)
    with TestClient(api_module.app) as test_client:
        yield test_client
    test_engine.close()


def test_browser_workspace_is_served(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "CORA AI" in response.text
    assert "Check permission" in response.text


def test_health_endpoint_reports_sqlite(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert response.json()["storage"] == "sqlite"


def test_grant_then_permission_allow(client):
    grant = client.post("/consents", json={
        "participant_id": "P001", "resource_id": "D001",
        "purpose": "research", "action": "grant",
    })
    assert grant.status_code == 200
    assert grant.json()["status"] == "granted"
    check = client.post("/permissions/check", json={
        "participant_id": "P001", "resource_id": "D001", "purpose": "research",
    })
    assert check.status_code == 200
    assert check.json()["decision"] == "ALLOW"


def test_refused_purpose_is_denied(client):
    client.post("/consents", json={
        "participant_id": "P001", "resource_id": "D001",
        "purpose": "model_training", "action": "refuse",
    })
    check = client.post("/permissions/check", json={
        "participant_id": "P001", "resource_id": "D001", "purpose": "model_training",
    })
    assert check.json()["decision"] == "DENY"


def test_withdrawn_consent_is_denied(client):
    base = {"participant_id": "P001", "resource_id": "D001", "purpose": "research"}
    client.post("/consents", json={**base, "action": "grant"})
    client.post("/consents", json={**base, "action": "withdraw"})
    check = client.post("/permissions/check", json=base)
    assert check.json()["decision"] == "DENY"


def test_invalid_action_is_rejected(client):
    response = client.post("/consents", json={
        "participant_id": "P001", "resource_id": "D001",
        "purpose": "research", "action": "approve",
    })
    assert response.status_code == 422


def test_audit_endpoint_returns_events(client):
    client.post("/consents", json={
        "participant_id": "P001", "resource_id": "D001",
        "purpose": "research", "action": "grant",
    })
    response = client.get("/audit")
    assert response.status_code == 200
    assert len(response.json()["events"]) == 1


def test_api_state_survives_database_reopen(client, tmp_path, monkeypatch):
    client.post("/consents", json={
        "participant_id": "P002", "resource_id": "D002",
        "purpose": "research", "action": "grant",
    })
    db_path = tmp_path / "api-test.sqlite3"
    api_module.engine.close()
    reopened = ConsentEngine(db_path)
    monkeypatch.setattr(api_module, "engine", reopened)
    try:
        response = client.get("/consents/P002/D002/research")
        assert response.status_code == 200
        assert response.json()["status"] == "granted"
        assert len(client.get("/audit").json()["events"]) == 1
    finally:
        reopened.close()
