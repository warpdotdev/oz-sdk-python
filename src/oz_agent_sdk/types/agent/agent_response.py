# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["AgentResponse", "Secret"]


class Secret(BaseModel):
    """Reference to a managed secret by name."""

    name: str
    """Name of the managed secret."""


class AgentResponse(BaseModel):
    available: bool
    """Whether this agent is within the team's plan limit and can be used for runs"""

    created_at: datetime
    """When the agent was created (RFC3339)"""

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

    description: Optional[str] = None
    """Optional description of the agent"""
