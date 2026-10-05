# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..secret_ref import SecretRef
from ..mcp_server_config import McpServerConfig

__all__ = ["ScorerCreateResponse", "AgentConfig", "Agent", "AllowedClassification"]


class AgentConfig(BaseModel):
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


class Agent(BaseModel):
    uid: str
    """Unique identifier of the selected agent"""

    include_descendants: Optional[bool] = None
    """Whether scoring this agent's run includes its descendant subtree"""


class AllowedClassification(BaseModel):
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


class ScorerCreateResponse(BaseModel):
    id: int
    """Scorer identifier"""

    agent_config: AgentConfig
    """Scorer-specific execution overrides for its hidden judge agent.

    An omitted or null field inherits the corresponding Factory agent default. A
    non-empty value replaces that default. Empty secrets and mcp_servers collections
    explicitly clear the optional Factory defaults.
    """

    agent_uids: List[str]
    """Agents attached to a selected_agents scorer; empty for all_agents"""

    agents: List[Agent]
    """Selected agents and whether each evaluation includes its run descendants"""

    allowed_classifications: List[AllowedClassification]

    created_at: datetime
    """When the scorer was created"""

    description: str
    """Description of the scorer"""

    factory_uid: str
    """UID of the factory that owns the scorer"""

    api_model_id: str = FieldInfo(alias="model_id")
    """LLM model dispatched judge runs use to evaluate this scorer's rubric."""

    name: str
    """Display name for the scorer"""

    sampling_rate: float
    """
    Percentage of the scorer's eligible runs that periodic scoring scores, to two
    decimal places. 0 stops automatic scoring.
    """

    scope_mode: Literal["all_agents", "selected_agents"]
    """Whether the scorer applies to every factory agent or selected agents"""

    scorer_kind: Literal["user", "benchmark_task_correctness"]
    """
    Whether the scorer is user-defined or a platform-owned managed scorer. Read-only
    on responses; create input does not accept scorer_kind.
    """

    scoring_prompt: str
    """Instructions used to score matching runs"""

    threshold: float
    """Score a run's classified label must meet or exceed to pass, from 0 to 1"""

    updated_at: datetime
    """When the scorer was updated"""

    version: int
    """Scorer definition version"""
