# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr
from ..mcp_server_config_param import McpServerConfigParam

__all__ = [
    "AgentCreateParams",
    "Harness",
    "HarnessAuthSecrets",
    "InferenceProviders",
    "InferenceProvidersAws",
    "Memory",
    "MemoryAttachedStore",
    "MemoryAutoMemory",
    "Secret",
]


class AgentCreateParams(TypedDict, total=False):
    name: Required[str]
    """A name for the agent"""

    agent_type: Optional[Literal["FOREMAN", "TRIAGE", "SPEC", "IMPLEMENT", "REVIEW", "VERIFY", "CUSTOM"]]
    """The well-known type of a named agent.

    The built-in factory agents use FOREMAN, TRIAGE, SPEC, IMPLEMENT, REVIEW, or
    VERIFY; every other agent is CUSTOM.
    """

    base_harness: Optional[str]
    """
    Optional default harness for runs executed by this agent. Deprecated - use
    harness instead. Kept for backward compatibility; when both are sent, harness is
    authoritative and a conflicting type is rejected with invalid_request.
    """

    base_model: Optional[str]
    """Optional base model for runs executed by this agent."""

    credential_strategy: Optional[Literal["CREATOR", "EXECUTOR"]]
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

    default_runner_uid: Optional[str]
    """Optional default runner UID for runs executed by this agent.

    When set, it overrides the selected environment's default runner for runs that
    do not specify their own `runner_id`. The editor must have View permission on
    the referenced runner.
    """

    description: Optional[str]
    """Optional description of the agent"""

    environment_id: Optional[str]
    """
    Optional default cloud environment ID for runs executed by this agent. The
    environment must be owned by the same team as the agent.
    """

    factory_uid: Optional[str]
    """Optional UID of the Factory to link this agent to.

    When omitted, the agent is not linked to any factory.
    """

    harness: Harness
    """
    Specifies which execution harness to use for the agent run. Default (nil/empty)
    uses Warp's built-in harness. When stored as a named agent's default
    (create/update agent identity), this field replaces the deprecated
    base_harness/base_model pair: a non-oz type here requires the agent's base_model
    to be empty, since the two describe mutually exclusive default models.
    """

    harness_auth_secrets: HarnessAuthSecrets
    """
    Authentication secrets for third-party harnesses. Only the secret for the
    harness specified gets injected into the environment.
    """

    inference_providers: InferenceProviders
    """Inference provider settings used for LLM calls."""

    mcp_servers: Dict[str, McpServerConfigParam]
    """
    Optional map of MCP server configurations by name to attach to runs executed by
    this agent. Run-level MCP config takes precedence over this agent-level default.
    """

    memory: Memory
    """Memory settings for creating an agent."""

    on_behalf_of_enabled: bool
    """
    Whether runs created with this agent's API key may use the on_behalf_of field to
    attribute runs to another team member. Defaults to false. Only team admins may
    set this field.
    """

    prompt: Optional[str]
    """Optional base prompt for this agent"""

    secrets: Iterable[Secret]
    """
    Optional list of secrets associated with the agent. Duplicate names within a
    single request are rejected. Each entry is unioned into the run-time secret
    scope when the agent executes.
    """

    skills: SequenceNotStr[str]
    """
    Optional list of skill specs to associate with the agent. Format:
    "{owner}/{repo}:{skill_path}" (e.g.,
    "warpdotdev/warp-server:.claude/skills/deploy/SKILL.md"). Each spec is validated
    and normalized at attach time using the team's GitHub credentials; inaccessible
    or malformed specs are rejected.
    """

    worker_host: Optional[str]
    """
    Optional default worker host for runs executed by this agent. Omission, null, or
    an empty value stores no Agent default, in which case the workspace default
    applies. A non-empty value is trimmed and stored; use "warp" to force
    Warp-hosted execution over a self-hosted workspace default. The precedence order
    for worker host resolution is:

    1. The host specified on the run itself
    2. The agent's default host
    3. The workspace default host
    """


class Harness(TypedDict, total=False):
    """
    Specifies which execution harness to use for the agent run.
    Default (nil/empty) uses Warp's built-in harness.
    When stored as a named agent's default (create/update agent identity),
    this field replaces the deprecated base_harness/base_model pair: a
    non-oz type here requires the agent's base_model to be empty, since
    the two describe mutually exclusive default models.
    """

    model_id: str
    """Model to use with a third-party harness (e.g.

    "claude-haiku-4-5"). Only applies when type is a non-oz harness; the top-level
    config model_id targets the built-in Warp harness instead. When omitted or
    empty, the harness uses its own default model.
    """

    reasoning_level: str
    """Reasoning effort for harnesses that support it (e.g.

    Codex). Only applies when type is a non-oz harness. Ignored by harnesses that do
    not support reasoning levels.
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


class MemoryAttachedStore(TypedDict, total=False):
    """Reference to a memory store to attach to an agent."""

    access: Required[Literal["read_write", "read_only"]]
    """Access level for the store."""

    instructions: Required[str]
    """Instructions for how the agent should use this memory store. Must not be empty."""

    uid: Required[str]
    """UID of the memory store."""


class MemoryAutoMemory(TypedDict, total=False):
    """Auto-memory settings for creating an agent."""

    enabled: bool
    """
    Whether to create and attach a default service-account-owned memory store for
    this agent. Defaults to true when omitted.
    """


class Memory(TypedDict, total=False):
    """Memory settings for creating an agent."""

    attached_stores: Iterable[MemoryAttachedStore]
    """
    Existing team memory stores to attach to the agent. Duplicate UIDs within a
    single request are rejected.
    """

    auto_memory: MemoryAutoMemory
    """Auto-memory settings for creating an agent."""


class Secret(TypedDict, total=False):
    """Reference to a managed secret by name."""

    name: Required[str]
    """Name of the managed secret."""
