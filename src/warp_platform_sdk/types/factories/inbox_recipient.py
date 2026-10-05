# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["InboxRecipient"]


class InboxRecipient(BaseModel):
    """Minimal public identity for a live notification recipient."""

    uid: str
    """Public Warp user UID."""

    email: Optional[str] = None
    """Recipient email, when available."""
