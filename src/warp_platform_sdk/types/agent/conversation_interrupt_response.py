# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ConversationInterruptResponse"]


class ConversationInterruptResponse(BaseModel):
    """Acknowledgement of an interrupt accepted through a conversation-keyed route."""

    run_id: str
    """The run whose turn is being interrupted."""
