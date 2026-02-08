# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AgentListParams"]


class AgentListParams(TypedDict, total=False):
    refresh: bool
    """
    When true, clears the agent list cache before fetching. Use this to force a
    refresh of the available agents.
    """

    repo: str
    """
    Optional repository specification to list agents from (format: "owner/repo"). If
    not provided, lists agents from all accessible environments.
    """

    sort_by: Literal["name", "last_run"]
    """Sort order for the returned agents.

    - "name": Sort alphabetically by name (default)
    - "last_run": Sort by most recently used
    """
