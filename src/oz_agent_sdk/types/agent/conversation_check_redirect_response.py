# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

__all__ = ["ConversationCheckRedirectResponse"]

class ConversationCheckRedirectResponse(BaseModel):
    session_id: Optional[str] = None
    """The shared session UUID to redirect to (only present when redirect is needed)"""