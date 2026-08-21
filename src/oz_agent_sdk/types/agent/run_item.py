# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
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

__all__ = [
    "RunItem",
    "AgentSkill",
    "RequestUsage",
    "RequestUsageInferenceCostBreakdownUsd",
    "RequestUsageUsageByCategory",
    "RequestUsageUsageByCategoryByokInferenceUsage",
    "RequestUsageUsageByCategoryByokInferenceUsageCostUsd",
    "RequestUsageUsageByCategoryByokInferenceUsageTokenCount",
    "RequestUsageUsageByCategoryCustomEndpointInferenceUsage",
    "RequestUsageUsageByCategoryCustomEndpointInferenceUsageCostUsd",
    "RequestUsageUsageByCategoryCustomEndpointInferenceUsageTokenCount",
    "RequestUsageUsageByCategoryDirectAPIInferenceUsage",
    "RequestUsageUsageByCategoryDirectAPIInferenceUsageCostUsd",
    "RequestUsageUsageByCategoryDirectAPIInferenceUsageTokenCount",
    "Schedule",
    "StatusMessage",
]


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


class RequestUsageInferenceCostBreakdownUsd(BaseModel):
    """
    Charged dollar cost of LLM inference, split by token type.
    Omitted when the data is not available.
    """

    input_cache_read_cost_usd: float
    """Cost of cache-read input tokens, in US dollars."""

    input_cache_write_cost_usd: float
    """Cost of cache-write input tokens, in US dollars."""

    input_cost_usd: float
    """Cost of non-cached input tokens, in US dollars."""

    output_cost_usd: float
    """Cost of output tokens, in US dollars."""


class RequestUsageUsageByCategoryByokInferenceUsageCostUsd(BaseModel):
    """
    Charged dollar cost of LLM inference, split by token type.
    Omitted when the data is not available.
    """

    input_cache_read_cost_usd: float
    """Cost of cache-read input tokens, in US dollars."""

    input_cache_write_cost_usd: float
    """Cost of cache-write input tokens, in US dollars."""

    input_cost_usd: float
    """Cost of non-cached input tokens, in US dollars."""

    output_cost_usd: float
    """Cost of output tokens, in US dollars."""


class RequestUsageUsageByCategoryByokInferenceUsageTokenCount(BaseModel):
    """A per-token-type token count."""

    input: int
    """Count of non-cached input tokens."""

    input_cache_read: int
    """Count of cache-read input tokens."""

    input_cache_write: int
    """Count of cache-write input tokens."""

    output: int
    """Count of output tokens."""


class RequestUsageUsageByCategoryByokInferenceUsage(BaseModel):
    """
    Full token count and dollar-cost detail inference usage.
    The counts and cost describe the same usage (e.g. token_count.input
    tokens cost cost_usd.input_cost_usd in total).
    """

    cost_usd: RequestUsageUsageByCategoryByokInferenceUsageCostUsd
    """
    Charged dollar cost of LLM inference, split by token type. Omitted when the data
    is not available.
    """

    token_count: RequestUsageUsageByCategoryByokInferenceUsageTokenCount
    """A per-token-type token count."""

    web_search_cost_usd: float
    """Total cost of those web searches, in US dollars."""

    web_search_count: int
    """Number of web searches performed by this model."""


class RequestUsageUsageByCategoryCustomEndpointInferenceUsageCostUsd(BaseModel):
    """
    Charged dollar cost of LLM inference, split by token type.
    Omitted when the data is not available.
    """

    input_cache_read_cost_usd: float
    """Cost of cache-read input tokens, in US dollars."""

    input_cache_write_cost_usd: float
    """Cost of cache-write input tokens, in US dollars."""

    input_cost_usd: float
    """Cost of non-cached input tokens, in US dollars."""

    output_cost_usd: float
    """Cost of output tokens, in US dollars."""


