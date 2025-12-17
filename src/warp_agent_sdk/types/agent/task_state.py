# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["TaskState"]

TaskState: TypeAlias = Literal["QUEUED", "PENDING", "CLAIMED", "INPROGRESS", "SUCCEEDED", "FAILED"]
