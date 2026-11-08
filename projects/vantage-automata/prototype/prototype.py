"""A tiny, safe demonstration of a human approval gate.

Run: python prototype.py
Only a local mock action is available. No external systems are contacted.
"""
from datetime import datetime, timezone
import json
from pathlib import Path

AUDIT_FILE = Path("audit.jsonl")


def write_audit(event: dict) -> None:
    event["timestamp_utc"] = datetime.now(timezone.utc).isoformat()
    with AUDIT_FILE.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=False) + "\n")


def prepare_proposal(instruction: str) -> dict:
    """Return a fixed mock proposal; no AI call is made."""
    if not instruction.strip():
        raise ValueError("Please enter a non-empty instruction.")
    return {
        "task_summary": instruction.strip(),
        "proposed_action": "Create a local demonstration note",
        "action_type": "mock_note",
        "requires_approval": True,
        "risk_level": "low",
    }


def run_mock_action(proposal: dict) -> str:
    """Harmless local mock action; does not change an external service."""
    return f"Mock action completed: {proposal['proposed_action']}"


def process_instruction(instruction: str, decision: str) -> dict:
    proposal = prepare_proposal(instruction)
    if decision not in {"approve", "reject"}:
        raise ValueError("Decision must be 'approve' or 'reject'.")

    write_audit({"event": "proposal_created", "proposal": proposal})
    if decision == "reject":
        result = {"status": "rejected", "message": "No action was performed."}
        write_audit({"event": "proposal_rejected", "result": result})
        return result

    message = run_mock_action(proposal)
    result = {"status": "completed", "message": message}
    write_audit({"event": "proposal_approved", "result": result})
    return result


def main() -> None:
    print("Vantage Automata — local approval demo")
    instruction = input("Enter a task instruction: ")
    try:
        proposal = prepare_proposal(instruction)
        print("\nProposed action:", proposal["proposed_action"])
        print("Risk level:", proposal["risk_level"])
        decision = input("Approve or reject? ").strip().lower()
        result = process_instruction(instruction, decision)
        print("\n", result["message"])
        print("Status:", result["status"])
        print("Audit record:", AUDIT_FILE.resolve())
    except ValueError as error:
        print("Input error:", error)


if __name__ == "__main__":
    main()
