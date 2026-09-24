# CCA Project Decisions

This file records established project-level decisions.

Ideas, proposals, hypotheses, unresolved questions, and temporary observations must not be recorded here as established decisions.

---

## DEC-001 — Reference CCA Before Compact Variants

**Status:** ACTIVE

The CCA Reference Architecture shall be constructed and sufficiently validated before designing Compact CCA or other specialized CCA variants.

Compact and specialized variants shall be treated as derived variants of the validated Reference Architecture rather than as competing primary architectures.

---

## DEC-002 — Architecture Before Optimization

**Status:** ACTIVE

CCA shall first be constructed as a coherent and sufficiently complete Reference Architecture.

Optimization, minimization, model-specific adaptation, and compact variants shall not constrain the primary architecture before the architecture has been validated.

---

## DEC-003 — Model and Runtime Independence

**Status:** ACTIVE

CCA architecture shall remain independent of any specific:

- AI model
- model family
- model size
- hardware platform
- operating system
- inference runtime
- programming language
- implementation technology

Runtime-specific information belongs to the runtime layer and must not redefine the CCA architecture.

---

## DEC-004 — Evidence-Based Architectural Change

**Status:** ACTIVE

CCA architecture shall not be expanded, reduced, or structurally modified solely because a component appears useful.

Architectural changes require sufficient grounding through an identified requirement, concrete use case, counterexample, observed failure, or other relevant evidence.

---

## DEC-005 — Minimum Sufficient Context

**Status:** ACTIVE

CCA shall retrieve and use the minimum context required for correct execution of the current task.

Information shall not be loaded merely because it exists.

This principle does not imply that the architecture itself must be minimal.

---

## DEC-006 — Architecture and Runtime Separation

**Status:** ACTIVE

CCA architectural definitions shall remain distinct from runtime-specific facts and implementation mechanisms.

Runtime state, available capabilities, and launch conditions shall be represented separately from the architectural definition.

---

## DEC-007 — Real-Model Validation

**Status:** ACTIVE

CCA shall be validated through controlled behavioral testing with a real AI model before the Reference Architecture is considered sufficiently established.

Architectural correctness shall not be inferred solely from textual consistency.

---

## DEC-008 — No Premature Architecture Expansion

**Status:** ACTIVE

New files, protocols, mechanisms, or architectural layers shall not be introduced solely to anticipate hypothetical future requirements.

Expansion shall be driven by demonstrated necessity or sufficiently grounded architectural evidence.

---

## Decision Maintenance

When a decision is changed, the existing decision shall not be silently rewritten as though the previous decision never existed.

A superseding decision shall explicitly identify the decision it replaces and explain the reason for the change.
