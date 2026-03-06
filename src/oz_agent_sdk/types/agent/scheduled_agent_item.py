# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..scope import Scope
from ..._models import BaseModel
from ..user_profile import UserProfile
from ..ambient_agent_config import AmbientAgentConfig
from .schedule_history_item import ScheduleHistoryItem
from ..cloud_environment_config import CloudEnvironmentConfig

__all__ = ["ScheduledAgentItem"]


class ScheduledAgentItem(BaseModel):
    id: str
    """Unique identifier for the scheduled agent"""

    created_at: datetime
    """Timestamp when the schedule was created (RFC3339)"""

    cron_schedule: str
    """
    Cron expression defining when the agent runs (e.g., "0 9 \\** \\** \\**" for daily at
    9am UTC)
    """

    enabled: bool
    """Whether the schedule is currently active"""

    name: str
    """Human-readable name for the schedule"""

    prompt: str
    """The prompt/instruction for the agent to execute"""

    updated_at: datetime
    """Timestamp when the schedule was last updated (RFC3339)"""

    agent_config: Optional[AmbientAgentConfig] = None
    """Configuration for a cloud agent run"""

    created_by: Optional[UserProfile] = None

    environment: Optional[CloudEnvironmentConfig] = None
    """Configuration for a cloud environment used by scheduled agents"""

    history: Optional[ScheduleHistoryItem] = None
    """Scheduler-derived history metadata for a scheduled agent"""

    last_spawn_error: Optional[str] = None
    """Error message from the last failed spawn attempt, if any"""

    scope: Optional[Scope] = None
    """Ownership scope for a resource (team or personal)"""

    updated_by: Optional[UserProfile] = None
