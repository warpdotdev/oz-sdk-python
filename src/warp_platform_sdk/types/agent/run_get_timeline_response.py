# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RunGetTimelineResponse", "Event"]


class Event(BaseModel):
    """A setup or lifecycle event recorded for an agent run."""

    event_type: Literal[
        "oz_run_created",
        "oz_run_claimed",
        "worker_container_ready",
        "shared_session_started",
        "agent_started",
        "oz_run_done",
        "oz_run_blocked",
        "oz_run_cancelled",
        "oz_run_failed",
        "oz_run_errored",
        "vm_shutdown",
    ]
    """Type of timeline event recorded for a run."""

    event_uuid: str
    """Unique client- or server-generated identifier for this event."""

    occurred_at: datetime
    """Timestamp when the event occurred."""

    run_id: str
    """Run that owns this event."""

    execution_id: Optional[int] = None
    """Run execution associated with this event, when available."""

    payload: Optional[Dict[str, object]] = None
    """Optional event-specific JSON payload. Contents vary by event type."""


class RunGetTimelineResponse(BaseModel):
    """Response body for listing run timeline events."""

    events: List[Event]
