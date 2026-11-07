# Vantage Automata — Initial API Contract

**Status:** Proposed contract for the first prototype. Endpoints and field names may be adjusted to match the implementation.

The backend owns the workflow state. The frontend requests changes and displays results; it does not decide whether an action is authorised.

## 1. Submit an instruction

**Endpoint:** `POST /api/tasks`

**Request**
```json
{
  "instruction": "Create a reminder to review the weekly sales report"
}
```

**Successful response — proposal created**
```json
{
  "task_id": "task_01",
  "status": "awaiting_approval",
  "proposal": {
    "task_summary": "The user wants a reminder to review the weekly sales report.",
    "proposed_action": {
      "type": "mock_action",
      "description": "Create a mock reminder for review of the weekly sales report."
    },
    "requires_approval": true,
    "risk_level": "low"
  }
}
```

The identifier above is illustrative. The application must generate a unique identifier for each real request.

**Validation behaviour**
- Empty or whitespace-only instructions return HTTP 400.
- Instructions over the configured length limit return HTTP 400.
- AI or mock-provider failures return a controlled server error.
- Invalid model output must not create an executable proposal.

## 2. Approve a proposal

**Endpoint:** `POST /api/tasks/{task_id}/approve`

**Request**
```json
{
  "decision": "approve"
}
```

**Successful response**
```json
{
  "task_id": "task_01",
  "status": "completed",
  "action_result": {
    "type": "mock_action",
    "message": "Mock action completed. No external service was changed."
  }
}
```

The backend must check that the proposal exists, is awaiting approval, has not expired and has not already been executed. It must then call only the approved mock action.

A repeated approval request must not execute the action again. Return the existing result or a suitable conflict response.

## 3. Reject a proposal

**Endpoint:** `POST /api/tasks/{task_id}/reject`

**Request**
```json
{
  "decision": "reject"
}
```

**Successful response**
```json
{
  "task_id": "task_01",
  "status": "rejected",
  "message": "The proposal was rejected. No action was executed."
}
```

A rejected proposal is terminal and cannot later be approved.

## 4. Retrieve task status

**Endpoint:** `GET /api/tasks/{task_id}`

**Successful response**
```json
{
  "task_id": "task_01",
  "status": "awaiting_approval",
  "created_at": "2026-11-07T12:00:00.000Z",
  "decision": null,
  "action_result": null
}
```

The timestamp is an example. The implementation must generate the actual timestamp.

## 5. Initial status values

| Status | Meaning |
|---|---|
| `awaiting_approval` | A valid proposal is waiting for the user. |
| `rejected` | The user rejected it; no action was run. |
| `completed` | The approved mock action completed. |
| `failed` | A permitted step failed and the failure was recorded. |
| `invalid` | The instruction or provider response did not pass validation. |

## 6. Audit record

Each task should record, at minimum:

- Task identifier.
- Original instruction.
- Validated proposal, if one was produced.
- Creation timestamp.
- User decision and decision timestamp.
- Execution status.
- Action result or error summary.

Do not store API keys, passwords or unnecessary personal information in the audit record.

## 7. Important boundary

This contract describes a proposed interface between frontend and backend. It is not evidence that these routes exist or work. Update it after implementation and testing so that it describes the actual API.
