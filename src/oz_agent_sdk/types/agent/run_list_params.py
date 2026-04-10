# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo
from .run_state import RunState
from .run_source_type import RunSourceType

__all__ = ["RunListParams"]


class RunListParams(TypedDict, total=False):
    artifact_type: Literal["PLAN", "PULL_REQUEST", "SCREENSHOT", "FILE"]
    """Filter runs by artifact type"""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter runs created after this timestamp (RFC3339 format)"""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter runs created before this timestamp (RFC3339 format)"""

    creator: str
    """Filter by creator UID (user or service account)"""

    cursor: str
    """Pagination cursor from previous response"""

    environment_id: str
    """Filter runs by environment ID"""

    execution_location: Literal["LOCAL", "REMOTE"]
    """Filter by where the run executed"""

    limit: int
    """Maximum number of runs to return"""

    model_id: str
    """Filter by model ID"""

    name: str
    """Filter by agent config name"""

    q: str
    """Fuzzy search query across run title, prompt, and skill_spec"""

    schedule_id: str
    """Filter runs by the scheduled agent ID that created them"""

    skill: str
    """
    Filter runs by skill spec (e.g., "owner/repo:path/to/SKILL.md"). Alias for
    skill_spec.
    """

    skill_spec: str
    """Filter runs by skill spec (e.g., "owner/repo:path/to/SKILL.md")"""

    sort_by: Literal["updated_at", "created_at", "title", "agent"]
    """Sort field for results.

    - `updated_at`: Sort by last update timestamp (default)
    - `created_at`: Sort by creation timestamp
    - `title`: Sort alphabetically by run title
    - `agent`: Sort alphabetically by skill. Runs without a skill are grouped last.
    """

    sort_order: Literal["asc", "desc"]
    """Sort direction"""

    source: RunSourceType
    """Filter by run source type"""

    state: List[RunState]
    """Filter by run state.

    Can be specified multiple times to match any of the given states.
    """

    updated_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter runs updated after this timestamp (RFC3339 format)"""
