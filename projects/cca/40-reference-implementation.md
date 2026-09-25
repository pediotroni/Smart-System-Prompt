# CCA Reference Implementation

## Purpose

The Reference Implementation realizes the CCA architecture as executable behavior while remaining independent of any specific model, hardware, runtime, or implementation technology.

```
CCA Architecture
      |
Reference Implementation
      |
Runtime Adapter
      |
Actual Runtime / AI Model
```

## Core responsibilities

1. Workspace Initialization
2. Project Registry Management
3. Active Context Management
4. Context Retrieval
5. Memory Classification and Persistence
6. Context Checkpointing
7. Validation and Consistency Checking

Forgetting is a cross-cutting lifecycle requirement of memory handling, not a separate eighth architecture component unless implementation evidence later requires one.

## Required behavior

The implementation must preserve:

- authoritative file boundaries
- project isolation
- Minimum Sufficient Context
- selective persistence
- explicit uncertainty/error states
- runtime capability truthfulness

### Forgetting boundary

The implementation must support the architectural distinction between:

- FORGET — logical removal from normal use/retrieval within scope
- SUPPRESS — retrieval exclusion without claiming physical deletion
- DELETE — physical removal only when the runtime exposes and verifies the required capability
- ROLLBACK — restore a prior valid state
- RESTORE — explicitly recover retained state

Every operation must report an explicit result. An unavailable deletion mechanism must never be reported as successful deletion.

Forgetting must operate on authoritative records and retrieval paths rather than creating a second memory store.

Copies outside the controlled runtime remain UNKNOWN unless actually controlled and verified.

## Existing baseline

The first concrete implementation is under `implementation/cca_reference/`.

It provides the seven established responsibilities, explicit operation-result statuses, typed state, an abstract Runtime Adapter, a deterministic in-memory adapter, and focused implementation tests.

The deterministic baseline has passed in GitHub Actions.

## Current status

**Architecture:** Established  
**Implementation Boundary:** Defined  
**Reference Implementation:** Initial Concrete Baseline Constructed  
**Controlled Baseline:** PASS  
**Forgetting Semantics:** Defined; implementation pending  
**Runtime Adapter:** Phase 3  
**Behavioral Validation:** In progress

## Next step

Complete the consolidation review, then implement and test only the forgetting behavior required by the architectural contract.