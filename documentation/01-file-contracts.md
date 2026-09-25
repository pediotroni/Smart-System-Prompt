# File Contracts

## Global authority

| File | Authority |
|---|---|
| `00-system.md` | CCA identity and rules |
| `10-runtime.md` | Current runtime |
| `11-capabilities.md` | Actual runtime capabilities |
| `12-launch.md` | Launch configuration |
| `20-project-index.md` | Project registry |
| `21-active-context.md` | Current context projection |
| `90-user-memory.md` | Durable user-requested memory |
| `91-user-plans.md` | Cross-project plans |
| `92-agreed-paths.md` | Explicitly agreed paths |
| `93-activity-log.md` | Concise activity events |
| `94-user-notes.md` | Residual durable notes |

## Project-local authority

| File | Authority |
|---|---|
| `01-project.md` | Project identity |
| `10-state.md` | Current project state |
| `11-current-task.md` | Current task |
| `20-decisions.md` | Established decisions |
| `21-findings.md` | Established findings |
| `30-todo.md` | Future work |

## Single Source of Truth

Update the authoritative source instead of creating duplicate authoritative copies.

Forgetting is an operation over authoritative records and retrieval scope; it does not create a second memory store. Physical deletion is separate from logical forgetting and requires verified deletion capability.