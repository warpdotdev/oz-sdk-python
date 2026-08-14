# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .mcp_server_config import McpServerConfig

__all__ = [
    "AmbientAgentConfig",
    "Harness",
    "HarnessAuthSecrets",
    "InferenceProviders",
    "InferenceProvidersAws",
    "MemoryStore",
    "SessionSharing",
]


class Harness(BaseModel):
    """
    Specifies which execution harness to use for the agent run.
    Default (nil/empty) uses Warp's built-in harness.
    When stored as a named agent's default (create/update agent identity),
    this field replaces the deprecated base_harness/base_model pair: a
    non-oz type here requires the agent's base_model to be empty, since
    the two describe mutually exclusive default models.
    """

    api_model_id: Optional[str] = FieldInfo(alias="model_id", default=None)
    """Model to use with a third-party harness (e.g.

    "claude-haiku-4-5"). Only applies when type is a non-oz harness; the top-level
    config model_id targets the built-in Oz harness instead. When omitted or empty,
    the harness uses its own default model.
    """

    reasoning_level: Optional[str] = None
    """Reasoning effort for harnesses that support it (e.g.

    Codex). Only applies when type is a non-oz harness. Ignored by harnesses that do
    not support reasoning levels.
    """

    type: Optional[Literal["oz", "claude", "gemini", "codex"]] = None
    """The harness type identifier.

    - oz: Warp's built-in harness (default)
    - claude: Claude Code harness
    - gemini: Gemini CLI harness
    - codex: Codex CLI harness
    """


class HarnessAuthSecrets(BaseModel):
    """
    Authentication secrets for third-party harnesses.
    Only the secret for the harness specified gets injected into the environment.
    """

    claude_auth_secret_name: Optional[str] = None
    """
    Name of a managed secret for Claude Code harness authentication. The secret must
    exist within the caller's personal or team scope. Only applicable when harness
    type is "claude".
    """

    codex_auth_secret_name: Optional[str] = None
    """
    Name of a managed secret for Codex harness authentication. The secret must exist
    within the caller's personal or team scope. Only applicable when harness type is
    "codex".
    """


class InferenceProvidersAws(BaseModel):
    """
    Configures AWS Bedrock as the LLM inference provider for this
    agent or run.
    """

    disabled: Optional[bool] = None
    """If true, opt out of Bedrock at this layer."""

    region: Optional[str] = None
    """AWS region used for STS when assuming the Bedrock inference role."""

    role_arn: Optional[str] = None
    """IAM role ARN to assume when calling Bedrock."""


class InferenceProviders(BaseModel):
    """Inference provider settings used for LLM calls."""

    aws: Optional[InferenceProvidersAws] = None
    """Configures AWS Bedrock as the LLM inference provider for this agent or run."""


class MemoryStore(BaseModel):
    """Reference to a memory store to attach to an agent."""

    access: Literal["read_write", "read_only"]
    """Access level for the store."""

    instructions: str
    """Instructions for how the agent should use this memory store. Must not be empty."""

    uid: str
    """UID of the memory store."""


class SessionSharing(BaseModel):
    """
    Configures sharing behavior for the run's shared session.
    When set, the worker emits `--share public:<level>` and the bundled Warp
    client applies an anyone-with-link ACL to the shared session once it has
    bootstrapped. The same ACL is mirrored onto the backing conversation so
    link viewers can read the conversation without being on the run's team.
    Subject to the workspace-level anyone-with-link sharing setting.
    """

    public_access: Optional[Literal["VIEWER", "EDITOR"]] = None
    """
    Grants anyone-with-link access at the specified level to the run's shared
    session and backing conversation.

    - VIEWER: link viewers can read the session and conversation.
    - EDITOR: link viewers can also interact with the session. Anonymous
      (unauthenticated) reads are not supported in this release; link viewers must
      still be authenticated Warp users.
    """


