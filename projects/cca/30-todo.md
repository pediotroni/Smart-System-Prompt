# CCA Project TODO

This file records future or pending work for the CCA project.

The current task is maintained separately in `11-current-task.md`.

TODO items must not be treated as established decisions, findings, or requirements until sufficient evidence exists.

---

## T-001 — Complete Reference CCA Project Baseline

**Status:** COMPLETED

Complete the required project-local files and verify that their responsibilities are consistent with the global file contracts.

---

## T-002 — Define Remaining Reference CCA Components

**Status:** PENDING

Identify the minimum remaining components required to transform the current architectural baseline into a coherent and testable Reference CCA implementation.

Do not introduce components without sufficient architectural justification.

---

## T-003 — Construct Reference CCA Implementation

**Status:** PENDING

Construct the required implementation components according to the established file contracts and protocols.

The implementation should preserve:

- authority boundaries
- project isolation
- runtime truthfulness
- selective context retrieval
- persistent continuity
- traceable state changes

---

## T-004 — Perform Integration and Consistency Review

**Status:** PENDING

Review the complete Reference CCA structure for:

- conflicting responsibilities
- duplicate authority
- missing dependencies
- inconsistent terminology
- unsupported assumptions
- broken information flow
- unnecessary architectural components

---

## T-005 — Establish a Controlled Testable Baseline

**Status:** PENDING

Prepare a sufficiently complete Reference CCA configuration for controlled behavioral testing with a real local AI model.

---

## T-006 — Perform Real-Model Behavioral Testing

**Status:** PENDING

Run controlled tests against the Reference CCA and record observed behavior.

Testing should distinguish between:

- PASS
- FAIL
- PARTIAL
- UNEXPECTED BEHAVIOR
- ARCHITECTURAL DEFECT
- MODEL CAPABILITY LIMIT

---

## T-007 — Investigate Rule and Instruction Precedence

**Status:** PENDING

Determine whether an explicit precedence model is required for conflicts among system rules, project state, current tasks, user instructions, established decisions, and other information categories.

This item should be resolved through concrete conflict cases rather than theoretical expansion alone.

---

## T-008 — Investigate Loop and Termination Control

**Status:** PENDING

Determine whether the Reference CCA requires explicit mechanisms for detecting:

- repeated operations
- lack of progress
- recursive retrieval
- repeated interpretation
- unresolved execution loops

Do not assume a fixed operation-count threshold without evidence.

---

## T-009 — Evaluate Archived Project Semantics

**Status:** PENDING

Determine the correct retrieval and activation behavior for project statuses including:

- ACTIVE
- PAUSED
- ARCHIVED
- COMPLETED

The behavior should distinguish default retrieval from explicit historical retrieval where necessary.

---

## T-010 — Evaluate Global Activity History Scope

**Status:** PENDING

Determine through implementation and testing whether the global activity log is sufficient for continuity or whether project-local activity history is necessary.

Do not add project-local activity logs unless their necessity is demonstrated.

---

## T-011 — Evaluate the Long-Term Role of User Notes

**Status:** PENDING

Evaluate whether `94-user-notes.md` represents a necessary durable information category or becomes an uncontrolled catch-all.

Do not remove or redesign the category without evidence.

---

## T-012 — Derive Compact and Specialized Variants

**Status:** DEFERRED

After the Reference CCA has been sufficiently implemented and validated, evaluate whether compact or specialized variants are justified.

Variants should be derived from the validated Reference CCA rather than independently redefining the architecture.

---

## TODO Maintenance

TODO items may be added, changed, deferred, completed, or rejected as project evidence develops.

Completed or rejected items should retain sufficient historical information to explain their disposition.

A TODO item must not be treated as a confirmed requirement merely because it appears in this file.
