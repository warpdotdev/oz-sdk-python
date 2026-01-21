# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .run_state import RunState
from .run_source_type import RunSourceType

__all__ = ["RunListParams"]


class RunListParams(TypedDict, total=False):
    config_name: str
    """Filter by agent config name"""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter runs created after this timestamp (RFC3339 format)"""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter runs created before this timestamp (RFC3339 format)"""

    creator: str
    """Filter by creator UID (user or service account)"""

    cursor: str
    """Pagination cursor from previous response"""

    limit: int
    """Maximum number of runs to return"""

    model_id: str
    """Filter by model ID"""

    source: RunSourceType
    """Filter by run source type"""

    state: List[RunState]
    """Filter by run state.

    Can be specified multiple times to match any of the given states.
    """
