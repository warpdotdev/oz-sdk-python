# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncBenchmarkSuitesCursorPage, AsyncBenchmarkSuitesCursorPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.factories.benchmarks import suite_list_params, suite_create_params, suite_launch_run_params
from ....types.factories.benchmarks.suite_get_response import SuiteGetResponse
from ....types.factories.benchmarks.suite_list_response import SuiteListResponse
from ....types.factories.benchmarks.suite_create_response import SuiteCreateResponse
from ....types.factories.benchmarks.suite_launch_run_response import SuiteLaunchRunResponse

__all__ = ["SuitesResource", "AsyncSuitesResource"]


class SuitesResource(SyncAPIResource):
    """Operations for creating and managing factories"""

    @cached_property
    def with_raw_response(self) -> SuitesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SuitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SuitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#with_streaming_response
        """
        return SuitesResourceWithStreamingResponse(self)

    def create(
        self,
        uid: str,
        *,
        agent_uid: str,
        factory_agent_type: str,
        name: str,
        suite_uid: str,
        description: str | Omit = omit,
        tasks: Iterable[suite_create_params.Task] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuiteCreateResponse:
        """
        Create a benchmark suite

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return self._post(
            path_template("/factory/{uid}/benchmarks/suites", uid=uid),
            body=maybe_transform(
                {
                    "agent_uid": agent_uid,
                    "factory_agent_type": factory_agent_type,
                    "name": name,
                    "suite_uid": suite_uid,
                    "description": description,
                    "tasks": tasks,
                },
                suite_create_params.SuiteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuiteCreateResponse,
        )

    def list(
        self,
        uid: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncBenchmarkSuitesCursorPage[SuiteListResponse]:
        """
        List benchmark suites

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return self._get_api_list(
            path_template("/factory/{uid}/benchmarks/suites", uid=uid),
            page=SyncBenchmarkSuitesCursorPage[SuiteListResponse],
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
                    suite_list_params.SuiteListParams,
                ),
            ),
            model=SuiteListResponse,
        )

    def get(
        self,
        suite_uid: str,
        *,
        uid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuiteGetResponse:
        """
        Get a benchmark suite with its tasks and configurations

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        if not suite_uid:
            raise ValueError(f"Expected a non-empty value for `suite_uid` but received {suite_uid!r}")
        return self._get(
            path_template("/factory/{uid}/benchmarks/suites/{suite_uid}", uid=uid, suite_uid=suite_uid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuiteGetResponse,
        )

    def launch_run(
        self,
        suite_uid: str,
        *,
        uid: str,
        repetition_count: int,
        configurations: Iterable[suite_launch_run_params.Configuration] | Omit = omit,
        historical_replay_run_uid: str | Omit = omit,
        scorer_selection: Iterable[int] | Omit = omit,
        tasks: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuiteLaunchRunResponse:
        """
        Launch a benchmark run from the current suite version

        Args:
          repetition_count: Number of repetitions per (task, configuration) pair, frozen onto the run. Like
              configurations and scorer_selection, this is chosen fresh at each launch rather
              than persisted on the suite.

          configurations: Optional launch-time configurations. When omitted, the suite's persistent
              configurations are used. An explicit empty list, or a suite with neither
              launch-time nor persistent configurations, is rejected.

          historical_replay_run_uid: Internal provenance for a prior-run replay. The server accepts historical agent
              entries only when they exactly match frozen entries from this run and the run
              belongs to the same suite.

          scorer_selection: Allowlist of live scorer IDs for this factory, applied to every trial in the
              run. Empty or absent means all applicable scorers. IDs must belong to the
              suite's factory and team (any status except deleted).

          tasks: Optional allowlist of immutable UIDs for current tasks in the addressed suite.
              Omitted runs all current suite tasks. Explicit empty, invalid, unknown, stale,
              cross-suite, and duplicate selections are rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        if not suite_uid:
            raise ValueError(f"Expected a non-empty value for `suite_uid` but received {suite_uid!r}")
        return self._post(
            path_template("/factory/{uid}/benchmarks/suites/{suite_uid}/runs", uid=uid, suite_uid=suite_uid),
            body=maybe_transform(
                {
                    "repetition_count": repetition_count,
                    "configurations": configurations,
                    "historical_replay_run_uid": historical_replay_run_uid,
                    "scorer_selection": scorer_selection,
                    "tasks": tasks,
                },
                suite_launch_run_params.SuiteLaunchRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuiteLaunchRunResponse,
        )


class AsyncSuitesResource(AsyncAPIResource):
    """Operations for creating and managing factories"""

    @cached_property
    def with_raw_response(self) -> AsyncSuitesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSuitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSuitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#with_streaming_response
        """
        return AsyncSuitesResourceWithStreamingResponse(self)

    async def create(
        self,
        uid: str,
        *,
        agent_uid: str,
        factory_agent_type: str,
        name: str,
        suite_uid: str,
        description: str | Omit = omit,
        tasks: Iterable[suite_create_params.Task] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuiteCreateResponse:
        """
        Create a benchmark suite

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return await self._post(
            path_template("/factory/{uid}/benchmarks/suites", uid=uid),
            body=await async_maybe_transform(
                {
                    "agent_uid": agent_uid,
                    "factory_agent_type": factory_agent_type,
                    "name": name,
                    "suite_uid": suite_uid,
                    "description": description,
                    "tasks": tasks,
                },
                suite_create_params.SuiteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuiteCreateResponse,
        )

    def list(
        self,
        uid: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SuiteListResponse, AsyncBenchmarkSuitesCursorPage[SuiteListResponse]]:
        """
        List benchmark suites

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return self._get_api_list(
            path_template("/factory/{uid}/benchmarks/suites", uid=uid),
            page=AsyncBenchmarkSuitesCursorPage[SuiteListResponse],
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
                    suite_list_params.SuiteListParams,
                ),
            ),
            model=SuiteListResponse,
        )

    async def get(
        self,
        suite_uid: str,
        *,
        uid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuiteGetResponse:
        """
        Get a benchmark suite with its tasks and configurations

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        if not suite_uid:
            raise ValueError(f"Expected a non-empty value for `suite_uid` but received {suite_uid!r}")
        return await self._get(
            path_template("/factory/{uid}/benchmarks/suites/{suite_uid}", uid=uid, suite_uid=suite_uid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuiteGetResponse,
        )

    async def launch_run(
        self,
        suite_uid: str,
        *,
        uid: str,
        repetition_count: int,
        configurations: Iterable[suite_launch_run_params.Configuration] | Omit = omit,
        historical_replay_run_uid: str | Omit = omit,
        scorer_selection: Iterable[int] | Omit = omit,
        tasks: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuiteLaunchRunResponse:
        """
        Launch a benchmark run from the current suite version

        Args:
          repetition_count: Number of repetitions per (task, configuration) pair, frozen onto the run. Like
              configurations and scorer_selection, this is chosen fresh at each launch rather
              than persisted on the suite.

          configurations: Optional launch-time configurations. When omitted, the suite's persistent
              configurations are used. An explicit empty list, or a suite with neither
              launch-time nor persistent configurations, is rejected.

          historical_replay_run_uid: Internal provenance for a prior-run replay. The server accepts historical agent
              entries only when they exactly match frozen entries from this run and the run
              belongs to the same suite.

          scorer_selection: Allowlist of live scorer IDs for this factory, applied to every trial in the
              run. Empty or absent means all applicable scorers. IDs must belong to the
              suite's factory and team (any status except deleted).

          tasks: Optional allowlist of immutable UIDs for current tasks in the addressed suite.
              Omitted runs all current suite tasks. Explicit empty, invalid, unknown, stale,
              cross-suite, and duplicate selections are rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        if not suite_uid:
            raise ValueError(f"Expected a non-empty value for `suite_uid` but received {suite_uid!r}")
        return await self._post(
            path_template("/factory/{uid}/benchmarks/suites/{suite_uid}/runs", uid=uid, suite_uid=suite_uid),
            body=await async_maybe_transform(
                {
                    "repetition_count": repetition_count,
                    "configurations": configurations,
                    "historical_replay_run_uid": historical_replay_run_uid,
                    "scorer_selection": scorer_selection,
                    "tasks": tasks,
                },
                suite_launch_run_params.SuiteLaunchRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuiteLaunchRunResponse,
        )


class SuitesResourceWithRawResponse:
    def __init__(self, suites: SuitesResource) -> None:
        self._suites = suites

        self.create = to_raw_response_wrapper(
            suites.create,
        )
        self.list = to_raw_response_wrapper(
            suites.list,
        )
        self.get = to_raw_response_wrapper(
            suites.get,
        )
        self.launch_run = to_raw_response_wrapper(
            suites.launch_run,
        )


class AsyncSuitesResourceWithRawResponse:
    def __init__(self, suites: AsyncSuitesResource) -> None:
        self._suites = suites

        self.create = async_to_raw_response_wrapper(
            suites.create,
        )
        self.list = async_to_raw_response_wrapper(
            suites.list,
        )
        self.get = async_to_raw_response_wrapper(
            suites.get,
        )
        self.launch_run = async_to_raw_response_wrapper(
            suites.launch_run,
        )


class SuitesResourceWithStreamingResponse:
    def __init__(self, suites: SuitesResource) -> None:
        self._suites = suites

        self.create = to_streamed_response_wrapper(
            suites.create,
        )
        self.list = to_streamed_response_wrapper(
            suites.list,
        )
        self.get = to_streamed_response_wrapper(
            suites.get,
        )
        self.launch_run = to_streamed_response_wrapper(
            suites.launch_run,
        )


class AsyncSuitesResourceWithStreamingResponse:
    def __init__(self, suites: AsyncSuitesResource) -> None:
        self._suites = suites

        self.create = async_to_streamed_response_wrapper(
            suites.create,
        )
        self.list = async_to_streamed_response_wrapper(
            suites.list,
        )
        self.get = async_to_streamed_response_wrapper(
            suites.get,
        )
        self.launch_run = async_to_streamed_response_wrapper(
            suites.launch_run,
        )