class RequestUsageUsageByCategoryCustomEndpointInferenceUsageTokenCount(BaseModel):
    """A per-token-type token count."""

    input: int
    """Count of non-cached input tokens."""

    input_cache_read: int
    """Count of cache-read input tokens."""

    input_cache_write: int
    """Count of cache-write input tokens."""

    output: int
    """Count of output tokens."""


class RequestUsageUsageByCategoryCustomEndpointInferenceUsage(BaseModel):
    """
    Full token count and dollar-cost detail inference usage.
    The counts and cost describe the same usage (e.g. token_count.input
    tokens cost cost_usd.input_cost_usd in total).
    """

    cost_usd: RequestUsageUsageByCategoryCustomEndpointInferenceUsageCostUsd
    """
    Charged dollar cost of LLM inference, split by token type. Omitted when the data
    is not available.
    """

    token_count: RequestUsageUsageByCategoryCustomEndpointInferenceUsageTokenCount
    """A per-token-type token count."""

    web_search_cost_usd: float
    """Total cost of those web searches, in US dollars."""

    web_search_count: int
    """Number of web searches performed by this model."""


class RequestUsageUsageByCategoryDirectAPIInferenceUsageCostUsd(BaseModel):
    """
    Charged dollar cost of LLM inference, split by token type.
    Omitted when the data is not available.
    """

    input_cache_read_cost_usd: float
    """Cost of cache-read input tokens, in US dollars."""

    input_cache_write_cost_usd: float
    """Cost of cache-write input tokens, in US dollars."""

    input_cost_usd: float
    """Cost of non-cached input tokens, in US dollars."""

    output_cost_usd: float
    """Cost of output tokens, in US dollars."""


class RequestUsageUsageByCategoryDirectAPIInferenceUsageTokenCount(BaseModel):
    """A per-token-type token count."""

    input: int
    """Count of non-cached input tokens."""

    input_cache_read: int
    """Count of cache-read input tokens."""

    input_cache_write: int
    """Count of cache-write input tokens."""

    output: int
    """Count of output tokens."""


class RequestUsageUsageByCategoryDirectAPIInferenceUsage(BaseModel):
    """
    Full token count and dollar-cost detail inference usage.
    The counts and cost describe the same usage (e.g. token_count.input
    tokens cost cost_usd.input_cost_usd in total).
    """

    cost_usd: RequestUsageUsageByCategoryDirectAPIInferenceUsageCostUsd
    """
    Charged dollar cost of LLM inference, split by token type. Omitted when the data
    is not available.
    """

    token_count: RequestUsageUsageByCategoryDirectAPIInferenceUsageTokenCount
    """A per-token-type token count."""

    web_search_cost_usd: float
    """Total cost of those web searches, in US dollars."""

    web_search_count: int
    """Number of web searches performed by this model."""


class RequestUsageUsageByCategory(BaseModel):
    """
    Usage charged for a single usage category, broken down by usage type
    (direct API/BYOK/custom endpoint) and, within each, by model ID.
    """

    platform_usage_usd: float
    """Platform usage charged for this category, in US dollars."""

    byok_inference_usage: Optional[Dict[str, RequestUsageUsageByCategoryByokInferenceUsage]] = None
    """Inference usage charged using a user's own API key, keyed by model ID."""

    custom_endpoint_inference_usage: Optional[Dict[str, RequestUsageUsageByCategoryCustomEndpointInferenceUsage]] = None
    """
    Inference usage charged using a custom endpoint, keyed by the custom model's
    config key.
    """

    direct_api_inference_usage: Optional[Dict[str, RequestUsageUsageByCategoryDirectAPIInferenceUsage]] = None
    """Inference usage incurred through Warp-provided model access, keyed by model ID."""


