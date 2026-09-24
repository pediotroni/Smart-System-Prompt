# CCA Reference Implementation — Component Interfaces

## Purpose

This document defines the internal interfaces between the seven responsibilities of the CCA Reference Implementation.

The purpose is to establish clear responsibility boundaries before implementation technology is selected.

These interfaces describe information flow and responsibility boundaries.

They do not prescribe:

- a programming language
- a software framework
- a class structure
- a process architecture
- a specific runtime
- a specific AI model

## Interface Principles

The Reference Implementation shall preserve the following principles:

1. Each component has a defined responsibility.
2. No component becomes an alternative authority for information owned elsewhere.
3. Components exchange information rather than silently modifying unrelated state.
4. Runtime-specific capabilities remain behind the Runtime Adapter boundary.
5. Unknown information must remain unknown.
6. Components must distinguish successful results from unavailable capabilities, missing information, conflicts, and failures.
7. Components should expose the minimum information required by the receiving component.
8. Internal interfaces must not force unnecessary coupling between components.

---

# Component 1 — Workspace Initialization

## Responsibility

Establish or load a CCA workspace according to the Bootstrap Protocol.

## Inputs

- workspace location
- requested startup mode, when known
- runtime capabilities
- existing workspace state, when accessible

## Outputs

- validated workspace state
- detected CCA structure
- initialization result
- workspace scope

## May Depend On

- Runtime Adapter
- filesystem capability
- Bootstrap Protocol

## Must Not

- invent runtime capabilities
- overwrite existing state without authorization
- modify unrelated workspaces
- determine project-specific business state

---

# Component 2 — Project Registry Management

## Responsibility

Resolve registered projects through `20-project-index.md`.

## Inputs

- workspace state
- project identifier or project selection request
- project registry

## Outputs

- resolved project identity
- project status
- project path
- project description
- project resolution result

## May Depend On

- Workspace Initialization
- Runtime Adapter
- `20-project-index.md`

## Must Not

- create project memory
- silently register nonexistent projects
- merge unrelated projects
- replace project-local state

---

# Component 3 — Active Context Management

## Responsibility

Maintain the operational projection represented by `21-active-context.md`.

## Inputs

- resolved project
- current task
- current mode
- related/reference projects
- next action
- relevant runtime context

## Outputs

- updated active-context projection
- active project selection
- current operational context

## May Depend On

- Project Registry Management
- relevant project state
- current task
- Runtime Adapter

## Must Not

- become the authoritative project state
- replace project history
- silently rewrite durable user memory
- merge unrelated project state

## Boundary

```
Active Context
      ≠
Project State
      ≠
Project History
```

Active Context is a working projection.

---

# Component 4 — Context Retrieval

## Responsibility

Retrieve the minimum context required for correct execution of the current task.

## Inputs

- current conversation
- active context
- current project
- current task
- task requirements
- available project and continuity records

## Outputs

- selected context
- retrieval rationale
- unresolved information requirements
- retrieval status

## May Depend On

- Active Context Management
- Project Registry Management
- project-local state
- decisions
- findings
- TODOs
- user continuity
- historical material
- external sources when explicitly required

## Retrieval Order

The component shall follow the established escalation principle:

```
Current Conversation
        ↓
Active Context
        ↓
Current Project State
        ↓
Decisions / Findings / TODO
        ↓
User Continuity
        ↓
Historical Material
        ↓
External Sources / Tools
```

Escalation should occur only when the current information is insufficient.

## Must Not

- load all available information by default
- mix unrelated projects
- treat every retrieved statement as authoritative
- invent missing context

---

# Component 5 — Memory Classification and Persistence

## Responsibility

Classify durable information and persist it in the appropriate authoritative location.

## Inputs

- current information
- conversation events
- decisions
- findings
- TODOs
- blockers
- rejected approaches
- user-requested memory
- agreed paths
- activity events

## Outputs

- classification result
- persistence decision
- target authoritative location
- write result

## Classification

The component may classify information as:

- DECISION
- FINDING
- TODO
- BLOCKER
- REJECTED
- USER MEMORY
- AGREED PATH
- ACTIVITY

## May Depend On

- Memory Write Protocol
- File Contracts
- Runtime Adapter
- Validation and Consistency Checking

## Must Not

