# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TaskGetByConversationParams"]


class TaskGetByConversationParams(TypedDict, total=False):
    conversation_id: Required[str]
    """The agent conversation ID the task is bound to."""
