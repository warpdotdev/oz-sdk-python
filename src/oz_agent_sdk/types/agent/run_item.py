# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .run_state import RunState
from ..user_profile import UserProfile
from .artifact_item import ArtifactItem
from .run_source_type import RunSourceType
from ..ambient_agent_config import AmbientAgentConfig

__all__ = ["RunItem", "AgentSkill", "RequestUsage", "Schedule", "Scope", "StatusMessage"]


class AgentSkill(BaseModel):
    """
    Information about the agent skill used for the run.
    Either full_path or bundled_skill_id will be set, but not both.
    """

    bundled_skill_id: Optional[str] = None
    """Unique identifier for bundled skills"""

    description: Optional[str] = None
    """Description of the skill"""

    full_path: Optional[str] = None
    """Path to the SKILL.md file (for file-based skills)"""

    name: Optional[str] = None
    """Human-readable name of the skill"""


class RequestUsage(BaseModel):
    """Resource usage information for the run"""

    compute_cost: Optional[float] = None
    """Cost of compute resources for the run"""

    inference_cost: Optional[float] = None
    """Cost of LLM inference for the run"""


class Schedule(BaseModel):
    """
    Information about the schedule that triggered this run (only present for scheduled runs)
    """

    cron_schedule: str
    """Cron expression at the time the run was created"""

    schedule_id: str
    """Unique identifier for the schedule"""

    schedule_name: str
    """Name of the schedule at the time the run was created"""


class Scope(BaseModel):
    """Ownership scope for a resource (team or personal)"""

    type: Literal["User", "Team"]
    """Type of ownership ("User" for personal, "Team" for team-owned)"""

    uid: Optional[str] = None
    """UID of the owning user or team"""


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
    - CANCELLED: Run was cancelled by user
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
    """Configuration for an cloud agent run"""

    agent_skill: Optional[AgentSkill] = None
    """
    Information about the agent skill used for the run. Either full_path or
    bundled_skill_id will be set, but not both.
    """

    artifacts: Optional[List[ArtifactItem]] = None
    """Artifacts created during the run (plans, pull requests, etc.)"""

    conversation_id: Optional[str] = None
    """UUID of the conversation associated with the run"""

    creator: Optional[UserProfile] = None

    is_sandbox_running: Optional[bool] = None
    """Whether the sandbox environment is currently running"""

    request_usage: Optional[RequestUsage] = None
    """Resource usage information for the run"""

    schedule: Optional[Schedule] = None
    """
    Information about the schedule that triggered this run (only present for
    scheduled runs)
    """

    scope: Optional[Scope] = None
    """Ownership scope for a resource (team or personal)"""

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
    - WEB_APP: Created from the Warp web app
    - GITHUB_ACTION: Created from a GitHub action
    - CLOUD_MODE: Created from a Cloud Mode
    - CLI: Created from the CLI
    """

    started_at: Optional[datetime] = None
    """Timestamp when the agent started working on the run (RFC3339)"""

    status_message: Optional[StatusMessage] = None
