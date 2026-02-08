# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .run_item import RunItem
from ..._models import BaseModel

__all__ = ["RunListResponse", "PageInfo"]


class PageInfo(BaseModel):
    has_next_page: bool
    """Whether there are more results available"""

    next_cursor: Optional[str] = None
    """Opaque cursor for fetching the next page"""


class RunListResponse(BaseModel):
    page_info: PageInfo

    runs: List[RunItem]
