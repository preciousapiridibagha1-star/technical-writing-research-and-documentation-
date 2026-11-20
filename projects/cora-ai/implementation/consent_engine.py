"""CORA AI deterministic consent engine — synthetic demonstration only.

This module contains no AI decision-making and stores no real participant data.
The permission decision is deterministic: exact participant, resource, purpose,
and current consent status must match. Anything else is denied.
"""
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Dict, List, Optional


VALID_ACTIONS = {"grant", "refuse", "withdraw"}


@dataclass
class ConsentRecord:
    participant_id: str
    resource_id: str
    purpose: str
    status: str
    updated_at: str


@dataclass
class AuditEvent:
    event_type: str
    participant_id: str
    resource_id: str
    purpose: str
    outcome: str
    recorded_at: str
    explanation: str


class ConsentEngine:
    """Small in-memory engine for the CORA AI learning prototype."""

    def __init__(self) -> None:
        self._consents: Dict[tuple, ConsentRecord] = {}
        self.audit_log: List[AuditEvent] = []

    @staticmethod
    def _now() -> str:
        return datetime.now(timezone.utc).isoformat()

    @staticmethod
    def _key(participant_id: str, resource_id: str, purpose: str) -> tuple:
        return (participant_id, resource_id, purpose)

    def record_consent(
        self,
        participant_id: str,
        resource_id: str,
        purpose: str,
        action: str,
    ) -> ConsentRecord:
        """Record grant/refuse/withdraw. Invalid or blank inputs are rejected."""
        values = (participant_id, resource_id, purpose)
        if not all(isinstance(value, str) and value.strip() for value in values):
            raise ValueError("Participant, resource and purpose are required.")
        if action not in VALID_ACTIONS:
            raise ValueError("Action must be grant, refuse or withdraw.")

        key = self._key(participant_id, resource_id, purpose)
        previous = self._consents.get(key)

        if action == "withdraw" and (previous is None or previous.status != "granted"):
            raise ValueError("Consent can only be withdrawn when it is currently granted.")

        status = {"grant": "granted", "refuse": "refused", "withdraw": "withdrawn"}[action]
        record = ConsentRecord(
            participant_id=participant_id,
            resource_id=resource_id,
            purpose=purpose,
            status=status,
            updated_at=self._now(),
        )
        self._consents[key] = record
        self.audit_log.append(AuditEvent(
            event_type="consent_change",
            participant_id=participant_id,
            resource_id=resource_id,
            purpose=purpose,
            outcome=status,
            recorded_at=record.updated_at,
            explanation=f"Consent status changed to {status} by an explicit prototype action.",
        ))
        return record

    def check_permission(
        self, participant_id: str, resource_id: str, purpose: str
    ) -> dict:
        """Return ALLOW only for an exact match with current granted consent."""
        key = self._key(participant_id, resource_id, purpose)
        record: Optional[ConsentRecord] = self._consents.get(key)

        if record is not None and record.status == "granted":
            decision, reason = "ALLOW", "A current grant exists for this exact purpose."
        elif record is None:
            decision, reason = "DENY", "No consent record exists for this exact purpose."
        else:
            decision, reason = "DENY", f"Current consent status is {record.status}."

        self.audit_log.append(AuditEvent(
            event_type="permission_check",
            participant_id=participant_id,
            resource_id=resource_id,
            purpose=purpose,
            outcome=decision,
            recorded_at=self._now(),
            explanation=reason,
        ))
        return {
            "decision": decision,
            "participant_id": participant_id,
            "resource_id": resource_id,
            "purpose": purpose,
            "reason": reason,
        }

    def get_consent(self, participant_id: str, resource_id: str, purpose: str):
        record = self._consents.get(self._key(participant_id, resource_id, purpose))
        return asdict(record) if record else None

    def get_audit_history(self) -> list:
        """Return a copy of the audit history as plain dictionaries."""
        return [asdict(event) for event in self.audit_log]
