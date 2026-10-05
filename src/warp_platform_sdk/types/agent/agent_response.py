# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..harness import Harness
from ..._models import BaseModel
from ..secret_ref import SecretRef
from .memory_response import MemoryResponse
from ..mcp_server_config import McpServerConfig
from ..harness_auth_secrets import HarnessAuthSecrets
from ..inference_providers_config import InferenceProvidersConfig

__all__ = ["AgentResponse"]


class AgentResponse(BaseModel):
    available: bool
    """Whether the agent is currently enabled. Defaults to true."""

    created_at: datetime
    """When the agent was created (RFC3339)"""

    default_runner_uid: str
    """
    Default runner UID for runs executed by this agent; when set, it overrides the
    selected environment's default runner for runs that do not specify their own
    `runner_id`. The precedence order for runner resolution is:

    1. The runner specified on the run itself
    2. The agent's default runner
    3. The selected environment's default runner
    4. The environment's legacy inline compute fields
    5. System defaults
    """

    memory: MemoryResponse
    """Memory settings for an agent."""

    name: str
    """Name of the agent"""

    secrets: List[SecretRef]
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
    """
    Default harness for runs executed by this agent; the precedence order for
    harness resolution is:

    1. The harness specified on the run itself
    2. The agent's base harness
    3. Warp Deprecated: use harness instead, which carries the full {type, model_id,
       reasoning_level} default.
    """

    base_model: Optional[str] = None
    """
    Base model for runs executed by this agent; the precedence order for model
    resolution is:

    1. The model specified on the run itself
    2. The agent's base model
    3. The team's default model
    """

    credential_strategy: Optional[Literal["CREATOR", "EXECUTOR"]] = None
    """
    Default credential strategy for runs executed by a named agent; an agent may
    leave this unset (see AgentResponse.credential_strategy for the full resolution
    order).

    - EXECUTOR: runs authenticate with the named agent's own credentials (e.g. a
      GitHub App installation token for the agent's team).
    - CREATOR: runs authenticate with the credentials of the principal that created
      the run.
    """

    description: Optional[str] = None
    """Optional description of the agent"""

    environment_id: Optional[str] = None
    """
    Default cloud environment ID for runs executed by this agent; the precedence
    order for environment resolution is:

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
    base_harness/base_model pair: a harness other than `oz` here requires the
    agent's base_model to be empty, since the two describe mutually exclusive
    default models.
    """

    harness_auth_secrets: Optional[HarnessAuthSecrets] = None
    """
    Authentication secrets for third-party harnesses. Only the secret for the
    harness specified gets injected into the environment.
    """

    inference_providers: Optional[InferenceProvidersConfig] = None
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

    worker_host: Optional[str] = None
    """
    Default worker host for runs executed by this agent, or empty when unset; the
    precedence order for worker host resolution is:

    1. The host specified on the run itself
    2. The agent's default host
    3. The workspace default host
    """
