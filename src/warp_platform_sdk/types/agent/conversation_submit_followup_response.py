# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ConversationSubmitFollowupResponse"]


class ConversationSubmitFollowupResponse(BaseModel):
    """
    Acknowledgement of a follow-up accepted through a conversation-keyed
    route: the run-keyed acknowledgement plus the run it was delivered to.
    """

    followup_id: Optional[str] = None
    """
    Identifier of the durable follow-up record, or null when the outcome did not
    create one (`queued_prompt`).
    """

    outcome: Literal["live_session", "queued_prompt", "handoff_execution", "queue_pending"]
    """How an accepted follow-up was routed.

    - live_session: the message was handed to the running session. This means the
      session-sharing service accepted it, not that the agent has started on it;
      observe the session's event stream for the new request.
    - queued_prompt: the run had not started yet, so the message was appended to its
      initial prompt.
    - handoff_execution: the previous execution had ended, so a new execution of the
      same run was created to continue the conversation.
    - queue_pending: the message is durably queued and will be delivered once the
      run can accept it.
    """

    run_id: str
    """The run the conversation resolved to."""
