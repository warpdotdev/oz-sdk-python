# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SecretRefParam"]


class SecretRefParam(TypedDict, total=False):
    """Reference to a managed secret by name."""

    name: Required[str]
    """Name of the managed secret."""
