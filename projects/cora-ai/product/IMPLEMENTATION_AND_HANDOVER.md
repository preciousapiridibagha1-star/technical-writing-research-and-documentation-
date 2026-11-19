# CORA AI — Implementation and Handover Plan

## 1. Delivery target

Deliver a working local synthetic-data demonstrator by 28 November 2026. The target is a small, testable MVP—not a production health-data service.

## 2. Build stages

### Stage 1 — Freeze the rules
Define the purpose keys, consent statuses, participant/resource references, role boundaries and default-deny behaviour. Keep the first demo purposes to research and AI model training.

### Stage 2 — Build the backend first
Create the consent record operations, withdrawal operation, permission-check service and audit event recording. Do not start with a complex user interface.

### Stage 3 — Prove the rules with tests
Test grant, refusal, withdrawal, exact-purpose matching, missing consent, access denial and audit history. The permission service must not depend on the AI model.

### Stage 4 — Build the simple web interface
Create participant consent, consent status, access request, decision result and administrator audit screens. Keep the layout plain and usable.

### Stage 5 — Add the AI assistant
Connect one configurable model provider through a server-side adapter. Give it only approved tools. Do not expose database credentials or unrestricted write operations. Confirm the core application works with AI disabled.

### Stage 6 — Demonstrate and document
Run the complete synthetic scenario. Record test results. Publish local setup, environment configuration, API examples, known limitations and handover instructions.

## 3. Proposed implementation stack

- React for the web interface.
- Python and FastAPI for the backend and REST API.
- SQLite for the local demonstrator.
- pytest for backend tests.
- One configurable AI provider through a server-side adapter.
- Environment variables for local configuration; secrets must not be committed.

This is a proposed stack. The final implementation may change if a technical reviewer identifies a simpler, safer option.

## 4. Work ownership

The product lead defines the problem, user journeys, consent rules, acceptance criteria, documentation and scope boundaries. AI coding tools may assist with drafting code and tests, but generated code must be reviewed.

A technically experienced collaborator or reviewer is needed to verify backend implementation, access-control boundaries, AI tool permissions, deployment readiness and security assumptions. The product lead should not claim to be the sole production engineer.

## 5. Definition of handover

The handover package includes:
- Source code and repository history.
- Installation and local-run instructions.
- Synthetic demonstration data.
- Automated tests and test instructions.
- API route and schema documentation.
- AI provider configuration instructions.
- Architecture and security-boundary explanation.
- Known limitations and production-readiness checklist.
- Licence file and third-party dependency notices.

## 6. Production boundary

The MVP is not approved for real participant or mental-health data. Production use requires the adopting organisation to provide and maintain authentication, authorisation, secure infrastructure, secret management, encryption, database hardening, backups, monitoring, incident response, retention/deletion processes and independent security/privacy review.

The API is an integration point, not automatic integration. A developer at the adopting organisation must connect the API to its identity system and ensure every relevant data-release path checks permission.

## 7. Sustainability, adoption and continuity

CORA AI will be delivered as a usable, documented open-source application that another organisation or developer can run, inspect, adapt and integrate into an existing system.

During the Fellowship, the Fellow is responsible for leading the project, delivering the agreed milestones, documenting decisions and working with the host and affected communities to refine the project. The handover package will make the software understandable and transferable beyond the Fellowship period.

The project will document how an adopting organisation can assign a maintainer, run the application, review and update the code, and connect the API to its own systems. The Fellow will make the code and non-confidential project materials openly available under the licence agreed with Mozilla.

This MVP does not assume that the Fellow personally operates a permanent hosted service or independently provides indefinite maintenance after the Fellowship. Long-term hosting, operational support and future extensions should have an identified owner in the adopting organisation or a community of maintainers. The project’s sustainability and post-Fellowship pathway will be discussed with the host and refined during the Fellowship, rather than treated as a reason to stop delivering or supporting the work during the grant period.

## 8. Release checklist


- [ ] All three MVP capabilities implemented.
- [ ] Synthetic end-to-end workflow demonstrated.
- [ ] Automated tests pass.
- [ ] AI assistant uses only allow-listed tools.
- [ ] AI cannot override permission decisions.
- [ ] Core functions work without AI.
- [ ] No secrets or real personal data committed.
- [ ] README and API documentation are complete.
- [ ] Licence and dependency notices are present.
- [ ] Limitations and handover responsibilities are explicit.
