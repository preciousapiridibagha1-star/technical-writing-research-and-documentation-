# 6. Project & Programme Delivery

## Evidence project: Planning a safe first Vantage Automata MVP

**Status:** Delivery plan documented; implementation and delivery outcomes not yet verified.  
**Purpose:** Demonstrate how a broad idea can be reduced to a manageable, reviewable project.

### Delivery objective

Produce a small demo that shows one complete journey: instruction → proposal → validation → human decision → mock action → audit record.

### Scope

**Included**
- One low-risk task type.
- Simple input interface.
- Structured proposal.
- Backend validation.
- Approve/reject decision.
- Mock action handler.
- Audit record.
- Basic automated tests.

**Excluded**
- Real customer records.
- Payments or financial actions.
- Sending external messages.
- Third-party integrations.
- Multi-user permissions.
- Autonomous execution.
- Production deployment.

### Milestones and acceptance evidence

| Milestone | Work | Evidence required |
|---|---|---|
| 1. Confirm scope | Select one task and define allowed outcomes | Approved one-page scope |
| 2. Design | Map screens, data fields and approval rules | Workflow and interface notes |
| 3. Build core flow | Implement input, proposal and validation | Source code and local demonstration |
| 4. Add controls | Implement approval, rejection and audit record | Recorded behaviour for both decisions |
| 5. Test | Check valid, invalid, rejected, approved and failed cases | Test output and issue log |
| 6. Review | Fix defects and document limitations | Review notes and updated README |

### Risks and responses

| Risk | Response |
|---|---|
| Scope expands into a general automation platform | Keep one task type and maintain an explicit exclusions list |
| AI returns malformed or unsafe output | Validate on the application side and fail closed |
| Approval applies to changed content | Bind approval to the exact proposal version |
| The same action runs twice | Add duplicate-execution protection |
| A mock action is mistaken for a real integration | Label the demo clearly and keep the mock handler isolated |
| A test is described as passed without evidence | Record actual test output before changing status |

### Before → after

**Before:** “Build Vantage Automata with AI agents and business integrations.” This is too broad to estimate, test or deliver as a first milestone.

**After:** “Build one local, low-risk approval journey using mock data. Demonstrate proposal validation, explicit approval/rejection, a harmless mock action and an audit record. Do not add external integrations.” The revised objective has observable acceptance evidence and a manageable boundary.

### Project controls

- Maintain a short decision log for changes to scope or architecture.
- Track risks and unresolved assumptions.
- Review progress against acceptance evidence, not activity alone.
- Record defects and decisions.
- Do not mark a milestone complete until its evidence exists.
- Keep a clear distinction between planned, in-progress, tested and released work.

### Programme delivery connection

The same approach can support a learning or fellowship project: define the intended outcome, identify the people served, break work into deliverables, schedule realistic milestones, track dependencies and risks, and report results honestly. The portfolio's fellowship mapping is planning evidence; it is not evidence that an application was submitted or a programme delivered.

### Current result and next proof

The current achievement is a defined, bounded delivery plan supported by requirements, workflows and test design. A completed delivery case study will require source code, test results, a demonstration, a short issue/fix record and a reflection on what changed during implementation.
