"""CORA AI deterministic consent engine backed by SQLite.

Synthetic demonstration only. Permission decisions are deterministic: an exact
participant, resource and purpose match with current granted consent is required.
"""
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
import sqlite3
from threading import RLock
from typing import Optional, Union


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
    """SQLite-backed consent engine; use ':memory:' for isolated tests."""

    def __init__(self, db_path: Union[str, Path] = ":memory:") -> None:
        self.db_path = str(db_path)
        if self.db_path != ":memory:":
            Path(self.db_path).expanduser().resolve().parent.mkdir(
                parents=True, exist_ok=True
            )
        self._lock = RLock()
        self._connection = sqlite3.connect(
            self.db_path, check_same_thread=False, timeout=10
        )
        self._connection.row_factory = sqlite3.Row
        with self._lock:
            self._connection.execute("PRAGMA foreign_keys = ON")
            self._connection.execute("PRAGMA busy_timeout = 10000")
            if self.db_path != ":memory:":
                self._connection.execute("PRAGMA journal_mode = WAL")
            self._initialise_schema()

    def _initialise_schema(self) -> None:
        self._connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS consents (
                participant_id TEXT NOT NULL,
                resource_id TEXT NOT NULL,
                purpose TEXT NOT NULL,
                status TEXT NOT NULL CHECK (
                    status IN ('granted', 'refused', 'withdrawn')
                ),
                updated_at TEXT NOT NULL,
                PRIMARY KEY (participant_id, resource_id, purpose)
            );

            CREATE TABLE IF NOT EXISTS audit_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_type TEXT NOT NULL,
                participant_id TEXT NOT NULL,
                resource_id TEXT NOT NULL,
                purpose TEXT NOT NULL,
                outcome TEXT NOT NULL,
                recorded_at TEXT NOT NULL,
                explanation TEXT NOT NULL
            );

            CREATE INDEX IF NOT EXISTS idx_audit_recorded_at
            ON audit_events(id);
            """
        )

    @staticmethod
    def _now() -> str:
        return datetime.now(timezone.utc).isoformat()

    @staticmethod
    def _record_from_row(row: sqlite3.Row) -> ConsentRecord:
        return ConsentRecord(
            participant_id=row["participant_id"],
            resource_id=row["resource_id"],
            purpose=row["purpose"],
            status=row["status"],
            updated_at=row["updated_at"],
        )

    def record_consent(
        self,
        participant_id: str,
        resource_id: str,
        purpose: str,
        action: str,
    ) -> ConsentRecord:
        """Atomically persist a grant/refusal/withdrawal and its audit event."""
        values = (participant_id, resource_id, purpose)
        if not all(isinstance(value, str) and value.strip() for value in values):
            raise ValueError("Participant, resource and purpose are required.")
        if action not in VALID_ACTIONS:
            raise ValueError("Action must be grant, refuse or withdraw.")

        status = {
            "grant": "granted",
            "refuse": "refused",
            "withdraw": "withdrawn",
        }[action]
        now = self._now()

        with self._lock:
            cursor = self._connection.cursor()
            try:
                cursor.execute("BEGIN IMMEDIATE")
                previous = cursor.execute(
                    """SELECT status FROM consents
                    WHERE participant_id=? AND resource_id=? AND purpose=?""",
                    values,
                ).fetchone()
                if action == "withdraw" and (
                    previous is None or previous["status"] != "granted"
                ):
                    raise ValueError(
                        "Consent can only be withdrawn when it is currently granted."
                    )

                cursor.execute(
                    """INSERT INTO consents
                    (participant_id, resource_id, purpose, status, updated_at)
                    VALUES (?, ?, ?, ?, ?)
                    ON CONFLICT(participant_id, resource_id, purpose)
                    DO UPDATE SET status=excluded.status, updated_at=excluded.updated_at""",
                    (*values, status, now),
                )
                cursor.execute(
                    """INSERT INTO audit_events
                    (event_type, participant_id, resource_id, purpose,
                     outcome, recorded_at, explanation)
                    VALUES (?, ?, ?, ?, ?, ?, ?)""",
                    (
                        "consent_change", *values, status, now,
                        f"Consent status changed to {status} by an explicit prototype action.",
                    ),
                )
                self._connection.commit()
            except Exception:
                self._connection.rollback()
                raise
            finally:
                cursor.close()

        return ConsentRecord(*values, status, now)

    def check_permission(
        self, participant_id: str, resource_id: str, purpose: str
    ) -> dict:
        """Return ALLOW only for exact current granted consent; otherwise DENY."""
        values = (participant_id, resource_id, purpose)
        now = self._now()
        with self._lock:
            cursor = self._connection.cursor()
            try:
                cursor.execute("BEGIN IMMEDIATE")
                row = cursor.execute(
                    """SELECT status FROM consents
                    WHERE participant_id=? AND resource_id=? AND purpose=?""",
                    values,
                ).fetchone()
                if row is not None and row["status"] == "granted":
                    decision = "ALLOW"
                    reason = "A current grant exists for this exact purpose."
                elif row is None:
                    decision = "DENY"
                    reason = "No consent record exists for this exact purpose."
                else:
                    decision = "DENY"
                    reason = f"Current consent status is {row['status']}."

                cursor.execute(
                    """INSERT INTO audit_events
                    (event_type, participant_id, resource_id, purpose,
                     outcome, recorded_at, explanation)
                    VALUES (?, ?, ?, ?, ?, ?, ?)""",
                    ("permission_check", *values, decision, now, reason),
                )
                self._connection.commit()
            except Exception:
                self._connection.rollback()
                raise
            finally:
                cursor.close()

        return {
            "decision": decision,
            "participant_id": participant_id,
            "resource_id": resource_id,
            "purpose": purpose,
            "reason": reason,
        }

    def get_consent(
        self, participant_id: str, resource_id: str, purpose: str
    ) -> Optional[dict]:
        with self._lock:
            row = self._connection.execute(
                """SELECT participant_id, resource_id, purpose, status, updated_at
                FROM consents
                WHERE participant_id=? AND resource_id=? AND purpose=?""",
                (participant_id, resource_id, purpose),
            ).fetchone()
        return asdict(self._record_from_row(row)) if row else None

    def get_audit_history(self) -> list:
        with self._lock:
            rows = self._connection.execute(
                """SELECT event_type, participant_id, resource_id, purpose,
                outcome, recorded_at, explanation
                FROM audit_events ORDER BY id ASC"""
            ).fetchall()
        return [dict(row) for row in rows]

    def clear(self) -> None:
        """Clear prototype records; intended for isolated tests and demos."""
        with self._lock:
            self._connection.execute("DELETE FROM audit_events")
            self._connection.execute("DELETE FROM consents")
            self._connection.commit()

    def close(self) -> None:
        with self._lock:
            self._connection.close()
