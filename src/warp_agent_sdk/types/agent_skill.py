# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["AgentSkill", "Variant", "VariantEnvironment", "VariantSource"]


class VariantEnvironment(BaseModel):
    name: str
    """Human-readable name of the environment"""

    uid: str
    """Unique identifier for the environment"""


class VariantSource(BaseModel):
    name: str
    """GitHub repository name"""

    owner: str
    """GitHub repository owner"""

    skill_path: str
    """Path to the skill definition file within the repository"""


class Variant(BaseModel):
    id: str
    """
    Stable identifier for this skill variant. Format: "{owner}/{repo}:{skill_path}"
    Example: "warpdotdev/warp-server:.claude/skills/deploy/SKILL.md"
    """

    base_prompt: str
    """Base prompt/instructions for the agent"""

    description: str
    """Description of the agent variant"""

    environments: List[VariantEnvironment]
    """Environments where this agent variant is available"""

    source: VariantSource

    last_run_timestamp: Optional[datetime] = None
    """Timestamp of the last time this skill was run (RFC3339)"""


class AgentSkill(BaseModel):
    name: str
    """Human-readable name of the agent"""

    variants: List[Variant]
    """Available variants of this agent"""
