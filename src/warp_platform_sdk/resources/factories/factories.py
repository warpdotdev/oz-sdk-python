# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .runs import (
    RunsResource,
    AsyncRunsResource,
    RunsResourceWithRawResponse,
    AsyncRunsResourceWithRawResponse,
    RunsResourceWithStreamingResponse,
    AsyncRunsResourceWithStreamingResponse,
)
from .inbox import (
    InboxResource,
    AsyncInboxResource,
    InboxResourceWithRawResponse,
    AsyncInboxResourceWithRawResponse,
    InboxResourceWithStreamingResponse,
    AsyncInboxResourceWithStreamingResponse,
)
from ...types import factory_list_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncFactoriesCursorPage, AsyncFactoriesCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.factory import Factory

__all__ = ["FactoriesResource", "AsyncFactoriesResource"]


class FactoriesResource(SyncAPIResource):
    """Operations for creating and managing factories"""

    @cached_property
    def inbox(self) -> InboxResource:
        """Operations for creating and managing factories"""
        return InboxResource(self._client)

    @cached_property
    def runs(self) -> RunsResource:
        """Operations for creating and managing factories"""
        return RunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> FactoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FactoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FactoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#with_streaming_response
        """
        return FactoriesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        search: str | Omit = omit,
        query_team_uid: str | Omit = omit,
        team_uid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncFactoriesCursorPage[Factory]:
        """
        List factories accessible to the authenticated principal, restricted to the
        request's active team when one is set. An optional team_uid query parameter
        overrides the active team and restricts results to a single team, and an
        optional search query parameter filters by a case-insensitive substring match on
        the factory name or alias.

        Args:
          cursor: Opaque cursor returned by a previous list response.

          limit: Maximum number of factories to return (default 50, max 100).

          search: Case-insensitive substring search over the factory name and alias.

          query_team_uid: Optional team UID to filter factories by ownership. Takes precedence over the
              X-Warp-Team-Uid header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Warp-Team-Uid": team_uid}), **(extra_headers or {})}
        return self._get_api_list(
            "/factory",
            page=SyncFactoriesCursorPage[Factory],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "search": search,
                        "query_team_uid": query_team_uid,
                    },
                    factory_list_params.FactoryListParams,
                ),
            ),
            model=Factory,
        )

    def get(
        self,
        uid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Factory:
        """
        Get a factory by its public UID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return self._get(
            path_template("/factory/{uid}", uid=uid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Factory,
        )


class AsyncFactoriesResource(AsyncAPIResource):
    """Operations for creating and managing factories"""

    @cached_property
    def inbox(self) -> AsyncInboxResource:
        """Operations for creating and managing factories"""
        return AsyncInboxResource(self._client)

    @cached_property
    def runs(self) -> AsyncRunsResource:
        """Operations for creating and managing factories"""
        return AsyncRunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFactoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFactoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFactoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#with_streaming_response
        """
        return AsyncFactoriesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        search: str | Omit = omit,
        query_team_uid: str | Omit = omit,
        team_uid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Factory, AsyncFactoriesCursorPage[Factory]]:
        """
        List factories accessible to the authenticated principal, restricted to the
        request's active team when one is set. An optional team_uid query parameter
        overrides the active team and restricts results to a single team, and an
        optional search query parameter filters by a case-insensitive substring match on
        the factory name or alias.

        Args:
          cursor: Opaque cursor returned by a previous list response.

          limit: Maximum number of factories to return (default 50, max 100).

          search: Case-insensitive substring search over the factory name and alias.

          query_team_uid: Optional team UID to filter factories by ownership. Takes precedence over the
              X-Warp-Team-Uid header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Warp-Team-Uid": team_uid}), **(extra_headers or {})}
        return self._get_api_list(
            "/factory",
            page=AsyncFactoriesCursorPage[Factory],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "search": search,
                        "query_team_uid": query_team_uid,
                    },
                    factory_list_params.FactoryListParams,
                ),
            ),
            model=Factory,
        )

    async def get(
        self,
        uid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Factory:
        """
        Get a factory by its public UID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return await self._get(
            path_template("/factory/{uid}", uid=uid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Factory,
        )


class FactoriesResourceWithRawResponse:
    def __init__(self, factories: FactoriesResource) -> None:
        self._factories = factories

        self.list = to_raw_response_wrapper(
            factories.list,
        )
        self.get = to_raw_response_wrapper(
            factories.get,
        )

    @cached_property
    def inbox(self) -> InboxResourceWithRawResponse:
        """Operations for creating and managing factories"""
        return InboxResourceWithRawResponse(self._factories.inbox)

    @cached_property
    def runs(self) -> RunsResourceWithRawResponse:
        """Operations for creating and managing factories"""
        return RunsResourceWithRawResponse(self._factories.runs)


class AsyncFactoriesResourceWithRawResponse:
    def __init__(self, factories: AsyncFactoriesResource) -> None:
        self._factories = factories

        self.list = async_to_raw_response_wrapper(
            factories.list,
        )
        self.get = async_to_raw_response_wrapper(
            factories.get,
        )

    @cached_property
    def inbox(self) -> AsyncInboxResourceWithRawResponse:
        """Operations for creating and managing factories"""
        return AsyncInboxResourceWithRawResponse(self._factories.inbox)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithRawResponse:
        """Operations for creating and managing factories"""
        return AsyncRunsResourceWithRawResponse(self._factories.runs)


class FactoriesResourceWithStreamingResponse:
    def __init__(self, factories: FactoriesResource) -> None:
        self._factories = factories

        self.list = to_streamed_response_wrapper(
            factories.list,
        )
        self.get = to_streamed_response_wrapper(
            factories.get,
        )

    @cached_property
    def inbox(self) -> InboxResourceWithStreamingResponse:
        """Operations for creating and managing factories"""
        return InboxResourceWithStreamingResponse(self._factories.inbox)

    @cached_property
    def runs(self) -> RunsResourceWithStreamingResponse:
        """Operations for creating and managing factories"""
        return RunsResourceWithStreamingResponse(self._factories.runs)


class AsyncFactoriesResourceWithStreamingResponse:
    def __init__(self, factories: AsyncFactoriesResource) -> None:
        self._factories = factories

        self.list = async_to_streamed_response_wrapper(
            factories.list,
        )
        self.get = async_to_streamed_response_wrapper(
            factories.get,
        )

    @cached_property
    def inbox(self) -> AsyncInboxResourceWithStreamingResponse:
        """Operations for creating and managing factories"""
        return AsyncInboxResourceWithStreamingResponse(self._factories.inbox)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithStreamingResponse:
        """Operations for creating and managing factories"""
        return AsyncRunsResourceWithStreamingResponse(self._factories.runs)
