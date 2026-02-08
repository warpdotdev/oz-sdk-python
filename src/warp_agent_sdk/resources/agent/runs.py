# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.agent import RunSourceType, run_list_params
from ..._base_client import make_request_options
from ...types.agent.run_item import RunItem
from ...types.agent.run_state import RunState
from ...types.agent.run_source_type import RunSourceType
from ...types.agent.run_list_response import RunListResponse

__all__ = ["RunsResource", "AsyncRunsResource"]


class RunsResource(SyncAPIResource):
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

    def retrieve(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunItem:
        """
        Retrieve detailed information about a specific agent run, including the full
        prompt, session link, and resolved configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            f"/agent/runs/{run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunItem,
        )

    def list(
        self,
        *,
        artifact_type: Literal["PLAN", "PULL_REQUEST"] | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        creator: str | Omit = omit,
        cursor: str | Omit = omit,
        environment_id: str | Omit = omit,
        limit: int | Omit = omit,
        model_id: str | Omit = omit,
        name: str | Omit = omit,
        q: str | Omit = omit,
        schedule_id: str | Omit = omit,
        skill: str | Omit = omit,
        skill_spec: str | Omit = omit,
        source: RunSourceType | Omit = omit,
        state: List[RunState] | Omit = omit,
        updated_after: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunListResponse:
        """Retrieve a paginated list of agent runs with optional filtering.

        Results are
        ordered by creation time (newest first).

        Args:
          artifact_type: Filter runs by artifact type (PLAN or PULL_REQUEST)

          created_after: Filter runs created after this timestamp (RFC3339 format)

          created_before: Filter runs created before this timestamp (RFC3339 format)

          creator: Filter by creator UID (user or service account)

          cursor: Pagination cursor from previous response

          environment_id: Filter runs by environment ID

          limit: Maximum number of runs to return

          model_id: Filter by model ID

          name: Filter by agent config name

          q: Fuzzy search query across run title, prompt, and skill_spec

          schedule_id: Filter runs by the scheduled agent ID that created them

          skill: Filter runs by skill spec (e.g., "owner/repo:path/to/SKILL.md"). Alias for
              skill_spec.

          skill_spec: Filter runs by skill spec (e.g., "owner/repo:path/to/SKILL.md")

          source: Filter by run source type

          state: Filter by run state. Can be specified multiple times to match any of the given
              states.

          updated_after: Filter runs updated after this timestamp (RFC3339 format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/agent/runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "artifact_type": artifact_type,
                        "created_after": created_after,
                        "created_before": created_before,
                        "creator": creator,
                        "cursor": cursor,
                        "environment_id": environment_id,
                        "limit": limit,
                        "model_id": model_id,
                        "name": name,
                        "q": q,
                        "schedule_id": schedule_id,
                        "skill": skill,
                        "skill_spec": skill_spec,
                        "source": source,
                        "state": state,
                        "updated_after": updated_after,
                    },
                    run_list_params.RunListParams,
                ),
            ),
            cast_to=RunListResponse,
        )

    def cancel(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """Cancel an agent run that is currently queued or in progress.

        Once cancelled, the
        run will transition to a failed state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._post(
            f"/agent/runs/{run_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncRunsResource(AsyncAPIResource):
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

    async def retrieve(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunItem:
        """
        Retrieve detailed information about a specific agent run, including the full
        prompt, session link, and resolved configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            f"/agent/runs/{run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunItem,
        )

    async def list(
        self,
        *,
        artifact_type: Literal["PLAN", "PULL_REQUEST"] | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        creator: str | Omit = omit,
        cursor: str | Omit = omit,
        environment_id: str | Omit = omit,
        limit: int | Omit = omit,
        model_id: str | Omit = omit,
        name: str | Omit = omit,
        q: str | Omit = omit,
        schedule_id: str | Omit = omit,
        skill: str | Omit = omit,
        skill_spec: str | Omit = omit,
        source: RunSourceType | Omit = omit,
        state: List[RunState] | Omit = omit,
        updated_after: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunListResponse:
        """Retrieve a paginated list of agent runs with optional filtering.

        Results are
        ordered by creation time (newest first).

        Args:
          artifact_type: Filter runs by artifact type (PLAN or PULL_REQUEST)

          created_after: Filter runs created after this timestamp (RFC3339 format)

          created_before: Filter runs created before this timestamp (RFC3339 format)

          creator: Filter by creator UID (user or service account)

          cursor: Pagination cursor from previous response

          environment_id: Filter runs by environment ID

          limit: Maximum number of runs to return

          model_id: Filter by model ID

          name: Filter by agent config name

          q: Fuzzy search query across run title, prompt, and skill_spec

          schedule_id: Filter runs by the scheduled agent ID that created them

          skill: Filter runs by skill spec (e.g., "owner/repo:path/to/SKILL.md"). Alias for
              skill_spec.

          skill_spec: Filter runs by skill spec (e.g., "owner/repo:path/to/SKILL.md")

          source: Filter by run source type

          state: Filter by run state. Can be specified multiple times to match any of the given
              states.

          updated_after: Filter runs updated after this timestamp (RFC3339 format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/agent/runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "artifact_type": artifact_type,
                        "created_after": created_after,
                        "created_before": created_before,
                        "creator": creator,
                        "cursor": cursor,
                        "environment_id": environment_id,
                        "limit": limit,
                        "model_id": model_id,
                        "name": name,
                        "q": q,
                        "schedule_id": schedule_id,
                        "skill": skill,
                        "skill_spec": skill_spec,
                        "source": source,
                        "state": state,
                        "updated_after": updated_after,
                    },
                    run_list_params.RunListParams,
                ),
            ),
            cast_to=RunListResponse,
        )

    async def cancel(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """Cancel an agent run that is currently queued or in progress.

        Once cancelled, the
        run will transition to a failed state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._post(
            f"/agent/runs/{run_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class RunsResourceWithRawResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.retrieve = to_raw_response_wrapper(
            runs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            runs.list,
        )
        self.cancel = to_raw_response_wrapper(
            runs.cancel,
        )


class AsyncRunsResourceWithRawResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.retrieve = async_to_raw_response_wrapper(
            runs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            runs.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            runs.cancel,
        )


class RunsResourceWithStreamingResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.retrieve = to_streamed_response_wrapper(
            runs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            runs.list,
        )
        self.cancel = to_streamed_response_wrapper(
            runs.cancel,
        )


class AsyncRunsResourceWithStreamingResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.retrieve = async_to_streamed_response_wrapper(
            runs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            runs.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            runs.cancel,
        )
