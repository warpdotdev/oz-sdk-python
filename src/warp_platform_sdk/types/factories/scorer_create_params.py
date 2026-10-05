# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr
from ..secret_ref_param import SecretRefParam
from ..mcp_server_config_param import McpServerConfigParam

__all__ = ["ScorerCreateParams", "AllowedClassification", "AgentConfig", "Agent"]


class ScorerCreateParams(TypedDict, total=False):
    allowed_classifications: Required[Iterable[AllowedClassification]]
    """Values the scorer may return; classification values must be unique"""

    factory_uid: Required[str]
    """UID of the factory that owns the scorer"""

    model_id: Required[str]
    """LLM model dispatched judge runs use to evaluate this scorer's rubric."""

    name: Required[str]
    """Display name for the scorer"""

    scope_mode: Required[Literal["all_agents", "selected_agents"]]
    """Whether the scorer applies to every factory agent or selected agents"""

    scoring_prompt: Required[str]
    """Instructions used to score matching runs"""

    threshold: Required[float]
    """Score a run's classified label must meet or exceed to pass, from 0 to 1."""

    agent_config: AgentConfig
    """Scorer-specific execution overrides for its hidden judge agent.

    An omitted or null field inherits the corresponding Factory agent default. A
    non-empty value replaces that default. Empty secrets and mcp_servers collections
    explicitly clear the optional Factory defaults.
    """

    agent_uids: SequenceNotStr[str]
    """
    Legacy shorthand for selected agents with include_descendants=false. Required
    and non-empty for selected_agents when agents is omitted; must be empty for
    all_agents and cannot be combined with agents.
    """

    agents: Iterable[Agent]
    """Selected agents and their evidence policy.

    Required and non-empty for selected_agents when agent_uids is omitted; must be
    empty for all_agents and cannot be combined with agent_uids.
    """

    description: Optional[str]
    """Optional description of the scorer"""

    sampling_rate: Optional[float]
    """
    Percentage of the scorer's eligible runs to score, from 0 to 100; omit to score
    every eligible run, and 0 stops automatic scoring (manual dispatch still works).
    A value with more than two decimal places is rounded to two rather than
    rejected, and the rounded value is what is stored. Sampling applies to periodic
    scoring only, and runs are chosen deterministically per (scorer, run), so
    lowering the rate reduces how many runs are scored rather than how often.
    """

    self_improvement_enabled: bool
    """
    Optionally enable self-improvement for the newly created scorer in the same
    transactional request, instead of a separate call to PUT
    /factory/scorers/{scorer_id}/self-improvement-config afterward; defaults to
    false. The response does not echo this back — a successful (2xx) response means
    the requested state was applied, confirmable at any time with GET
    .../self-improvement-config. Setting this to true requires a human user
    principal, matching the restriction on the PUT endpoint; a service-account
    principal gets the same error as calling that endpoint directly.
    """


class AllowedClassification(TypedDict, total=False):
    score: Required[float]
    """Score this classification carries, from 0 to 1.

    A run passes when its scored label's score is greater than or equal to the
    scorer's threshold. A score of exactly 0 is valid, so this is not enforced with
    a "required" binding (which would reject the zero value); handlers validate its
    range explicitly instead.
    """

    value: Required[str]
    """Classification value returned by the scorer"""

    description: Optional[str]
    """
    Optional free-text meaning of this classification, surfaced to the judge
    alongside the value. Omit or leave blank for a score-only label.
    """


class AgentConfig(TypedDict, total=False):
    """Scorer-specific execution overrides for its hidden judge agent.

    An
    omitted or null field inherits the corresponding Factory agent default.
    A non-empty value replaces that default. Empty secrets and mcp_servers
    collections explicitly clear the optional Factory defaults.
    """

    default_runner_uid: Optional[str]
    """Runner used by scorer judge runs.

    Omit or set null to inherit the Factory agent default.
    """

    mcp_servers: Optional[Dict[str, McpServerConfigParam]]
    """MCP servers attached to scorer judge runs.

    Omit or set null to inherit the Factory agent defaults; an empty object attaches
    none.
    """

    secrets: Optional[Iterable[SecretRefParam]]
    """Managed secrets attached to scorer judge runs.

    Omit or set null to inherit the Factory agent defaults; an empty array attaches
    none.
    """


class Agent(TypedDict, total=False):
    uid: Required[str]
    """Unique identifier of the selected agent"""

    include_descendants: bool
    """Whether scoring this agent's run includes its descendant subtree"""
