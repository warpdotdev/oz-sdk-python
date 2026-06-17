# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._resource import SyncAPIResource, AsyncAPIResource

from ..._compat import cached_property

from ..._utils import path_template

from ...types.agent.conversation_check_redirect_response import ConversationCheckRedirectResponse

from ..._base_client import make_request_options

from ..._types import NotGiven

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from typing_extensions import Literal, overload
from ..._types import Timeout, Headers, NotGiven, not_given, Omit, omit, NoneType, Query, Body

__all__ = ["ConversationsResource", "AsyncConversationsResource"]

class ConversationsResource(SyncAPIResource):
    """Operations for running and managing cloud agents"""
    @cached_property
    def with_raw_response(self) -> ConversationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ConversationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConversationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#with_streaming_response
        """
        return ConversationsResourceWithStreamingResponse(self)

    def check_redirect(self,
    conversation_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> ConversationCheckRedirectResponse:
        """Check whether a conversation should redirect to a live shared session.

        Returns a
        session_id if the underlying ambient agent task still has a live shared session,
        or an empty object if no redirect is needed.

        This endpoint is public (no authentication required) so that anonymous viewers
        can resolve a publicly-shared conversation link before signing in. Access to the
        underlying live session is still gated by the session-sharing service ACLs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
          raise ValueError(
            f'Expected a non-empty value for `conversation_id` but received {conversation_id!r}'
          )
        return self._get(
            path_template("/agent/conversations/{conversation_id}/redirect", conversation_id=conversation_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, security={}),
            cast_to=ConversationCheckRedirectResponse,
        )

class AsyncConversationsResource(AsyncAPIResource):
    """Operations for running and managing cloud agents"""
    @cached_property
    def with_raw_response(self) -> AsyncConversationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConversationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConversationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#with_streaming_response
        """
        return AsyncConversationsResourceWithStreamingResponse(self)

    async def check_redirect(self,
    conversation_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> ConversationCheckRedirectResponse:
        """Check whether a conversation should redirect to a live shared session.

        Returns a
        session_id if the underlying ambient agent task still has a live shared session,
        or an empty object if no redirect is needed.

        This endpoint is public (no authentication required) so that anonymous viewers
        can resolve a publicly-shared conversation link before signing in. Access to the
        underlying live session is still gated by the session-sharing service ACLs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
          raise ValueError(
            f'Expected a non-empty value for `conversation_id` but received {conversation_id!r}'
          )
        return await self._get(
            path_template("/agent/conversations/{conversation_id}/redirect", conversation_id=conversation_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, security={}),
            cast_to=ConversationCheckRedirectResponse,
        )

class ConversationsResourceWithRawResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self._conversations = conversations

        self.check_redirect = to_raw_response_wrapper(
            conversations.check_redirect,
        )

class AsyncConversationsResourceWithRawResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

        self.check_redirect = async_to_raw_response_wrapper(
            conversations.check_redirect,
        )

class ConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self._conversations = conversations

        self.check_redirect = to_streamed_response_wrapper(
            conversations.check_redirect,
        )

class AsyncConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

        self.check_redirect = async_to_streamed_response_wrapper(
            conversations.check_redirect,
        )