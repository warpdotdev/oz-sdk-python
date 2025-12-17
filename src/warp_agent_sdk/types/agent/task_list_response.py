# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .task_item import TaskItem

__all__ = ["TaskListResponse", "PageInfo"]


class PageInfo(BaseModel):
    has_next_page: bool
    """Whether there are more results available"""

    next_cursor: Optional[str] = None
    """Opaque cursor for fetching the next page"""


class TaskListResponse(BaseModel):
    page_info: PageInfo

    tasks: List[TaskItem]
