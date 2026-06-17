# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from datetime import datetime

from typing import Optional

from ..ambient_agent_config import AmbientAgentConfig

from ..user_profile import UserProfile

from ..cloud_environment_config import CloudEnvironmentConfig

from .scheduled_agent_history_item import ScheduledAgentHistoryItem

from ..scope import Scope

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

    agent_uid: Optional[str] = None
    """UID of the agent that this schedule runs as"""

    created_by: Optional[UserProfile] = None

    environment: Optional[CloudEnvironmentConfig] = None
    """Configuration for a cloud environment used by scheduled agents"""

    history: Optional[ScheduledAgentHistoryItem] = None
    """Scheduler-derived history metadata for a scheduled agent"""

    last_spawn_error: Optional[str] = None
    """Error message from the last failed spawn attempt, if any"""

    scope: Optional[Scope] = None
    """Ownership scope for a resource (team or personal)"""

    updated_by: Optional[UserProfile] = None