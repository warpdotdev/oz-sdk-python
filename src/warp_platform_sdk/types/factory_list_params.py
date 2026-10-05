# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FactoryListParams"]


class FactoryListParams(TypedDict, total=False):
    cursor: str
    """Opaque cursor returned by a previous list response."""

    limit: int
    """Maximum number of factories to return (default 50, max 100)."""

    search: str
    """Case-insensitive substring search over the factory name and alias."""

    filter_team_uid: Annotated[str, PropertyInfo(alias="team_uid")]
    """Optional team UID to filter factories by ownership.

    Takes precedence over the X-Warp-Team-Uid header.
    """

    team_uid: Annotated[str, PropertyInfo(alias="X-Warp-Team-Uid")]
