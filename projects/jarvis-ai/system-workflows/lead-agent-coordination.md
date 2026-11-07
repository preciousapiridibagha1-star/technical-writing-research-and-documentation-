# Jarvis AI — Lead-Agent Coordination Workflow

**Status:** Proposed operating workflow; not implemented or tested.

## Objective

Describe how an owner-approved business goal could be translated into bounded specialist tasks, reviewed and returned to the owner.

## Workflow

1. **Owner defines the goal.** The owner supplies the desired outcome, constraints, priority and any relevant context.
2. **Lead agent checks the brief.** It identifies missing information, ambiguity, conflicting instructions and tasks that require a human decision.
3. **Plan is proposed.** The lead agent divides the goal into smaller tasks and identifies the proposed specialist role for each.
4. **Owner reviews the plan where required.** Work with material cost, customer impact, sensitive data or external consequences requires explicit approval before proceeding.
5. **Specialists complete bounded tasks.** Each specialist receives only the information and permissions needed for its assigned task.
6. **Outputs are checked.** The lead agent checks completeness, consistency, source quality and whether the output meets the task brief.
7. **Exceptions are escalated.** Unclear, conflicting, sensitive or low-confidence work returns to the owner or an authorised staff member.
8. **Results are consolidated.** The lead agent prepares a concise report showing completed work, outstanding items, uncertainties and decisions needed.
9. **Owner decides next steps.** The owner retains authority over business priorities and consequential actions.

## Responsibility boundaries

| Activity | Lead agent | Specialist agent | Human owner/staff |
|---|---|---|---|
| Interpret approved goal | Coordinate | No | Set direction and clarify |
| Break work into tasks | Propose | No | Review when required |
| Complete specialist task | Coordinate | Perform bounded task | Supervise |
| Verify evidence and completeness | Review and flag | Provide sources/output | Resolve material uncertainty |
| Approve consequential action | No | No | Yes |
| Change agent permissions | No | No | Authorised administrator |
| Handle sensitive exception | Escalate | Stop and escalate | Decide |

## Failure and escalation conditions

The proposed workflow should stop or request human input when:
- The goal is ambiguous or internally inconsistent.
- Required information is unavailable.
- A specialist returns unsupported claims or conflicting results.
- The task exceeds its assigned permissions.
- The action may affect money, legal obligations, employment, customer rights or sensitive personal information.
- The system cannot establish whether an action has already occurred.

## Evidence required before claiming implementation

A future implementation should be demonstrated with a traceable task showing the original goal, task decomposition, specialist inputs and outputs, review decisions, escalations and final owner-facing report. A diagram or written workflow alone does not demonstrate that agent coordination works.
