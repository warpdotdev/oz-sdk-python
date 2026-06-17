# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing_extensions import Literal

from typing import Optional

__all__ = ["Scope"]

class Scope(BaseModel):
    """Ownership scope for a resource (team or personal)"""
    type: Literal["User", "Team"]
    """Type of ownership ("User" for personal, "Team" for team-owned)"""

    uid: Optional[str] = None
    """UID of the owning user or team"""