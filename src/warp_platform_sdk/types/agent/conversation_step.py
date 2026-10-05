# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "ConversationStep",
    "Message",
    "MessageContent",
    "MessageContentTextContentBlock",
    "MessageContentActionContentBlock",
    "MessageContentActionResultContentBlock",
    "MessageContentEventContentBlock",
]


class MessageContentTextContentBlock(BaseModel):
    text: str
    """Plain text content"""

    type: Literal["text"]

    message_id: Optional[str] = None
    """
    Underlying transcript message ID that produced this content block, when
    available
    """


class MessageContentActionContentBlock(BaseModel):
    id: str
    """Unique identifier for the action"""

    category: Literal["command", "files", "search", "integration", "documents", "computer", "review", "skill"]
    """High-level category of an action performed during the conversation"""

    input: Dict[str, object]
    """Curated public input for this action.

    This object is owned by the API and is not a raw internal tool payload.
    """

    name: str
    """Public action name, such as run_command or edit_files"""

    type: Literal["action"]

    message_id: Optional[str] = None
    """
    Underlying transcript message ID that produced this content block, when
    available
    """


class MessageContentActionResultContentBlock(BaseModel):
    action_id: str
    """Identifier of the corresponding action"""

    category: Literal["command", "files", "search", "integration", "documents", "computer", "review", "skill"]
    """High-level category of an action performed during the conversation"""

    name: str
    """Public action name matching the corresponding action block"""

    output: Dict[str, object]
    """Curated public result for this action.

    Large or binary internal payloads should be summarized rather than passed
    through raw.
    """

    state: Literal["running", "completed", "failed", "denied"]
    """State of an action result"""

    type: Literal["action_result"]

    message_id: Optional[str] = None
    """
    Underlying transcript message ID that produced this content block, when
    available
    """


class MessageContentEventContentBlock(BaseModel):
    data: Dict[str, object]
    """Minimal structured metadata for the event"""

    name: str
    """Event type for intentionally exposed non-core transcript events"""

    type: Literal["event"]

    message_id: Optional[str] = None
    """
    Underlying transcript message ID that produced this content block, when
    available
    """


MessageContent: TypeAlias = Annotated[
    Union[
        MessageContentTextContentBlock,
        MessageContentActionContentBlock,
        MessageContentActionResultContentBlock,
        MessageContentEventContentBlock,
    ],
    PropertyInfo(discriminator="type"),
]


class Message(BaseModel):
    content: List[MessageContent]

    role: Literal["user", "assistant", "tool", "system"]
    """Role of the normalized message"""

    message_ids: Optional[List[str]] = None
    """Underlying transcript message IDs grouped into this normalized message"""

    request_id: Optional[str] = None
    """
    Request identifier shared by transcript messages from the same request, when
    available
    """

    timestamp: Optional[datetime] = None
    """
    Timestamp of the first transcript message included in this normalized message
    (RFC3339)
    """


class ConversationStep(BaseModel):
    id: str
    """Unique identifier for the step"""

    messages: List[Message]
    """Ordered normalized messages for this step"""

    steps: List["ConversationStep"]
    """Nested delegated work performed as part of this step"""

    completed_at: Optional[datetime] = None
    """
    Latest transcript message timestamp contained in this step or any nested step
    (RFC3339)
    """

    description: Optional[str] = None
    """Original instruction or delegated work description for the step"""

    started_at: Optional[datetime] = None
    """
    Earliest transcript message timestamp contained in this step or any nested step
    (RFC3339)
    """

    summary: Optional[str] = None
    """Summary of the work completed for the step"""
