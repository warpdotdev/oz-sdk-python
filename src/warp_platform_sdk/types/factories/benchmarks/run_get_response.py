# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from ...user_profile import UserProfile

__all__ = ["RunGetResponse", "ConfigurationStat", "Configuration", "ConfigurationAgentConfig", "Trial", "TrialAttempt"]


class ConfigurationStat(BaseModel):
    id: int

    display_name: str
    """Optional name given to this configuration at launch. Empty when none was given."""

    fail_count: int

    pass_count: int

    role: Literal["baseline", "candidate"]

    trial_count: int
    """Trials dispatched so far for this configuration specifically."""

    avg_total_credits_per_trial: Optional[str] = None
    """Average credits per dispatched trial for this configuration so far.

    Null until this configuration has at least one dispatched trial; a real "0" once
    one has, even before any cost is measured.
    """

    avg_wall_time_s: Optional[float] = None
    """Average wall-clock time per dispatched trial for this configuration so far.

    Null until this configuration has at least one dispatched trial; a real 0 once
    one has, even before any duration is measured.
    """

    harness: Optional[str] = None
    """The configuration's frozen harness. Empty means the agent's default."""

    model: Optional[str] = None
    """The configuration's frozen model. Empty means the agent's default."""

    pass_rate: Optional[float] = None
    """pass_count / (pass_count + fail_count).

    Null until this configuration has at least one scored trial.
    """

    runner_id: Optional[str] = None
    """The configuration's frozen runner id. Empty means the platform default runner."""


class ConfigurationAgentConfig(BaseModel):
    agent_uid: str

    harness: str

    model: str

    agent_name: Optional[str] = None

    harness_auth_secret_name: Optional[str] = None


class Configuration(BaseModel):
    id: int

    display_name: str
    """Optional name given to this configuration at launch. Empty when none was given."""

    role: Literal["baseline", "candidate"]

    agent_configs: Optional[List[ConfigurationAgentConfig]] = None
    """Complete launch-time model/harness matrix keyed by stable Agent UID."""

    harness: Optional[str] = None
    """The configuration's frozen harness. Empty means the agent's default."""

    harness_auth_secret_name: Optional[str] = None
    """
    Optional managed-secret name this configuration's third-party harness
    authenticates with. Empty or omitted is valid for Oz. For a third-party harness
    that requires auth, empty or omitted means from the worker environment on a
    self-hosted host, or a launch violation on Warp-hosted.
    """

    model: Optional[str] = None
    """The configuration's frozen model. Empty means the agent's default."""

    runner_id: Optional[str] = None
    """Optional runner UID this configuration was launched with.

    Absent means the agent's or environment's default runner applied.
    """


class TrialAttempt(BaseModel):
    attempt_number: int
    """This run's 1-indexed position in the trial's attempt chain."""

    run_id: str

    state: str
    """
    The underlying agent run's terminal state (or its current state, for the chain's
    newest attempt).
    """


class Trial(BaseModel):
    id: int

    configuration_id: int

    rep_index: int

    state: Literal["pending", "running", "succeeded", "failed", "cancelled"]
    """Lifecycle state of a benchmark trial."""

    suite_task_id: int

    attempt_count: Optional[int] = None
    """How many attempts (the first dispatch plus every retry) this trial has used.

    1 for a trial that never retried, or for a run predating the retry mechanism.
    """

    attempts: Optional[List[TrialAttempt]] = None
    """This trial's attempt chain, oldest first, ending with its current run.

    Empty for a trial with no dispatched run, or for a run predating the retry
    mechanism.
    """

    run_id: Optional[str] = None

    task_title: Optional[str] = None
    """
    The suite task's title, frozen at launch, for labeling trials by name instead of
    id.
    """

    task_uid: Optional[str] = None
    """The immutable suite task UID frozen at launch. Absent on legacy runs."""


class RunGetResponse(BaseModel):
    created_at: datetime

    factory_uid: str

    state: Literal["pending", "running", "scoring", "completed", "failed", "cancelled"]
    """Lifecycle state of a benchmark run."""

    suite_name: str

    suite_uid: str

    uid: str

    updated_at: datetime

    agent_name: Optional[str] = None
    """Display name of the Factory agent frozen onto this run at launch.

    Absent on legacy runs.
    """

    agent_uid: Optional[str] = None
    """UID of the Factory agent frozen onto this run at launch."""

    completed_at: Optional[datetime] = None

    configuration_stats: Optional[List[ConfigurationStat]] = None
    """
    Per-configuration top-line stats, one entry per configuration frozen at launch
    (including a configuration with no trials dispatched yet). Null until the run
    has produced at least one trial, same as the other top-line stat fields above.
    """

    configurations: Optional[List[Configuration]] = None
    """
    The suite's configurations, frozen at launch, for grouping trials before results
    are available.
    """

    cost_usd: Optional[float] = None
    """
    Combined trial and scoring cost in US dollars: run_metrics.cost_usd plus
    run_metrics.scoring_cost_usd, each what the runs were billed. Matches the run
    detail page's Total cost. Null until the run has produced at least one trial.
    """

    creator: Optional[UserProfile] = None
    """The principal (user or service account) that launched this run, when known.

    Absent when creator identity is unknown or no longer retained.
    """

    elapsed_s: Optional[float] = None
    """
    The run's elapsed wall-clock time in seconds so far, matching
    BenchmarkResultsResponse's run_metrics.elapsed_s. Null when the run has not
    started or elapsed time is otherwise unavailable.
    """

    repetition_count: Optional[int] = None

    scorer_count: Optional[int] = None
    """Number of scorers applied to the run.

    Null until the run has produced at least one trial.
    """

    scorer_selection: Optional[List[int]] = None
    """The launch payload's scorer allowlist, frozen at launch.

    Empty or absent means all applicable scorers.
    """

    started_at: Optional[datetime] = None

    task_count: Optional[int] = None
    """Distinct suite tasks covered by the run's trials so far.

    Null until the run has produced at least one trial.
    """

    total_credits: Optional[str] = None
    """
    Total cost across the run's trials so far, in credits, matching
    BenchmarkResultsResponse's run_metrics.total_credits. Null until the run has
    produced at least one trial.
    """

    trial_count: Optional[int] = None
    """Number of trials dispatched so far.

    Null until the run has produced at least one trial.
    """

    trials: Optional[List[Trial]] = None
