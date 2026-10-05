# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncScorerResultsCursorPage, AsyncScorerResultsCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.factories import (
    scorer_list_params,
    scorer_create_params,
    scorer_list_results_params,
    scorer_list_result_reasons_params,
)
from ...types.factories.scorer_list_response import ScorerListResponse
from ...types.factories.scorer_create_response import ScorerCreateResponse
from ...types.factories.scorer_list_results_response import ScorerListResultsResponse
from ...types.factories.scorer_list_result_reasons_response import ScorerListResultReasonsResponse

__all__ = ["ScorersResource", "AsyncScorersResource"]


class ScorersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScorersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ScorersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScorersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#with_streaming_response
        """
        return ScorersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        allowed_classifications: Iterable[scorer_create_params.AllowedClassification],
        factory_uid: str,
        model_id: str,
        name: str,
        scope_mode: Literal["all_agents", "selected_agents"],
        scoring_prompt: str,
        threshold: float,
        agent_config: scorer_create_params.AgentConfig | Omit = omit,
        agent_uids: SequenceNotStr[str] | Omit = omit,
        agents: Iterable[scorer_create_params.Agent] | Omit = omit,
        description: Optional[str] | Omit = omit,
        sampling_rate: Optional[float] | Omit = omit,
        self_improvement_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScorerCreateResponse:
        """
        Create an active run scorer for a factory with either selected-agent or
        all-agent scope. Creating a scorer does not start scoring. Pass
        self_improvement_enabled to also turn on self-improvement for the new scorer in
        the same request; the scorer and its self-improvement config are created
        atomically.

        Args:
          allowed_classifications: Values the scorer may return; classification values must be unique

          factory_uid: UID of the factory that owns the scorer

          model_id: LLM model dispatched judge runs use to evaluate this scorer's rubric.

          name: Display name for the scorer

          scope_mode: Whether the scorer applies to every factory agent or selected agents

          scoring_prompt: Instructions used to score matching runs

          threshold: Score a run's classified label must meet or exceed to pass, from 0 to 1.

          agent_config: Scorer-specific execution overrides for its hidden judge agent. An omitted or
              null field inherits the corresponding Factory agent default. A non-empty value
              replaces that default. Empty secrets and mcp_servers collections explicitly
              clear the optional Factory defaults.

          agent_uids: Legacy shorthand for selected agents with include_descendants=false. Required
              and non-empty for selected_agents when agents is omitted; must be empty for
              all_agents and cannot be combined with agents.

          agents: Selected agents and their evidence policy. Required and non-empty for
              selected_agents when agent_uids is omitted; must be empty for all_agents and
              cannot be combined with agent_uids.

          description: Optional description of the scorer

          sampling_rate: Percentage of the scorer's eligible runs to score, from 0 to 100; omit to score
              every eligible run, and 0 stops automatic scoring (manual dispatch still works).
              A value with more than two decimal places is rounded to two rather than
              rejected, and the rounded value is what is stored. Sampling applies to periodic
              scoring only, and runs are chosen deterministically per (scorer, run), so
              lowering the rate reduces how many runs are scored rather than how often.

          self_improvement_enabled: Optionally enable self-improvement for the newly created scorer in the same
              transactional request, instead of a separate call to PUT
              /factory/scorers/{scorer_id}/self-improvement-config afterward; defaults to
              false. The response does not echo this back — a successful (2xx) response means
              the requested state was applied, confirmable at any time with GET
              .../self-improvement-config. Setting this to true requires a human user
              principal, matching the restriction on the PUT endpoint; a service-account
              principal gets the same error as calling that endpoint directly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/factory/scorers",
            body=maybe_transform(
                {
                    "allowed_classifications": allowed_classifications,
                    "factory_uid": factory_uid,
                    "model_id": model_id,
                    "name": name,
                    "scope_mode": scope_mode,
                    "scoring_prompt": scoring_prompt,
                    "threshold": threshold,
                    "agent_config": agent_config,
                    "agent_uids": agent_uids,
                    "agents": agents,
                    "description": description,
                    "sampling_rate": sampling_rate,
                    "self_improvement_enabled": self_improvement_enabled,
                },
                scorer_create_params.ScorerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScorerCreateResponse,
        )

    def list(
        self,
        *,
        end_date: Union[str, datetime] | Omit = omit,
        factory_uid: str | Omit = omit,
        include_managed: bool | Omit = omit,
        recent_outcomes_limit: int | Omit = omit,
        start_date: Union[str, datetime] | Omit = omit,
        team_uid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScorerListResponse:
        """
        List the scorers owned by the caller's team, including scope agents and
        aggregate scoring stats. Pass factory_uid to narrow the result to a single
        factory.

        Args:
          end_date: RFC3339 UTC timestamp, exclusive. See start_date.

          factory_uid: Filter scorers by factory. Omit to list every scorer the team owns.

          include_managed: When true, include platform-owned managed scorers (for example the benchmark
              correctness scorer) alongside user scorers. Defaults to false so general scorer
              management only lists user-defined scorers.

          recent_outcomes_limit: Maximum number of recent scored outcomes to include in each scorer's
              pass_rate_summary.recent_outcomes (1-100, default 50). pass_count, fail_count,
              and pass_rate are computed over that same windowed set so the headline always
              agrees with the strip.

          start_date: RFC3339 UTC timestamp, inclusive; must be provided together with end_date and be
              strictly before it, or both omitted to use the unscoped window scorer detail
              pages use. Together with end_date, scopes pass_rate_summary (pass_count,
              fail_count, pass_rate, and recent_outcomes) to live scores in [start_date,
              end_date) instead of the flat recent_outcomes_limit-only window. result_count
              and last_scored_at are never affected by this parameter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Warp-Team-Uid": team_uid}), **(extra_headers or {})}
        return self._get(
            "/factory/scorers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "factory_uid": factory_uid,
                        "include_managed": include_managed,
                        "recent_outcomes_limit": recent_outcomes_limit,
                        "start_date": start_date,
                    },
                    scorer_list_params.ScorerListParams,
                ),
            ),
            cast_to=ScorerListResponse,
        )

    def list_result_reasons(
        self,
        scorer_id: int,
        *,
        run_id: SequenceNotStr[str],
        team_uid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScorerListResultReasonsResponse:
        """Read the judge's reasoning for the given runs.

        A run whose reason is missing or
        unreadable is reported individually so one unavailable reason never fails the
        request.

        Args:
          run_id: Runs to read reasons for. Repeat the parameter once per run; at most 100
              distinct runs (the results page maximum) per request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Warp-Team-Uid": team_uid}), **(extra_headers or {})}
        return self._get(
            path_template("/factory/scorers/{scorer_id}/results/reasons", scorer_id=scorer_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"run_id": run_id}, scorer_list_result_reasons_params.ScorerListResultReasonsParams
                ),
            ),
            cast_to=ScorerListResultReasonsResponse,
        )

    def list_results(
        self,
        scorer_id: int,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        team_uid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncScorerResultsCursorPage[ScorerListResultsResponse]:
        """List the scorer's most recent scoring attempts, newest first.

        A failed attempt
        carries no classification. Pagination is a keyset cursor over attempted_at with
        the attempt id as a stable tiebreak.

        Args:
          cursor: Opaque cursor returned by a previous list response.

          limit: Maximum number of results to return (1-100, default 50)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Warp-Team-Uid": team_uid}), **(extra_headers or {})}
        return self._get_api_list(
            path_template("/factory/scorers/{scorer_id}/results", scorer_id=scorer_id),
            page=SyncScorerResultsCursorPage[ScorerListResultsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    scorer_list_results_params.ScorerListResultsParams,
                ),
            ),
            model=ScorerListResultsResponse,
        )


class AsyncScorersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScorersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScorersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScorersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#with_streaming_response
        """
        return AsyncScorersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        allowed_classifications: Iterable[scorer_create_params.AllowedClassification],
        factory_uid: str,
        model_id: str,
        name: str,
        scope_mode: Literal["all_agents", "selected_agents"],
        scoring_prompt: str,
        threshold: float,
        agent_config: scorer_create_params.AgentConfig | Omit = omit,
        agent_uids: SequenceNotStr[str] | Omit = omit,
        agents: Iterable[scorer_create_params.Agent] | Omit = omit,
        description: Optional[str] | Omit = omit,
        sampling_rate: Optional[float] | Omit = omit,
        self_improvement_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScorerCreateResponse:
        """
        Create an active run scorer for a factory with either selected-agent or
        all-agent scope. Creating a scorer does not start scoring. Pass
        self_improvement_enabled to also turn on self-improvement for the new scorer in
        the same request; the scorer and its self-improvement config are created
        atomically.

        Args:
          allowed_classifications: Values the scorer may return; classification values must be unique

          factory_uid: UID of the factory that owns the scorer

          model_id: LLM model dispatched judge runs use to evaluate this scorer's rubric.

          name: Display name for the scorer

          scope_mode: Whether the scorer applies to every factory agent or selected agents

          scoring_prompt: Instructions used to score matching runs

          threshold: Score a run's classified label must meet or exceed to pass, from 0 to 1.

          agent_config: Scorer-specific execution overrides for its hidden judge agent. An omitted or
              null field inherits the corresponding Factory agent default. A non-empty value
              replaces that default. Empty secrets and mcp_servers collections explicitly
              clear the optional Factory defaults.

          agent_uids: Legacy shorthand for selected agents with include_descendants=false. Required
              and non-empty for selected_agents when agents is omitted; must be empty for
              all_agents and cannot be combined with agents.

          agents: Selected agents and their evidence policy. Required and non-empty for
              selected_agents when agent_uids is omitted; must be empty for all_agents and
              cannot be combined with agent_uids.

          description: Optional description of the scorer

          sampling_rate: Percentage of the scorer's eligible runs to score, from 0 to 100; omit to score
              every eligible run, and 0 stops automatic scoring (manual dispatch still works).
              A value with more than two decimal places is rounded to two rather than
              rejected, and the rounded value is what is stored. Sampling applies to periodic
              scoring only, and runs are chosen deterministically per (scorer, run), so
              lowering the rate reduces how many runs are scored rather than how often.

          self_improvement_enabled: Optionally enable self-improvement for the newly created scorer in the same
              transactional request, instead of a separate call to PUT
              /factory/scorers/{scorer_id}/self-improvement-config afterward; defaults to
              false. The response does not echo this back — a successful (2xx) response means
              the requested state was applied, confirmable at any time with GET
              .../self-improvement-config. Setting this to true requires a human user
              principal, matching the restriction on the PUT endpoint; a service-account
              principal gets the same error as calling that endpoint directly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/factory/scorers",
            body=await async_maybe_transform(
                {
                    "allowed_classifications": allowed_classifications,
                    "factory_uid": factory_uid,
                    "model_id": model_id,
                    "name": name,
                    "scope_mode": scope_mode,
                    "scoring_prompt": scoring_prompt,
                    "threshold": threshold,
                    "agent_config": agent_config,
                    "agent_uids": agent_uids,
                    "agents": agents,
                    "description": description,
                    "sampling_rate": sampling_rate,
                    "self_improvement_enabled": self_improvement_enabled,
                },
                scorer_create_params.ScorerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScorerCreateResponse,
        )

    async def list(
        self,
        *,
        end_date: Union[str, datetime] | Omit = omit,
        factory_uid: str | Omit = omit,
        include_managed: bool | Omit = omit,
        recent_outcomes_limit: int | Omit = omit,
        start_date: Union[str, datetime] | Omit = omit,
        team_uid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScorerListResponse:
        """
        List the scorers owned by the caller's team, including scope agents and
        aggregate scoring stats. Pass factory_uid to narrow the result to a single
        factory.

        Args:
          end_date: RFC3339 UTC timestamp, exclusive. See start_date.

          factory_uid: Filter scorers by factory. Omit to list every scorer the team owns.

          include_managed: When true, include platform-owned managed scorers (for example the benchmark
              correctness scorer) alongside user scorers. Defaults to false so general scorer
              management only lists user-defined scorers.

          recent_outcomes_limit: Maximum number of recent scored outcomes to include in each scorer's
              pass_rate_summary.recent_outcomes (1-100, default 50). pass_count, fail_count,
              and pass_rate are computed over that same windowed set so the headline always
              agrees with the strip.

          start_date: RFC3339 UTC timestamp, inclusive; must be provided together with end_date and be
              strictly before it, or both omitted to use the unscoped window scorer detail
              pages use. Together with end_date, scopes pass_rate_summary (pass_count,
              fail_count, pass_rate, and recent_outcomes) to live scores in [start_date,
              end_date) instead of the flat recent_outcomes_limit-only window. result_count
              and last_scored_at are never affected by this parameter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Warp-Team-Uid": team_uid}), **(extra_headers or {})}
        return await self._get(
            "/factory/scorers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "factory_uid": factory_uid,
                        "include_managed": include_managed,
                        "recent_outcomes_limit": recent_outcomes_limit,
                        "start_date": start_date,
                    },
                    scorer_list_params.ScorerListParams,
                ),
            ),
            cast_to=ScorerListResponse,
        )

    async def list_result_reasons(
        self,
        scorer_id: int,
        *,
        run_id: SequenceNotStr[str],
        team_uid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScorerListResultReasonsResponse:
        """Read the judge's reasoning for the given runs.

        A run whose reason is missing or
        unreadable is reported individually so one unavailable reason never fails the
        request.

        Args:
          run_id: Runs to read reasons for. Repeat the parameter once per run; at most 100
              distinct runs (the results page maximum) per request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Warp-Team-Uid": team_uid}), **(extra_headers or {})}
        return await self._get(
            path_template("/factory/scorers/{scorer_id}/results/reasons", scorer_id=scorer_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"run_id": run_id}, scorer_list_result_reasons_params.ScorerListResultReasonsParams
                ),
            ),
            cast_to=ScorerListResultReasonsResponse,
        )

    def list_results(
        self,
        scorer_id: int,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        team_uid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ScorerListResultsResponse, AsyncScorerResultsCursorPage[ScorerListResultsResponse]]:
        """List the scorer's most recent scoring attempts, newest first.

        A failed attempt
        carries no classification. Pagination is a keyset cursor over attempted_at with
        the attempt id as a stable tiebreak.

        Args:
          cursor: Opaque cursor returned by a previous list response.

          limit: Maximum number of results to return (1-100, default 50)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Warp-Team-Uid": team_uid}), **(extra_headers or {})}
        return self._get_api_list(
            path_template("/factory/scorers/{scorer_id}/results", scorer_id=scorer_id),
            page=AsyncScorerResultsCursorPage[ScorerListResultsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    scorer_list_results_params.ScorerListResultsParams,
                ),
            ),
            model=ScorerListResultsResponse,
        )


