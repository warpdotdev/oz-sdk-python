# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AgentUpdateParams"]


class AgentUpdateParams(TypedDict, total=False):
    name: str
    """The new name for the agent"""
