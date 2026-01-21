# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .ambient_agent_config_param import AmbientAgentConfigParam

__all__ = ["AgentRunParams"]


class AgentRunParams(TypedDict, total=False):
    prompt: Required[str]
    """The prompt/instruction for the agent to execute"""

    config: AmbientAgentConfigParam
    """Configuration for an ambient agent run"""

    team: bool
    """Make the run visible to all team members, not only the calling user"""

    title: str
    """Custom title for the run (auto-generated if not provided)"""
