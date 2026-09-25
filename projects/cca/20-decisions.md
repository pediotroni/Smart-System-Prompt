# CCA Project Decisions

This file records established project-level decisions.

Ideas, proposals, hypotheses, unresolved questions, and temporary observations must not be recorded here as established decisions.

---

## DEC-001 — Reference CCA Before Compact Variants

**Status:** ACTIVE

The CCA Reference Architecture shall be constructed and sufficiently validated before designing Compact CCA or other specialized CCA variants.

---

## DEC-002 — Architecture Before Optimization

**Status:** ACTIVE

CCA shall first be constructed as a coherent and sufficiently complete Reference Architecture. Optimization and compact variants must not distort the primary architecture before validation.

---

## DEC-003 — Model and Runtime Independence

**Status:** ACTIVE

CCA architecture shall remain independent of any specific AI model, hardware, operating system, inference runtime, programming language, or implementation technology.

---

## DEC-004 — Evidence-Based Architectural Change

**Status:** ACTIVE

Architectural changes require an identified requirement, concrete use case, counterexample, observed failure, or other sufficiently grounded reason.

---

## DEC-005 — Minimum Sufficient Context

**Status:** ACTIVE

CCA shall retrieve and use the minimum context required for correct execution. Information shall not be loaded merely because it exists.

---

## DEC-006 — Architecture and Runtime Separation

**Status:** ACTIVE

Architectural definitions remain distinct from runtime-specific facts and implementation mechanisms.

---

## DEC-007 — Real-Model Validation

**Status:** ACTIVE

CCA shall be validated through controlled behavioral testing with a real AI model before the Reference CCA is considered sufficiently established.

---

## DEC-008 — No Premature Architecture Expansion

**Status:** ACTIVE

New mechanisms shall not be introduced merely to anticipate hypothetical future requirements.

This decision is subject to DEC-009: an explicit, concrete user requirement is sufficient architectural evidence to define a required capability, while implementation complexity remains evidence-gated.

---

## DEC-009 — Forgetting Is a First-Class Capability

**Status:** ACTIVE

CCA shall support explicit, scoped information-forgetting semantics.

The architecture must distinguish logical forgetting/suppression from physical deletion and must never claim successful deletion without verified capability and evidence.

Forgetting shall operate on existing authoritative records and retrieval paths rather than creating a parallel memory system.

Implementation details and stronger deletion guarantees remain subject to behavioral and runtime validation.

**Reason:** Explicit requirement to support forgetting and removal while preserving CCA's truthfulness and selective-persistence principles.

---

## Decision Maintenance

When a decision changes, the existing decision shall not be silently rewritten. A superseding decision must identify what it replaces and why.