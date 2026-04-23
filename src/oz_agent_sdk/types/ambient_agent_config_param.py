# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, TypedDict

from .mcp_server_config_param import McpServerConfigParam

__all__ = ["AmbientAgentConfigParam", "Harness", "HarnessAuthSecrets", "SessionSharing"]


class Harness(TypedDict, total=False):
    """
    Specifies which execution harness to use for the agent run.
    Default (nil/empty) uses Warp's built-in harness.
    """

    type: Literal["oz", "claude", "gemini"]
    """The harness type identifier.

    - oz: Warp's built-in harness (default)
    - claude: Claude Code harness
    - gemini: Gemini CLI harness
    """


class HarnessAuthSecrets(TypedDict, total=False):
    """
    Authentication secrets for third-party harnesses.
    Only the secret for the harness specified gets injected into the environment.
    """

    claude_auth_secret_name: str
    """
    Name of a managed secret for Claude Code harness authentication. The secret must
    exist within the caller's personal or team scope. Only applicable when harness
    type is "claude".
    """


class SessionSharing(TypedDict, total=False):
    """
    Configures sharing behavior for the run's shared session.
    When set, the worker emits `--share public:<level>` and the bundled Warp
    client applies an anyone-with-link ACL to the shared session once it has
    bootstrapped. The same ACL is mirrored onto the backing conversation so
    link viewers can read the conversation without being on the run's team.
    Subject to the workspace-level anyone-with-link sharing setting.
    """

    public_access: Literal["VIEWER", "EDITOR"]
    """
    Grants anyone-with-link access at the specified level to the run's shared
    session and backing conversation.

    - VIEWER: link viewers can read the session and conversation.
    - EDITOR: link viewers can also interact with the session. Anonymous
      (unauthenticated) reads are not supported in this release; link viewers must
      still be authenticated Warp users.
    """


class AmbientAgentConfigParam(TypedDict, total=False):
    """Configuration for a cloud agent run"""

    base_prompt: str
    """Custom base prompt for the agent"""

    computer_use_enabled: bool
    """
    Controls whether computer use is enabled for this agent. If not set, defaults to
    false.
    """

    environment_id: str
    """UID of the environment to run the agent in"""

    harness: Harness
    """
    Specifies which execution harness to use for the agent run. Default (nil/empty)
    uses Warp's built-in harness.
    """

    harness_auth_secrets: HarnessAuthSecrets
    """
    Authentication secrets for third-party harnesses. Only the secret for the
    harness specified gets injected into the environment.
    """

    idle_timeout_minutes: int
    """
    Number of minutes to keep the agent environment alive after task completion. If
    not set, defaults to 10 minutes. Maximum allowed value is min(60,
    floor(max_instance_runtime_seconds / 60) for your billing tier).
    """

    mcp_servers: Dict[str, McpServerConfigParam]
    """Map of MCP server configurations by name"""

    model_id: str
    """LLM model to use (uses team default if not specified)"""

    name: str
    """
    Human-readable label for grouping, filtering, and traceability. Automatically
    set to the skill name when running a skill-based agent. Set this explicitly to
    categorize runs by intent (e.g., "nightly-dependency-check") so you can filter
    and track them via the name query parameter on GET /agent/runs.
    """

    session_sharing: SessionSharing
    """
    Configures sharing behavior for the run's shared session. When set, the worker
    emits `--share public:<level>` and the bundled Warp client applies an
    anyone-with-link ACL to the shared session once it has bootstrapped. The same
    ACL is mirrored onto the backing conversation so link viewers can read the
    conversation without being on the run's team. Subject to the workspace-level
    anyone-with-link sharing setting.
    """

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
