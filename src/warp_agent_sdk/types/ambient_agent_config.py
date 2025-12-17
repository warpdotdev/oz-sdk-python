# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AmbientAgentConfig", "McpServers"]


class McpServers(BaseModel):
    """Configuration for an MCP server.

    Must have exactly one of: warp_id, command, or url.
    """

    args: Optional[List[str]] = None
    """Stdio transport - command arguments"""

    command: Optional[str] = None
    """Stdio transport - command to run"""

    env: Optional[Dict[str, str]] = None
    """Environment variables for the server"""

    headers: Optional[Dict[str, str]] = None
    """HTTP headers for SSE/HTTP transport"""

    url: Optional[str] = None
    """SSE/HTTP transport - server URL"""

    warp_id: Optional[str] = None
    """Reference to a Warp shared MCP server by UUID"""


class AmbientAgentConfig(BaseModel):
    """Configuration for an ambient agent task"""

    base_prompt: Optional[str] = None
    """Custom base prompt for the agent"""

    environment_id: Optional[str] = None
    """UID of a CloudEnvironment GSO to use"""

    mcp_servers: Optional[Dict[str, McpServers]] = None
    """Map of MCP server configurations by name"""

    api_model_id: Optional[str] = FieldInfo(alias="model_id", default=None)
    """LLM model to use (uses workspace default if not specified)"""

    name: Optional[str] = None
    """Config name for searchability and traceability"""
