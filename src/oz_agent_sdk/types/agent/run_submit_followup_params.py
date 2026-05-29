# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RunSubmitFollowupParams"]


class RunSubmitFollowupParams(TypedDict, total=False):
    message: Required[str]
    """The follow-up message to send to the run."""

    mode: Literal["normal", "plan", "orchestrate"]
    """Optional query mode for the follow-up.

    Defaults to `normal` when omitted. The server does not infer mode from prompt
    prefixes such as `/plan`.
    """
