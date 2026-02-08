# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UserProfile"]


class UserProfile(BaseModel):
    display_name: Optional[str] = None
    """Display name of the creator"""

    photo_url: Optional[str] = None
    """URL to the creator's photo"""

    type: Optional[Literal["user", "service_account"]] = None
    """Type of the creator principal"""

    uid: Optional[str] = None
    """Unique identifier of the creator"""
