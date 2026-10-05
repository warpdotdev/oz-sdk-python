# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AgentGetRunByExternalReferenceParams"]


class AgentGetRunByExternalReferenceParams(TypedDict, total=False):
    url: Required[str]
    """The canonical URL of the external reference artifact to look up."""
