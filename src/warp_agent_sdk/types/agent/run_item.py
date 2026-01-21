# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .run_state import RunState
from .run_source_type import RunSourceType
from ..ambient_agent_config import AmbientAgentConfig

__all__ = ["RunItem", "Creator", "RequestUsage", "StatusMessage"]


class Creator(BaseModel):
    display_name: Optional[str] = None
    """Display name of the creator"""

    photo_url: Optional[str] = None
    """URL to the creator's photo"""

    type: Optional[Literal["user", "service_account"]] = None
    """Type of the creator principal"""

    uid: Optional[str] = None
    """Unique identifier of the creator"""


class RequestUsage(BaseModel):
    """Resource usage information for the run"""

    compute_cost: Optional[float] = None
    """Cost of compute resources for the run"""

    inference_cost: Optional[float] = None
    """Cost of LLM inference for the run"""


class StatusMessage(BaseModel):
    message: Optional[str] = None
    """Human-readable status message"""


class RunItem(BaseModel):
    created_at: datetime
    """Timestamp when the run was created (RFC3339)"""

    prompt: str
    """The prompt/instruction for the agent"""

    run_id: str
    """Unique identifier for the run"""

    state: RunState
    """Current state of the run:

    - QUEUED: Run is waiting to be picked up
    - PENDING: Run is being prepared
    - CLAIMED: Run has been claimed by a worker
    - INPROGRESS: Run is actively being executed
    - SUCCEEDED: Run completed successfully
    - FAILED: Run failed
    """

    task_id: str
    """Unique identifier for the task (typically matches run_id).

    Deprecated - use run_id instead.
    """

    title: str
    """Human-readable title for the run"""

    updated_at: datetime
    """Timestamp when the run was last updated (RFC3339)"""

    agent_config: Optional[AmbientAgentConfig] = None
    """Configuration for an ambient agent run"""

    conversation_id: Optional[str] = None
    """UUID of the conversation associated with the run"""

    creator: Optional[Creator] = None

    is_sandbox_running: Optional[bool] = None
    """Whether the sandbox environment is currently running"""

    request_usage: Optional[RequestUsage] = None
    """Resource usage information for the run"""

    session_id: Optional[str] = None
    """UUID of the shared session (if available)"""

    session_link: Optional[str] = None
    """URL to view the agent session"""

    source: Optional[RunSourceType] = None
    """Source that created the run:

    - LINEAR: Created from Linear integration
    - API: Created via the Warp API
    - SLACK: Created from Slack integration
    - LOCAL: Created from local CLI/app
    - SCHEDULED_AGENT: Created by a scheduled agent
    """

    started_at: Optional[datetime] = None
    """Timestamp when the agent started working on the run (RFC3339)"""

    status_message: Optional[StatusMessage] = None
