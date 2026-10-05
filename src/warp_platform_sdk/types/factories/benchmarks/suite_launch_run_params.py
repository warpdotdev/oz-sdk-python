# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["SuiteLaunchRunParams", "Configuration", "ConfigurationAgentConfig"]


class SuiteLaunchRunParams(TypedDict, total=False):
    uid: Required[str]

    repetition_count: Required[int]
    """Number of repetitions per (task, configuration) pair, frozen onto the run.

    Like configurations and scorer_selection, this is chosen fresh at each launch
    rather than persisted on the suite.
    """

    configurations: Iterable[Configuration]
    """Optional launch-time configurations.

    When omitted, the suite's persistent configurations are used. An explicit empty
    list, or a suite with neither launch-time nor persistent configurations, is
    rejected.
    """

    historical_replay_run_uid: str
    """Internal provenance for a prior-run replay.

    The server accepts historical agent entries only when they exactly match frozen
    entries from this run and the run belongs to the same suite.
    """

    scorer_selection: Iterable[int]
    """Allowlist of live scorer IDs for this factory, applied to every trial in the
    run.

    Empty or absent means all applicable scorers. IDs must belong to the suite's
    factory and team (any status except deleted).
    """

    tasks: SequenceNotStr[str]
    """Optional allowlist of immutable UIDs for current tasks in the addressed suite.

    Omitted runs all current suite tasks. Explicit empty, invalid, unknown, stale,
    cross-suite, and duplicate selections are rejected.
    """


class ConfigurationAgentConfig(TypedDict, total=False):
    agent_uid: Required[str]

    harness: Required[str]

    model: Required[str]

    agent_name: str

    harness_auth_secret_name: Optional[str]


class Configuration(TypedDict, total=False):
    role: Required[Literal["baseline", "candidate"]]

    agent_configs: Iterable[ConfigurationAgentConfig]
    """Optional per-named-Agent overrides keyed by stable Agent UID."""

    display_name: str
    """Optional name for this configuration."""

    harness: str

    harness_auth_secret_name: Optional[str]
    """
    Optional managed-secret name this configuration's third-party harness
    authenticates with. Empty or omitted is valid for Oz. For a third-party harness
    that requires auth, empty or omitted means from the worker environment on a
    self-hosted host, or a launch violation on Warp-hosted.
    """

    model: str

    runner_id: Optional[str]
    """Optional runner UID, constrained to the Factory's existing runner roster.

    Omitted or empty uses the agent's or environment's default.
    """
