# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable

from .mcp_server_config_param import McpServerConfigParam

from .._types import SequenceNotStr

from typing_extensions import Literal, TypedDict, Required

__all__ = ["AmbientAgentConfigParam", "Harness", "HarnessAuthSecrets", "InferenceProviders", "InferenceProvidersAws", "MemoryStore", "SessionSharing"]

class Harness(TypedDict, total=False):
    """
    Specifies which execution harness to use for the agent run.
    Default (nil/empty) uses Warp's built-in harness.
    """
    type: Literal["oz", "claude", "gemini", "codex"]
    """The harness type identifier.

    - oz: Warp's built-in harness (default)
    - claude: Claude Code harness
    - gemini: Gemini CLI harness
    - codex: Codex CLI harness
    """

class HarnessAuthSecrets(TypedDict, total=False):
    """
    Authentication secrets for third-party harnesses.
    Only the secret for the harness specified gets injected into the environment.
    """
    claude_auth_secret_name: str
    """
    Name of a managed secret for Claude Code harness authentication. The secret must
    exist within the caller's personal or team scope. Only applicable when harness
    type is "claude".
    """

    codex_auth_secret_name: str
    """
    Name of a managed secret for Codex harness authentication. The secret must exist
    within the caller's personal or team scope. Only applicable when harness type is
    "codex".
    """

class InferenceProvidersAws(TypedDict, total=False):
    """
    Configures AWS Bedrock as the LLM inference provider for this
    agent or run.
    """
    disabled: bool
    """If true, opt out of Bedrock at this layer."""

    region: str
    """AWS region used for STS when assuming the Bedrock inference role."""

    role_arn: str
    """IAM role ARN to assume when calling Bedrock."""

class InferenceProviders(TypedDict, total=False):
    """Inference provider settings used for LLM calls."""
    aws: InferenceProvidersAws
    """Configures AWS Bedrock as the LLM inference provider for this agent or run."""

class MemoryStore(TypedDict, total=False):
    """Reference to a memory store to attach to an agent."""
    access: Required[Literal["read_write", "read_only"]]
    """Access level for the store."""

    instructions: Required[str]
    """Instructions for how the agent should use this memory store. Must not be empty."""

    uid: Required[str]
    """UID of the memory store."""

class SessionSharing(TypedDict, total=False):
    """
    Configures sharing behavior for the run's shared session.
    When set, the worker emits `--share public:<level>` and the bundled Warp
    client applies an anyone-with-link ACL to the shared session once it has
    bootstrapped. The same ACL is mirrored onto the backing conversation so
    link viewers can read the conversation without being on the run's team.
    Subject to the workspace-level anyone-with-link sharing setting.
    """
    public_access: Literal["VIEWER", "EDITOR"]
    """
    Grants anyone-with-link access at the specified level to the run's shared
    session and backing conversation.

    - VIEWER: link viewers can read the session and conversation.
    - EDITOR: link viewers can also interact with the session. Anonymous
      (unauthenticated) reads are not supported in this release; link viewers must
      still be authenticated Warp users.
    """

class AmbientAgentConfigParam(TypedDict, total=False):
    """Configuration for a cloud agent run"""
    base_prompt: str
    """Custom base prompt for the agent"""

    computer_use_enabled: bool
    """
    Controls whether computer use is enabled for this agent. If not set, defaults to
    false.
    """

    environment_id: str
    """UID of the environment to run the agent in"""

    harness: Harness
    """
    Specifies which execution harness to use for the agent run. Default (nil/empty)
    uses Warp's built-in harness.
    """

    harness_auth_secrets: HarnessAuthSecrets
    """
    Authentication secrets for third-party harnesses. Only the secret for the
    harness specified gets injected into the environment.
    """

    idle_timeout_minutes: int
    """
    Number of minutes to keep the agent environment alive after task completion. If
    not set, defaults to 10 minutes. Maximum allowed value is min(60,
    floor(max_instance_runtime_seconds / 60) for your billing tier).
    """

    inference_providers: InferenceProviders
    """Inference provider settings used for LLM calls."""

    mcp_servers: Dict[str, McpServerConfigParam]
    """Map of MCP server configurations by name"""

    memory_stores: Iterable[MemoryStore]
    """Memory stores to attach to this run."""

    model_id: str
    """LLM model to use (uses team default if not specified)"""

    name: str
    """
    Human-readable label for grouping, filtering, and traceability. Automatically
    set to the skill name when running a skill-based agent. Set this explicitly to
    categorize runs by intent (e.g., "nightly-dependency-check") so you can filter
    and track them via the name query parameter on GET /agent/runs.
    """

    session_sharing: SessionSharing
    """
    Configures sharing behavior for the run's shared session. When set, the worker
    emits `--share public:<level>` and the bundled Warp client applies an
    anyone-with-link ACL to the shared session once it has bootstrapped. The same
    ACL is mirrored onto the backing conversation so link viewers can read the
    conversation without being on the run's team. Subject to the workspace-level
    anyone-with-link sharing setting.
    """

    skill_spec: str
    """
    Skill specification identifying the primary agent skill to use. Format:
    "{owner}/{repo}:{skill_path}" Example:
    "warpdotdev/warp-server:.claude/skills/deploy/SKILL.md" Mutually exclusive with
    skills in create/update requests. Responses include the first skills entry here
    for backward compatibility. Use the list agents endpoint to discover available
    skills.
    """

    skills: SequenceNotStr[str]
    """
    Ordered skill specifications to attach to the run. Format:
    "{owner}/{repo}:{skill_path}" Example:
    "warpdotdev/warp-server:.claude/skills/deploy/SKILL.md" Mutually exclusive with
    skill_spec in create/update requests.
    """

    worker_host: str
    """
    Self-hosted worker ID that should execute this task. If not specified or set to
    "warp", the task runs on Warp-hosted workers.
    """