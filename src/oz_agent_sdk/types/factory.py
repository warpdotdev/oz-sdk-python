# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .mcp_server_config import McpServerConfig

__all__ = [
    "Factory",
    "AgentDefaults",
    "AgentDefaultsSecret",
    "AgentDefaultsHarness",
    "AgentDefaultsHarnessAuthSecrets",
    "Integration",
    "Repository",
    "Scoring",
    "Creator",
]


class AgentDefaultsSecret(BaseModel):
    """Reference to a managed secret by name."""

    name: str
    """Name of the managed secret."""


class AgentDefaultsHarness(BaseModel):
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
    config model_id targets the built-in Warp harness instead. When omitted or
    empty, the harness uses its own default model.
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


class AgentDefaultsHarnessAuthSecrets(BaseModel):
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


class AgentDefaults(BaseModel):
    """
    Default execution settings inherited by the factory's named agents
    when they declare no override of their own.
    """

    default_runner_uid: str
    """Default runner UID for the factory's named agents.

    Empty when unset, in which case the environment's default runner applies.
    """

    mcp_servers: Dict[str, McpServerConfig]
    """MCP server configurations attached to the factory's named agents by default.

    Only warp_id (managed MCP) entries are representable for a Warp-managed factory.
    """

    secrets: List[AgentDefaultsSecret]
    """Secrets attached to the factory's named agents by default."""

    worker_host: str
    """Default worker host for the factory's named agents.

    Empty when unset, in which case the workspace default applies.
    """

    harness: Optional[AgentDefaultsHarness] = None
    """
    Specifies which execution harness to use for the agent run. Default (nil/empty)
    uses Warp's built-in harness. When stored as a named agent's default
    (create/update agent identity), this field replaces the deprecated
    base_harness/base_model pair: a non-oz type here requires the agent's base_model
    to be empty, since the two describe mutually exclusive default models.
    """

    harness_auth_secrets: Optional[AgentDefaultsHarnessAuthSecrets] = None
    """
    Authentication secrets for third-party harnesses. Only the secret for the
    harness specified gets injected into the environment.
    """


class Integration(BaseModel):
    """An integration provider attached to a factory."""

    type: Literal["jira", "linear", "slack"]
    """Integration provider that can be attached to a factory.

    github is not accepted here; repository access comes from the factory's code
    forge.
    """


class Repository(BaseModel):
    """A repository scoped to a factory."""

    owner: str
    """Repository owner (or full namespace for GitLab)."""

    repo: str
    """Repository name."""


class Scoring(BaseModel):
    default_model: Optional[str] = None
    """
    Optional factory override for the model used by managed scorers and
    scorer-creation prefills. null or absent resolves to the platform judge default.
    User-created scorers still require an explicit model_id on create.
    """


class Creator(BaseModel):
    """The user who created a factory, when resolvable."""

    uid: str
    """Firebase UID of the user who created the factory."""

    email: Optional[str] = None
    """Creator's email, when available."""


class Factory(BaseModel):
    """Public representation of a factory."""

    agent_defaults: AgentDefaults
    """
    Default execution settings inherited by the factory's named agents when they
    declare no override of their own.
    """

    alias: Optional[str] = None
    """
    Optional display handle for the factory, unique across the team's Warp workspace
    when set.
    """

    avatar_url: Optional[str] = None
    """Short-lived signed URL for displaying the factory's avatar.

    The URL may change between reads.
    """

    code_forge: Literal["GITHUB", "GITLAB", "NONE"]
    """Source-control provider hosting the factory's repositories.

    NONE declares a repo-less factory with no native repositories; its environment
    relies on setup_commands to clone from any host instead.
    """

    created_at: datetime
    """Time the factory was created."""

    credential_strategy: Literal["CREATOR", "EXECUTOR"]
    """Default credential strategy for runs executed by the factory's named agents.

    Factories default to EXECUTOR.

    - EXECUTOR: runs authenticate with the named agent's own credentials (e.g. a
      GitHub App installation token for the factory's team).
    - CREATOR: runs authenticate with the credentials of the principal that created
      the run. A run-level config.credential_strategy always takes precedence over
      this factory default. The strategy inherited from the factory is validated at
      run creation time (the required credential must be mintable), like an explicit
      run-level value.
    """

    default_environment: Optional[str] = None
    """Public UID of the factory's default environment.

    File-managed factories may omit this default.
    """

    default_model: Optional[str] = None
    """The default model ID for the factory's runs.

    File-managed factories may omit this default. Live-managed create and PATCH
    requests still capture a concrete validated model ID.
    """

    description: Optional[str] = None
    """Optional description of the factory."""

    integrations: Optional[List[Integration]] = None
    """
    Integration providers attached to the factory, independent of the automation
    triggers configured for it. null means the factory has not declared anything
    yet; an empty array means no providers are attached.
    """

    name: str
    """Display name of the factory."""

    repositories: List[Repository]
    """Repositories scoped to the factory, independent of its default environment."""

    scoring: Scoring

    team_uid: str
    """Public UID of the team that owns the factory."""

    uid: str
    """Public UID of the factory."""

    updated_at: datetime
    """Time the factory was last updated."""

    creator: Optional[Creator] = None
    """The user who created a factory, when resolvable."""
