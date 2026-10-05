# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MemoryStoreRef"]


class MemoryStoreRef(BaseModel):
    """Reference to a memory store to attach to an agent."""

    access: Literal["read_write", "read_only"]
    """Access level for the store."""

    instructions: str
    """Instructions for how the agent should use this memory store. Must not be empty."""

    uid: str
    """UID of the memory store."""
