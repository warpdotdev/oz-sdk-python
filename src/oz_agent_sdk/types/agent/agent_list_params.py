# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AgentListParams"]


class AgentListParams(TypedDict, total=False):
    factory_uid: str
    """Optional UID of a Factory to filter by.

    When provided, only agents linked to that factory (and owned by the caller's
    team) are returned. Ignored unless the factory API is enabled.
    """
