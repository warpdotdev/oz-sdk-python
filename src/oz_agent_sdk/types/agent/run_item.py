# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..scope import Scope
from ..._models import BaseModel
from .run_state import RunState
from ..error_code import ErrorCode
from ..user_profile import UserProfile
from .artifact_item import ArtifactItem
from .run_source_type import RunSourceType
from ..ambient_agent_config import AmbientAgentConfig

__all__ = ["RunItem", "AgentSkill", "RequestUsage", "Schedule", "StatusMessage"]


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


class StatusMessage(BaseModel):
    """Status message for a run.

    For terminal error states, includes structured
    error code and retryability info from the platform error catalog.
    """

    message: str
    """Human-readable status message"""

    error_code: Optional[ErrorCode] = None
    """
    Machine-readable error code identifying the problem type. Used in the `type` URI
    of Error responses and in the `error_code` field of RunStatusMessage.

    User errors (run transitions to FAILED):

    - `insufficient_credits` — Team has no remaining add-on credits
    - `feature_not_available` — Required feature not enabled for user's plan
    - `external_authentication_required` — User hasn't authorized a required
      external service
    - `not_authorized` — Principal lacks permission for the requested operation
    - `invalid_request` — Request is malformed or contains invalid parameters
    - `resource_not_found` — Referenced resource does not exist
    - `budget_exceeded` — Spending budget limit has been reached
    - `integration_disabled` — Integration is disabled and must be enabled
    - `integration_not_configured` — Integration setup is incomplete
    - `operation_not_supported` — Requested operation not supported for this
      resource/state
    - `environment_setup_failed` — Client-side environment setup failed
    - `content_policy_violation` — Prompt or setup commands violated content policy
    - `conflict` — Request conflicts with the current state of the resource

    Warp errors (run transitions to ERROR):

    - `authentication_required` — Request lacks valid authentication credentials
    - `resource_unavailable` — Transient infrastructure issue (retryable)
    - `internal_error` — Unexpected server-side error (retryable)
    """

    retryable: Optional[bool] = None
    """Whether the error is transient and the client may retry by submitting a new run.

    Only present on terminal error states. When false, retrying without addressing
    the underlying cause will not succeed.
    """


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
    - BLOCKED: Run is blocked (e.g., awaiting user input or approval)
    - ERROR: Run encountered an error
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
    """Configuration for a cloud agent run"""

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

    execution_location: Optional[Literal["LOCAL", "REMOTE"]] = None
    """Where the run executed:

    - LOCAL: Executed in the user's local Oz environment
    - REMOTE: Executed by a remote/cloud worker
    """

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
    """Status message for a run.

    For terminal error states, includes structured error code and retryability info
    from the platform error catalog.
    """
