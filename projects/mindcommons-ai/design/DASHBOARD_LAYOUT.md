# Main Dashboard Layout

This is a proposed layout for the MindCommons AI web application. It is a structural wireframe, not a screenshot or a final visual design.

## Desktop dashboard concept

```text
┌──────────────────────┬─────────────────────────────────────────────────────────────┐
│ MINDCOMMONS AI       │  Search / Notifications / Profile                          │
│                      ├─────────────────────────────────────────────────────────────┤
│  Overview            │  Good morning, [Name]                                       │
│  My Permissions      │  Your workspace at a glance                                 │
│  Data-use Requests   │                                                             │
│  Review Queue        │  ┌────────────────┐ ┌────────────────┐ ┌──────────────────┐  │
│  Community Rules     │  │ Pending tasks  │ │ Recent activity│ │ Benefit progress │  │
│  Transparency        │  │       04       │ │       12       │ │       68%        │  │
│  Community Benefits  │  └────────────────┘ └────────────────┘ └──────────────────┘  │
│                      │                                                             │
│  ──────────────────  │  YOUR WORKSPACE                                             │
│  Help & Support      │  ┌──────────────────────────────────┐ ┌──────────────────┐ │
│  Settings            │  │                                  │ │ ASK MINDCOMMONS  │ │
│                      │  │  Main role-specific content      │ │ AI               │ │
│                      │  │                                  │ │                  │ │
│                      │  │  • Requests / permissions        │ │ "What can I help │ │
│                      │  │  • Status and next steps         │ │  you understand  │ │
│                      │  │  • Review or action buttons      │ │  today?"         │ │
│                      │  │  • Recent records                │ │                  │ │
│                      │  │                                  │ │ [Ask a question] │ │
│                      │  └──────────────────────────────────┘ └──────────────────┘ │
│                      │                                                             │
└──────────────────────┴─────────────────────────────────────────────────────────────┘
```

## How the layout changes by role

The shell stays consistent, but the menu, cards and main content change according to the signed-in user's role.

| Role | Main dashboard content |
|---|---|
| Participant | My permissions, what each choice means, updates and support |
| Researcher | Draft requests, submitted requests, missing information and request status |
| Governance reviewer | Pending reviews, flagged issues, decisions awaiting action and review history |
| Community representative | Community rules, oversight activity, benefit commitments and progress |
| Administrator | User and role management, system status and configuration |

## AI assistant placement

The AI assistant appears as a side panel on desktop and a slide-up panel on mobile. It understands the current page and the user's role, but it can only retrieve information that the user is authorised to see.

The assistant should show when it is summarising information, provide links to the underlying record where permitted, and clearly state when it cannot answer.

## Design rules

- Keep the left navigation short and role-specific.
- Use three or four useful summary cards at most.
- Keep the main task area more prominent than analytics.
- Make the AI assistant easy to reach but never force users to chat to complete essential tasks.
- Use plain labels and readable status text.
- On mobile, collapse the navigation and open the AI assistant as a panel.
- Do not display identifiable participant health information on public-facing screens.

## Next design output

A high-fidelity visual mockup should be created from this wireframe after the product roles and MVP scope have been reviewed. The first screen to visualise should be the Governance & Community Workspace, followed by the Participant Centre.
