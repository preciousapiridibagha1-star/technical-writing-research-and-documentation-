# How to Write a Useful Project README

**Document type:** Technical writing guide  
**Audience:** Contributors, maintainers and people evaluating a software project  
**Status:** General guidance; not a claim that a specific project was tested.

## Purpose

A project README is often the first document a visitor reads. It should help them understand what the project does, whether it is relevant to them and what they need to do next.

## Recommended structure

### 1. Project name and short description

Explain the purpose in one or two sentences. Avoid slogans that do not tell the reader what the project actually does.

### 2. Status

State whether the project is experimental, under active development, maintained, archived or a proposal. Do not imply production readiness without evidence.

### 3. Key capabilities

List the main functions that exist today. Separate implemented capabilities from planned features.

### 4. Prerequisites

Identify required software, versions, accounts, permissions, hardware or environment variables. Do not make the reader discover these through failed commands.

### 5. Installation or setup

Provide commands in the correct order. Explain where commands should be run and what successful completion looks like.

### 6. Configuration

Describe required settings and environment variables. Use placeholders for secrets and explain how to store credentials securely. Never publish real keys or passwords.

### 7. Usage

Show a minimal working example. Explain inputs, expected outputs and important limitations.

### 8. Testing

Explain how to run the tests and what they cover. Distinguish automated tests, manual checks and untested areas.

### 9. Troubleshooting

Include common errors, likely causes and safe steps to resolve them. Avoid speculative fixes presented as certain.

### 10. Contribution and support

Explain how to report issues, propose changes and contact maintainers, where appropriate.

### 11. Licence and acknowledgements

State the applicable licence and credit third-party work as required.

## Editorial review checklist

- Can a new reader explain the project's purpose after reading the opening?
- Is the current status honest and visible?
- Are setup steps complete and ordered?
- Are supported operating systems and versions clear?
- Are commands and file paths accurate?
- Are expected outputs described?
- Are secrets protected?
- Are limitations and known issues visible?
- Are links valid and relevant?
- Does the README match the current repository?

## Common weaknesses

| Weakness | Why it matters | Improvement |
|---|---|---|
| Vague opening | Reader cannot identify the purpose | State the problem and intended user |
| Features mixed with roadmap | Planned work appears implemented | Separate current capabilities and future plans |
| Missing prerequisites | Setup fails unexpectedly | List versions, tools and accounts first |
| Commands without context | Reader does not know where to run them | Name the terminal, directory and expected result |
| No troubleshooting | Users get stuck without guidance | Document common failures and recovery |
| Unsupported quality claims | Creates false confidence | Replace claims with verifiable status and evidence |

A good README is not simply long. It gives the right reader enough accurate information to take the next step safely.
