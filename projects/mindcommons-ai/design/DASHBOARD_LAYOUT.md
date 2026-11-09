# Governance & Community Dashboard — Layout Concept

**Status:** Proposed screen structure only. Not a live product or evidence of an SRHIN workflow.

## Primary job of this screen

Help an authorised community steward or governance reviewer understand which proposed data uses need attention, what existing decisions and conditions apply, and what follow-up commitments are due.

The dashboard does not replace GENSCORE, Gencurate, LEWG, the Data, Ethics & Safety Monitoring Board or SRHIN's existing reporting. It is a possible interface for connecting records if a real gap is validated.

## Desktop structure

```text
┌──────────────────┬───────────────────────────────────────────────────────────────┐
│ MINDCOMMONS AI   │ Search records   Help   Notifications   Profile                │
│                  ├───────────────────────────────────────────────────────────────┤
│ Overview         │ Community stewardship                                         │
│ Data-use register│ See proposals, conditions and follow-up that need attention    │
│ New-use requests │                                                               │
│ Review workspace │ ┌─────────────────┐ ┌──────────────────┐ ┌──────────────────┐ │
│ Decision history │ │ New proposals   │ │ Reviews due      │ │ Commitments due  │ │
│ Benefit tracking │ │       06        │ │        03        │ │        04        │ │
│ Governance links │ └─────────────────┘ └──────────────────┘ └──────────────────┘ │
│                  │                                                               │
│                  │ REQUESTS NEEDING ATTENTION                                    │
│                  │ ┌──────────────────────────────────────────┬───────────────┐  │
│                  │ │ Proposal / purpose / submitted           │ Status        │  │
│                  │ │ New research use — synthetic example     │ Needs review  │  │
│                  │ │ Changed collaborator — synthetic example │ More info     │  │
│                  │ │ AI model evaluation — synthetic example  │ Routed        │  │
│                  │ └──────────────────────────────────────────┴───────────────┘  │
│                  │                                                               │
│                  │ GOVERNANCE CONDITIONS             COMMUNITY BENEFITS          │
│                  │ • Condition due for review        • Commitment / owner         │
│                  │ • Reviewer assigned                • Progress / next update    │
│                  │                                                               │
│                  │                                   ┌─────────────────────────┐ │
│                  │                                   │ MINDCOMMONS AI ASSISTANT│ │
│                  │                                   │ Ask about a rule,       │ │
│                  │                                   │ decision or request.   │ │
│                  │                                   │                         │ │
│                  │                                   │ “Summarise the approved │ │
│                  │                                   │ conditions for this     │ │
│                  │                                   │ proposal and show the   │ │
│                  │                                   │ source records.”        │ │
│                  │                                   │ [Ask a question...]     │ │
│                  │                                   └─────────────────────────┘ │
└──────────────────┴───────────────────────────────────────────────────────────────┘
```

All names, counts and request examples in any visual mockup must be clearly synthetic placeholders. Do not show real participant data.

## Main areas

1. **Data-use register:** approved purposes, conditions, decision authority, status, review date and source-record link.
2. **New-use requests:** new or changed purposes, collaborators, model-training/evaluation or commercial-use proposals.
3. **Review workspace:** applicable conditions, missing evidence, routing and human decision record.
4. **Decision history:** decision, rationale, conditions, reviewer authority and review date.
5. **Benefit tracking:** community-defined commitments, owner, progress and evidence of delivery.
6. **Governance links:** authoritative charter, SOP, ethics approval or community decision source.

## AI assistant behaviour

The assistant is visible in the workspace and can:
- Explain the current governance rule using the linked approved source.
- Summarise a proposal and identify missing information.
- Compare the proposal with documented conditions.
- Show why it flagged an issue and link to the underlying record.
- Summarise due follow-up and benefit commitments for authorised users.

It must not create a new rule, make an approval, or reveal restricted records. If source records are missing or contradictory, it says so and routes the question to an authorised human.

## Visual design direction

- Desktop-first, responsive, calm and professional.
- Warm off-white canvas, deep navy typography, forest-teal primary actions and a restrained violet accent for AI.
- Clear status chips and generous whitespace.
- The request queue is the main focus; analytics are secondary.
- The AI panel is prominent but does not dominate the workflow.
- Every consequential item links to its source record.
- Mobile layout stacks cards and turns the AI panel into a slide-up drawer.

## Important limitation

This is a design hypothesis for a possible stewardship workflow. The exact information, roles, labels and screen structure must change if SRHIN's existing process or community preferences differ.
