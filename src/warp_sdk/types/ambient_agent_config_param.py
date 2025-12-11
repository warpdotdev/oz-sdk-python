# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["AmbientAgentConfigParam", "McpServers"]


class McpServers(TypedDict, total=False):
    """Configuration for an MCP server.

    Must have exactly one of: warp_id, command, or url.
    """

    args: SequenceNotStr[str]
    """Stdio transport - command arguments"""

    command: str
    """Stdio transport - command to run"""

    env: Dict[str, str]
    """Environment variables for the server"""

    headers: Dict[str, str]
    """HTTP headers for SSE/HTTP transport"""

    url: str
    """SSE/HTTP transport - server URL"""

    warp_id: str
    """Reference to a Warp shared MCP server by UUID"""


class AmbientAgentConfigParam(TypedDict, total=False):
    """Configuration for an ambient agent task"""

    base_prompt: str
    """Custom base prompt for the agent"""

    environment_id: str
    """UID of a CloudEnvironment GSO to use"""

    mcp_servers: Dict[str, McpServers]
    """Map of MCP server configurations by name"""

    model_id: str
    """LLM model to use (uses workspace default if not specified)"""

    name: str
    """Config name for searchability and traceability"""
