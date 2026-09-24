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

**Status:** COMPLETED

The minimum Reference CCA implementation responsibilities were identified and their internal interfaces were defined in `41-component-interfaces.md`.

The seven responsibilities are:

1. Workspace Initialization
2. Project Registry Management
3. Active Context Management
4. Context Retrieval
5. Memory Classification and Persistence
6. Context Checkpointing
7. Validation and Consistency Checking

No additional component was introduced for the currently open questions.

---

## T-003 — Construct Reference CCA Implementation

**Status:** COMPLETED

A first concrete, runtime-independent Reference CCA implementation has been constructed under `implementation/cca_reference/`.

The implementation realizes the seven established responsibilities and includes a deterministic in-memory runtime adapter and focused tests.

This is an implementation baseline, not yet a behaviorally validated CCA deployment.

---

## T-004 — Perform Integration and Consistency Review

**Status:** COMPLETED

The interface-level consistency review was completed.

The review identified and corrected a dependency-graph overstatement and synchronized the affected project status records. No additional implementation component was justified.

---

## T-005 — Establish a Controlled Testable Baseline

**Status:** COMPLETED

A deterministic controlled baseline has been executed successfully in GitHub Actions.

Verified execution:

- Workflow: `CCA Reference Baseline`
- Run ID: `36058064392`
- Commit: `33c79d76d0c3968d55fe8bf63c647062ccce9d5f`
- Conclusion: `success`

The baseline exercises all seven established responsibilities.

This establishes a verified implementation-level PASS. It does not establish real-model behavioral correctness.

---

## T-006 — Perform Real-Model Behavioral Testing

**Status:** IN PREPARATION

Define and execute the minimum controlled behavioral test suite against one verified model/runtime configuration.

The controlled plan is recorded in `42-behavioral-validation-plan.md`.

The minimum suite covers:

- returning-run continuity
- selective retrieval
- multi-project isolation
- memory classification and deduplication
- context checkpoint and recovery
- capability truthfulness
- missing / unknown / conflict handling

Testing must separate primary behavioral results from secondary diagnosis.

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

After the Reference CCA has been sufficiently implemented and behaviorally validated, evaluate whether compact or specialized variants are justified.

Variants should be derived from the validated Reference CCA rather than independently redefining the architecture.

---

## TODO Maintenance

TODO items may be added, changed, deferred, completed, or rejected as project evidence develops.

Completed or rejected items should retain sufficient historical information to explain their disposition.

A TODO item must not be treated as a confirmed requirement merely because it appears in this file.
