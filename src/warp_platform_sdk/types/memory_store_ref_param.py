# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MemoryStoreRefParam"]


class MemoryStoreRefParam(TypedDict, total=False):
    """Reference to a memory store to attach to an agent."""

    access: Required[Literal["read_write", "read_only"]]
    """Access level for the store."""

    instructions: Required[str]
    """Instructions for how the agent should use this memory store. Must not be empty."""

    uid: Required[str]
    """UID of the memory store."""