- persist the complete conversation by default
- create competing authoritative copies
- convert assumptions into facts
- silently overwrite established state
- treat a temporary observation as durable memory without sufficient basis

---

# Component 6 — Context Checkpointing

## Responsibility

Preserve the information necessary for continuity before context compaction, session loss, or significant context transition.

## Inputs

- current project state
- active context
- current task
- findings
- decisions
- rejected approaches
- blockers
- open questions
- next actions
- important user-requested memory

## Outputs

- checkpoint result
- persisted continuity state
- recovery information

## May Depend On

- Active Context Management
- Memory Classification and Persistence
- relevant project state
- Context Checkpoint Protocol

## Must Not

- create a parallel history system without justification
- persist irrelevant conversation volume
- silently discard established state
- assume that a checkpoint is equivalent to a full transcript

---

# Component 7 — Validation and Consistency Checking

## Responsibility

Verify that CCA state and implementation behavior remain structurally consistent.

## Inputs

- workspace structure
- project registry
- active context
- project-local state
- file contracts
- protocol definitions
- implementation state
- runtime capability state

## Outputs

- validation result
- detected inconsistencies
- detected conflicts
- missing dependencies
- unsupported references
- recommended corrective action

## Minimum Validation Scope

The component shall be capable of detecting, where applicable:

- missing required files
- invalid references
- duplicate authority
- authority conflicts
- inconsistent terminology
- invalid project references
- project isolation violations
- invalid state
- unsupported assumptions
- capability claims without evidence

## Must Not

- silently repair established state
- redefine architecture without authorization
- treat a model failure as automatically being an architectural failure
- treat an implementation convenience as an architectural requirement

---

# Inter-Component Relationships

The initial dependency structure is:

```
Workspace Initialization
          │
          ▼
Project Registry Management
          │
          ▼
Active Context Management
          │
          ▼
Context Retrieval
          │
          ├──────────────► Memory Classification / Persistence
          │
          └──────────────► Context Checkpointing

Validation and Consistency Checking
          │
          └──► validates the state and relationships of the other components
```

This diagram represents responsibility flow, not necessarily a fixed execution sequence.

Components may be invoked independently when required.

---

# Runtime Adapter Boundary

The Reference Implementation does not directly assume concrete runtime capabilities.

The Runtime Adapter is responsible for exposing verified runtime operations such as:

- read
- write
- edit
- execute
- model invocation
- external tool invocation

The Reference Implementation consumes these capabilities through an abstract interface.

Therefore:

```
Reference Implementation
          │
          ▼
Runtime Capability Interface
          │
          ▼
Concrete Runtime Adapter
```

A capability must not be considered available merely because the architecture requests it.

---

# Error Propagation

Components shall preserve the distinction between:

- SUCCESS
- UNKNOWN
- UNAVAILABLE
- MISSING
- CONFLICT
- INVALID
- FAILURE

An error or uncertainty originating in one component must not be silently transformed into a successful result by another component.

For example:

```
Filesystem unavailable
        ↓
Workspace Initialization
        ↓
UNAVAILABLE
        ↓
not
        ↓
"workspace initialized"
```

---

# Authority Flow

The Reference Implementation must preserve the distinction between:

```
Authoritative State
        │
        ▼
Retrieval / Projection
        │
        ▼
Operational Use
```

and must not create:

```
Authoritative State A
        +
Authoritative State B
```

for the same information category.

When information changes, the authoritative source remains the place where the change is recorded.

---

# Current Boundary Status

**Workspace Initialization Interface:** Defined

**Project Registry Interface:** Defined

**Active Context Interface:** Defined

**Context Retrieval Interface:** Defined

**Memory Persistence Interface:** Defined

**Checkpoint Interface:** Defined

**Validation Interface:** Defined

**Runtime Adapter Boundary:** Defined

**Concrete Technology:** Intentionally Not Selected

---

# Deferred Interface Questions

The following questions remain intentionally open:

- rule and instruction precedence
- loop and termination control
- archived-project retrieval semantics
- project-local versus global activity history
- long-term role of `94-user-notes.md`

These shall not be converted into new interfaces until sufficient evidence demonstrates that they require independent implementation treatment.

## Next Step

Perform an interface-level consistency review and identify any missing dependency, circular dependency, duplicated responsibility, or unnecessary coupling before beginning concrete implementation.
