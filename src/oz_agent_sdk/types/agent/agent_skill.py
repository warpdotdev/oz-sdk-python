# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["AgentSkill"]


class AgentSkill(BaseModel):
    """
    Information about the agent skill used for the run.
    Either full_path or bundled_skill_id will be set, but not both.
    """

    bundled_skill_id: Optional[str] = None
    """Unique identifier for bundled skills"""

    description: Optional[str] = None
    """Description of the skill"""

    full_path: Optional[str] = None
    """Path to the SKILL.md file (for file-based skills)"""

    name: Optional[str] = None
    """Human-readable name of the skill"""
