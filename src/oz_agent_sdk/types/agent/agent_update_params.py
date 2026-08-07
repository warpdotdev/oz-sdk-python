# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr
from ..mcp_server_config_param import McpServerConfigParam

__all__ = [
    "AgentUpdateParams",
    "HarnessAuthSecrets",
    "InferenceProviders",
    "InferenceProvidersAws",
    "Memory",
    "MemoryAttachedStore",
    "Secret",
]


class AgentUpdateParams(TypedDict, total=False):
    agent_type: Optional[Literal["FOREMAN", "TRIAGE", "SPEC", "IMPLEMENT", "REVIEW", "VERIFY", "CUSTOM"]]
    """The well-known type of a named agent.

    The built-in factory agents use FOREMAN, TRIAGE, SPEC, IMPLEMENT, REVIEW, or
    VERIFY; every other agent is CUSTOM.
    """

    base_harness: Optional[str]
    """Replacement default harness.

    Omit or pass `null` to leave unchanged, or pass an empty string to clear.
    """

    base_model: Optional[str]
    """Replacement base model.

    Omit or pass `null` to leave unchanged, or pass an empty string to clear.
    """

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
    """Replacement default runner UID.

    Omit or pass `null` to leave unchanged, or pass an empty string to clear. A
    non-empty value must reference a runner the editor can View.
    """

    description: Optional[str]
    """Replacement description.

    Omit or pass `null` to leave unchanged, or use an empty value to clear.
    """

    environment_id: Optional[str]
    """Replacement default cloud environment ID.

    Omit or pass `null` to leave unchanged, or pass an empty string to clear.
    """

    harness_auth_secrets: Optional[HarnessAuthSecrets]
    """
    Authentication secrets for third-party harnesses. Only the secret for the
    harness specified gets injected into the environment.
    """

    inference_providers: Optional[InferenceProviders]
    """Inference provider settings used for LLM calls."""

    mcp_servers: Dict[str, McpServerConfigParam]
    """Replacement map of MCP server configurations by name.

    Omit to leave unchanged, pass an empty object to clear, or pass a non-empty
    object to replace. Run-level MCP config takes precedence over this agent-level
    default.
    """

    memory: Optional[Memory]
    """Memory settings for updating an agent."""

    name: str
    """The new name for the agent"""

    on_behalf_of_enabled: Optional[bool]
    """
    Whether runs created with this agent's API key may use the on_behalf_of field to
    attribute runs to another team member. Omit or pass `null` to leave unchanged.
    Only team admins may set this field.
    """

    prompt: Optional[str]
    """Replacement prompt.

    Omit or pass `null` to leave unchanged, or use an empty value to clear.
    """

    secrets: Optional[Iterable[Secret]]
    """Replacement list of secrets.

    Omit to leave unchanged, pass an empty array to clear, or pass a non-empty array
    to replace. Duplicate names are rejected.
    """

    skills: Optional[SequenceNotStr[str]]
    """Replacement list of skill specs.

    Omit to leave unchanged, pass an empty array to clear, or pass a non-empty array
    to replace.
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


class Memory(TypedDict, total=False):
    """Memory settings for updating an agent."""

    attached_stores: Optional[Iterable[MemoryAttachedStore]]
    """Replacement list of attached team memory stores.

    Omit to leave unchanged, pass an empty array to clear, or pass a non-empty array
    to replace.
    """


class Secret(TypedDict, total=False):
    """Reference to a managed secret by name."""

    name: Required[str]
    """Name of the managed secret."""
