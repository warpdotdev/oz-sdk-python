# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from ..._models import BaseModel

__all__ = ["ConversationRetrieveResponse"]


class ConversationRetrieveResponse(BaseModel):
    conversation_id: str
    """Unique identifier for the conversation"""

    steps: List["ConversationStep"]
    """Root steps in the conversation"""


from .conversation_step import ConversationStep
