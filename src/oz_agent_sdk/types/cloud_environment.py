# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .scope import Scope
from .._models import BaseModel
from .user_profile import UserProfile
from .agent.run_state import RunState
from .cloud_environment_config import CloudEnvironmentConfig

__all__ = ["CloudEnvironment", "LastTaskCreated"]


class LastTaskCreated(BaseModel):
    """Summary of the most recently created task for an environment"""

    id: str
    """Unique identifier of the task"""

    created_at: datetime
    """When the task was created (RFC3339)"""

    state: RunState
    """Current state of the run:

    - QUEUED: Run is waiting to be picked up
    - PENDING: Run is being prepared
    - CLAIMED: Run has been claimed by a worker
    - INPROGRESS: Run is actively being executed
    - SUCCEEDED: Run completed successfully
    - FAILED: Run failed
    - BLOCKED: Run is blocked (e.g., awaiting user input or approval)
    - ERROR: Run encountered an error
    - CANCELLED: Run was cancelled by user
    """

    title: str
    """Title of the task"""

    updated_at: datetime
    """When the task was last updated (RFC3339)"""

    started_at: Optional[datetime] = None
    """When the task started running (RFC3339), null if not yet started"""


class CloudEnvironment(BaseModel):
    """A cloud environment for running agents"""

    config: CloudEnvironmentConfig
    """Configuration for a cloud environment used by scheduled agents"""

    last_updated: datetime
    """Timestamp when the environment was last updated (RFC3339)"""

    setup_failed: bool
    """True when the most recent task failed during setup before it started running"""

    uid: str
    """Unique identifier for the environment"""

    creator: Optional[UserProfile] = None

    last_editor: Optional[UserProfile] = None

    last_task_created: Optional[LastTaskCreated] = None
    """Summary of the most recently created task for an environment"""

    last_task_run_timestamp: Optional[datetime] = None
    """Timestamp of the most recent task run in this environment (RFC3339)"""

    scope: Optional[Scope] = None
    """Ownership scope for a resource (team or personal)"""
