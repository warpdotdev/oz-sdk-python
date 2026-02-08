# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import Base64FileInput
from .._utils import PropertyInfo
from .._models import set_pydantic_config
from .ambient_agent_config_param import AmbientAgentConfigParam

__all__ = ["AgentRunParams", "Image"]


class AgentRunParams(TypedDict, total=False):
    config: AmbientAgentConfigParam
    """Configuration for an cloud agent run"""

    conversation_id: str
    """
    Optional conversation ID to continue an existing conversation. If provided, the
    agent will continue from where the previous run left off.
    """

    images: Iterable[Image]
    """
    Optional images to include with the prompt (max 5). Images are uploaded to cloud
    storage and made available to the agent.
    """

    prompt: str
    """
    The prompt/instruction for the agent to execute. Required unless a skill is
    specified via the skill field or config.skill_spec.
    """

    skill: str
    """Skill specification to use as the base prompt for the agent. Supported formats:

    - "repo:skill_name" - Simple name in specific repo
    - "repo:skill_path" - Full path in specific repo
    - "org/repo:skill_name" - Simple name with org and repo
    - "org/repo:skill_path" - Full path with org and repo When provided, this takes
      precedence over config.skill_spec.
    """

    team: bool
    """
    Whether to create a team-owned run. Defaults to true for users on a single team.
    """

    title: str
    """Custom title for the run (auto-generated if not provided)"""


class Image(TypedDict, total=False):
    """A base64-encoded image to include with the prompt"""

    data: Required[Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]]
    """Base64-encoded image data"""

    mime_type: Required[Literal["image/jpeg", "image/png", "image/gif", "image/webp"]]
    """
    MIME type of the image. Supported types: image/jpeg, image/png, image/gif,
    image/webp
    """


set_pydantic_config(Image, {"arbitrary_types_allowed": True})