class AmbientAgentConfig(BaseModel):
    """Configuration for a cloud agent run"""

    base_prompt: Optional[str] = None
    """Custom base prompt for the agent"""

    computer_use_enabled: Optional[bool] = None
    """
    Controls whether computer use is enabled for this agent. If not set, defaults to
    true.
    """

    credential_strategy: Optional[Literal["CREATOR", "EXECUTOR"]] = None
    """
    Controls which principal's credentials are used when the platform mints tokens
    (e.g. GitHub or GitLab OAuth tokens) on behalf of this run.

    - EXECUTOR (default when unset): credentials are sourced from the run's
      execution principal. For agent principals this produces a GitHub App
      installation token; for user principals this produces their personal OAuth
      token.
    - CREATOR: credentials are always sourced from the run creator, regardless of
      the execution principal. Useful when a service account executes the run but
      Git operations should authenticate as the human who triggered it. When unset,
      behavior is identical to EXECUTOR and no additional pre-flight validation is
      performed.
    """

    environment_id: Optional[str] = None
    """UID of the environment to run the agent in"""

    harness: Optional[Harness] = None
    """
    Specifies which execution harness to use for the agent run. Default (nil/empty)
    uses Warp's built-in harness. When stored as a named agent's default
    (create/update agent identity), this field replaces the deprecated
    base_harness/base_model pair: a non-oz type here requires the agent's base_model
    to be empty, since the two describe mutually exclusive default models.
    """

    harness_auth_secrets: Optional[HarnessAuthSecrets] = None
    """
    Authentication secrets for third-party harnesses. Only the secret for the
    harness specified gets injected into the environment.
    """

    idle_timeout_minutes: Optional[int] = None
    """
    Number of minutes to keep the agent environment alive after task completion. If
    not set, defaults to 10 minutes. Maximum allowed value is min(60,
    floor(max_instance_runtime_seconds / 60) for your billing tier).
    """

    inference_providers: Optional[InferenceProviders] = None
    """Inference provider settings used for LLM calls."""

    mcp_servers: Optional[Dict[str, McpServerConfig]] = None
    """Map of MCP server configurations by name"""

    memory_stores: Optional[List[MemoryStore]] = None
    """Memory stores to attach to this run."""

    api_model_id: Optional[str] = FieldInfo(alias="model_id", default=None)
    """LLM model to use (uses team default if not specified)"""

    name: Optional[str] = None
    """
    Human-readable label for grouping, filtering, and traceability. Automatically
    set to the skill name when running a skill-based agent. Set this explicitly to
    categorize runs by intent (e.g., "nightly-dependency-check") so you can filter
    and track them via the name query parameter on GET /agent/runs.
    """

    runner_id: Optional[str] = None
    """
    UID of the runner providing the run's compute (platform, instance shape, and
    setup commands). When omitted on a request, the runner is resolved at run
    creation from the agent's default runner, then the environment's default runner,
    and the resolved UID is recorded on the run.
    """

    session_sharing: Optional[SessionSharing] = None
    """
    Configures sharing behavior for the run's shared session. When set, the worker
    emits `--share public:<level>` and the bundled Warp client applies an
    anyone-with-link ACL to the shared session once it has bootstrapped. The same
    ACL is mirrored onto the backing conversation so link viewers can read the
    conversation without being on the run's team. Subject to the workspace-level
    anyone-with-link sharing setting.
    """

    skill_spec: Optional[str] = None
    """
    Skill specification identifying the primary agent skill to use. Format:
    "{owner}/{repo}:{skill_path}" Example:
    "warpdotdev/warp-server:.claude/skills/deploy/SKILL.md" Mutually exclusive with
    skills in create/update requests. Responses include the first skills entry here
    for backward compatibility. Use the list agents endpoint to discover available
    skills.
    """

    skills: Optional[List[str]] = None
    """
    Ordered skill specifications to attach to the run. Format:
    "{owner}/{repo}:{skill_path}" Example:
    "warpdotdev/warp-server:.claude/skills/deploy/SKILL.md" Mutually exclusive with
    skill_spec in create/update requests.
    """

    worker_host: Optional[str] = None
    """
    Self-hosted worker ID that should execute this task. If not specified or set to
    "warp", the task runs on Warp-hosted workers.
    """
