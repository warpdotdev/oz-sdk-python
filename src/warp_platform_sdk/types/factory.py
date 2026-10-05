# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .harness import Harness
from .._models import BaseModel
from .secret_ref import SecretRef
from .mcp_server_config import McpServerConfig
from .harness_auth_secrets import HarnessAuthSecrets

__all__ = [
    "Factory",
    "AgentDefaults",
    "Integration",
    "IntegrationJira",
    "IntegrationLinear",
    "IntegrationMicrosoftTeams",
    "IntegrationSlack",
    "Repository",
    "ScorerDefaults",
    "Scoring",
    "Creator",
    "SelfImprovement",
]


class AgentDefaults(BaseModel):
    """
    Default execution settings inherited by the factory's named agents
    when they declare no override of their own.
    """

    default_runner_uid: str
    """Default runner UID for the factory's named agents.

    Empty when unset, in which case the environment's default runner applies.
    """

    mcp_servers: Dict[str, McpServerConfig]
    """MCP server configurations attached to the factory's named agents by default.

    Only warp_id (managed MCP) entries are representable for a Warp-managed factory.
    """

    secrets: List[SecretRef]
    """Secrets attached to the factory's named agents by default."""

    worker_host: str
    """Default worker host for the factory's named agents.

    Empty when unset, in which case the workspace default applies.
    """

    harness: Optional[Harness] = None
    """
    Specifies which execution harness to use for the agent run. Default (nil/empty)
    uses Warp's built-in harness. When stored as a named agent's default
    (create/update agent identity), this field replaces the deprecated
    base_harness/base_model pair: a harness other than `oz` here requires the
    agent's base_model to be empty, since the two describe mutually exclusive
    default models.
    """

    harness_auth_secrets: Optional[HarnessAuthSecrets] = None
    """
    Authentication secrets for third-party harnesses. Only the secret for the
    harness specified gets injected into the environment.
    """


class IntegrationJira(BaseModel):
    """
    Jira project keys from earlier integration selections, when present.
    Issue discovery follows enabled agent-session automations instead.
    """

    project_keys: List[str]
    """
    Jira project keys (for example APP, not the numeric project ID) for the one-time
    agent-session automation seed. Discovery follows enabled seated automation
    filters afterward.
    """


class IntegrationLinear(BaseModel):
    """
    Linear team IDs from earlier integration selections, when present.
    Issue discovery follows enabled agent-session automations instead.
    """

    team_ids: List[str]
    """
    Linear team IDs for the one-time agent-session automation seed. Discovery
    follows enabled seated automation filters afterward.
    """


class IntegrationMicrosoftTeams(BaseModel):
    """Plain channel-thread reply settings.

    These apply when the shared
    per-Factory reply-setting rollout is enabled.
    """

    auto_respond_to_thread_replies: Optional[bool] = None
    """
    When true, eligible plain channel thread replies still reach the reply-intent
    classifier. When false, those replies are ignored unless they @-mention the
    Factory. Each provider defines the omitted default. Direct messages are
    unchanged.
    """


class IntegrationSlack(BaseModel):
    """Plain channel-thread reply settings.

    These apply when the shared
    per-Factory reply-setting rollout is enabled.
    """

    auto_respond_to_thread_replies: Optional[bool] = None
    """
    When true, eligible plain channel thread replies still reach the reply-intent
    classifier. When false, those replies are ignored unless they @-mention the
    Factory. Each provider defines the omitted default. Direct messages are
    unchanged.
    """


class Integration(BaseModel):
    """An integration provider attached to a factory."""

    type: Literal["jira", "linear", "microsoft-teams", "slack"]
    """Integration provider that can be attached to a factory.

    github is not accepted here; repository access comes from the factory's code
    forge.
    """

    jira: Optional[IntegrationJira] = None
    """
    Jira project keys from earlier integration selections, when present. Issue
    discovery follows enabled agent-session automations instead.
    """

    linear: Optional[IntegrationLinear] = None
    """
    Linear team IDs from earlier integration selections, when present. Issue
    discovery follows enabled agent-session automations instead.
    """

    microsoft_teams: Optional[IntegrationMicrosoftTeams] = FieldInfo(alias="microsoft-teams", default=None)
    """Plain channel-thread reply settings.

    These apply when the shared per-Factory reply-setting rollout is enabled.
    """

    slack: Optional[IntegrationSlack] = None
    """Plain channel-thread reply settings.

    These apply when the shared per-Factory reply-setting rollout is enabled.
    """


class Repository(BaseModel):
    """A repository scoped to a factory."""

    owner: str
    """Repository owner (or full namespace for GitLab)."""

    repo: str
    """Repository name."""

    code_forge: Optional[Literal["GITHUB", "GITLAB", "AZURE_DEVOPS"]] = None
    """The concrete source-control provider hosting a repository."""

    provider_metadata: Optional[Dict[str, str]] = None
    """
    Provider-specific repository identity and settings, such as the Azure DevOps
    organization, project ID, and repository ID.
    """


