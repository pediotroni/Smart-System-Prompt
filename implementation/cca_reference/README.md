# CCA Reference Implementation

This directory contains the first concrete implementation of the CCA Reference
Implementation boundary.

## Scope

The implementation realizes the seven established responsibilities:

1. Workspace Initialization
2. Project Registry Management
3. Active Context Management
4. Context Retrieval
5. Memory Classification and Persistence
6. Context Checkpointing
7. Validation and Consistency Checking

The core implementation has no dependency on a specific AI model, inference
engine, operating system, hardware platform, or filesystem implementation.

The InMemoryRuntimeAdapter exists only as a deterministic test adapter. It does
not establish the Phase 3 runtime adapters.

## Running the tests

From this directory:

    python -m pytest

The implementation is intentionally small. It is a reference baseline, not a
production framework or optimization target.
