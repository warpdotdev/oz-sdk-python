# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..mcp_server_config import McpServerConfig

__all__ = [
    "AgentResponse",
    "Memory",
    "MemoryAttachedStore",
    "MemoryAutoMemory",
    "MemoryAutoMemoryStore",
    "Secret",
    "Harness",
    "HarnessAuthSecrets",
    "InferenceProviders",
    "InferenceProvidersAws",
]


class MemoryAttachedStore(BaseModel):
    """Reference to a memory store to attach to an agent."""

    access: Literal["read_write", "read_only"]
    """Access level for the store."""

    instructions: str
    """Instructions for how the agent should use this memory store. Must not be empty."""

    uid: str
    """UID of the memory store."""


class MemoryAutoMemoryStore(BaseModel):
    """Memory store attached to an agent."""

    access: Literal["read_write", "read_only"]
    """Access level for the store."""

    instructions: str
    """Instructions for how the agent should use this memory store."""

    owner_type: Literal["user", "service_account", "team"]
    """Public owner type."""

    owner_uid: str
    """Public UID of the user, service account, or team that owns the memory store."""

    uid: str
    """UID of the memory store."""

    description: Optional[str] = None
    """Optional description for the memory store."""


class MemoryAutoMemory(BaseModel):
    """Auto-memory state for an agent."""

    enabled: bool
    """Whether this agent has an agent-owned memory store."""

    store: Optional[MemoryAutoMemoryStore] = None
    """Memory store attached to an agent."""


class Memory(BaseModel):
    """Memory settings for an agent."""

    attached_stores: List[MemoryAttachedStore]
    """Team memory stores attached to the agent."""

    auto_memory: MemoryAutoMemory
    """Auto-memory state for an agent."""


class Secret(BaseModel):
    """Reference to a managed secret by name."""

    name: str
    """Name of the managed secret."""


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


class AgentResponse(BaseModel):
    available: bool
    """Whether this agent is within the team's plan limit and can be used for runs"""

    created_at: datetime
    """When the agent was created (RFC3339)"""

    default_runner_uid: str
    """Default runner UID for runs executed by this agent.

    When set, it overrides the selected environment's default runner for runs that
    do not specify their own `runner_id`. The precedence order for runner resolution
    is:

    1. The runner specified on the run itself
    2. The agent's default runner
    3. The selected environment's default runner
    4. The environment's legacy inline compute fields
    5. System defaults
    """

    memory: Memory
    """Memory settings for an agent."""

    name: str
    """Name of the agent"""

    secrets: List[Secret]
    """Secrets that this agent may access by default."""

    skills: List[str]
    """
    Ordered list of normalized skill specs associated with this agent. Always
    present; empty when no skills are attached.
    """

    uid: str
    """Unique identifier for the agent"""

    updated_at: datetime
    """When the agent was last updated (RFC3339)"""

    agent_type: Optional[Literal["FOREMAN", "TRIAGE", "SPEC", "IMPLEMENT", "REVIEW", "VERIFY", "CUSTOM"]] = None
    """The well-known type of a named agent.

    The built-in factory agents use FOREMAN, TRIAGE, SPEC, IMPLEMENT, REVIEW, or
    VERIFY; every other agent is CUSTOM.
    """

    base_harness: Optional[str] = None
    """Default harness for runs executed by this agent.

    The precedence order for harness resolution is:

    1. The harness specified on the run itself
    2. The agent's base harness
    3. Oz Deprecated - use harness instead, which carries the full {type, model_id,
       reasoning_level} default.
    """

    base_model: Optional[str] = None
    """Base model for runs executed by this agent.

    The precedence order for model resolution is:

    1. The model specified on the run itself
    2. The agent's base model
    3. The team's default model
    """

    credential_strategy: Optional[Literal["CREATOR", "EXECUTOR"]] = None
    """Default credential strategy for runs executed by a named agent.

    - EXECUTOR: runs authenticate with the named agent's own credentials (e.g. a
      GitHub App installation token for the agent's team).
    - CREATOR: runs authenticate with the credentials of the principal that created
      the run. Unlike the factory default, an agent may leave this unset. The
      strategy applied to a run is resolved in this order: the run's
      config.credential_strategy, then the agent's default, then the factory's
      default for factory-seeded agents, and finally EXECUTOR. The inherited
      strategy is validated at run creation time (the required credential must be
      mintable), like an explicit run-level value.
    """

    description: Optional[str] = None
    """Optional description of the agent"""

    environment_id: Optional[str] = None
    """Default cloud environment ID for runs executed by this agent.

    The precedence order for environment resolution is:

    1. The environment specified on the run itself
    2. The agent's default environment
    3. An empty environment
    """

    factory_uid: Optional[str] = None
    """UID of the Factory this agent was seeded for.

    Null (or omitted) for agents that do not belong to a factory.
    """

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

    inference_providers: Optional[InferenceProviders] = None
    """Inference provider settings used for LLM calls."""

    mcp_servers: Optional[Dict[str, McpServerConfig]] = None
    """
    MCP server configurations attached to this agent by default. Run-level MCP
    config takes precedence over this agent-level default.
    """

    on_behalf_of_enabled: Optional[bool] = None
    """
    Whether runs created with this agent's API key may use the on_behalf_of field to
    attribute runs to another team member.
    """

    prompt: Optional[str] = None
    """Optional base prompt for this agent"""
