"""Vantage Automata: safe, local approval-flow demonstration.

This demo uses a deterministic proposal and a mock action. It does not call an
AI provider, access external services, or modify real business data.
"""
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import json
from pathlib import Path
from uuid import uuid4

AUDIT_FILE = Path("vantage_audit.jsonl")

@dataclass
class Proposal:
    proposal_id: str
    instruction: str
    action: str
    description: str
    status: str = "PENDING"


def prepare_proposal(instruction: str) -> Proposal:
    cleaned = " ".join(instruction.split())
    if not cleaned:
        raise ValueError("Please enter an instruction.")
    if len(cleaned) > 240:
        raise ValueError("Instruction must be 240 characters or fewer.")
    if not cleaned.lower().startswith("remind me to "):
        raise ValueError("Demo scope: use an instruction beginning 'Remind me to ...'.")
    task = cleaned[len("Remind me to "):].strip()
    if not task:
        raise ValueError("Please describe what you want to be reminded about.")
    return Proposal(str(uuid4()), cleaned, "CREATE_MOCK_REMINDER",
                    f"Create a local demo reminder: {task}")


def write_audit(proposal: Proposal, decision: str, outcome: str) -> None:
    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "proposal": asdict(proposal),
        "decision": decision,
        "outcome": outcome,
    }
    with AUDIT_FILE.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(record, ensure_ascii=False) + "\n")


def run_mock_action(proposal: Proposal) -> str:
    if proposal.action != "CREATE_MOCK_REMINDER":
        raise ValueError("Action is not permitted by this demo.")
    return "MOCK_SUCCESS: reminder simulated; no external action was taken."


def main() -> None:
    print("Vantage Automata — local approval demo (mock actions only)")
    try:
        proposal = prepare_proposal(input(
            "Instruction (e.g. Remind me to review my notes): "))
    except ValueError as error:
        print(f"Not accepted: {error}")
        return

    print("\nProposed action")
    print(f"ID: {proposal.proposal_id}")
    print(f"Action: {proposal.description}")
    decision = input("Approve this exact proposal? [y/N]: ").strip().lower()
    if decision == "y":
        outcome = run_mock_action(proposal)
        proposal.status = "APPROVED"
        write_audit(proposal, "APPROVED", outcome)
        print(outcome)
    else:
        proposal.status = "REJECTED"
        outcome = "STOPPED: no action was taken."
        write_audit(proposal, "REJECTED", outcome)
        print(outcome)
    print(f"Audit record appended to {AUDIT_FILE.resolve()}")


if __name__ == "__main__":
    main()
