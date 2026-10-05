# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RunListScoresResponse", "Score"]


class Score(BaseModel):
    attempt_status: Literal["in_flight", "scored", "failed"]
    """
    Classification of a run's current attempt against one evaluation. "scored" takes
    precedence over in-flight: a live score reads as scored even while a replacement
    judge runs, and is_in_flight reports that overlap independently.
    """

    attempted_at: datetime
    """When the evaluation last attempted this run"""

    is_in_flight: bool
    """True when a non-terminal judge run currently holds this pair"""

    scorer_id: int
    """The evaluation that attempted this run"""

    scorer_name: str
    """Display name of the evaluation"""

    trigger_source: Literal["automatic", "manual"]
    """
    Whether the current attempt was requested by an automatic scoring dispatch or a
    manual dispatch request
    """

    classification: Optional[str] = None
    """The live classification; absent when there is no live score"""

    scored_at: Optional[datetime] = None
    """When the live score was recorded; absent when there is no live score"""

    scoring_run_id: Optional[str] = None
    """
    The Warp run that performed the judging; absent when scoring was never
    dispatched for this attempt
    """


class RunListScoresResponse(BaseModel):
    run_id: str
    """The run these scores belong to"""

    scores: List[Score]
    """One entry per evaluation that has attempted the run, most recent attempt first"""
