# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ScheduleInfo"]


class ScheduleInfo(BaseModel):
    """
    Information about the schedule that triggered this run (only present for scheduled runs)
    """

    cron_schedule: str
    """Cron expression at the time the run was created"""

    schedule_id: str
    """Unique identifier for the schedule"""

    schedule_name: str
    """Name of the schedule at the time the run was created"""
