# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..user_profile import UserProfile
from ..ambient_agent_config import AmbientAgentConfig
from ..cloud_environment_config import CloudEnvironmentConfig

__all__ = ["ScheduledAgentItem", "History", "Scope"]


class History(BaseModel):
    """Scheduler-derived history metadata for a scheduled agent"""

    last_ran: Optional[datetime] = None
    """Timestamp of the last successful run (RFC3339)"""

    next_run: Optional[datetime] = None
    """Timestamp of the next scheduled run (RFC3339)"""


class Scope(BaseModel):
    """Ownership scope for a resource (team or personal)"""

    type: Literal["User", "Team"]
    """Type of ownership ("User" for personal, "Team" for team-owned)"""

    uid: Optional[str] = None
    """UID of the owning user or team"""


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
    """Configuration for an cloud agent run"""

    created_by: Optional[UserProfile] = None

    environment: Optional[CloudEnvironmentConfig] = None
    """Configuration for a cloud environment used by scheduled agents"""

    history: Optional[History] = None
    """Scheduler-derived history metadata for a scheduled agent"""

    last_spawn_error: Optional[str] = None
    """Error message from the last failed spawn attempt, if any"""

    scope: Optional[Scope] = None
    """Ownership scope for a resource (team or personal)"""

    updated_by: Optional[UserProfile] = None
