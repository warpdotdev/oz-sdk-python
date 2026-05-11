# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["AgentCreateParams", "Secret"]


class AgentCreateParams(TypedDict, total=False):
    name: Required[str]
    """A name for the agent"""

    base_model: Optional[str]
    """Optional base model for runs executed by this agent."""

    description: Optional[str]
    """Optional description of the agent"""

    prompt: Optional[str]
    """Optional base prompt for this agent"""

    secrets: Iterable[Secret]
    """
    Optional list of secrets associated with the agent. Duplicate names within a
    single request are rejected. Each entry is unioned into the run-time secret
    scope when the agent executes.
    """

    skills: SequenceNotStr[str]
    """
    Optional list of skill specs to associate with the agent. Format:
    "{owner}/{repo}:{skill_path}" (e.g.,
    "warpdotdev/warp-server:.claude/skills/deploy/SKILL.md"). Each spec is validated
    and normalized at attach time using the team's GitHub credentials; inaccessible
    or malformed specs are rejected.
    """


class Secret(TypedDict, total=False):
    """Reference to a managed secret by name."""

    name: Required[str]
    """Name of the managed secret."""
