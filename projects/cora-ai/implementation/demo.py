"""Run the CORA AI synthetic consent demonstration."""
import json

from consent_engine import ConsentEngine


def main():
    cora = ConsentEngine()
    participant = "P001"
    resource = "D001"

    print("\n1. Grant research consent")
    print(cora.record_consent(participant, resource, "research", "grant"))

    print("\n2. Refuse model-training consent")
    print(cora.record_consent(participant, resource, "model_training", "refuse"))

    print("\n3. Check research access (expected ALLOW)")
    print(json.dumps(cora.check_permission(participant, resource, "research"), indent=2))

    print("\n4. Check model-training access (expected DENY)")
    print(json.dumps(cora.check_permission(participant, resource, "model_training"), indent=2))

    print("\n5. Withdraw research consent")
    print(cora.record_consent(participant, resource, "research", "withdraw"))

    print("\n6. Check research access again (expected DENY)")
    print(json.dumps(cora.check_permission(participant, resource, "research"), indent=2))

    print("\n7. Audit history")
    print(json.dumps(cora.get_audit_history(), indent=2))


if __name__ == "__main__":
    main()
