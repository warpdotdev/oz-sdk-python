# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr
from .harness_param import HarnessParam
from .secret_ref_param import SecretRefParam
from .memory_store_ref_param import MemoryStoreRefParam
from .mcp_server_config_param import McpServerConfigParam
from .harness_auth_secrets_param import HarnessAuthSecretsParam
from .session_sharing_config_param import SessionSharingConfigParam
from .inference_providers_config_param import InferenceProvidersConfigParam

__all__ = ["AgentConfigSnapshotParam"]


class AgentConfigSnapshotParam(TypedDict, total=False):
    """Configuration for a cloud agent run"""

    base_prompt: str
    """Custom base prompt for the agent"""

    computer_use_enabled: bool
    """
    Controls whether computer use is enabled for this agent. If not set, defaults to
    true.
    """

    computer_use_model_id: str
    """
    Model the computer use subagent runs on; if omitted, the subagent picks its own
    model automatically. Only applies to the built-in Warp harness — the value is
    accepted but has no effect under a third-party harness or when computer use is
    disabled. Requires an agent CLI version that supports the --computer-use-model
    flag.
    """

    credential_strategy: Optional[Literal["CREATOR", "EXECUTOR"]]
    """
    Controls which principal's credentials are used when the platform mints tokens
    (e.g. GitHub or GitLab OAuth tokens) on behalf of this run.

    - EXECUTOR (default when unset): credentials are sourced from the run's
      execution principal — a GitHub App installation token for agent principals, a
      personal OAuth token for user principals.
    - CREATOR: credentials are always sourced from the run creator regardless of the
      execution principal, useful when a service account executes the run but Git
      operations should authenticate as the triggering human.
    """

    environment_id: str
    """UID of the environment to run the agent in"""

    harness: HarnessParam
    """
    Specifies which execution harness to use for the agent run. Default (nil/empty)
    uses Warp's built-in harness. When stored as a named agent's default
    (create/update agent identity), this field replaces the deprecated
    base_harness/base_model pair: a harness other than `oz` here requires the
    agent's base_model to be empty, since the two describe mutually exclusive
    default models.
    """

    harness_auth_secrets: HarnessAuthSecretsParam
    """
    Authentication secrets for third-party harnesses. Only the secret for the
    harness specified gets injected into the environment.
    """

    idle_timeout_minutes: int
    """
    Number of minutes to keep the agent environment alive after task completion. Set
    to 0 to shut down immediately after task completion. If not set, defaults to 10
    minutes. Maximum allowed value is min(60, floor(max_instance_runtime_seconds
    / 60) for your billing tier).
    """

    inference_providers: InferenceProvidersConfigParam
    """Inference provider settings used for LLM calls."""

    mcp_servers: Dict[str, McpServerConfigParam]
    """Map of MCP server configurations by name"""

    memory_stores: Iterable[MemoryStoreRefParam]
    """Memory stores to attach to this run."""

    model_id: str
    """LLM model to use (uses team default if not specified)"""

    name: str
    """
    Human-readable label for grouping, filtering, and traceability. Automatically
    set to the skill name when running a skill-based agent. Set this explicitly to
    categorize runs by intent (e.g., "nightly-dependency-check") so you can filter
    and track them via the name query parameter on GET /agent/runs.
    """

    runner_id: str
    """
    UID of the runner providing the run's compute (platform, instance shape, and
    setup commands). When omitted on a request, the runner is resolved at run
    creation from the agent's default runner, then the environment's default runner,
    and the resolved UID is recorded on the run.
    """

    secrets: Iterable[SecretRefParam]
    """Optional run-specific managed secret allowlist.

    Omission and an empty array both add no generic secrets. Secret references from
    the resolved environment and execution principal are still unioned into the
    run's secret scope.
    """

    session_sharing: SessionSharingConfigParam
    """
    Configures sharing behavior for the run's shared session; when set, the worker
    emits `--share public:<level>` and the bundled Warp client applies an
    anyone-with-link ACL to the shared session once it has bootstrapped. The same
    ACL is mirrored onto the backing conversation so link viewers can read it
    without being on the run's team, subject to the workspace-level anyone-with-link
    sharing setting.
    """

    skill_spec: str
    """
    Skill specification identifying the primary agent skill to use, in
    `{owner}/{repo}:{skill_path}` format (e.g.
    `warpdotdev/warp-server:.claude/skills/deploy/SKILL.md`); mutually exclusive
    with `skills` in create/update requests. Responses include the first `skills`
    entry here for backward compatibility; use the list agents endpoint to discover
    available skills.
    """

    skills: SequenceNotStr[str]
    """
    Ordered skill specifications to attach to the run. Format:
    "{owner}/{repo}:{skill_path}" Example:
    "warpdotdev/warp-server:.claude/skills/deploy/SKILL.md" Mutually exclusive with
    skill_spec in create/update requests.
    """

    worker_host: str
    """
    Self-hosted worker ID that should execute this task. If not specified or set to
    "warp", the task runs on Warp-hosted workers.
    """
