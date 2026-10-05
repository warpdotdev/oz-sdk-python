# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ScorerListResultsParams"]


class ScorerListResultsParams(TypedDict, total=False):
    cursor: str
    """Opaque cursor returned by a previous list response."""

    limit: int
    """Maximum number of results to return (1-100, default 50)"""

    team_uid: Annotated[str, PropertyInfo(alias="X-Warp-Team-Uid")]
