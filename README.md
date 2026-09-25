# Cognitive Continuity Agent (CCA)

CCA is a model-, hardware-, and runtime-independent architecture for maintaining useful continuity across conversations, context shifts, sessions, and multiple projects.

> Context loss is not memory loss.

The repository separates persistent state, active context, project state, runtime configuration, findings, decisions, TODOs, and user continuity.

CCA also defines explicit, scoped forgetting semantics. Logical forgetting/suppression is distinct from physical deletion; deletion is never claimed without verified capability and evidence.

The canonical architecture is defined by `00-system.md` and the documented protocols in `documentation/`.

For local deployment, `documentation/08-runtime-system-prompt.md` provides a compact executable system-prompt projection derived from the architecture. It is intended to be copied into a model WebUI's **System Prompt** field; it is not a second architectural authority.

See `documentation/` for the normative architecture and operational protocols.
