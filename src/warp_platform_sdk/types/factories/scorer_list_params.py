# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ScorerListParams"]


class ScorerListParams(TypedDict, total=False):
    end_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """RFC3339 UTC timestamp, exclusive. See start_date."""

    factory_uid: str
    """Filter scorers by factory. Omit to list every scorer the team owns."""

    include_managed: bool
    """
    When true, include platform-owned managed scorers (for example the benchmark
    correctness scorer) alongside user scorers. Defaults to false so general scorer
    management only lists user-defined scorers.
    """

    recent_outcomes_limit: int
    """
    Maximum number of recent scored outcomes to include in each scorer's
    pass_rate_summary.recent_outcomes (1-100, default 50). pass_count, fail_count,
    and pass_rate are computed over that same windowed set so the headline always
    agrees with the strip.
    """

    start_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    RFC3339 UTC timestamp, inclusive; must be provided together with end_date and be
    strictly before it, or both omitted to use the unscoped window scorer detail
    pages use. Together with end_date, scopes pass_rate_summary (pass_count,
    fail_count, pass_rate, and recent_outcomes) to live scores in [start_date,
    end_date) instead of the flat recent_outcomes_limit-only window. result_count
    and last_scored_at are never affected by this parameter.
    """

    team_uid: Annotated[str, PropertyInfo(alias="X-Warp-Team-Uid")]
