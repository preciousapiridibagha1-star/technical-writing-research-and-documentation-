# Contributing to CORA AI

Thank you for considering a contribution. CORA AI is an early open-source
prototype exploring purpose-specific consent, deterministic data-use permission
checks and an inspectable audit history.

## Before you start

- Read the project [README](README.md), product definition and MVP scope.
- Review the implementation limitations. This project is not production-ready.
- Use fictional identifiers and synthetic data only. Never submit real health,
  participant or other sensitive personal data in issues, pull requests or tests.
- Open an issue before beginning a substantial change so the scope can be agreed.

## Useful first contributions

- Improve the browser interface's accessibility and mobile usability.
- Add tests for API edge cases without weakening default-deny behaviour.
- Propose and review a SQLite persistence design.
- Improve setup instructions and user-facing explanations.
- Review the consent and audit model and document assumptions or risks.

## Development setup

From `projects/cora-ai/implementation/api`:

```bash
python -m venv .venv
pip install -r requirements.txt
uvicorn app:app --reload
```

Open `http://127.0.0.1:8000/`. Run API tests with `pytest -v` from the
same directory. Run consent-engine tests with `python -m unittest -v` from
`projects/cora-ai/implementation`.

## Contribution expectations

- Keep changes focused and explain the problem they solve.
- Add or update tests for changed behaviour.
- Preserve exact-purpose matching and default-deny permission decisions.
- Never let an AI assistant grant consent, change a participant's choice,
  approve access or override a backend denial.
- Document security, privacy and data-retention implications.
- Do not claim production readiness, legal compliance, host endorsement or
  real-world deployment without independent evidence.

Contributions are reviewed before merging. Opening a pull request does not
guarantee acceptance. The maintainers may request changes or clarification.

## Current project status

The browser workspace is an early synthetic demo. It currently uses
in-memory state, has no authentication and is not connected to real datasets.
Persistent storage, security controls, independent privacy/security review and
community co-design remain future work.
