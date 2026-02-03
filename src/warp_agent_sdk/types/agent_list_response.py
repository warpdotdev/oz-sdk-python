# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .agent_skill import AgentSkill

__all__ = ["AgentListResponse"]


class AgentListResponse(BaseModel):
    agents: List[AgentSkill]
    """List of available agents"""
