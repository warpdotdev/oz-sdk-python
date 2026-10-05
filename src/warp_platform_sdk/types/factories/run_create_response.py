# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..agent.run_state import RunState

__all__ = ["RunCreateResponse"]


class RunCreateResponse(BaseModel):
    """Response body for a dispatched factory run."""

    factory_uid: str
    """Public UID of the factory the run was dispatched to."""

    foreman_agent: str
    """Name of the factory's foreman agent that received the run."""

    run_id: str
    """Unique identifier for the dispatched run."""

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

    ticket_ref: str
    """
    The canonical <source>:<id> ticket reference the run was stamped with, either
    the caller-supplied ticket_ref or a minted adhoc reference.
    """

    run_url: Optional[str] = None
    """URL to view the dispatched run in the Factory app.

    Empty when the Factory app origin is not configured.
    """
