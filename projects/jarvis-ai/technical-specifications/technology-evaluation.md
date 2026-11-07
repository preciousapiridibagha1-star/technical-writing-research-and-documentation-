# Jarvis AI — Technology Evaluation Framework

**Status:** Evaluation framework for proposed technologies; no component is confirmed as integrated.

## Purpose

The architecture outline names Open WebUI, CrewAI, n8n, PostgreSQL and Ollama. This document defines how those and alternative technologies should be assessed before any implementation decision.

## Proposed component roles to investigate

| Component | Possible role in the proposed system | Questions to validate |
|---|---|---|
| Open WebUI | User-facing interface for interacting with model services | Does it meet the required user experience, authentication, access-control and deployment needs? |
| CrewAI | Framework for defining and coordinating agent tasks | Is multi-agent coordination necessary? How are tools, permissions, state and failures controlled? |
| n8n | Workflow automation and service orchestration | Which integrations are supported? How are credentials, retries, approvals and execution logs managed? |
| PostgreSQL | Relational data storage | What data model, access controls, backup, retention and hosting approach are required? |
| Ollama | Local model serving and experimentation | Which models fit the task, hardware, quality, latency and privacy requirements? |

These are candidate roles for research, not validated claims about compatibility or suitability in a particular deployment.

## Evaluation criteria

Score each candidate against the actual project requirements:

1. **Functional fit:** Does it perform the required responsibility?
2. **Integration fit:** Can it communicate reliably with the other selected components?
3. **Security:** How are identity, permissions, secrets and data protected?
4. **Privacy and data control:** Where is information processed and stored? What leaves the environment?
5. **Reliability:** What happens during outages, timeouts, retries and partial failures?
6. **Observability:** Can operators inspect activity, errors and decisions?
7. **Cost:** What are hosting, usage, maintenance and scaling costs?
8. **Maintainability:** Can the team understand, update and support it?
9. **Portability:** How difficult would it be to replace the component?
10. **Human oversight:** Can the design preserve approval, escalation and override?

## Selection method

- Write the requirement before selecting the tool.
- Identify at least one credible alternative.
- Consult current official documentation.
- Build a small proof of concept only where it answers a specific uncertainty.
- Record the result, limitations and date reviewed.
- Do not infer integration from the fact that two products have APIs or appear in the same diagram.

## Initial conclusion

The current stack is a hypothesis, not a final architecture. The appropriate components cannot be selected responsibly until a specific MVP workflow, data boundary, operating environment and implementation capacity are defined.
