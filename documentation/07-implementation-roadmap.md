# Implementation Roadmap

## Phase 1 — Architecture baseline

- [x] Core identity
- [x] File contracts
- [x] Reading protocol
- [x] Memory write and forgetting protocol
- [x] Bootstrap protocol
- [x] Project switching protocol
- [x] Context checkpoint protocol

## Phase 2 — Reference implementation

- [x] Workspace initialization
- [x] Project registry
- [x] Active-context projection
- [x] Retrieval engine
- [x] Memory classification/write engine
- [x] Checkpoint engine
- [x] Validation and consistency checks
- [ ] Forgetting semantics implementation

The initial concrete baseline is under `implementation/cca_reference/`.

The deterministic controlled baseline has passed in GitHub Actions.

## Phase 3 — Runtime adapters

- [ ] Filesystem
- [ ] Shell
- [ ] Web/tools
- [ ] llama.cpp adapter (optional)

A concrete adapter is required for real-model behavioral testing.

## Phase 4 — Validation

- [ ] Returning-run continuity
- [ ] Selective retrieval
- [ ] Multi-project isolation
- [ ] Memory classification/deduplication
- [ ] Context checkpoint/recovery
- [ ] Capability truthfulness
- [ ] Missing / unknown / conflict handling
- [ ] Forgetting / suppression / deletion semantics

The minimum suite is defined in `projects/cca/42-behavioral-validation-plan.md`.

## Current Gate

**Controlled Reference Baseline:** PASS  
**Real-Model Behavioral Validation:** IN PROGRESS

Architecture changes remain evidence-gated; the explicit forgetting requirement is now part of the Reference Architecture, while implementation and stronger deletion guarantees require validation.