# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr
from ..harness_param import HarnessParam
from ..secret_ref_param import SecretRefParam
from ..memory_store_ref_param import MemoryStoreRefParam
from ..mcp_server_config_param import McpServerConfigParam
from ..harness_auth_secrets_param import HarnessAuthSecretsParam
from ..inference_providers_config_param import InferenceProvidersConfigParam

__all__ = ["AgentUpdateParams", "Memory"]


class AgentUpdateParams(TypedDict, total=False):
    agent_type: Optional[Literal["FOREMAN", "TRIAGE", "SPEC", "IMPLEMENT", "REVIEW", "VERIFY", "CUSTOM"]]
    """The well-known type of a named agent.

    The built-in factory agents use FOREMAN, TRIAGE, SPEC, IMPLEMENT, REVIEW, or
    VERIFY; every other agent is CUSTOM.
    """

    base_harness: Optional[str]
    """
    Replacement default harness; omit or pass `null` to leave unchanged, or pass an
    empty string to clear. Deprecated - use harness instead, kept only for backward
    compatibility: when both are sent, harness is authoritative and a conflicting
    type is rejected with invalid_request.
    """

    base_model: Optional[str]
    """Replacement base model.

    Omit or pass `null` to leave unchanged, or pass an empty string to clear.
    """

    credential_strategy: Optional[Literal["CREATOR", "EXECUTOR"]]
    """
    Default credential strategy for runs executed by a named agent; an agent may
    leave this unset (see AgentResponse.credential_strategy for the full resolution
    order).

    - EXECUTOR: runs authenticate with the named agent's own credentials (e.g. a
      GitHub App installation token for the agent's team).
    - CREATOR: runs authenticate with the credentials of the principal that created
      the run.
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

    harness: Optional[HarnessParam]
    """
    Specifies which execution harness to use for the agent run. Default (nil/empty)
    uses Warp's built-in harness. When stored as a named agent's default
    (create/update agent identity), this field replaces the deprecated
    base_harness/base_model pair: a harness other than `oz` here requires the
    agent's base_model to be empty, since the two describe mutually exclusive
    default models.
    """

    harness_auth_secrets: Optional[HarnessAuthSecretsParam]
    """
    Authentication secrets for third-party harnesses. Only the secret for the
    harness specified gets injected into the environment.
    """

    inference_providers: Optional[InferenceProvidersConfigParam]
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

    secrets: Optional[Iterable[SecretRefParam]]
    """Replacement list of secrets.

    Omit to leave unchanged, pass an empty array to clear, or pass a non-empty array
    to replace. Duplicate names are rejected.
    """

    skills: Optional[SequenceNotStr[str]]
    """Replacement list of skill specs.

    Omit to leave unchanged, pass an empty array to clear, or pass a non-empty array
    to replace.
    """

    worker_host: Optional[str]
    """Replacement default worker host.

    Omit or pass `null` to leave unchanged, or pass an empty string to clear (the
    workspace default then applies). A non-empty value is trimmed and replaces the
    stored default; use "warp" to force Warp-hosted execution over a self-hosted
    workspace default.
    """


class Memory(TypedDict, total=False):
    """Memory settings for updating an agent."""

    attached_stores: Optional[Iterable[MemoryStoreRefParam]]
    """Replacement list of attached team memory stores.

    Omit to leave unchanged, pass an empty array to clear, or pass a non-empty array
    to replace.
    """
