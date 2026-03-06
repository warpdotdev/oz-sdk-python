# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ScheduleHistoryItem"]


class ScheduleHistoryItem(BaseModel):
    """Scheduler-derived history metadata for a scheduled agent"""

    last_ran: Optional[datetime] = None
    """Timestamp of the last successful run (RFC3339)"""

    next_run: Optional[datetime] = None
    """Timestamp of the next scheduled run (RFC3339)"""
