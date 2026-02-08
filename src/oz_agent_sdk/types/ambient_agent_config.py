# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .mcp_server_config import McpServerConfig

__all__ = ["AmbientAgentConfig"]


class AmbientAgentConfig(BaseModel):
    """Configuration for an cloud agent run"""

    base_prompt: Optional[str] = None
    """Custom base prompt for the agent"""

    computer_use_enabled: Optional[bool] = None
    """
    Controls whether computer use is enabled for this agent. If not set, defaults to
    false.
    """

    environment_id: Optional[str] = None
    """UID of the environment to run the agent in"""

    mcp_servers: Optional[Dict[str, McpServerConfig]] = None
    """Map of MCP server configurations by name"""

    api_model_id: Optional[str] = FieldInfo(alias="model_id", default=None)
    """LLM model to use (uses team default if not specified)"""

    name: Optional[str] = None
    """Config name for searchability and traceability"""

    skill_spec: Optional[str] = None
    """
    Skill specification identifying which agent skill to use. Format:
    "{owner}/{repo}:{skill_path}" Example:
    "warpdotdev/warp-server:.claude/skills/deploy/SKILL.md" Use the list agents
    endpoint to discover available skills.
    """

    worker_host: Optional[str] = None
    """
    Self-hosted worker ID that should execute this task. If not specified or set to
    "warp", the task runs on Warp-hosted workers.
    """
