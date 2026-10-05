# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TaskGetByRunParams"]


class TaskGetByRunParams(TypedDict, total=False):
    run_id: Required[str]
    """Any run ID in the task's run tree."""
