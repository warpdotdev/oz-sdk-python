# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TaskUpdateParams"]


class TaskUpdateParams(TypedDict, total=False):
    uid: Required[str]

    description: Optional[str]
    """Updated description. null or an empty string clears the description."""

    stage: Literal["TRIAGE", "SPEC", "IMPLEMENT", "REVIEW", "COMPLETE", "CANCELLED"]
    """
    Lifecycle stage of a factory task, mirroring the seeded factory agent roles plus
    the terminal COMPLETE and CANCELLED states. COMPLETE and CANCELLED are terminal
    in intent but not enforced: any stage may be written explicitly at any time.
    CANCELLED is set automatically when the task's current top-level run is
    cancelled, regardless of that run's agent type.
    """

    title: str
    """Updated title. Must be non-empty when provided."""
