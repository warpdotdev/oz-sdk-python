# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..mcp_server_config import McpServerConfig

__all__ = [
    "AgentResponse",
    "Memory",
    "MemoryAttachedStore",
    "MemoryAutoMemory",
    "MemoryAutoMemoryStore",
    "Secret",
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
    3. Oz
    """

    base_model: Optional[str] = None
    """Base model for runs executed by this agent.

    The precedence order for model resolution is:

    1. The model specified on the run itself
    2. The agent's base model
    3. The team's default model
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

    prompt: Optional[str] = None
    """Optional base prompt for this agent"""
