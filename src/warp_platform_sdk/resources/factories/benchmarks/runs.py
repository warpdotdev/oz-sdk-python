# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncRunsCursorPage, AsyncRunsCursorPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.factories.benchmarks import run_list_params
from ....types.factories.benchmarks.run_get_response import RunGetResponse
from ....types.factories.benchmarks.run_list_response import RunListResponse
from ....types.factories.benchmarks.run_get_results_response import RunGetResultsResponse

__all__ = ["RunsResource", "AsyncRunsResource"]


class RunsResource(SyncAPIResource):
    """Operations for creating and managing factories"""

    @cached_property
    def with_raw_response(self) -> RunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#accessing-raw-response-data-eg-headers
        """
        return RunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#with_streaming_response
        """
        return RunsResourceWithStreamingResponse(self)

    def list(
        self,
        uid: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        state: List[Literal["pending", "running", "scoring", "completed", "failed", "cancelled"]] | Omit = omit,
        suite_uid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncRunsCursorPage[RunListResponse]:
        """
        List benchmark runs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return self._get_api_list(
            path_template("/factory/{uid}/benchmarks/runs", uid=uid),
            page=SyncRunsCursorPage[RunListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "state": state,
                        "suite_uid": suite_uid,
                    },
                    run_list_params.RunListParams,
                ),
            ),
            model=RunListResponse,
        )

    def get(
        self,
        run_uid: str,
        *,
        uid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunGetResponse:
        """
        Get benchmark run detail

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        if not run_uid:
            raise ValueError(f"Expected a non-empty value for `run_uid` but received {run_uid!r}")
        return self._get(
            path_template("/factory/{uid}/benchmarks/runs/{run_uid}", uid=uid, run_uid=run_uid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunGetResponse,
        )

    def get_results(
        self,
        run_uid: str,
        *,
        uid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunGetResultsResponse:
        """
        Get benchmark run results

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        if not run_uid:
            raise ValueError(f"Expected a non-empty value for `run_uid` but received {run_uid!r}")
        return self._get(
            path_template("/factory/{uid}/benchmarks/runs/{run_uid}/results", uid=uid, run_uid=run_uid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunGetResultsResponse,
        )


class AsyncRunsResource(AsyncAPIResource):
    """Operations for creating and managing factories"""

    @cached_property
    def with_raw_response(self) -> AsyncRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#with_streaming_response
        """
        return AsyncRunsResourceWithStreamingResponse(self)

    def list(
        self,
        uid: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        state: List[Literal["pending", "running", "scoring", "completed", "failed", "cancelled"]] | Omit = omit,
        suite_uid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RunListResponse, AsyncRunsCursorPage[RunListResponse]]:
        """
        List benchmark runs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return self._get_api_list(
            path_template("/factory/{uid}/benchmarks/runs", uid=uid),
            page=AsyncRunsCursorPage[RunListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "state": state,
                        "suite_uid": suite_uid,
                    },
                    run_list_params.RunListParams,
                ),
            ),
            model=RunListResponse,
        )

    async def get(
        self,
        run_uid: str,
        *,
        uid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunGetResponse:
        """
        Get benchmark run detail

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        if not run_uid:
            raise ValueError(f"Expected a non-empty value for `run_uid` but received {run_uid!r}")
        return await self._get(
            path_template("/factory/{uid}/benchmarks/runs/{run_uid}", uid=uid, run_uid=run_uid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunGetResponse,
        )

    async def get_results(
        self,
        run_uid: str,
        *,
        uid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunGetResultsResponse:
        """
        Get benchmark run results

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        if not run_uid:
            raise ValueError(f"Expected a non-empty value for `run_uid` but received {run_uid!r}")
        return await self._get(
            path_template("/factory/{uid}/benchmarks/runs/{run_uid}/results", uid=uid, run_uid=run_uid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunGetResultsResponse,
        )


class RunsResourceWithRawResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.list = to_raw_response_wrapper(
            runs.list,
        )
        self.get = to_raw_response_wrapper(
            runs.get,
        )
        self.get_results = to_raw_response_wrapper(
            runs.get_results,
        )


class AsyncRunsResourceWithRawResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.list = async_to_raw_response_wrapper(
            runs.list,
        )
        self.get = async_to_raw_response_wrapper(
            runs.get,
        )
        self.get_results = async_to_raw_response_wrapper(
            runs.get_results,
        )


class RunsResourceWithStreamingResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.list = to_streamed_response_wrapper(
            runs.list,
        )
        self.get = to_streamed_response_wrapper(
            runs.get,
        )
        self.get_results = to_streamed_response_wrapper(
            runs.get_results,
        )


class AsyncRunsResourceWithStreamingResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.list = async_to_streamed_response_wrapper(
            runs.list,
        )
        self.get = async_to_streamed_response_wrapper(
            runs.get,
        )
        self.get_results = async_to_streamed_response_wrapper(
            runs.get_results,
        )
