# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .inbox_recipient import InboxRecipient

__all__ = ["InboxItem", "Question"]


class Question(BaseModel):
    id: str

    options: List[str]

    question: str

    type: Literal["single_select", "multi_select"]

    recommended_option_index: Optional[int] = None


class InboxItem(BaseModel):
    """One shared unresolved notification in the Factory Inbox."""

    created_at: datetime
    """Notification declaration time."""

    factory_task_uid: str

    factory_uid: str

    kind: Literal["question", "answer_question", "spec_review", "pr_review", "blocked", "failed"]
    """The action requested by a Factory notification."""

    notification_uid: str
    """Identifier accepted by the dismiss endpoint."""

    recipients: List[InboxRecipient]
    """
    Live, undismissed recipients for this shared notification, sorted
    deterministically. Slack routing and personal dismissal state are not exposed.
    """

    stage: Literal["TRIAGE", "SPEC", "IMPLEMENT", "REVIEW", "COMPLETE", "CANCELLED"]
    """
    Lifecycle stage of a factory task, mirroring the seeded factory agent roles plus
    the terminal COMPLETE and CANCELLED states. COMPLETE and CANCELLED are terminal
    in intent but not enforced: any stage may be written explicitly at any time.
    CANCELLED is set automatically when the task's current top-level run is
    cancelled, regardless of that run's agent type.
    """

    title: str
    """Notification headline."""

    description: Optional[str] = None
    """Notification body, when present."""

    is_read: Optional[bool] = None
    """
    Whether the authenticated user has read this notification. Always present in
    `mine` scope, including when false. Omitted in `team` scope, even when filtering
    by recipient.
    """

    origin_link: Optional[str] = None
    """Server-derived link back to the task's origin, when present."""

    questions: Optional[List[Question]] = None

    run_id: Optional[str] = None
    """
    Producing run ID from factory_task_notifications.created_by_run_id. Present when
    the producing run is known.
    """

    url: Optional[str] = None
    """Legacy first artifact URL supplied by a review notification."""

    urls: Optional[List[str]] = None
    """Canonical artifact URLs in a composite PR review request."""
