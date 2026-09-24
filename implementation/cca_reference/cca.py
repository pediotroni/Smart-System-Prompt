"""Runtime-independent CCA Reference Implementation."""
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Iterable, Mapping, Protocol


class ResultStatus(str, Enum):
    SUCCESS = "SUCCESS"
    UNKNOWN = "UNKNOWN"
    UNAVAILABLE = "UNAVAILABLE"
    MISSING = "MISSING"
    CONFLICT = "CONFLICT"
    INVALID = "INVALID"
    FAILURE = "FAILURE"


class MemoryClass(str, Enum):
    DECISION = "DECISION"
    FINDING = "FINDING"
    TODO = "TODO"
    BLOCKER = "BLOCKER"
    REJECTED = "REJECTED"
    USER_MEMORY = "USER MEMORY"
    AGREED_PATH = "AGREED PATH"
    ACTIVITY = "ACTIVITY"


@dataclass(frozen=True)
class OperationResult:
    status: ResultStatus
    value: Any = None
    message: str = ""


@dataclass
class Project:
    project_id: str
    status: str
    path: str
    description: str = ""


@dataclass
class ActiveContext:
    primary_project: str | None = None
    current_task: str | None = None
    current_mode: str | None = None
    related_projects: list[str] = field(default_factory=list)
    reference_projects: list[str] = field(default_factory=list)
    next_action: str | None = None


@dataclass(frozen=True)
class MemoryEntry:
    category: MemoryClass
    content: str
    scope: str = "global"


@dataclass
class Checkpoint:
    project_id: str | None
    active_context: ActiveContext
    state: Mapping[str, Any]
    findings: tuple[str, ...] = ()
    decisions: tuple[str, ...] = ()
    rejected: tuple[str, ...] = ()
    blockers: tuple[str, ...] = ()
    open_questions: tuple[str, ...] = ()
    next_actions: tuple[str, ...] = ()


class RuntimeAdapter(Protocol):
    def capabilities(self) -> Mapping[str, bool]:
        ...

    def read(self, path: str) -> OperationResult:
        ...

    def write(self, path: str, content: str) -> OperationResult:
        ...


class InMemoryRuntimeAdapter:
    """Deterministic test adapter; not a production runtime adapter."""

    def __init__(self, files: Mapping[str, str] | None = None) -> None:
        self.files = dict(files or {})

    def capabilities(self) -> Mapping[str, bool]:
        return {
            "filesystem_read": True,
            "filesystem_write": True,
            "shell": False,
            "web": False,
            "external_tools": False,
            "model_invocation": False,
        }

    def read(self, path: str) -> OperationResult:
        if path not in self.files:
            return OperationResult(ResultStatus.MISSING, message=f"Missing: {path}")
        return OperationResult(ResultStatus.SUCCESS, self.files[path])

    def write(self, path: str, content: str) -> OperationResult:
        self.files[path] = content
        return OperationResult(ResultStatus.SUCCESS, path)


class WorkspaceInitializer:
    """Responsibility 1: establish validated workspace scope."""

    def __init__(self, runtime: RuntimeAdapter) -> None:
        self.runtime = runtime

    def initialize(self, workspace: str) -> OperationResult:
        if not workspace:
            return OperationResult(ResultStatus.INVALID, message="Workspace is empty.")
        caps = self.runtime.capabilities()
        if not caps.get("filesystem_read", False):
            return OperationResult(
                ResultStatus.UNAVAILABLE,
                message="Filesystem read capability is not established.",
            )
        return OperationResult(
            ResultStatus.SUCCESS,
            {"workspace": workspace, "capabilities": dict(caps)},
        )


class ProjectRegistry:
    """Responsibility 2: resolve registered projects without creating state."""

    def __init__(self, projects: Iterable[Project] = ()) -> None:
        self._projects = {p.project_id: p for p in projects}

    def resolve(self, project_id: str) -> OperationResult:
        project = self._projects.get(project_id)
        if project is None:
            return OperationResult(
                ResultStatus.MISSING,
                message=f"Project is not registered: {project_id}",
            )
        return OperationResult(ResultStatus.SUCCESS, project)

    def all(self) -> tuple[Project, ...]:
        return tuple(self._projects.values())


class ActiveContextManager:
    """Responsibility 3: maintain the working context projection."""

    def __init__(self) -> None:
        self.context = ActiveContext()

    def activate(
        self,
        project: Project,
        *,
        current_task: str | None = None,
        current_mode: str | None = None,
        related_projects: Iterable[str] = (),
        reference_projects: Iterable[str] = (),
        next_action: str | None = None,
    ) -> OperationResult:
        self.context = ActiveContext(
            primary_project=project.project_id,
            current_task=current_task,
            current_mode=current_mode,
            related_projects=list(related_projects),
            reference_projects=list(reference_projects),
            next_action=next_action,
        )
        return OperationResult(ResultStatus.SUCCESS, self.context)


