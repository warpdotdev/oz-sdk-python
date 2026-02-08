# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

from .mcp_server_config_param import McpServerConfigParam

__all__ = ["AmbientAgentConfigParam"]


class AmbientAgentConfigParam(TypedDict, total=False):
    """Configuration for an cloud agent run"""

    base_prompt: str
    """Custom base prompt for the agent"""

    computer_use_enabled: bool
    """
    Controls whether computer use is enabled for this agent. If not set, defaults to
    false.
    """

    environment_id: str
    """UID of the environment to run the agent in"""

    mcp_servers: Dict[str, McpServerConfigParam]
    """Map of MCP server configurations by name"""

    model_id: str
    """LLM model to use (uses team default if not specified)"""

    name: str
    """Config name for searchability and traceability"""

    skill_spec: str
    """
    Skill specification identifying which agent skill to use. Format:
    "{owner}/{repo}:{skill_path}" Example:
    "warpdotdev/warp-server:.claude/skills/deploy/SKILL.md" Use the list agents
    endpoint to discover available skills.
    """

    worker_host: str
    """
    Self-hosted worker ID that should execute this task. If not specified or set to
    "warp", the task runs on Warp-hosted workers.
    """