class ScorersResourceWithRawResponse:
    def __init__(self, scorers: ScorersResource) -> None:
        self._scorers = scorers

        self.create = to_raw_response_wrapper(
            scorers.create,
        )
        self.list = to_raw_response_wrapper(
            scorers.list,
        )
        self.list_result_reasons = to_raw_response_wrapper(
            scorers.list_result_reasons,
        )
        self.list_results = to_raw_response_wrapper(
            scorers.list_results,
        )


class AsyncScorersResourceWithRawResponse:
    def __init__(self, scorers: AsyncScorersResource) -> None:
        self._scorers = scorers

        self.create = async_to_raw_response_wrapper(
            scorers.create,
        )
        self.list = async_to_raw_response_wrapper(
            scorers.list,
        )
        self.list_result_reasons = async_to_raw_response_wrapper(
            scorers.list_result_reasons,
        )
        self.list_results = async_to_raw_response_wrapper(
            scorers.list_results,
        )


class ScorersResourceWithStreamingResponse:
    def __init__(self, scorers: ScorersResource) -> None:
        self._scorers = scorers

        self.create = to_streamed_response_wrapper(
            scorers.create,
        )
        self.list = to_streamed_response_wrapper(
            scorers.list,
        )
        self.list_result_reasons = to_streamed_response_wrapper(
            scorers.list_result_reasons,
        )
        self.list_results = to_streamed_response_wrapper(
            scorers.list_results,
        )


class AsyncScorersResourceWithStreamingResponse:
    def __init__(self, scorers: AsyncScorersResource) -> None:
        self._scorers = scorers

        self.create = async_to_streamed_response_wrapper(
            scorers.create,
        )
        self.list = async_to_streamed_response_wrapper(
            scorers.list,
        )
        self.list_result_reasons = async_to_streamed_response_wrapper(
            scorers.list_result_reasons,
        )
        self.list_results = async_to_streamed_response_wrapper(
            scorers.list_results,
        )
