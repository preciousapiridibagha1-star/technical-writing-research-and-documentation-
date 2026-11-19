# CORA AI — Screen Layout

**Status:** Functional layout specification for the locked MVP.

## Navigation
- Home
- Participant consent
- Access request
- Audit history
- AI assistant

Role-based visibility determines which screens and records a user can access.

## Participant consent screen
Show one purpose per section, with a plain-language explanation and the current status. Provide explicit grant, refuse and withdraw actions. Do not preselect a choice or use the AI assistant to make the choice.

## Consent status
Show each purpose separately, its current status, the consent-text version and the date of the latest decision.

## Access request screen
Allow the requester to select a synthetic participant/resource and one exact purpose. The backend performs the check. The interface must not make the decision in browser code.

## Decision result
Display ALLOW or DENY, the reason returned by the permission service and the request reference. The AI assistant may explain the reason but cannot change it.

## Audit history
Show event type, timestamp, purpose, pseudonymous reference, actor/service and result. Only authorised administrators can inspect this screen.

## AI assistant placement
A persistent but compact assistant panel or expandable drawer. Suggested prompts include:
- Explain what research consent means.
- Help me understand my current consent status.
- Check whether this request has all required information.
- Explain why this access request was denied.

## Visual direction
Keep the interface clean, accessible and uncluttered. The product is a small utility, not an analytics dashboard. Use synthetic data only in screenshots and mockups.

## Privacy and access
Do not display real participant names, clinical information, recordings or identifiable data. Enforce screen and record permissions on the backend, not only by hiding interface elements.
