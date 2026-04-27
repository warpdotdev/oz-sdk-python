# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RunSubmitFollowupParams"]


class RunSubmitFollowupParams(TypedDict, total=False):
    message: Required[str]
    """The follow-up message to send to the run."""
