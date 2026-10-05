# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ScorerListResultReasonsResponse", "Reason"]


class Reason(BaseModel):
    run_id: str
    """The run this reason belongs to"""

    status: Literal["available", "absent", "unavailable"]
    """
    Availability of the run's judge reason: "available" when the reason was read,
    "absent" when the judge recorded none, and "unavailable" when a recorded reason
    could not be read back.
    """

    reason: Optional[str] = None
    """
    The judge's reasoning, truncated beyond 8KB when it was recorded; absent unless
    status is "available".
    """


class ScorerListResultReasonsResponse(BaseModel):
    reasons: List[Reason]
