"""Controlled baseline checks for the CCA Reference Implementation.

This runner uses only the Python standard library so the baseline does not
depend on pytest or another test framework.
"""

from cca import (
    ActiveContext,
    CCAReference,
    InMemoryRuntimeAdapter,
    ForgetRequest,
    MemoryClass,
    Project,
    ResultStatus,
)


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def run() -> None:
    runtime = InMemoryRuntimeAdapter(
        {"20-project-index.md": "cca | ACTIVE | projects/cca/ | CCA"}
    )
    cca = CCAReference(
        runtime,
        [Project("cca", "ACTIVE", "projects/cca/", "Cognitive Continuity Agent")],
    )

    workspace = cca.workspace.initialize("workspace")
    check(workspace.status is ResultStatus.SUCCESS, "workspace initialization failed")
    check(workspace.value["capabilities"]["model_invocation"] is False,
          "test adapter falsely claims model invocation")

    project = cca.registry.resolve("cca")
    check(project.status is ResultStatus.SUCCESS, "registered project was not resolved")
    missing = cca.registry.resolve("missing")
    check(missing.status is ResultStatus.MISSING, "missing project was not reported")

    active = cca.active_context.activate(
        project.value,
        current_task="Controlled Reference CCA Baseline",
        current_mode="Validation",
        next_action="Run baseline checks",
    )
    check(active.status is ResultStatus.SUCCESS, "active context activation failed")

    retrieved = cca.retrieval.retrieve(
        current_conversation="baseline",
        active_context=active.value,
        project_state={"status": "implementation"},
        decisions=["DEC-007"],
        history=["historical-event"],
        required_categories=["project_state", "decisions"],
    )
    check(retrieved.status is ResultStatus.SUCCESS, "retrieval failed")
    check("project_state" in retrieved.value, "required project state missing")
    check("decisions" in retrieved.value, "required decisions missing")
    check("history" not in retrieved.value, "unrequested history was retrieved")

    classified = cca.memory.classify(
        MemoryClass.FINDING,
        "The reference baseline supports deterministic implementation checks.",
        scope="cca",
    )
    check(classified.status is ResultStatus.SUCCESS, "memory classification failed")
    check(cca.memory.persist(classified.value).status is ResultStatus.SUCCESS,
          "memory persistence failed")
    check(cca.memory.persist(classified.value).status is ResultStatus.CONFLICT,
          "duplicate memory was not detected")

    forgotten = cca.memory.forget(
        ForgetRequest(target=classified.value, scope="cca")
    )
    check(forgotten.status is ResultStatus.SUCCESS, "logical forgetting failed")
    active_memories = cca.memory.active_entries(scope="cca")
    check(active_memories.status is ResultStatus.SUCCESS, "active memory retrieval failed")
    check(classified.value not in active_memories.value,
          "forgotten memory remained normally retrievable")

    checkpoint = cca.checkpoint.create(
        project_id="cca",
        active_context=active.value,
        state={"implementation": "baseline"},
        findings=("baseline constructed",),
        decisions=("DEC-007",),
        next_actions=("real-model testing",),
    )
    check(checkpoint.status is ResultStatus.SUCCESS, "checkpoint creation failed")
    check(checkpoint.value.project_id == "cca", "checkpoint lost project identity")

    valid = cca.validation.validate(
        projects=cca.registry.all(),
        active_context=active.value,
        authoritative_paths={"project_index": "20-project-index.md"},
    )
    check(valid.status is ResultStatus.SUCCESS, "valid state was rejected")

    invalid = cca.validation.validate(
        projects=cca.registry.all(),
        active_context=ActiveContext(primary_project="missing"),
        authoritative_paths={"project_index": "20-project-index.md"},
    )
    check(invalid.status is ResultStatus.INVALID, "invalid active project was accepted")

    print("CCA Reference Baseline: PASS")


if __name__ == "__main__":
    run()
