# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["AgentUpdateParams", "Secret"]


class AgentUpdateParams(TypedDict, total=False):
    base_model: Optional[str]
    """Replacement base model.

    Omit or pass `null` to leave unchanged, or pass an empty string to clear.
    """

    description: Optional[str]
    """Replacement description.

    Omit or pass `null` to leave unchanged, or use an empty value to clear.
    """

    name: str
    """The new name for the agent"""

    prompt: Optional[str]
    """Replacement prompt.

    Omit or pass `null` to leave unchanged, or use an empty value to clear.
    """

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


class Secret(TypedDict, total=False):
    """Reference to a managed secret by name."""

    name: Required[str]
    """Name of the managed secret."""