class ContextRetrieval:
    """Responsibility 4: select minimum sufficient context."""

    def retrieve(
        self,
        *,
        current_conversation: str | None,
        active_context: ActiveContext,
        project_state: Mapping[str, Any] | None = None,
        decisions: Iterable[str] = (),
        findings: Iterable[str] = (),
        todos: Iterable[str] = (),
        user_continuity: Iterable[str] = (),
        history: Iterable[str] = (),
        required_categories: Iterable[str] = (),
    ) -> OperationResult:
        context: dict[str, Any] = {
            "current_conversation": current_conversation,
            "active_context": active_context,
        }
        required = set(required_categories)
        if "project_state" in required:
            context["project_state"] = dict(project_state or {})
        if "decisions" in required:
            context["decisions"] = list(decisions)
        if "findings" in required:
            context["findings"] = list(findings)
        if "todos" in required:
            context["todos"] = list(todos)
        if "user_continuity" in required:
            context["user_continuity"] = list(user_continuity)
        if "history" in required:
            context["history"] = list(history)
        return OperationResult(ResultStatus.SUCCESS, context)


class MemoryManager:
    """Responsibility 5: classify and persist durable information."""

    def __init__(self) -> None:
        self.entries: list[MemoryEntry] = []

    def classify(
        self, category: MemoryClass, content: str, scope: str = "global"
    ) -> OperationResult:
        if not content.strip():
            return OperationResult(ResultStatus.INVALID, message="Memory content is empty.")
        return OperationResult(
            ResultStatus.SUCCESS,
            MemoryEntry(category=category, content=content, scope=scope),
        )

    def persist(self, entry: MemoryEntry) -> OperationResult:
        if entry in self.entries:
            return OperationResult(
                ResultStatus.CONFLICT, message="Duplicate memory entry."
            )
        self.entries.append(entry)
        return OperationResult(ResultStatus.SUCCESS, entry)


class CheckpointManager:
    """Responsibility 6: capture recoverable continuity state."""

    def __init__(self) -> None:
        self.latest: Checkpoint | None = None

    def create(
        self,
        *,
        project_id: str | None,
        active_context: ActiveContext,
        state: Mapping[str, Any],
        findings: Iterable[str] = (),
        decisions: Iterable[str] = (),
        rejected: Iterable[str] = (),
        blockers: Iterable[str] = (),
        open_questions: Iterable[str] = (),
        next_actions: Iterable[str] = (),
    ) -> OperationResult:
        self.latest = Checkpoint(
            project_id=project_id,
            active_context=active_context,
            state=dict(state),
            findings=tuple(findings),
            decisions=tuple(decisions),
            rejected=tuple(rejected),
            blockers=tuple(blockers),
            open_questions=tuple(open_questions),
            next_actions=tuple(next_actions),
        )
        return OperationResult(ResultStatus.SUCCESS, self.latest)


class ValidationEngine:
    """Responsibility 7: detect consistency defects without silent repair."""

    def validate(
        self,
        *,
        projects: Iterable[Project],
        active_context: ActiveContext,
        authoritative_paths: Mapping[str, str],
    ) -> OperationResult:
        errors: list[str] = []
        project_list = list(projects)
        ids = [p.project_id for p in project_list]
        if len(ids) != len(set(ids)):
            errors.append("Duplicate project identifiers.")

        if active_context.primary_project is not None:
            if active_context.primary_project not in set(ids):
                errors.append("Active project is not registered.")

        seen_paths: dict[str, str] = {}
        for category, path in authoritative_paths.items():
            previous = seen_paths.get(path)
            if previous is not None and previous != category:
                errors.append(
                    f"Duplicate authoritative path: {path} used by "
                    f"{previous} and {category}."
                )
            seen_paths[path] = category

        if errors:
            return OperationResult(ResultStatus.INVALID, errors)
        return OperationResult(
            ResultStatus.SUCCESS, {"checked_projects": len(project_list)}
        )


class CCAReference:
    """Composition root exposing the seven Reference CCA responsibilities."""

    def __init__(
        self,
        runtime: RuntimeAdapter,
        projects: Iterable[Project] = (),
    ) -> None:
        self.workspace = WorkspaceInitializer(runtime)
        self.registry = ProjectRegistry(projects)
        self.active_context = ActiveContextManager()
        self.retrieval = ContextRetrieval()
        self.memory = MemoryManager()
        self.checkpoint = CheckpointManager()
        self.validation = ValidationEngine()
