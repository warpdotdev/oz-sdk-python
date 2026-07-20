# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

from ..ambient_agent_config_param import AmbientAgentConfigParam

__all__ = ["ScheduleUpdateParams"]


class ScheduleUpdateParams(TypedDict, total=False):
    cron_schedule: Required[str]
    """Cron expression defining when the agent runs"""

    enabled: Required[bool]
    """Whether the schedule should be active"""

    name: Required[str]
    """Human-readable name for the schedule"""

    agent_config: AmbientAgentConfigParam
    """Configuration for a cloud agent run"""

    agent_uid: str
    """
    Agent UID to use as the execution principal for this schedule. Only valid for
    team-owned schedules.
    """

    metadata: Dict[str, str]
    """
    Custom key/value metadata attached to a run at creation time and immutable
    afterward. At most 20 keys. Keys are 1-64 bytes matching [a-zA-Z0-9._-]+
    (case-sensitive); values are 0-256 bytes of UTF-8 and cannot contain NUL
    characters. Requests with invalid metadata are rejected. A run's effective
    metadata is merged per key at creation: explicit request keys override keys
    inherited from the parent run, which override automatic keys (ticket_id and
    ticket_source on Linear- and Jira-triggered runs).
    """

    mode: Literal["normal", "plan", "orchestrate"]
    """Optional query mode applied to every triggered run.

    Defaults to `normal` when omitted. The server does not infer mode from prompt
    prefixes such as `/plan`.
    """

    prompt: str
    """
    The prompt/instruction for the agent to execute. Required unless
    agent_config.skill_spec or agent_config.skills is provided.
    """
