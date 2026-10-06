# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from ...user_profile import UserProfile

__all__ = ["RunListResponse", "ConfigurationStat"]


class ConfigurationStat(BaseModel):
    id: int

    display_name: str
    """Optional name given to this configuration at launch. Empty when none was given."""

    fail_count: int

    pass_count: int

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


class RunListResponse(BaseModel):
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
