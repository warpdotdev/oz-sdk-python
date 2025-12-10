# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .task_state import TaskState
from .task_source_type import TaskSourceType

__all__ = ["TaskListParams"]


class TaskListParams(TypedDict, total=False):
    config_name: str
    """Filter by agent config name"""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter tasks created after this timestamp (RFC3339 format)"""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter tasks created before this timestamp (RFC3339 format)"""

    creator: str
    """Filter by creator UID (user or service account)"""

    cursor: str
    """Pagination cursor from previous response"""

    limit: int
    """Maximum number of tasks to return"""

    model_id: str
    """Filter by model ID"""

    source: TaskSourceType
    """Filter by task source type"""

    state: List[TaskState]
    """Filter by task state.

    Can be specified multiple times to match any of the given states.
    """
