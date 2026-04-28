# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ConversationCheckRedirectResponse"]


class ConversationCheckRedirectResponse(BaseModel):
    session_id: Optional[str] = None
    """The shared session UUID to redirect to (only present when redirect is needed)"""
