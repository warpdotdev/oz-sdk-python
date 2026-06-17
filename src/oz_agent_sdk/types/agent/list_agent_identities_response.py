# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import List

from .agent_response import AgentResponse

__all__ = ["ListAgentIdentitiesResponse"]

class ListAgentIdentitiesResponse(BaseModel):
    agents: List[AgentResponse]