# Context Checkpoint Protocol

Before context compaction, shift, session loss, or another cognitive boundary, preserve only information required for continuation:

- current state
- current task
- findings
- decisions
- rejected approaches
- blockers
- open questions
- next actions
- important user-requested memory

Write required information to its authoritative persistent location before discarding working context.

If information was explicitly forgotten or suppressed, do not checkpoint it as active/retrievable state.

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