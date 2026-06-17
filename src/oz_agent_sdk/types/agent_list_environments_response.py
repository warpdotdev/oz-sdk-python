# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import List

from .cloud_environment import CloudEnvironment

__all__ = ["AgentListEnvironmentsResponse"]

class AgentListEnvironmentsResponse(BaseModel):
    environments: List[CloudEnvironment]
    """List of accessible cloud environments"""