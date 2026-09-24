# CCA Reference Implementation

## Purpose

This document defines the boundary and structural responsibilities of the CCA Reference Implementation.

The Reference Implementation realizes the established CCA architecture as executable behavior while preserving the architecture's model, hardware, runtime, and implementation independence.

It is not a replacement for the CCA architecture.

## Implementation Boundary

The Reference Implementation operates between the CCA architectural definitions and a concrete runtime environment.

```text
CCA Architecture
      |
      v
Reference Implementation
      |
      v
Runtime Adapter
      |
      v
Actual Runtime / AI Model
```

The Reference Implementation must not require a specific:

* AI model
* model family
* model size
* inference engine
* hardware platform
* operating system
* programming language
* runtime environment

Runtime-specific behavior belongs to the Runtime Adapter layer.

## Core Responsibilities

The Reference Implementation realizes:

1. Workspace Initialization
2. Project Registry Management
3. Active Context Management
4. Context Retrieval
5. Memory Classification and Persistence
6. Context Checkpointing
7. Validation and Consistency Checking

These responsibilities correspond to the components established during the Reference CCA component definition phase.

## Concrete Baseline

The first concrete baseline is located under `implementation/cca_reference/`.

It provides:

- a runtime-independent composition root
- concrete implementations of the seven established responsibilities
- explicit operation-result statuses
- typed project, active-context, memory, and checkpoint state
- an abstract Runtime Adapter boundary
- a deterministic in-memory adapter for implementation-level testing
- focused tests for selective retrieval, project resolution, memory deduplication, and validation

The baseline intentionally does not implement Phase 3 runtime adapters.

## Authority Boundaries

The Reference Implementation must preserve the authority defined by the CCA file contracts.

Authoritative information must remain in its designated location.

Implementation components must not create competing authoritative copies of:

* system rules
* runtime state
* capabilities
* project registry
* active context
* project state
* decisions
* findings
* TODO items
* user continuity

## Runtime Separation

The Reference Implementation must not assume that a capability exists merely because the architecture refers to it.

Actual capabilities must be established by the Runtime Adapter or another verified runtime mechanism.

Examples include:

* filesystem access
* file modification
* command execution
* web access
* external tools
* model invocation

A declared path or configuration value does not itself establish capability.

## Project Isolation

Project-local state must remain isolated according to the project registry and project-switching protocol.

Switching the active project must not silently modify or merge unrelated project state.

## Selective Retrieval

The Reference Implementation must apply the Minimum Sufficient Context principle.

Available information must not be loaded merely because it exists.

Retrieval should proceed according to task relevance and the established Reading Protocol.

## Selective Persistence

The Reference Implementation must apply the Memory Write Protocol.

Conversation content must not be persisted as a transcript dump.

Persistent information must be classified and written only when its continuity value and authority are sufficiently established.

## Error and Uncertainty Handling

The Reference Implementation must distinguish between:

* unavailable capability
* unknown runtime state
* missing information
* conflicting information
* invalid state
* implementation failure
* model capability limitation

It must not silently convert uncertainty into fact.

## Validation Boundary

The Reference Implementation must be testable independently of any single model or runtime.

Behavioral testing shall later determine whether the implementation correctly realizes the architecture.

Observed model limitations must not automatically be treated as architectural defects.

## Deferred Concerns

The following remain open and are not yet defined as independent implementation components:

* rule and instruction precedence
* loop and termination control
* archived-project retrieval semantics
* global versus project-local activity history
* long-term role of `94-user-notes.md`

These concerns shall be resolved only when sufficient evidence exists.

## Current Status

**Architecture:** Established  
**Implementation Boundary:** Defined  
**Reference Implementation:** Initial Concrete Baseline Constructed  
**Runtime Adapter:** Phase 3; Not Started  
**Behavioral Validation:** Not Started

## Next Step

Establish a controlled testable baseline and validate the implementation before introducing further architectural elements.
