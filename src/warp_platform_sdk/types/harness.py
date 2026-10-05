# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Harness"]


class Harness(BaseModel):
    """
    Specifies which execution harness to use for the agent run.
    Default (nil/empty) uses Warp's built-in harness.
    When stored as a named agent's default (create/update agent identity),
    this field replaces the deprecated base_harness/base_model pair: a
    harness other than `oz` here requires the agent's base_model to be
    empty, since the two describe mutually exclusive default models.
    """

    api_model_id: Optional[str] = FieldInfo(alias="model_id", default=None)
    """Model to use with a third-party harness (e.g.

    "claude-haiku-4-5"). Only applies when type is a harness other than `oz`; the
    top-level config model_id targets the built-in Warp harness instead. When
    omitted or empty, the harness uses its own default model. For an individual
    Warp-managed Factory Claude Code agent, send an explicit empty string to use the
    environment's model. Omitting model_id when replacing that agent's harness is
    invalid.
    """

    reasoning_level: Optional[str] = None
    """Reasoning effort for harnesses that support it (e.g.

    Codex). Only applies when type is a harness other than `oz`. Ignored by
    harnesses that do not support reasoning levels.
    """

    type: Optional[Literal["oz", "claude", "gemini", "codex"]] = None
    """The harness type identifier.

    - oz: Warp's built-in harness (default)
    - claude: Claude Code harness
    - gemini: Gemini CLI harness
    - codex: Codex CLI harness
    """
