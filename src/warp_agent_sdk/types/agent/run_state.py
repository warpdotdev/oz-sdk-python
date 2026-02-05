# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["RunState"]

RunState: TypeAlias = Literal["QUEUED", "PENDING", "CLAIMED", "INPROGRESS", "SUCCEEDED", "FAILED", "CANCELLED"]
