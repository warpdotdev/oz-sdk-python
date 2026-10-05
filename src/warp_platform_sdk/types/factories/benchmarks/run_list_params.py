# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["RunListParams"]


class RunListParams(TypedDict, total=False):
    cursor: str

    limit: int

    state: List[Literal["pending", "running", "scoring", "completed", "failed", "cancelled"]]

    suite_uid: str
