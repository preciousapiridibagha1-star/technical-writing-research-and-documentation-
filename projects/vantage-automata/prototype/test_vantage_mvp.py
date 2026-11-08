import unittest
from unittest.mock import patch
from vantage_mvp import (
    Proposal, prepare_proposal, run_mock_action,
    proposal_fingerprint, approve_and_execute,
)


class VantageMVPTests(unittest.TestCase):
    def setUp(self):
        self.proposal = prepare_proposal("Remind me to review my notes")
        self.fingerprint = proposal_fingerprint(self.proposal)
        self.executed_ids = set()

    def test_valid_reminder_creates_pending_proposal(self):
        self.assertEqual(self.proposal.action, "CREATE_MOCK_REMINDER")
        self.assertEqual(self.proposal.status, "PENDING")

    def test_empty_instruction_is_rejected(self):
        with self.assertRaises(ValueError):
            prepare_proposal("   ")

    def test_out_of_scope_instruction_is_rejected(self):
        with self.assertRaises(ValueError):
            prepare_proposal("Send an email to my client")

    def test_overlong_instruction_is_rejected(self):
        with self.assertRaises(ValueError):
            prepare_proposal("Remind me to " + "x" * 240)

    def test_unauthorised_action_type_is_rejected(self):
        proposal = Proposal("id", "test", "SEND_PAYMENT", "send payment")
        with self.assertRaises(ValueError):
            run_mock_action(proposal)

    def test_changed_proposal_invalidates_approval(self):
        self.proposal.description = "Send a payment instead"
        with self.assertRaisesRegex(ValueError, "changed after review"):
            approve_and_execute(
                self.proposal, self.proposal.proposal_id,
                self.fingerprint, self.executed_ids
            )
        self.assertEqual(self.proposal.status, "PENDING")
        self.assertEqual(self.executed_ids, set())

    def test_wrong_proposal_id_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "does not match"):
            approve_and_execute(
                self.proposal, "another-id", self.fingerprint, self.executed_ids
            )

    def test_duplicate_execution_is_blocked(self):
        first = approve_and_execute(
            self.proposal, self.proposal.proposal_id,
            self.fingerprint, self.executed_ids
        )
        self.assertIn("MOCK_SUCCESS", first)
        with self.assertRaisesRegex(ValueError, "no longer pending"):
            approve_and_execute(
                self.proposal, self.proposal.proposal_id,
                self.fingerprint, self.executed_ids
            )

    def test_execution_failure_stops_without_automatic_retry(self):
        with patch("vantage_mvp.run_mock_action", side_effect=RuntimeError("test")):
            outcome = approve_and_execute(
                self.proposal, self.proposal.proposal_id,
                self.fingerprint, self.executed_ids
            )
        self.assertTrue(outcome.startswith("SAFE_FAILURE"))
        self.assertEqual(self.proposal.status, "FAILED")
        self.assertIn(self.proposal.proposal_id, self.executed_ids)


if __name__ == "__main__":
    unittest.main()
