# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..error_code import ErrorCode

__all__ = ["RunStatusMessage"]


class RunStatusMessage(BaseModel):
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