class ScorerDefaults(BaseModel):
    """Sparse execution defaults for scorers.

    An omitted field inherits the
    corresponding agent default; an explicit empty collection overrides
    the agent default with no values.
    """

    default_runner_uid: Optional[str] = None
    """Default runner UID for scorers. Omitted to inherit the agent default."""

    mcp_servers: Optional[Dict[str, McpServerConfig]] = None
    """Scorer-default MCP servers.

    Omitted to inherit the agent defaults; an empty object explicitly clears them.
    """

    secrets: Optional[List[SecretRef]] = None
    """Scorer-default secrets.

    Omitted to inherit the agent defaults; an empty array explicitly clears them.
    """


class Scoring(BaseModel):
    default_model: Optional[str] = None
    """
    Optional factory override for the model used by managed scorers and
    scorer-creation prefills. null or absent resolves to the platform judge default.
    User-created scorers still require an explicit model_id on create.
    """


class Creator(BaseModel):
    """The user who created a factory, when resolvable."""

    uid: str
    """Firebase UID of the user who created the factory."""

    email: Optional[str] = None
    """Creator's email, when available."""


class SelfImprovement(BaseModel):
    """Self-improvement settings from GitHub-managed Factory YAML.

    Omitted when none are declared, in which case team admins are the reviewer pool.
    """

    reviewer_type: Literal["none", "admins", "team", "custom"]
    """
    Owning-team pool one eligible reviewer is randomly requested from for
    self-improvement pull requests. `admins` requests a team admin or owner and is
    the default when the Factory declares no self-improvement settings. `team`
    requests any team member. `custom` requests a member listed in
    `reviewer_emails`. `none` explicitly disables reviewer assignment.
    """

    failed_run_threshold: Optional[int] = None
    """
    Per-agent count of distinct scored-failing source runs required for scheduled
    self-improvement. Must be between 1 and 50: one self-improvement run can triage
    at most 50 failure findings. Omitted to use the server default. The age-based
    flush and manual dispatch are unchanged.
    """

    reviewer_emails: Optional[List[str]] = None
    """Owning-team member emails reviewers are chosen from.

    Only allowed when `reviewer_type` is `custom`: a Factory YAML change that sets
    emails with any other reviewer type fails validation, including the pull request
    check.
    """


class Factory(BaseModel):
    """Public representation of a factory."""

    agent_defaults: AgentDefaults
    """
    Default execution settings inherited by the factory's named agents when they
    declare no override of their own.
    """

    alias: Optional[str] = None
    """
    Optional display handle for the factory, unique across the team's Warp workspace
    when set.
    """

    avatar_url: Optional[str] = None
    """Short-lived signed URL for displaying the factory's avatar.

    The URL may change between reads.
    """

    code_forge: Literal["GITHUB", "GITLAB", "AZURE_DEVOPS", "NONE"]
    """Primary source-control provider for the factory.

    GITHUB and GITLAB identify the compatibility primary when repositories span one
    or more forges. AZURE_DEVOPS identifies Azure Repos. NONE declares a repo-less
    factory with no native repositories; its environment relies on setup_commands to
    clone from any host.
    """

    code_forges: List[Literal["GITHUB", "GITLAB", "AZURE_DEVOPS", "NONE"]]
    """Effective source-control providers for the factory.

    When the effective set is empty, this contains the primary code_forge.
    """

    created_at: datetime
    """Time the factory was created."""

    credential_strategy: Literal["CREATOR", "EXECUTOR"]
    """Default credential strategy for runs executed by the factory's named agents.

    - EXECUTOR (default): runs authenticate with the named agent's own credentials
      (e.g. a GitHub App installation token for the factory's team).
    - CREATOR: runs authenticate with the credentials of the principal that created
      the run.
    """

    default_environment: Optional[str] = None
    """Public UID of the factory's default environment.

    File-managed factories may omit this default.
    """

    default_model: Optional[str] = None
    """The default model ID for the factory's runs.

    File-managed factories may omit this default. Live-managed create and PATCH
    requests still capture a concrete validated model ID.
    """

    description: Optional[str] = None
    """Optional description of the factory."""

    integrations: Optional[List[Integration]] = None
    """
    Integration providers attached to the factory, independent of the automation
    triggers configured for it. null means the factory has not declared anything
    yet; an empty array means no providers are attached.
    """

    name: str
    """Display name of the factory."""

    repositories: List[Repository]
    """Repositories scoped to the factory, independent of its default environment."""

    scorer_defaults: ScorerDefaults
    """Sparse execution defaults for scorers.

    An omitted field inherits the corresponding agent default; an explicit empty
    collection overrides the agent default with no values.
    """

    scoring: Scoring

    team_uid: str
    """Public UID of the team that owns the factory."""

    uid: str
    """Public UID of the factory."""

    updated_at: datetime
    """Time the factory was last updated."""

    creator: Optional[Creator] = None
    """The user who created a factory, when resolvable."""

    self_improvement: Optional[SelfImprovement] = None
    """Self-improvement settings from GitHub-managed Factory YAML.

    Omitted when none are declared, in which case team admins are the reviewer pool.
    """
