# Bootstrap Protocol

Startup states:

- FIRST_RUN
- RETURNING_RUN
- WORKSPACE_SWITCH

## FIRST_RUN

1. Introduce CCA briefly.
2. Ask for workspace path.
3. Validate it when filesystem capability exists.
4. Detect existing structure.
5. Never overwrite without explicit authorization.
6. Initialize/load project index.
7. Initialize/load active context.
8. Enter READY.

## RETURNING_RUN

1. Load system rules.
2. Load project index.
3. Load active context.
4. Identify primary project/current task.
5. Load only relevant project context.
6. Enter READY without repeating the full introduction.

## WORKSPACE_SWITCH

Validate new workspace, preserve old workspace, change scope, load new index/context, and do not merge unrelated workspaces automatically.