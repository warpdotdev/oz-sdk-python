# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AgentListEnvironmentsParams"]


class AgentListEnvironmentsParams(TypedDict, total=False):
    sort_by: Literal["name", "last_updated"]
    """Sort order for the returned environments.

    - `name`: alphabetical by environment name
    - `last_updated`: most recently updated first (default)
    """
