# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "AgentUpdateParams",
    "HarnessAuthSecrets",
    "InferenceProviders",
    "InferenceProvidersAws",
    "MemoryStore",
    "Secret",
]


class AgentUpdateParams(TypedDict, total=False):
    base_harness: Optional[str]
    """Replacement default harness.

    Omit or pass `null` to leave unchanged, or pass an empty string to clear.
    """

    base_model: Optional[str]
    """Replacement base model.

    Omit or pass `null` to leave unchanged, or pass an empty string to clear.
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

    memory_stores: Optional[Iterable[MemoryStore]]
    """Replacement list of memory stores.

    Omit to leave unchanged, pass an empty array to clear, or pass a non-empty array
    to replace.
    """

    name: str
    """The new name for the agent"""

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
