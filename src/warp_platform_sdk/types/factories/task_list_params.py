# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["TaskListParams"]


class TaskListParams(TypedDict, total=False):
    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter to tasks created after this timestamp (RFC3339 format)."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter to tasks created before this timestamp (RFC3339 format)."""

    created_by: SequenceNotStr[str]
    """
    Filter to tasks whose seed run was started by any of these teammates, each given
    as their email address. Can be specified multiple times to match any of the
    given teammates.
    """

    cursor: str
    """
    Opaque cursor returned by a previous list response. Valid only for the
    sort_by/sort_order it was issued under; omit to restart the listing.
    """

    full_list: bool
    """
    Include canonical ticket_source and ticket_id metadata from each task's bound
    run, plus its derived outputs. Defaults to false.
    """

    include_current_run: bool
    """
    Include each task's current top-level run, resolved in one batch for the
    returned page. Defaults to false.
    """

    limit: int
    """Maximum number of tasks to return (default 50, max 100)."""

    q: str
    """Case-insensitive substring search over the task title."""

    sort_by: Literal["created_at", "updated_at"]
    """Sort field for results."""

    sort_order: Literal["asc", "desc"]
    """Sort direction."""

    stage: List[Literal["TRIAGE", "SPEC", "IMPLEMENT", "REVIEW", "COMPLETE", "CANCELLED"]]
    """Filter by task stage.

    Can be specified multiple times to match any of the given stages.
    """

    updated_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter to tasks updated after this timestamp (RFC3339 format)."""
