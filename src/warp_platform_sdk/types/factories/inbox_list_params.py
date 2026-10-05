# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .inbox_scope import InboxScope

__all__ = ["InboxListParams"]


class InboxListParams(TypedDict, total=False):
    cursor: str
    """Opaque cursor from page_info.next_cursor."""

    factory_uid: str
    """Exact Factory UID filter, intersected with authorized factories."""

    limit: int
    """Maximum number of items to return. Defaults to 50."""

    recipient_uid: str
    """Exact public user UID filter within the authorized Factory and team scope.

    In `mine` scope this can only match the authenticated user.
    """

    scope: InboxScope
    """
    `mine` returns notifications assigned to the authenticated user and is the
    default. `team` returns notifications across live recipients in the authorized
    Factory and team scope.
    """

    team_uid: Annotated[str, PropertyInfo(alias="X-Warp-Team-Uid")]
