# 5. Technical Writing & Documentation

## Evidence: Turning a broad system idea into usable documentation

**Status:** Existing writing samples retained; this page demonstrates the editorial approach using the Vantage Automata concept.

### Before → after: project description

**Before**

“Vantage Automata is an AI-powered platform that automates tasks for businesses and individuals.”

Problems:
- “AI-powered” does not explain what the system does.
- “Automates tasks” suggests broad capabilities that have not been built.
- The user, workflow and approval boundary are unclear.
- The sentence may imply a finished product.

**After**

“Vantage Automata is a proposed task-approval system. It turns a user's instruction into a structured action proposal, checks that proposal against defined rules, and asks the user to approve or reject it. The first planned demo uses mock data and does not connect to external services.”

Why the revision is better:
- It names the system's purpose.
- It explains the workflow in ordinary language.
- It identifies the user's role.
- It states the implementation boundary.
- It avoids claiming features that have not been verified.

### Before → after: instructions

**Before:** “Submit the task and approve it.”

**After:**
1. Enter one task in the instruction box.
2. Select **Prepare proposal**.
3. Review the proposed action and the information it will use.
4. Select **Approve** to run the mock action, or **Reject** to stop it.
5. Check the result and audit record.

The improved version tells the reader what to do, what to expect and how to stop the process. It is still illustrative documentation; it should only be published as an operational user guide after the interface and behaviour have been tested.

### Documentation principles used

- Write for the reader's task, not the writer's knowledge.
- Explain unfamiliar terms when they first appear.
- Use headings that help readers find answers.
- Put prerequisites and warnings before the relevant steps.
- Keep one instruction to one clear action where possible.
- Use examples that match the actual system.
- Label conceptual examples and untested instructions.
- Review links, screenshots, version details and terminology.

### Existing portfolio samples

The repository retains the software overview, FAQ, user guide, README-writing guide, before-and-after example and documentation review checklist. They should be read as samples for the proposed Vantage workflow unless a document explicitly names another verified product.

### Quality check

Before publishing a guide, confirm:
- The product and version are identified.
- Every step can be followed in the current interface.
- Expected results and error paths are explained.
- Permissions and data handling are accurate.
- Screenshots match the described version.
- A second reader can complete the task without undocumented help.

### What this demonstrates

The before-and-after examples show the ability to remove vague claims, make instructions actionable and align documentation with the actual evidence. No untested guide is represented as a verified product manual.
