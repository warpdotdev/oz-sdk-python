# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, strip_not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncFactoryInboxCursorPage, AsyncFactoryInboxCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.factories import InboxScope, inbox_list_params
from ...types.factories.inbox_item import InboxItem
from ...types.factories.inbox_scope import InboxScope

__all__ = ["InboxResource", "AsyncInboxResource"]


class InboxResource(SyncAPIResource):
    """Operations for creating and managing factories"""

    @cached_property
    def with_raw_response(self) -> InboxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#accessing-raw-response-data-eg-headers
        """
        return InboxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#with_streaming_response
        """
        return InboxResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        factory_uid: str | Omit = omit,
        limit: int | Omit = omit,
        recipient_uid: str | Omit = omit,
        scope: InboxScope | Omit = omit,
        team_uid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncFactoryInboxCursorPage[InboxItem]:
        """
        List unresolved notifications across factories authorized for the authenticated
        principal and active team. The default `mine` scope preserves the personal Inbox
        and requires user credentials. The `team` scope lists notifications assigned to
        any live recipient and can be used by user or service-account credentials.
        Delivery routing is configured separately from Inbox assignment.

        Args:
          cursor: Opaque cursor from page_info.next_cursor.

          factory_uid: Exact Factory UID filter, intersected with authorized factories.

          limit: Maximum number of items to return. Defaults to 50.

          recipient_uid: Exact public user UID filter within the authorized Factory and team scope. In
              `mine` scope this can only match the authenticated user.

          scope: `mine` returns notifications assigned to the authenticated user and is the
              default. `team` returns notifications across live recipients in the authorized
              Factory and team scope.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Warp-Team-Uid": team_uid}), **(extra_headers or {})}
        return self._get_api_list(
            "/factory-inbox",
            page=SyncFactoryInboxCursorPage[InboxItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "factory_uid": factory_uid,
                        "limit": limit,
                        "recipient_uid": recipient_uid,
                        "scope": scope,
                    },
                    inbox_list_params.InboxListParams,
                ),
            ),
            model=InboxItem,
        )


class AsyncInboxResource(AsyncAPIResource):
    """Operations for creating and managing factories"""

    @cached_property
    def with_raw_response(self) -> AsyncInboxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInboxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#with_streaming_response
        """
        return AsyncInboxResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        factory_uid: str | Omit = omit,
        limit: int | Omit = omit,
        recipient_uid: str | Omit = omit,
        scope: InboxScope | Omit = omit,
        team_uid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[InboxItem, AsyncFactoryInboxCursorPage[InboxItem]]:
        """
        List unresolved notifications across factories authorized for the authenticated
        principal and active team. The default `mine` scope preserves the personal Inbox
        and requires user credentials. The `team` scope lists notifications assigned to
        any live recipient and can be used by user or service-account credentials.
        Delivery routing is configured separately from Inbox assignment.

        Args:
          cursor: Opaque cursor from page_info.next_cursor.

          factory_uid: Exact Factory UID filter, intersected with authorized factories.

          limit: Maximum number of items to return. Defaults to 50.

          recipient_uid: Exact public user UID filter within the authorized Factory and team scope. In
              `mine` scope this can only match the authenticated user.

          scope: `mine` returns notifications assigned to the authenticated user and is the
              default. `team` returns notifications across live recipients in the authorized
              Factory and team scope.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Warp-Team-Uid": team_uid}), **(extra_headers or {})}
        return self._get_api_list(
            "/factory-inbox",
            page=AsyncFactoryInboxCursorPage[InboxItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "factory_uid": factory_uid,
                        "limit": limit,
                        "recipient_uid": recipient_uid,
                        "scope": scope,
                    },
                    inbox_list_params.InboxListParams,
                ),
            ),
            model=InboxItem,
        )


class InboxResourceWithRawResponse:
    def __init__(self, inbox: InboxResource) -> None:
        self._inbox = inbox

        self.list = to_raw_response_wrapper(
            inbox.list,
        )


class AsyncInboxResourceWithRawResponse:
    def __init__(self, inbox: AsyncInboxResource) -> None:
        self._inbox = inbox

        self.list = async_to_raw_response_wrapper(
            inbox.list,
        )


class InboxResourceWithStreamingResponse:
    def __init__(self, inbox: InboxResource) -> None:
        self._inbox = inbox

        self.list = to_streamed_response_wrapper(
            inbox.list,
        )


class AsyncInboxResourceWithStreamingResponse:
    def __init__(self, inbox: AsyncInboxResource) -> None:
        self._inbox = inbox

        self.list = async_to_streamed_response_wrapper(
            inbox.list,
        )
