# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RunSubmitFollowupParams", "Attachment"]


class RunSubmitFollowupParams(TypedDict, total=False):
    attachments: Iterable[Attachment]
    """Files to deliver with the message, at most 25.

    Each entry must name an attachment previously prepared for this run through
    `POST /agent/runs/{runId}/attachments/prepare` and uploaded to its upload
    target; an unknown `attachment_id` is rejected with 422. Files are only
    materialized for the agent on the Oz harness; other harnesses receive a notice
    naming the files.
    """

    message: str
    """The follow-up message to send to the run.

    May be empty when `attachments` is non-empty.
    """

    mode: Literal["normal", "plan", "orchestrate"]
    """Optional query mode for the follow-up.

    Defaults to `normal` when omitted. The server does not infer mode from prompt
    prefixes such as `/plan`. The mode only takes effect when the follow-up is
    queued ahead of the run starting or starts a new execution; a follow-up injected
    into a live session runs in the session's current mode.
    """


class Attachment(TypedDict, total=False):
    """A prepared attachment to deliver with a follow-up message."""

    attachment_id: Required[str]
    """
    The `attachment_id` (a UUID) returned by the attachment prepare endpoint for
    this run.
    """

    file_name: str
    """
    Optional display name shown to the agent in place of the name recorded when the
    attachment was prepared. The stored object is unaffected.
    """
