# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import List

from .scheduled_agent_item import ScheduledAgentItem

__all__ = ["ScheduleListResponse"]

class ScheduleListResponse(BaseModel):
    schedules: List[ScheduledAgentItem]
    """List of scheduled agents"""