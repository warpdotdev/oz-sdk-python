# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["AgentCreateParams", "InferenceProviders", "InferenceProvidersAws", "MemoryStore", "Secret"]


class AgentCreateParams(TypedDict, total=False):
    name: Required[str]
    """A name for the agent"""

    base_model: Optional[str]
    """Optional base model for runs executed by this agent."""

    description: Optional[str]
    """Optional description of the agent"""

    inference_providers: InferenceProviders
    """Inference provider settings used for LLM calls."""

    memory_stores: Iterable[MemoryStore]
    """
    Optional list of memory stores to attach to the agent. Each store must be
    team-owned by the same team as the agent. Duplicate UIDs within a single request
    are rejected.
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


class InferenceProvidersAws(TypedDict, total=False):
    """
    Configures AWS Bedrock as the LLM inference provider for this
    agent or run.
    """

    disabled: bool
    """If true, opt out of Bedrock at this layer."""

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


class Secret(TypedDict, total=False):
    """Reference to a managed secret by name."""

    name: Required[str]
    """Name of the managed secret."""
