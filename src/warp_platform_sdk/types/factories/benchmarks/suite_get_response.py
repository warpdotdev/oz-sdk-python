# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ...._models import BaseModel
from ...user_profile import UserProfile

__all__ = ["SuiteGetResponse", "Configuration", "ConfigurationAgentConfig", "Task", "TaskStartingRepoRef"]


class ConfigurationAgentConfig(BaseModel):
    agent_uid: str

    harness: str

    model: str

    agent_name: Optional[str] = None

    harness_auth_secret_name: Optional[str] = None


class Configuration(BaseModel):
    agent_configs: Optional[List[ConfigurationAgentConfig]] = None
    """Optional per-named-Agent overrides keyed by stable Agent UID."""

    display_name: Optional[str] = None
    """Optional name for this configuration."""

    harness: Optional[str] = None

    harness_auth_secret_name: Optional[str] = None
    """
    Optional managed-secret name this configuration's third-party harness
    authenticates with. Empty or omitted is valid for Oz. For a third-party harness
    that requires auth, empty or omitted means from the worker environment on a
    self-hosted host, or a launch violation on Warp-hosted.
    """

    model: Optional[str] = None

    runner_id: Optional[str] = None
    """Optional runner UID, constrained to the Factory's existing runner roster.

    Omitted or empty uses the agent's or environment's default.
    """


class TaskStartingRepoRef(BaseModel):
    """A repository location and optional starting ref for a suite task."""

    code_forge: str

    owner: str

    repo: str

    ref: Optional[str] = None


class Task(BaseModel):
    id: int
    """Deprecated internal storage identifier retained for compatibility."""

    prompt: str

    success_criteria: str
    """
    Plain-text criteria the built-in Correctness scorer grades each trial against,
    as the authoritative requirements. The task prompt provides context only.
    """

    title: str

    uid: str
    """Immutable public task identifier."""

    labels: Optional[Dict[str, str]] = None

    source_run_id: Optional[str] = None

    starting_repo_refs: Optional[List[TaskStartingRepoRef]] = None

    tags: Optional[List[str]] = None


class SuiteGetResponse(BaseModel):
    agent_uid: str
    """UID of the concrete Factory agent every task in this suite dispatches as.

    Must resolve to a live, available agent linked to this Factory whose agent_type
    equals factory_agent_type.
    """

    created_at: datetime

    factory_agent_type: str
    """
    Coarse Factory agent type of the selected agent_uid, kept in sync with it at
    save time.
    """

    factory_uid: str

    name: str

    spawnable_descendant_agent_uids: List[str]
    """
    Stable UID-sorted list of live, non-system Factory agents transitively reachable
    from this suite's selected root under the server's effective delegation policy.
    """

    uid: str

    updated_at: datetime

    configurations: Optional[List[Configuration]] = None
    """File-authored launch defaults.

    Omitted on suites without persistent configurations.
    """

    creator: Optional[UserProfile] = None
    """The suite's creator, when known.

    Absent when creator identity is unknown or no longer retained.
    """

    description: Optional[str] = None

    tasks: Optional[List[Task]] = None
