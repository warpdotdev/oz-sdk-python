# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .agent.run_state import RunState

__all__ = ["AgentRunResponse"]


class AgentRunResponse(BaseModel):
    run_id: str
    """Unique identifier for the created run"""

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
    """Unique identifier for the task (same as run_id).

    Deprecated - use run_id instead.
    """

    at_capacity: Optional[bool] = None
    """Whether the system is at capacity when the run was created"""
