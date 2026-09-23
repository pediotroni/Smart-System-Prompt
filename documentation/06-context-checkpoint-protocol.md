# Context Checkpoint Protocol

Before context compaction/shift/session loss, preserve when applicable:

- current state
- findings
- decisions
- rejected approaches
- blockers
- open questions
- next actions
- important user-requested memory

Write required information to its authoritative persistent location before discarding working context.

After restart:

```
System rules
 -> Active context
 -> Current project state
 -> Current task
 -> Relevant decisions/findings/TODO
 -> Additional history only if needed
```

> Context loss is not memory loss.