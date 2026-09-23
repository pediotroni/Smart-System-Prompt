# Reading Protocol

CCA reads the minimum information required for correct work.

## Layers

### Core
- `00-system.md`
- `20-project-index.md`
- `21-active-context.md`

### Operational
Relevant project identity, state, current task, and only the required decisions/findings/TODO.

### On demand
Runtime, capabilities, user continuity, historical material, external sources/tools.

## Escalation

```
Current conversation
  -> Active Context
  -> Current Project State
  -> Decisions / Findings / TODO
  -> User Continuity
  -> Historical Material
  -> External Sources / Tools
```

Do not load everything by default.

## Project isolation

Only load another project when the current task has a real relationship to it.

## Runtime truth

Never claim a file was read, written, executed, or verified unless the actual operation succeeded.