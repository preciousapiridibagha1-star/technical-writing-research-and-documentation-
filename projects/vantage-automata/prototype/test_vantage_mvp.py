import unittest
from vantage_mvp import prepare_proposal, run_mock_action, Proposal

class VantageMVPTests(unittest.TestCase):
    def test_valid_reminder_creates_proposal(self):
        proposal = prepare_proposal("Remind me to review my notes")
        self.assertEqual(proposal.action, "CREATE_MOCK_REMINDER")
        self.assertEqual(proposal.status, "PENDING")

    def test_empty_instruction_is_rejected(self):
        with self.assertRaises(ValueError):
            prepare_proposal("   ")

    def test_out_of_scope_instruction_is_rejected(self):
        with self.assertRaises(ValueError):
            prepare_proposal("Send an email to my client")

    def test_overlong_instruction_is_rejected(self):
        with self.assertRaises(ValueError):
            prepare_proposal("Remind me to " + "x" * 240)

    def test_mock_action_is_restricted(self):
        proposal = Proposal("id", "test", "SEND_PAYMENT", "send payment")
        with self.assertRaises(ValueError):
            run_mock_action(proposal)

if __name__ == "__main__":
    unittest.main()
