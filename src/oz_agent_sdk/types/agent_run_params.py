# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import Base64FileInput
from .._utils import PropertyInfo
from .._models import set_pydantic_config
from .ambient_agent_config_param import AmbientAgentConfigParam

__all__ = ["AgentRunParams", "Attachment"]


class AgentRunParams(TypedDict, total=False):
    agent_identity_uid: str
    """
    Optional agent identity UID to use as the execution principal for the run. This
    is only valid for runs that are team owned.
    """

    attachments: Iterable[Attachment]
    """
    Optional file attachments to include with the prompt (max 5). Attachments are
    uploaded to cloud storage and made available to the agent.
    """

    config: AmbientAgentConfigParam
    """Configuration for a cloud agent run"""

    conversation_id: str
    """
    Optional conversation ID to continue an existing conversation. If provided, the
    agent will continue from where the previous run left off.
    """

    interactive: bool
    """Whether the run should be interactive. If not set, defaults to false."""

    metadata: Dict[str, str]
    """
    Custom key/value metadata attached to a run at creation time and immutable
    afterward. At most 20 keys. Keys are 1-64 bytes matching [a-zA-Z0-9._-]+
    (case-sensitive); values are 0-256 bytes of UTF-8 and cannot contain NUL
    characters. Requests with invalid metadata are rejected. A run's effective
    metadata is merged per key at creation: explicit request keys override keys
    inherited from the parent run, which override automatic keys (ticket_id and
    ticket_source on Linear- and Jira-triggered runs).
    """

    mode: Literal["normal", "plan", "orchestrate"]
    """Optional query mode for the run.

    Defaults to `normal` when omitted. The server does not infer mode from prompt
    prefixes such as `/plan`, so callers should pass this field explicitly to
    request non-normal behavior.
    """

    parent_run_id: str
    """
    Optional run ID of the parent that spawned this run. Used for orchestration
    hierarchies.
    """

    prompt: str
    """
    The prompt/instruction for the agent to execute. Required unless a skill is
    specified via the skill field, config.skill_spec, or config.skills. Handoff
    requests may omit prompt when conversation_id is set.
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


class Attachment(TypedDict, total=False):
    """A base64-encoded file attachment to include with the prompt"""

    data: Required[Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]]
    """Base64-encoded attachment data"""

    file_name: Required[str]
    """Name of the attached file"""

    mime_type: Required[str]
    """
    MIME type of the attachment. Supported image types: image/jpeg, image/png,
    image/gif, image/webp
    """


set_pydantic_config(Attachment, {"arbitrary_types_allowed": True})
