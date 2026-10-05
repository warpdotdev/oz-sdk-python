# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RunCreateParams"]


class RunCreateParams(TypedDict, total=False):
    prompt: Required[str]
    """
    The prompt sent to the factory's foreman, not wrapped in any factory intake
    envelope. Required and non-empty.
    """

    ticket_ref: str
    """
    Originating ticket reference in <source>:<id> form (for example,
    linear:REMOTE-123); omit to mint an adhoc reference. Stamped onto the run as
    ticket_id/ticket_source metadata.
    """

    ticket_url: str
    """Optional URL of the ticket named by ticket_ref.

    Stamped onto the run as ticket_url metadata when given.
    """

    title: str
    """
    Human-readable title for the dispatched run and its factory task. Omit to derive
    one automatically from the prompt.
    """
