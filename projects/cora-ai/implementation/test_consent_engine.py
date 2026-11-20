"""Automated checks for the CORA AI deterministic consent engine."""
import unittest

from consent_engine import ConsentEngine


class ConsentEngineTests(unittest.TestCase):
    def setUp(self):
        self.engine = ConsentEngine()

    def test_no_record_defaults_to_deny(self):
        result = self.engine.check_permission("P001", "D001", "research")
        self.assertEqual(result["decision"], "DENY")

    def test_grant_allows_only_exact_purpose(self):
        self.engine.record_consent("P001", "D001", "research", "grant")
        self.assertEqual(
            self.engine.check_permission("P001", "D001", "research")["decision"],
            "ALLOW",
        )
        self.assertEqual(
            self.engine.check_permission("P001", "D001", "model_training")["decision"],
            "DENY",
        )

    def test_refusal_denies_access(self):
        self.engine.record_consent("P001", "D001", "model_training", "refuse")
        self.assertEqual(
            self.engine.check_permission("P001", "D001", "model_training")["decision"],
            "DENY",
        )

    def test_withdrawal_changes_grant_to_deny(self):
        self.engine.record_consent("P001", "D001", "research", "grant")
        self.engine.record_consent("P001", "D001", "research", "withdraw")
        self.assertEqual(
            self.engine.check_permission("P001", "D001", "research")["decision"],
            "DENY",
        )

    def test_different_participant_or_resource_is_denied(self):
        self.engine.record_consent("P001", "D001", "research", "grant")
        self.assertEqual(
            self.engine.check_permission("P002", "D001", "research")["decision"],
            "DENY",
        )
        self.assertEqual(
            self.engine.check_permission("P001", "D002", "research")["decision"],
            "DENY",
        )

    def test_withdrawal_without_current_grant_is_rejected(self):
        with self.assertRaises(ValueError):
            self.engine.record_consent("P001", "D001", "research", "withdraw")

    def test_invalid_action_is_rejected(self):
        with self.assertRaises(ValueError):
            self.engine.record_consent("P001", "D001", "research", "maybe")

    def test_audit_history_records_changes_and_checks(self):
        self.engine.record_consent("P001", "D001", "research", "grant")
        self.engine.check_permission("P001", "D001", "research")
        history = self.engine.get_audit_history()
        self.assertEqual(len(history), 2)
        self.assertEqual(history[0]["event_type"], "consent_change")
        self.assertEqual(history[1]["event_type"], "permission_check")


if __name__ == "__main__":
    unittest.main()
