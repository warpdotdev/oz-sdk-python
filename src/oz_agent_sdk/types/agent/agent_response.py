# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["AgentResponse"]


class AgentResponse(BaseModel):
    available: bool
    """Whether this agent is within the team's plan limit and can be used for runs"""

    created_at: datetime
    """When the agent was created (RFC3339)"""

    name: str
    """Name of the agent"""

    uid: str
    """Unique identifier for the agent"""
