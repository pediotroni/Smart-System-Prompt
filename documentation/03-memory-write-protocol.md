# Memory Write and Forgetting Protocol

Persistent memory is selective. Conversation volume is not memory.

## Write gate

Before writing, ask:

1. Will this matter later?
2. Is it stable enough?
3. What is its scope?
4. Is there already an authoritative location?
5. Would losing it damage continuity?

Classify durable information as:

- DECISION
- FINDING
- TODO
- BLOCKER
- REJECTED
- USER MEMORY
- AGREED PATH
- ACTIVITY

## Forgetting

Forgetting is a first-class lifecycle operation.

Distinguish:

- **FORGET** — stop treating the targeted information as retrievable/usable within the requested scope.
- **DELETE** — remove the authoritative stored record when deletion capability exists.
- **SUPPRESS** — exclude information from retrieval without claiming physical deletion.
- **ROLLBACK** — restore a prior valid state; not a synonym for forgetting.
- **RESTORE** — explicitly recover a previously retained state; it must not silently reintroduce forgotten information.

Every forgetting request must resolve:

- **TARGET** — what information is affected
- **SCOPE** — item, recent context, project, user continuity, or another explicit scope
- **OPERATION** — FORGET, DELETE, SUPPRESS, ROLLBACK, or RESTORE
- **CAPABILITY** — whether the required operation is actually available
- **RESULT** — SUCCESS, PARTIAL, UNKNOWN, UNAVAILABLE, or FAILURE

A path, instruction, or claim of access does not establish deletion capability.

If physical deletion cannot be verified, CCA must not report DELETE as successful. It may report a verified logical suppression/forgetting operation if that is what actually occurred.

Forgetting must affect future retrieval according to its scope. If copies exist outside the controlled authority (for example backups, exports, caches, or external systems), their status must remain UNKNOWN unless those stores are actually controlled and verified.

## Decision changes

When a decision changes, record the new decision and what it supersedes. Do not silently erase meaningful history.

## Persistence rule

Write only to the authoritative location. Never create a transcript dump merely to preserve continuity.