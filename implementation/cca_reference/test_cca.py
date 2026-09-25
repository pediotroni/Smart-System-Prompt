"""Focused tests for the CCA Reference Implementation."""
from cca import (
    ActiveContext,
    CCAReference,
    ForgetRequest,
    InMemoryRuntimeAdapter,
    MemoryClass,
    MemoryManager,
    Project,
    ResultStatus,
    ValidationEngine,
)


def test_workspace_requires_verified_read_capability():
    result = CCAReference(InMemoryRuntimeAdapter()).workspace.initialize("workspace")
    assert result.status is ResultStatus.SUCCESS


def test_project_resolution_and_active_context():
    project = Project("cca", "ACTIVE", "projects/cca")
    cca = CCAReference(InMemoryRuntimeAdapter(), [project])

    resolved = cca.registry.resolve("cca")
    assert resolved.status is ResultStatus.SUCCESS

    activated = cca.active_context.activate(
        resolved.value,
        current_task="Construct Reference CCA Implementation",
    )
    assert activated.status is ResultStatus.SUCCESS
    assert activated.value.primary_project == "cca"


def test_retrieval_is_selective():
    cca = CCAReference(InMemoryRuntimeAdapter())
    result = cca.retrieval.retrieve(
        current_conversation="current",
        active_context=cca.active_context.context,
        decisions=["decision-1"],
        history=["history-1"],
        required_categories=["decisions"],
    )
    assert result.status is ResultStatus.SUCCESS
    assert result.value["decisions"] == ["decision-1"]
    assert "history" not in result.value


def test_memory_deduplicates_exact_entries():
    manager = MemoryManager()
    entry_result = manager.classify(MemoryClass.FINDING, "context loss is not memory loss")
    assert entry_result.status is ResultStatus.SUCCESS
    assert manager.persist(entry_result.value).status is ResultStatus.SUCCESS
    assert manager.persist(entry_result.value).status is ResultStatus.CONFLICT


def test_validation_rejects_unregistered_active_project():
    validator = ValidationEngine()
    result = validator.validate(
        projects=[Project("cca", "ACTIVE", "projects/cca")],
        active_context=ActiveContext(primary_project="missing"),
        authoritative_paths={"project_index": "20-project-index.md"},
    )
    assert result.status is ResultStatus.INVALID


def test_forgetting_is_scoped_and_does_not_claim_delete():
    manager = MemoryManager()
    entry_result = manager.classify(MemoryClass.FINDING, "forget me", scope="project-a")
    assert entry_result.status is ResultStatus.SUCCESS
    entry = entry_result.value
    assert manager.persist(entry).status is ResultStatus.SUCCESS

    forgotten = manager.forget(ForgetRequest(target=entry, scope="project-a"))
    assert forgotten.status is ResultStatus.SUCCESS
    assert manager.active_entries(scope="project-a").value == ()

    mismatch = manager.forget(ForgetRequest(target=entry, scope="project-b"))
    assert mismatch.status is ResultStatus.INVALID
