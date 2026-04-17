# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .mcp_server_config import McpServerConfig

__all__ = ["AmbientAgentConfig", "Harness", "HarnessAuthSecrets"]


class Harness(BaseModel):
    """
    Specifies which execution harness to use for the agent run.
    Default (nil/empty) uses Warp's built-in harness.
    """

    type: Optional[Literal["oz", "claude"]] = None
    """The harness type identifier.

    - oz: Warp's built-in harness (default)
    - claude: Claude Code harness
    """


class HarnessAuthSecrets(BaseModel):
    """
    Authentication secrets for third-party harnesses.
    Only the secret for the harness specified gets injected into the environment.
    """

    claude_auth_secret_name: Optional[str] = None
    """
    Name of a managed secret for Claude Code harness authentication. The secret must
    exist within the caller's personal or team scope. Only applicable when harness
    type is "claude".
    """


class AmbientAgentConfig(BaseModel):
    """Configuration for a cloud agent run"""

    base_prompt: Optional[str] = None
    """Custom base prompt for the agent"""

    computer_use_enabled: Optional[bool] = None
    """
    Controls whether computer use is enabled for this agent. If not set, defaults to
    false.
    """

    environment_id: Optional[str] = None
    """UID of the environment to run the agent in"""

    harness: Optional[Harness] = None
    """
    Specifies which execution harness to use for the agent run. Default (nil/empty)
    uses Warp's built-in harness.
    """

    harness_auth_secrets: Optional[HarnessAuthSecrets] = None
    """
    Authentication secrets for third-party harnesses. Only the secret for the
    harness specified gets injected into the environment.
    """

    idle_timeout_minutes: Optional[int] = None
    """
    Number of minutes to keep the agent environment alive after task completion. If
    not set, defaults to 10 minutes. Maximum allowed value is min(60,
    floor(max_instance_runtime_seconds / 60) for your billing tier).
    """

    mcp_servers: Optional[Dict[str, McpServerConfig]] = None
    """Map of MCP server configurations by name"""

    api_model_id: Optional[str] = FieldInfo(alias="model_id", default=None)
    """LLM model to use (uses team default if not specified)"""

    name: Optional[str] = None
    """
    Human-readable label for grouping, filtering, and traceability. Automatically
    set to the skill name when running a skill-based agent. Set this explicitly to
    categorize runs by intent (e.g., "nightly-dependency-check") so you can filter
    and track them via the name query parameter on GET /agent/runs.
    """

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
