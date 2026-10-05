# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .environment import Environment

__all__ = ["AgentListEnvironmentsResponse"]


class AgentListEnvironmentsResponse(BaseModel):
    environments: List[Environment]
    """List of accessible cloud environments"""
