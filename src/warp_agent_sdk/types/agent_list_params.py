# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AgentListParams"]


class AgentListParams(TypedDict, total=False):
    repo: str
    """
    Optional repository specification to list agents from (format: "owner/repo"). If
    not provided, lists agents from all accessible environments.
    """
