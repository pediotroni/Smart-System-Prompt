# Implementation Roadmap

## Phase 1 — Architecture baseline

- [x] Core identity
- [x] File contracts
- [x] Reading protocol
- [x] Memory write protocol
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

The initial concrete baseline is implemented under `implementation/cca_reference/`.

The deterministic controlled baseline has been executed successfully in GitHub Actions.

## Phase 3 — Runtime adapters

- [ ] Filesystem
- [ ] Shell
- [ ] Web/tools
- [ ] llama.cpp adapter (optional)

Phase 3 remains a runtime-integration track. It is not a prerequisite for the model-independent implementation baseline, but a concrete adapter is required for real-model behavioral testing.

## Phase 4 — Validation

- [ ] Single-project continuity
- [ ] Multi-project isolation
- [ ] Context-shift recovery
- [ ] Memory deduplication
- [ ] Conflict detection
- [ ] Capability truthfulness

The minimum behavioral suite is defined in `projects/cca/42-behavioral-validation-plan.md`.

## Current Gate

**Controlled Reference Baseline:** PASS  
**Real-Model Behavioral Validation:** Pending

Do not expand the architecture until behavioral evidence demonstrates a concrete requirement or deficiency.
