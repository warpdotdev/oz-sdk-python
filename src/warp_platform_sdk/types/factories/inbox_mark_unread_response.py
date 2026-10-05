# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["InboxMarkUnreadResponse", "Outcome"]


class Outcome(BaseModel):
    notification_uid: str

    ok: bool


class InboxMarkUnreadResponse(BaseModel):
    outcomes: List[Outcome]
