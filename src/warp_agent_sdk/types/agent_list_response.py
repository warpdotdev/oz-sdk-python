# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["AgentListResponse", "Agent", "AgentVariant", "AgentVariantEnvironment", "AgentVariantSource"]


class AgentVariantEnvironment(BaseModel):
    name: str
    """Human-readable name of the environment"""

    uid: str
    """Unique identifier for the environment"""


class AgentVariantSource(BaseModel):
    name: str
    """GitHub repository name"""

    owner: str
    """GitHub repository owner"""

    skill_path: str
    """Path to the skill definition file within the repository"""


class AgentVariant(BaseModel):
    id: str
    """
    Stable identifier for this skill variant. Format: "{owner}/{repo}:{skill_path}"
    Example: "warpdotdev/warp-server:.claude/skills/deploy/SKILL.md"
    """

    base_prompt: str
    """Base prompt/instructions for the agent"""

    description: str
    """Description of the agent variant"""

    environments: List[AgentVariantEnvironment]
    """Environments where this agent variant is available"""

    source: AgentVariantSource


class Agent(BaseModel):
    name: str
    """Human-readable name of the agent"""

    variants: List[AgentVariant]
    """Available variants of this agent"""


class AgentListResponse(BaseModel):
    agents: List[Agent]
    """List of available agents"""
