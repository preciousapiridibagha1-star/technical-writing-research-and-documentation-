# FAQ: Understanding an AI-Assisted Task Approval System

**Document type:** Illustrative FAQ sample  
**Audience:** People evaluating a proposed AI-assisted task workflow  
**Status:** Explains a concept, not a currently available product.

## What is an AI-assisted task approval system?
It is a proposed workflow in which AI interprets a user's instruction and prepares a suggested action. The user reviews the suggestion and decides whether it may proceed.

## Does submitting an instruction mean the system can act immediately?
No. Submitting an instruction asks the system to prepare a proposal. It does not authorise execution. Approval must be a separate, explicit decision.

## What happens if the AI misunderstands the instruction?
The user should be able to reject the proposal. The system should stop without executing the proposed action. Invalid or incomplete AI output should also be blocked before it is presented as an approval-ready proposal.

## Why is human approval important?
It gives the user an opportunity to check what the system understood and what it intends to do. It is particularly important where an action could affect people, money, customer information or external services.

## What happens if I reject a proposal?
The workflow should record the rejection and stop. A rejected proposal should not later be executed through a repeated or delayed request.

## What is a mock action?
A mock action simulates an operation without changing a real external service. It allows developers to test the workflow before introducing real-world effects.

## Does approval mean the system can perform any related action?
No. Approval should apply only to the specific action described in the proposal. A materially changed proposal should require a new review and approval.

## What if the system receives the approval request twice?
The backend should check the task's current state and prevent duplicate execution. This behaviour must be tested, not merely assumed.

## Does this concept guarantee that AI will be accurate?
No. AI systems can misunderstand instructions or produce incorrect information. The proposed design includes validation, human review, error handling and limits, but those controls must be implemented and evaluated.

## Is this concept currently a deployed product?
No. This FAQ describes a proposed system design. It is not a user manual for a live service and does not claim that a working implementation is available.
