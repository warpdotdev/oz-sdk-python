# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

__all__ = ["SessionCheckRedirectResponse"]

class SessionCheckRedirectResponse(BaseModel):
    conversation_id: Optional[str] = None
    """The conversation ID to redirect to (only present when redirect is needed)"""