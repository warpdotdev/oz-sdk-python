# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..memory_store_ref import MemoryStoreRef
from .auto_memory_response import AutoMemoryResponse

__all__ = ["MemoryResponse"]


class MemoryResponse(BaseModel):
    """Memory settings for an agent."""

    attached_stores: List[MemoryStoreRef]
    """Team memory stores attached to the agent."""

    auto_memory: AutoMemoryResponse
    """Auto-memory state for an agent."""
