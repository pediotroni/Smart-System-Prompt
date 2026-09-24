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
Behavioral validation remains a separate Phase 4 activity.

## Phase 3 — Runtime adapters

- [ ] Filesystem
- [ ] Shell
- [ ] Web/tools
- [ ] llama.cpp adapter (optional)

## Phase 4 — Validation

- [ ] Single-project continuity
- [ ] Multi-project isolation
- [ ] Context-shift recovery
- [ ] Memory deduplication
- [ ] Conflict detection
- [ ] Capability truthfulness