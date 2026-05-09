# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["AgentUpdateParams", "MemoryStore", "Secret"]


class AgentUpdateParams(TypedDict, total=False):
    base_model: Optional[str]
    """Replacement base model.

    Omit or pass `null` to leave unchanged, or pass an empty string to clear.
    """

    description: Optional[str]
    """Replacement description.

    Omit or pass `null` to leave unchanged, or use an empty value to clear.
    """

    memory_stores: Optional[Iterable[MemoryStore]]
    """Replacement list of memory stores.

    Omit to leave unchanged, pass an empty array to clear, or pass a non-empty array
    to replace.
    """

    name: str
    """The new name for the agent"""

    secrets: Optional[Iterable[Secret]]
    """Replacement list of secrets.

    Omit to leave unchanged, pass an empty array to clear, or pass a non-empty array
    to replace. Duplicate names are rejected.
    """

    skills: Optional[SequenceNotStr[str]]
    """Replacement list of skill specs.

    Omit to leave unchanged, pass an empty array to clear, or pass a non-empty array
    to replace.
    """


class MemoryStore(TypedDict, total=False):
    """Reference to a memory store to attach to an agent."""

    access: Required[Literal["read_write", "read_only"]]
    """Access level for the store."""

    instructions: Required[str]
    """Instructions for how the agent should use this memory store. Must not be empty."""

    uid: Required[str]
    """UID of the memory store."""


class Secret(TypedDict, total=False):
    """Reference to a managed secret by name."""

    name: Required[str]
    """Name of the managed secret."""
