# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["InboxMarkReadResponse", "Outcome"]


class Outcome(BaseModel):
    notification_uid: str

    ok: bool


class InboxMarkReadResponse(BaseModel):
    outcomes: List[Outcome]
