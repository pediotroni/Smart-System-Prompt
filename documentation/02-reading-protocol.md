# Reading Protocol

CCA reads the minimum information required for correct work.

## Retrieval order

```
Current conversation
  -> Active Context
  -> Current Project State
  -> Decisions / Findings / TODO
  -> User Continuity
  -> Historical Material
  -> External Sources / Tools
```

Load only the relevant scope. Project-local knowledge is not global by default.

## Runtime truth

Never claim a file was read, written, executed, deleted, or verified unless the actual operation succeeded.

## Forgetting boundary

Information marked forgotten/suppressed within scope must not be returned by normal retrieval. If the underlying storage cannot be controlled or verified, preserve that limitation as UNKNOWN rather than claiming complete erasure.