# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MemoryStoreAttachmentResponse"]


class MemoryStoreAttachmentResponse(BaseModel):
    """Memory store attached to an agent."""

    access: Literal["read_write", "read_only"]
    """Access level for the store."""

    instructions: str
    """Instructions for how the agent should use this memory store."""

    owner_type: Literal["user", "service_account", "team"]
    """Public owner type."""

    owner_uid: str
    """Public UID of the user, service account, or team that owns the memory store."""

    uid: str
    """UID of the memory store."""

    description: Optional[str] = None
    """Optional description for the memory store."""
