# Vantage Automata — User Guide Sample

**Document type:** Illustrative user guide  
**Product status:** Vantage Automata is a concept. This guide explains the proposed experience; it is not instructions for a live application.

## What this guide covers

This sample explains how a person would submit a task, review an AI-prepared suggestion and decide whether to approve or reject it.

## Before you begin

In a future test version, you would need:

- Access to the Vantage test application.
- A task that can safely be represented with sample data.
- No real payment, customer message or account change in the task.

Do not enter passwords, bank details or private customer information into a demonstration.

## 1. Enter a task

1. Open the task input screen.
2. Describe what you want the system to prepare.
3. Include important details, such as the intended result and any limits.
4. Select the option to prepare a proposal.

**Example:** "Prepare a reminder for the team to review the weekly stock report tomorrow. Do not send any message."

The system should check the instruction before asking AI to prepare a proposal.

## 2. Review the proposed action

When the proposal is ready, read it carefully.

Check:
- Does it match what you asked for?
- Are the details correct?
- Is the action within the system's permitted scope?
- Does it include anything you did not request?

Do not approve a proposal just because it sounds confident.

## 3. Approve or reject

- Choose **Approve** only when the proposal is correct and safe for the test.
- Choose **Reject** if it is wrong, unclear or outside the agreed scope.

A rejection should stop that proposed action. It should not silently continue in the background.

## 4. Check the result

After a decision, the proposed application should show the outcome.

For a safe demonstration, approval should trigger only a mock action, such as adding a sample item to a test list. It should not send a real message or change a real account.

## If something does not look right

- **The proposal is unclear:** reject it and write a clearer instruction.
- **The proposal contains details you did not provide:** do not approve it.
- **The system shows an error:** stop and report the error to the person responsible for the test.
- **The action appears to affect a real service:** do not continue; the test setup should be reviewed.

## What approval means

Approval applies only to the specific proposal shown for review. It does not give the system permission to perform other tasks or take future actions.

## Current limitations

Vantage Automata is not currently available as a verified working product. The steps above describe the intended user experience. They have not been tested in a live application.
