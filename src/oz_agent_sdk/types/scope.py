# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Scope"]


class Scope(BaseModel):
    """Ownership scope for a resource (team or personal)"""

    type: Literal["User", "Team"]
    """Type of ownership ("User" for personal, "Team" for team-owned)"""

    uid: Optional[str] = None
    """UID of the owning user or team"""
