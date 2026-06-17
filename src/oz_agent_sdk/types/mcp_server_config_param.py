# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["McpServerConfigParam"]


class McpServerConfigParam(TypedDict, total=False):
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
