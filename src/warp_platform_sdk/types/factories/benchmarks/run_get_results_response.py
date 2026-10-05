# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = [
    "RunGetResultsResponse",
    "Configuration",
    "ConfigurationAgentConfig",
    "RunMetrics",
    "TrialProgress",
    "Trial",
    "TrialAttempt",
]


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

    metrics: object
    """Objective credit and wall-time measurements for this configuration."""

    retried_trial_count: int
    """This configuration's trial count with at least one retry (attempt_count > 1)."""

    retry_count: int
    """
    Total number of retries (attempt_count - 1, summed) across this configuration's
    trials.
    """

    role: Literal["baseline", "candidate"]

    scoring: object
    """Pass/fail tally with the derived pass rate across all applicable scorers."""

    agent_configs: Optional[List[ConfigurationAgentConfig]] = None
    """Complete launch-time model/harness matrix keyed by stable Agent UID."""

    harness: Optional[str] = None
    """The configuration's frozen harness. Empty means the agent's default."""

    harness_auth_secret_name: Optional[str] = None
    """
    Optional managed-secret name this configuration's third-party harness
    authenticated with. Frozen from the launch payload.
    """

    model: Optional[str] = None
    """The configuration's frozen model. Empty means the agent's default."""


class RunMetrics(BaseModel):
    compute_credits: str

    cost_usd: float
    """Estimated trial-run spend at the owning team's current credit price.

    Not a billed amount.
    """

    elapsed_s: float

    platform_credits: str

    scoring_cost_usd: float
    """Estimated scoring and judge spend at the owning team's current credit price.

    Not a billed amount.
    """

    total_credits: str
    """Credits consumed by benchmark trial runs."""

    scoring_credits: Optional[str] = None
    """Credits consumed by distinct dispatched scoring and judge runs.

    Present only when the benchmark in-progress UI feature is enabled.
    """


class TrialProgress(BaseModel):
    """Logical (task, configuration, repetition) trial counts by lifecycle
    state.

    A retry remains part of its original trial. completed is
    succeeded + failed + cancelled.
    """

    cancelled: int

    completed: int

    failed: int

    pending: int

    running: int

    succeeded: int

    total: int


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
    configuration_id: int

    metrics: object

    rep_index: int

    scores: List[object]

    state: str

    suite_task_id: int
    """Frozen internal storage coordinate retained for compatibility."""

    attempt_count: Optional[int] = None

    attempts: Optional[List[TrialAttempt]] = None

    judge_runs: Optional[List[object]] = None

    run_id: Optional[str] = None

    task_title: Optional[str] = None

    task_uid: Optional[str] = None
    """The immutable suite task UID frozen at launch. Absent on legacy runs."""

    terminal_reason: Optional[Literal["timeout", "failure"]] = None
    """Normalized terminal reason for a failed trial.

    timeout means its newest dispatched run ended with an authoritative
    infrastructure timeout; every other failed trial reports failure. Omitted for
    queued, running, succeeded, and cancelled trials, and when the benchmark
    in-progress UI feature is disabled.
    """


class RunGetResultsResponse(BaseModel):
    """
    The progressive results/comparison payload, returned for every run
    state; before the first score lands, aggregates are empty and only
    the progress fields are meaningful. provisional is true for pending,
    running, and scoring, while a completed run's aggregates are final;
    cancelled/failed runs are terminal, but incomplete_reason explains
    why their aggregates only reflect work that landed before cleanup
    began.
    """

    summary_status: Literal["pending", "available", "unavailable"]
    """Generation state of the completed-run summary.

    Pending past the two-minute deadline is returned as unavailable. Failed and
    cancelled runs are unavailable with no narrative.
    """

    benchmark_run_uid: Optional[str] = None

    configurations: Optional[List[Configuration]] = None

    cost_latency: Optional[object] = None

    incomplete_reason: Optional[str] = None
    """
    Set only for a cancelled or failed run, explaining why its aggregates are
    terminal but incomplete.
    """

    provisional: Optional[bool] = None
    """
    True while the run is pending, running, or scoring; every aggregate may still
    change.
    """

    repetition_count: Optional[int] = None

    run_metrics: Optional[RunMetrics] = None

    run_state: Optional[Literal["pending", "running", "scoring", "completed", "failed", "cancelled"]] = None
    """Lifecycle state of a benchmark run."""

    score_progress: Optional[object] = None
    """
    Score-work ledger row counts by lifecycle state, plus the derived received =
    scored and expected = pending + judging + scored + finished_unscored (excludes
    awaiting_trial and not_scoreable).
    """

    scorers: Optional[List[object]] = None

    suite_name: Optional[str] = None

    summary_narrative: Optional[str] = None
    """The stored summary paragraph. Present only when summary_status is available."""

    trial_progress: Optional[TrialProgress] = None
    """Logical (task, configuration, repetition) trial counts by lifecycle state.

    A retry remains part of its original trial. completed is succeeded + failed +
    cancelled.
    """

    trials: Optional[List[Trial]] = None

    trials_being_judged: Optional[int] = None
    """Succeeded trials with at least one pending or judging score-work row."""

    trials_scoring_finished: Optional[int] = None
    """
    Succeeded trials whose applicable score-work rows are all scored or
    finished_unscored.
    """
