# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AgentResponse", "MemoryStore", "Secret", "InferenceProviders", "InferenceProvidersAws"]


class MemoryStore(BaseModel):
    """Reference to a memory store to attach to an agent."""

    access: Literal["read_write", "read_only"]
    """Access level for the store."""

    instructions: str
    """Instructions for how the agent should use this memory store. Must not be empty."""

    uid: str
    """UID of the memory store."""


class Secret(BaseModel):
    """Reference to a managed secret by name."""

    name: str
    """Name of the managed secret."""


class InferenceProvidersAws(BaseModel):
    """
    Configures AWS Bedrock as the LLM inference provider for this
    agent or run.
    """

    disabled: Optional[bool] = None
    """If true, opt out of Bedrock at this layer."""

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

    memory_stores: List[MemoryStore]
    """
    Memory stores attached to this agent. Always present; empty when no stores are
    attached.
    """

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

    base_model: Optional[str] = None
    """Base model for runs executed by this agent.

    The precedence order for model resolution is:

    1. The model specified on the run itself
    2. The agent's base model
    3. The team's default model
    """

    description: Optional[str] = None
    """Optional description of the agent"""

    inference_providers: Optional[InferenceProviders] = None
    """Inference provider settings used for LLM calls."""

    prompt: Optional[str] = None
    """Optional base prompt for this agent"""
