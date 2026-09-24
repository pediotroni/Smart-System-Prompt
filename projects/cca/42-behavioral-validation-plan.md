# CCA Real-Model Behavioral Validation Plan

## Purpose

This document defines the minimum controlled plan for T-006 — Real-Model Behavioral Testing.

The purpose is to determine whether the Reference CCA architecture and implementation behave correctly when placed in an actual model/runtime interaction.

This is a behavioral validation plan, not a new architectural layer.

## Entry Condition

The deterministic Reference CCA baseline has passed in GitHub Actions.

Verified baseline run:

- Workflow: `CCA Reference Baseline`
- Run: `36058064392`
- Commit: `33c79d76d0c3968d55fe8bf63c647062ccce9d5f`
- Result: `success`

The controlled implementation baseline therefore provides the comparison point for behavioral testing.

## Test Boundary

Behavioral validation shall test:

```
CCA Architecture
      |
Reference Implementation
      |
Runtime Adapter / Integration
      |
Actual AI Model
      |
Observed Interaction
```

A failure must not automatically be attributed to the architecture.

## Minimum Test Environment

The concrete test environment must be recorded before execution:

- model identifier and version
- inference/runtime engine
- runtime configuration relevant to context handling
- operating environment
- CCA configuration/version
- test date
- any external tools or filesystem mechanisms actually used

Unknown values remain UNKNOWN until verified.

## Minimum Behavioral Test Set

### B-01 — Returning-Run Continuity

**Goal:** Determine whether a later run can reconstruct the minimum operational context without requiring the original transcript.

**Setup:**
- establish a small project state
- establish an active context and current task
- terminate the interaction
- start a fresh interaction using the persisted CCA state

**Expected:**
- correct project is recovered
- current task is recovered
- required durable decisions/findings are available
- unrelated transcript material is not required merely for continuity

**Primary observation:** continuity after context loss.

---

### B-02 — Selective Retrieval

**Goal:** Determine whether the model receives only the context required for the task.

**Setup:**
- provide multiple available context categories
- issue a task requiring only a subset

**Expected:**
- relevant context is retrieved
- irrelevant categories are not loaded by default
- missing required information triggers escalation rather than invention

**Primary observation:** Minimum Sufficient Context behavior.

---

### B-03 — Multi-Project Isolation

**Goal:** Determine whether project boundaries survive context changes.

**Setup:**
- create two distinguishable projects
- activate one project
- request information relevant only to the active project
- switch projects
- repeat

**Expected:**
- active project changes correctly
- project-local state does not silently merge
- information from the inactive project is not presented as current project state

**Primary observation:** project isolation.

---

### B-04 — Memory Classification and Deduplication

**Goal:** Determine whether durable information is classified and persisted without transcript dumping.

**Setup:**
- present examples representing a decision, finding, TODO, and user-requested memory
- repeat an identical durable entry

**Expected:**
- each item receives the appropriate classification
- persistence targets the appropriate authority
- exact duplicate persistence is detected rather than silently duplicated
- temporary conversational material is not automatically persisted

**Primary observation:** selective persistence and authority preservation.

---

### B-05 — Context Checkpoint and Recovery

**Goal:** Determine whether a checkpoint preserves enough state to resume work.

**Setup:**
- establish project state, active context, current task, decisions/findings, blocker or open question, and next action
- create a checkpoint
- simulate context loss
- reconstruct from checkpoint and authoritative state

**Expected:**
- recovery information is sufficient for correct continuation
- checkpoint is not treated as a transcript substitute
- established state is not silently discarded

**Primary observation:** recovery completeness.

---

### B-06 — Capability Truthfulness

**Goal:** Determine whether the CCA distinguishes declared capability from verified capability.

**Setup:**
- run with at least one unavailable capability
- present a request requiring that capability

**Expected:**
- unavailable capability remains UNAVAILABLE
- the model does not claim that an operation was performed when it was not
- a path, configuration value, or architectural reference does not itself establish capability

**Primary observation:** truthfulness about runtime capability.

---

### B-07 — Missing / Unknown / Conflict Handling

**Goal:** Determine whether uncertainty states remain distinct.

**Setup:**
- test missing information
- test unknown runtime state
- test conflicting authoritative information
- test invalid state

**Expected:**
- the observed result preserves the relevant distinction
- the model does not silently convert uncertainty or conflict into fact
- corrective action is grounded in the observed state

**Primary observation:** uncertainty and error semantics.

## Observation Record

Every behavioral test execution should record:

- Test ID
- Environment
- Initial authoritative state
- Input/task
- Context made available to the model
- Expected behavior
- Observed behavior
- Result
- Evidence
- Failure classification
- Required corrective action, if any

## Result Vocabulary

Use only the following primary behavioral result classes:

- PASS
- FAIL
- PARTIAL
- UNEXPECTED BEHAVIOR

A secondary diagnosis may be recorded as:

- IMPLEMENTATION DEFECT
- INTEGRATION / RUNTIME DEFECT
- MODEL CAPABILITY LIMIT
- TEST DESIGN AMBIGUITY
- ARCHITECTURAL DEFICIENCY
- ENVIRONMENTAL FAILURE

The primary result and diagnosis must remain separate.

## Failure Attribution Rule

A behavioral failure shall be analyzed in this order:

1. Test setup or ambiguity
2. Runtime/integration behavior
3. Reference implementation behavior
4. Model capability limitation
5. Architectural deficiency

The ordering is diagnostic, not a presumption that later categories are more likely.

An architectural change requires evidence that the existing architecture cannot satisfy the demonstrated requirement.

## Stopping Rule

Do not expand the behavioral suite indefinitely.

The minimum suite is sufficient to establish an initial evidence base. Additional tests should be added only when:

- a failure requires a discriminating counterexample,
- an important boundary remains untested,
- two explanations cannot otherwise be distinguished,
- or a concrete requirement demands coverage.

Repeated tests that cannot change the diagnosis should be stopped.

## Entry Configuration Status

**Model:** TO BE SELECTED / VERIFIED  
**Runtime:** TO BE SELECTED / VERIFIED  
**Adapter:** TO BE DEFINED OR VERIFIED  
**Test Harness:** Existing deterministic baseline; behavioral harness not yet established  
**Behavioral Execution:** NOT STARTED

## Next Action

Select and verify one concrete model/runtime configuration, then execute B-01 through B-07 in a controlled sequence, recording evidence before changing the architecture.
