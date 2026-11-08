"""Vantage Automata: safe, local approval-flow demonstration.

This demo uses deterministic proposals and a mock action. It does not call an
AI provider, access external services, or modify real business data.
"""
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import hashlib
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
    prefix = "Remind me to "
    if not cleaned.lower().startswith(prefix.lower()):
        raise ValueError("Demo scope: use an instruction beginning 'Remind me to ...'.")
    task = cleaned[len(prefix):].strip()
    if not task:
        raise ValueError("Please describe what you want to be reminded about.")
    return Proposal(str(uuid4()), cleaned, "CREATE_MOCK_REMINDER",
                    f"Create a local demo reminder: {task}")


def proposal_fingerprint(proposal: Proposal) -> str:
    """Bind approval to the exact proposal content shown to the user."""
    approved_content = {
        "proposal_id": proposal.proposal_id,
        "instruction": proposal.instruction,
        "action": proposal.action,
        "description": proposal.description,
    }
    canonical = json.dumps(approved_content, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


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


def approve_and_execute(
    proposal: Proposal,
    approved_proposal_id: str,
    approved_fingerprint: str,
    executed_ids: set,
) -> str:
    """Execute once, only if the current proposal matches what was approved."""
    if proposal.status != "PENDING":
        raise ValueError("Proposal is no longer pending; no action was taken.")
    if approved_proposal_id != proposal.proposal_id:
        raise ValueError("Approval does not match this proposal; no action was taken.")
    if approved_fingerprint != proposal_fingerprint(proposal):
        raise ValueError("Proposal changed after review; approval is invalid.")
    if proposal.proposal_id in executed_ids:
        raise ValueError("Duplicate execution blocked; no action was taken.")

    # Record the attempt before execution: this demo favours at-most-once behaviour.
    executed_ids.add(proposal.proposal_id)
    proposal.status = "APPROVED"
    try:
        outcome = run_mock_action(proposal)
        return outcome
    except Exception:
        proposal.status = "FAILED"
        return "SAFE_FAILURE: action failed; it was not retried automatically."


def main() -> None:
    print("Vantage Automata — local approval demo (mock actions only)")
    try:
        proposal = prepare_proposal(input(
            "Instruction (e.g. Remind me to review my notes): "))
    except ValueError as error:
        print(f"Not accepted: {error}")
        return

    # Capture the exact content shown for approval.
    displayed_fingerprint = proposal_fingerprint(proposal)
    print("\nProposed action")
    print(f"ID: {proposal.proposal_id}")
    print(f"Action: {proposal.description}")
    decision = input("Approve this exact proposal? [y/N]: ").strip().lower()

    if decision == "y":
        outcome = approve_and_execute(
            proposal, proposal.proposal_id, displayed_fingerprint, set()
        )
        decision_label = "APPROVED"
    else:
        proposal.status = "REJECTED"
        outcome = "STOPPED: no action was taken."
        decision_label = "REJECTED"

    write_audit(proposal, decision_label, outcome)
    print(outcome)
    print(f"Audit record appended to {AUDIT_FILE.resolve()}")


if __name__ == "__main__":
    main()
