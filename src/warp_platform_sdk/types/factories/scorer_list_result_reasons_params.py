# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ScorerListResultReasonsParams"]


class ScorerListResultReasonsParams(TypedDict, total=False):
    run_id: Required[SequenceNotStr[str]]
    """Runs to read reasons for.

    Repeat the parameter once per run; at most 100 distinct runs (the results page
    maximum) per request.
    """

    team_uid: Annotated[str, PropertyInfo(alias="X-Warp-Team-Uid")]