class RequestUsage(BaseModel):
    """Resource usage information for the run"""

    compute_cost: Optional[float] = None
    """Credits consumed by compute resources for the run"""

    compute_cost_usd: Optional[float] = None
    """compute_cost in US dollars, converted at the owning team's current credit price.

    An approximate cost, not a billed amount.
    """

    inference_cost: Optional[float] = None
    """Credits consumed by LLM inference for the run"""

    inference_cost_breakdown_usd: Optional[RequestUsageInferenceCostBreakdownUsd] = None
    """
    Charged dollar cost of LLM inference, split by token type. Omitted when the data
    is not available.
    """

    inference_cost_usd: Optional[float] = None
    """
    inference_cost in US dollars, converted at the owning team's current credit
    price. An approximate cost, not a billed amount.
    """

    platform_cost: Optional[float] = None
    """Credits consumed by platform usage for the run"""

    platform_cost_usd: Optional[float] = None
    """platform_cost in US dollars, converted at the owning team's current credit
    price.

    An approximate cost, not a billed amount.
    """

    total_tokens: Optional[int] = None
    """
    Total LLM token count (summed across every usage category and model) for the
    run's conversation. Omitted when the data is not available.
    """

    usage_by_category: Optional[Dict[str, RequestUsageUsageByCategory]] = None
    """
    Full-granularity token and dollar-cost breakdown for the run's conversation,
    keyed by usage category (e.g. "primary_agent", "conversation_compaction") and
    model id. This differs from total_tokens/inference_cost_breakdown_usd which
    combine usage across all categories and models. Omitted when the data is not
    available.
    """


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

    session_debug_until: Optional[datetime] = None
    """
    When a failed run's shared session stops being held open for debugging. Only
    present while that window is open.

    The window is an idle window owned by the agent process: activity in the session
    pushes this deadline out. The agent republishes it periodically rather than on
    every keystroke, so the value can lag the true deadline by up to a throttle
    interval, and always in the conservative direction.
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

    - LOCAL: Executed in the user's local Warp environment
    - REMOTE: Executed by a remote/cloud worker
    """

    executor: Optional[UserProfile] = None

    is_run_type_cancellable: Optional[bool] = None
    """Whether the run's type is eligible for cancellation via the API.

    State-independent: false for GitHub Action and local runs; true for all other
    run types (including self-hosted). Clients should still gate the control on the
    run's current state.
    """

    is_sandbox_running: Optional[bool] = None
    """Whether the sandbox environment is currently running"""

    metadata: Optional[Dict[str, str]] = None
    """
    Custom key/value metadata attached to a run at creation time and immutable
    afterward. At most 20 keys. Keys are 1-64 bytes matching [a-zA-Z0-9._-]+
    (case-sensitive); values are 0-256 bytes of UTF-8 and cannot contain NUL
    characters. Requests with invalid metadata are rejected. A run's effective
    metadata is merged per key at creation: explicit request keys override keys
    inherited from the parent run, which override automatic keys (ticket_id and
    ticket_source on Linear- and Jira-triggered runs).
    """

    parent_run_id: Optional[str] = None
    """UUID of the parent run that spawned this run"""

    request_usage: Optional[RequestUsage] = None
    """Resource usage information for the run"""

    run_time: Optional[str] = None
    """Total runtime as an ISO 8601 duration (e.g.

    "PT2M30S"), computed server-side from run executions.
    """

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
    - JIRA: Created from Jira integration
    - SELF_IMPROVEMENT: Created by Warp's self-improvement pipeline
    - GITHUB_WEBHOOK: Created from a GitHub webhook event
    - GITLAB_WEBHOOK: Created from a GitLab webhook event
    - AUTOFIX: Created by Warp's autofix pipeline
    - RUN_SCORER: Created by Warp's run-scoring judge
    - ORCHESTRATION: Created as a child run by the orchestration layer
      (parent_run_id set)
    """

    started_at: Optional[datetime] = None
    """Timestamp when the agent started working on the run (RFC3339)"""

    status_message: Optional[StatusMessage] = None
    """Status message for a run.

    For terminal error states, includes structured error code and retryability info
    from the platform error catalog.
    """

    trigger_url: Optional[str] = None
    """URL to the run trigger (e.g. Slack thread, Linear issue, schedule)"""
