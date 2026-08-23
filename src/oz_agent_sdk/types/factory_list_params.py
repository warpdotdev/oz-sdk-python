# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FactoryListParams"]


class FactoryListParams(TypedDict, total=False):
    cursor: str
    """Opaque cursor returned by a previous list response."""

    limit: int
    """Maximum number of factories to return (default 50, max 100)."""

    search: str
    """Case-insensitive substring search over the factory name and alias."""

    team_uid: str
    """Optional team UID to filter factories by ownership."""
