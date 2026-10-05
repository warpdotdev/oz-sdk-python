# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..secret_ref import SecretRef
from ..mcp_server_config import McpServerConfig

__all__ = [
    "ScorerListResponse",
    "Scorer",
    "ScorerAgentConfig",
    "ScorerAgent",
    "ScorerAllowedClassification",
    "ScorerPassRateSummary",
]


class ScorerAgentConfig(BaseModel):
    """Scorer-specific execution overrides for its hidden judge agent.

    An
    omitted or null field inherits the corresponding Factory agent default.
    A non-empty value replaces that default. Empty secrets and mcp_servers
    collections explicitly clear the optional Factory defaults.
    """

    default_runner_uid: Optional[str] = None
    """Runner used by scorer judge runs.

    Omit or set null to inherit the Factory agent default.
    """

    mcp_servers: Optional[Dict[str, McpServerConfig]] = None
    """MCP servers attached to scorer judge runs.

    Omit or set null to inherit the Factory agent defaults; an empty object attaches
    none.
    """

    secrets: Optional[List[SecretRef]] = None
    """Managed secrets attached to scorer judge runs.

    Omit or set null to inherit the Factory agent defaults; an empty array attaches
    none.
    """


class ScorerAgent(BaseModel):
    include_descendants: bool
    """Whether scoring this agent's run includes its descendant subtree"""

    name: str
    """Display name of the agent"""

    uid: str
    """Unique identifier of the agent"""


class ScorerAllowedClassification(BaseModel):
    score: float
    """Score this classification carries, from 0 to 1.

    A run passes when its scored label's score is greater than or equal to the
    scorer's threshold. A score of exactly 0 is valid, so this is not enforced with
    a "required" binding (which would reject the zero value); handlers validate its
    range explicitly instead.
    """

    value: str
    """Classification value returned by the scorer"""

    description: Optional[str] = None
    """
    Optional free-text meaning of this classification, surfaced to the judge
    alongside the value. Omit or leave blank for a score-only label.
    """


class ScorerPassRateSummary(BaseModel):
    fail_count: int
    """
    Number of live scores whose derived outcome is fail, within the same
    recent_outcomes_limit window as recent_outcomes (not the scorer's all-time
    history).
    """

    pass_count: int
    """
    Number of live scores whose derived outcome is pass, within the same
    recent_outcomes_limit window as recent_outcomes (not the scorer's all-time
    history).
    """

    recent_outcomes: List[Literal["pass", "fail"]]
    """
    The scorer's most recent live scores' outcomes, oldest first, for a compact
    history strip; length is bounded by recent_outcomes_limit, and failed attempts
    (no live score) are not included. pass_count and fail_count are computed over
    this exact same windowed set, so the headline rate and the strip always describe
    the same scores.
    """

    pass_rate: Optional[float] = None
    """
    pass_count / (pass_count + fail_count), over the same recent window as
    pass_count and fail_count. Null when there are no scoreable (pass or fail)
    scores in that window. Clients must not use result_count as the denominator.
    """


class Scorer(BaseModel):
    id: int
    """Scorer identifier"""

    agent_config: ScorerAgentConfig
    """Scorer-specific execution overrides for its hidden judge agent.

    An omitted or null field inherits the corresponding Factory agent default. A
    non-empty value replaces that default. Empty secrets and mcp_servers collections
    explicitly clear the optional Factory defaults.
    """

    agents: List[ScorerAgent]
    """Named agents in scope; empty when the scorer covers all factory agents"""

    allowed_classifications: List[ScorerAllowedClassification]

    created_at: datetime
    """When the scorer was created"""

    description: str
    """Description of the scorer"""

    factory_uid: str
    """Public UID of the factory that owns the scorer"""

    api_model_id: str = FieldInfo(alias="model_id")
    """LLM model dispatched judge runs use to evaluate this scorer's rubric."""

    name: str
    """Display name for the scorer"""

    pass_rate_summary: ScorerPassRateSummary

    result_count: int
    """Number of live scores recorded for the scorer"""

    sampling_rate: float
    """
    Percentage of the scorer's eligible runs that periodic scoring scores, to two
    decimal places. 0 stops automatic scoring.
    """

    scope_mode: Literal["all_agents", "selected_agents"]
    """all_agents (every agent in the scorer's factory) or selected_agents"""

    scorer_kind: Literal["user", "benchmark_task_correctness"]
    """
    Whether the scorer is user-defined or a platform-owned managed scorer. Read-only
    on responses; create input does not accept scorer_kind.
    """

    scoring_prompt: str
    """Instructions used to score the agent's runs"""

    self_improvement_enabled: bool
    """Whether self-improvement is enabled for this scorer"""

    threshold: float
    """Score a run's classified label must meet or exceed to pass, from 0 to 1"""

    updated_at: datetime
    """When the scorer was last updated"""

    version: int
    """Scorer definition version"""

    last_scored_at: Optional[datetime] = None
    """When the scorer last recorded a score"""


class ScorerListResponse(BaseModel):
    scorers: List[Scorer]
