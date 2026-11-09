# System Architecture — Community Data-Use Accountability Ledger

**Status:** Proposed logical architecture only. No stack, integration or deployment selected.

## 1. Architectural principle

A thin accountability layer that references existing authoritative records. It should not replace Gencurate, consent systems, LEWG, ethics oversight, governance charters or existing reporting.

## 2. Three capabilities

1. Approved-use record.
2. Change-of-use review.
3. Community-obligation follow-up.

## 3. Logical architecture

```mermaid
flowchart TB
  CS[Authorised community stewards]
  RV[Authorised governance reviewers]
  RS[Researchers]

  subgraph UI[Focused accountability workspace]
    USE[Approved-use records]
    CHANGE[Change-of-use request and review]
    OBL[Community-obligation follow-up]
    AI[Contextual AI assistant]
  end

  subgraph APP[Application controls]
    AUTH[Role and record permissions]
    FLOW[Request routing and human decision workflow]
    RULE[Approved conditions and checklist references]
    AUDIT[Decision and change history]
    MIN[Data minimisation and privacy filters]
  end

  MODEL[AI assistance service]
  SOURCE[Approved source records and documents]

  subgraph EXIST[Existing authoritative SRHIN records / systems]
    GEN[Gencurate / consent references]
    GOV[LEWG and authorised governance decisions]
    ETH[Ethics approvals, charters and SOPs]
    AGREEMENTS[Community-agreed commitments]
  end

  CS --> USE
  CS --> OBL
  RS --> CHANGE
  RV --> CHANGE
  USE --> AUTH
  CHANGE --> AUTH
  OBL --> AUTH
  CHANGE --> FLOW
  FLOW --> RULE
  FLOW --> AUDIT
  AI --> MODEL
  MODEL --> SOURCE
  MODEL --> MIN
  MIN --> AUTH
  SOURCE -. approved references only .-> GEN
  SOURCE -. approved decision references .-> GOV
  SOURCE -. approved policy references .-> ETH
  SOURCE -. authorised commitment references .-> AGREEMENTS
```

## 4. Data minimisation

The ledger should hold only the minimum metadata needed to connect an approved use, its conditions, a change request and agreed commitments. It should not store raw voice recordings, transcripts, diagnoses, participant identities or copies of sensitive datasets. The source system remains authoritative.

## 5. AI boundary

The application checks permissions first. AI receives only the permitted records needed for the current task.

AI may explain source material, help complete a request, flag missing fields, compare a proposal with structured approved conditions and prepare summaries. It may not approve, deny, grant access, modify consent, create policy or determine benefit fairness.

## 6. Example sequence

```mermaid
sequenceDiagram
  participant Researcher
  participant App as Accountability Ledger
  participant AI as AI Assistant
  participant Reviewer as Authorised Human Reviewer
  participant Steward as Community Steward

  Researcher->>App: Submit proposed change to approved use
  App->>App: Check role and required fields
  App->>AI: Prepare summary using permitted records
  AI-->>App: Summary, missing fields, source-linked flags
  App->>Reviewer: Route to authority defined by approved rules
  Reviewer->>App: Record human decision and conditions
  App->>App: Update use record and audit history
  App-->>Steward: Show authorised decision and follow-up
  App->>App: Track agreed community commitments
```

## 7. Integration assumptions

No API, database, SSO, Gencurate connection or data export is assumed. A manual source reference may be safer and sufficient. Integration is considered only after SRHIN confirms need, permission, technical feasibility, ownership and security requirements.

## 8. Non-functional requirements to validate

Role-based access, audit logging, encryption, retention and deletion rules, low-bandwidth access, accessible plain-language content, backup/recovery, data residency and applicable legal/ethics requirements must be defined with SRHIN specialists. This document does not claim compliance or certification.

## 9. Status

This is a logical design hypothesis, not an implementation. No prototype is being built at this stage.
