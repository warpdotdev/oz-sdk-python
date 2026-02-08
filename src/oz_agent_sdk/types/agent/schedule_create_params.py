# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..ambient_agent_config_param import AmbientAgentConfigParam

__all__ = ["ScheduleCreateParams"]


class ScheduleCreateParams(TypedDict, total=False):
    cron_schedule: Required[str]
    """
    Cron expression defining when the agent runs (e.g., "0 9 \\** \\** \\**" for daily at
    9am UTC)
    """

    name: Required[str]
    """Human-readable name for the schedule"""

    prompt: Required[str]
    """The prompt/instruction for the agent to execute"""

    agent_config: AmbientAgentConfigParam
    """Configuration for an cloud agent run"""

    enabled: bool
    """Whether the schedule should be active immediately"""

    team: bool
    """
    Whether to create a team-owned schedule. Defaults to true for users on a single
    team.
    """
