# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .task_state import TaskState
from .task_source_type import TaskSourceType
from ..ambient_agent_config import AmbientAgentConfig

__all__ = ["TaskItem", "Creator", "StatusMessage"]


class Creator(BaseModel):
    type: Optional[Literal["user", "service_account"]] = None
    """Type of the creator principal"""

    uid: Optional[str] = None
    """Unique identifier of the creator"""


class StatusMessage(BaseModel):
    message: Optional[str] = None
    """Human-readable status message"""


class TaskItem(BaseModel):
    created_at: datetime
    """Timestamp when the task was created (RFC3339)"""

    prompt: str
    """The prompt/instruction for the agent"""

    state: TaskState
    """Current state of the task:

    - QUEUED: Task is waiting to be picked up
    - PENDING: Task is being prepared
    - CLAIMED: Task has been claimed by a worker
    - INPROGRESS: Task is actively being executed
    - SUCCEEDED: Task completed successfully
    - FAILED: Task failed
    """

    task_id: str
    """Unique identifier for the task"""

    title: str
    """Human-readable title for the task"""

    updated_at: datetime
    """Timestamp when the task was last updated (RFC3339)"""

    agent_config: Optional[AmbientAgentConfig] = None
    """Configuration for an ambient agent task"""

    creator: Optional[Creator] = None

    session_id: Optional[str] = None
    """UUID of the shared session (if available)"""

    session_link: Optional[str] = None
    """URL to view the agent session"""

    source: Optional[TaskSourceType] = None
    """Source that created the task:

    - LINEAR: Created from Linear integration
    - API: Created via the public API
    - SLACK: Created from Slack integration
    - LOCAL: Created from local CLI/app
    - SCHEDULED_AGENT: Created by a scheduled agent
    """

    status_message: Optional[StatusMessage] = None
