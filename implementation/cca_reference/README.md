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

## Controlled baseline

`test_baseline.py` exercises one coherent path through all seven responsibilities
and checks capability truthfulness, project resolution, active-context activation,
selective retrieval, memory persistence and duplicate detection, checkpoint
creation, and validation of valid and invalid active-project state.

The runner uses only the Python standard library.

From this directory:

    python test_baseline.py

Expected result:

    CCA Reference Baseline: PASS

A PASS from this deterministic runner establishes only implementation-level
baseline behavior. It is not real-model behavioral validation.

The implementation is intentionally small. It is a reference baseline, not a
production framework or optimization target.
