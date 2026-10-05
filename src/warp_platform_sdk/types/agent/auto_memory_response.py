# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .memory_store_attachment_response import MemoryStoreAttachmentResponse

__all__ = ["AutoMemoryResponse"]


class AutoMemoryResponse(BaseModel):
    """Auto-memory state for an agent."""

    enabled: bool
    """Whether this agent has an agent-owned memory store."""

    store: Optional[MemoryStoreAttachmentResponse] = None
    """Memory store attached to an agent."""
