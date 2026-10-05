# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.factories import run_create_params
from ...types.factories.run_create_response import RunCreateResponse
from ...types.factories.run_list_scores_response import RunListScoresResponse

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

    def create(
        self,
        uid: str,
        *,
        prompt: str,
        ticket_ref: str | Omit = omit,
        ticket_url: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunCreateResponse:
        """
        Dispatch a run to a factory, using prompt as the run's prompt and an optional
        title, ticket_ref, and ticket_url. Returns the created run; its factory task is
        created asynchronously and can be resolved afterwards with GET
        /factory/{uid}/task-by-run.

        Args:
          prompt: The prompt sent to the factory's foreman, not wrapped in any factory intake
              envelope. Required and non-empty.

          ticket_ref: Originating ticket reference in <source>:<id> form (for example,
              linear:REMOTE-123); omit to mint an adhoc reference. Stamped onto the run as
              ticket_id/ticket_source metadata.

          ticket_url: Optional URL of the ticket named by ticket_ref. Stamped onto the run as
              ticket_url metadata when given.

          title: Human-readable title for the dispatched run and its factory task. Omit to derive
              one automatically from the prompt.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return self._post(
            path_template("/factory/{uid}/runs", uid=uid),
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "ticket_ref": ticket_ref,
                    "ticket_url": ticket_url,
                    "title": title,
                },
                run_create_params.RunCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunCreateResponse,
        )

    def list_scores(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunListScoresResponse:
        """
        List the current live attempt for each evaluation that has attempted the given
        run, most recent attempt first. Excludes a deleted evaluation's data. Requires
        only view access to the run, since reading scores is part of viewing the run.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            path_template("/factory/runs/{run_id}/scores", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunListScoresResponse,
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

    async def create(
        self,
        uid: str,
        *,
        prompt: str,
        ticket_ref: str | Omit = omit,
        ticket_url: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunCreateResponse:
        """
        Dispatch a run to a factory, using prompt as the run's prompt and an optional
        title, ticket_ref, and ticket_url. Returns the created run; its factory task is
        created asynchronously and can be resolved afterwards with GET
        /factory/{uid}/task-by-run.

        Args:
          prompt: The prompt sent to the factory's foreman, not wrapped in any factory intake
              envelope. Required and non-empty.

          ticket_ref: Originating ticket reference in <source>:<id> form (for example,
              linear:REMOTE-123); omit to mint an adhoc reference. Stamped onto the run as
              ticket_id/ticket_source metadata.

          ticket_url: Optional URL of the ticket named by ticket_ref. Stamped onto the run as
              ticket_url metadata when given.

          title: Human-readable title for the dispatched run and its factory task. Omit to derive
              one automatically from the prompt.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return await self._post(
            path_template("/factory/{uid}/runs", uid=uid),
            body=await async_maybe_transform(
                {
                    "prompt": prompt,
                    "ticket_ref": ticket_ref,
                    "ticket_url": ticket_url,
                    "title": title,
                },
                run_create_params.RunCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunCreateResponse,
        )

    async def list_scores(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunListScoresResponse:
        """
        List the current live attempt for each evaluation that has attempted the given
        run, most recent attempt first. Excludes a deleted evaluation's data. Requires
        only view access to the run, since reading scores is part of viewing the run.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            path_template("/factory/runs/{run_id}/scores", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunListScoresResponse,
        )


class RunsResourceWithRawResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.create = to_raw_response_wrapper(
            runs.create,
        )
        self.list_scores = to_raw_response_wrapper(
            runs.list_scores,
        )


class AsyncRunsResourceWithRawResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.create = async_to_raw_response_wrapper(
            runs.create,
        )
        self.list_scores = async_to_raw_response_wrapper(
            runs.list_scores,
        )


class RunsResourceWithStreamingResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.create = to_streamed_response_wrapper(
            runs.create,
        )
        self.list_scores = to_streamed_response_wrapper(
            runs.list_scores,
        )


class AsyncRunsResourceWithStreamingResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.create = async_to_streamed_response_wrapper(
            runs.create,
        )
        self.list_scores = async_to_streamed_response_wrapper(
            runs.list_scores,
        )
