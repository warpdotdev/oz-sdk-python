# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import List

from .agent_skill import AgentSkill

__all__ = ["AgentListResponse"]

class AgentListResponse(BaseModel):
    agents: List[AgentSkill]
    """List of available agents"""