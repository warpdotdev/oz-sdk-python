# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["SuiteLaunchRunResponse"]


class SuiteLaunchRunResponse(BaseModel):
    state: Literal["pending", "running", "scoring", "completed", "failed", "cancelled"]
    """Lifecycle state of a benchmark run."""

    uid: str
