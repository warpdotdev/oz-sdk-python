# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AgentListModelsResponse", "Model"]


class Model(BaseModel):
    id: str
    """Unique identifier for the model (e.g. "claude-4-6-opus-high" or "gpt-5-4-high")"""

    display_name: str
    """Human-readable name of the model"""

    provider: Literal["OPENAI", "ANTHROPIC", "GOOGLE", "UNKNOWN"]
    """The LLM provider"""

    vision_supported: bool
    """Whether the model supports vision/image inputs"""

    description: Optional[str] = None
    """Optional extra descriptor for the model"""

    disable_reason: Optional[Literal["PROVIDER_OUTAGE", "OUT_OF_REQUESTS", "ADMIN_DISABLED", "REQUIRES_UPGRADE"]] = None
    """If set, the model is currently unavailable for the given reason"""

    reasoning_level: Optional[str] = None
    """Reasoning level descriptor, if any (e.g. "low", "medium", "high")"""


class AgentListModelsResponse(BaseModel):
    default_model_id: str
    """The ID of the default model for agent runs"""

    models: List[Model]
    """List of available models"""
