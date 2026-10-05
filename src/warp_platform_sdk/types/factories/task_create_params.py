# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TaskCreateParams"]


class TaskCreateParams(TypedDict, total=False):
    conversation_id: Required[str]
    """UUID of the agent conversation to bind the task to.

    The conversation's most recent run must be owned by the factory's team, and the
    conversation must not already be bound to a live task.
    """

    title: Required[str]
    """Human-readable title of the task. Required and non-empty."""

    description: Optional[str]
    """Optional description of the task."""

    stage: Literal["TRIAGE", "SPEC", "IMPLEMENT", "REVIEW", "COMPLETE", "CANCELLED"]
    """
    Lifecycle stage of a factory task, mirroring the seeded factory agent roles plus
    the terminal COMPLETE and CANCELLED states. COMPLETE and CANCELLED are terminal
    in intent but not enforced: any stage may be written explicitly at any time.
    CANCELLED is set automatically when the task's current top-level run is
    cancelled, regardless of that run's agent type.
    """
