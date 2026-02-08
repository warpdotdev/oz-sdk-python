# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..ambient_agent_config_param import AmbientAgentConfigParam

__all__ = ["ScheduleUpdateParams"]


class ScheduleUpdateParams(TypedDict, total=False):
    cron_schedule: Required[str]
    """Cron expression defining when the agent runs"""

    enabled: Required[bool]
    """Whether the schedule should be active"""

    name: Required[str]
    """Human-readable name for the schedule"""

    prompt: Required[str]
    """The prompt/instruction for the agent to execute"""

    agent_config: AmbientAgentConfigParam
    """Configuration for an cloud agent run"""
