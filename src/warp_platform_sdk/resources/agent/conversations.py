# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...types.agent import conversation_submit_followup_params
from ..._base_client import make_request_options
from ...types.agent.conversation_retrieve_response import ConversationRetrieveResponse
from ...types.agent.conversation_interrupt_response import ConversationInterruptResponse
from ...types.agent.conversation_check_redirect_response import ConversationCheckRedirectResponse
from ...types.agent.conversation_submit_followup_response import ConversationSubmitFollowupResponse

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

    def retrieve(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationRetrieveResponse:
        """
        Retrieve a conversation directly by conversation ID in Warp's normalized
        task/message format.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._get(
            path_template("/agent/conversations/{conversation_id}", conversation_id=conversation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationRetrieveResponse,
        )

    def check_redirect(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationCheckRedirectResponse:
        """
        Check whether a conversation should redirect to a live shared session, returning
        a session_id if the underlying ambient agent task still has one (or an empty
        object if no redirect is needed). Public and unauthenticated, so anonymous
        viewers can resolve a shared conversation link before signing in; access to the
        underlying live session is still gated by the session-sharing service ACLs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._get(
            path_template("/agent/conversations/{conversation_id}/redirect", conversation_id=conversation_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=ConversationCheckRedirectResponse,
        )

    def download_screenshot(
        self,
        screenshot_uid: str,
        *,
        conversation_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Download a computer-use screenshot that was offloaded from the conversation's
        task history into object storage. The response is a redirect to a short-lived
        signed URL, so clients must follow redirects to receive the image. Requires view
        access to the conversation named in the path; a fork's history may reference
        screenshots stored under its source conversation's ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        if not screenshot_uid:
            raise ValueError(f"Expected a non-empty value for `screenshot_uid` but received {screenshot_uid!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            path_template(
                "/agent/conversations/{conversation_id}/screenshots/{screenshot_uid}/download",
                conversation_id=conversation_id,
                screenshot_uid=screenshot_uid,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def get_transcript(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """Retrieve the raw conversation transcript for a conversation.

        Returns a 302
        redirect to a time-limited download URL for the transcript. Supported for
        third-party harness conversations (Claude Code, Codex, Gemini).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            path_template("/agent/conversations/{conversation_id}/transcript", conversation_id=conversation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def interrupt(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationInterruptResponse:
        """
        The same operation as `POST /agent/runs/{runId}/interrupt`, addressed by the
        conversation the run is serving. The run is picked with the same policy as the
        conversation follow-up route, and the caller must be able to view the
        conversation and the resolved run.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._post(
            path_template("/agent/conversations/{conversation_id}/interrupt", conversation_id=conversation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationInterruptResponse,
        )

    def submit_followup(
        self,
        conversation_id: str,
        *,
        attachments: Iterable[conversation_submit_followup_params.Attachment] | Omit = omit,
        message: str | Omit = omit,
        mode: Literal["normal", "plan", "orchestrate"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationSubmitFollowupResponse:
        """
        The same operation as `POST /agent/runs/{runId}/followups`, targeted by the
        conversation the run is serving rather than the run itself.

        `attachments` must name ids prepared through
        `POST /agent/conversations/{conversation_id}/attachments/prepare` (or the
        run-keyed prepare) for the run that is newest at that time. If a new run appears
        for the conversation between prepare and follow-up, the follow-up resolves to
        the new run and answers 422 `unknown_attachment`; prepare again. A handoff is a
        new execution of the same run and does not have this problem.

        `mode` only takes effect when the follow-up is queued ahead of the run starting
        or starts a new execution; a follow-up injected into a live session runs in the
        session's current mode.

        Args:
          attachments: Files to deliver with the message, at most 25. Each entry must name an
              attachment previously prepared for this run through
              `POST /agent/runs/{runId}/attachments/prepare` and uploaded to its upload
              target; an unknown `attachment_id` is rejected with 422. Files are only
              materialized for the agent on the Oz harness; other harnesses receive a notice
              naming the files.

          message: The follow-up message to send to the run. May be empty when `attachments` is
              non-empty.

          mode: Optional query mode for the follow-up. Defaults to `normal` when omitted. The
              server does not infer mode from prompt prefixes such as `/plan`. The mode only
              takes effect when the follow-up is queued ahead of the run starting or starts a
              new execution; a follow-up injected into a live session runs in the session's
              current mode.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._post(
            path_template("/agent/conversations/{conversation_id}/followups", conversation_id=conversation_id),
            body=maybe_transform(
                {
                    "attachments": attachments,
                    "message": message,
                    "mode": mode,
                },
                conversation_submit_followup_params.ConversationSubmitFollowupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationSubmitFollowupResponse,
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

    async def retrieve(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationRetrieveResponse:
        """
        Retrieve a conversation directly by conversation ID in Warp's normalized
        task/message format.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return await self._get(
            path_template("/agent/conversations/{conversation_id}", conversation_id=conversation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationRetrieveResponse,
        )

    async def check_redirect(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationCheckRedirectResponse:
        """
        Check whether a conversation should redirect to a live shared session, returning
        a session_id if the underlying ambient agent task still has one (or an empty
        object if no redirect is needed). Public and unauthenticated, so anonymous
        viewers can resolve a shared conversation link before signing in; access to the
        underlying live session is still gated by the session-sharing service ACLs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return await self._get(
            path_template("/agent/conversations/{conversation_id}/redirect", conversation_id=conversation_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=ConversationCheckRedirectResponse,
        )

    async def download_screenshot(
        self,
        screenshot_uid: str,
        *,
        conversation_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Download a computer-use screenshot that was offloaded from the conversation's
        task history into object storage. The response is a redirect to a short-lived
        signed URL, so clients must follow redirects to receive the image. Requires view
        access to the conversation named in the path; a fork's history may reference
        screenshots stored under its source conversation's ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        if not screenshot_uid:
            raise ValueError(f"Expected a non-empty value for `screenshot_uid` but received {screenshot_uid!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            path_template(
                "/agent/conversations/{conversation_id}/screenshots/{screenshot_uid}/download",
                conversation_id=conversation_id,
                screenshot_uid=screenshot_uid,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def get_transcript(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """Retrieve the raw conversation transcript for a conversation.

        Returns a 302
        redirect to a time-limited download URL for the transcript. Supported for
        third-party harness conversations (Claude Code, Codex, Gemini).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            path_template("/agent/conversations/{conversation_id}/transcript", conversation_id=conversation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def interrupt(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationInterruptResponse:
        """
        The same operation as `POST /agent/runs/{runId}/interrupt`, addressed by the
        conversation the run is serving. The run is picked with the same policy as the
        conversation follow-up route, and the caller must be able to view the
        conversation and the resolved run.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return await self._post(
            path_template("/agent/conversations/{conversation_id}/interrupt", conversation_id=conversation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationInterruptResponse,
        )

    async def submit_followup(
        self,
        conversation_id: str,
        *,
        attachments: Iterable[conversation_submit_followup_params.Attachment] | Omit = omit,
        message: str | Omit = omit,
        mode: Literal["normal", "plan", "orchestrate"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationSubmitFollowupResponse:
        """
        The same operation as `POST /agent/runs/{runId}/followups`, targeted by the
        conversation the run is serving rather than the run itself.

        `attachments` must name ids prepared through
        `POST /agent/conversations/{conversation_id}/attachments/prepare` (or the
        run-keyed prepare) for the run that is newest at that time. If a new run appears
        for the conversation between prepare and follow-up, the follow-up resolves to
        the new run and answers 422 `unknown_attachment`; prepare again. A handoff is a
        new execution of the same run and does not have this problem.

        `mode` only takes effect when the follow-up is queued ahead of the run starting
        or starts a new execution; a follow-up injected into a live session runs in the
        session's current mode.

        Args:
          attachments: Files to deliver with the message, at most 25. Each entry must name an
              attachment previously prepared for this run through
              `POST /agent/runs/{runId}/attachments/prepare` and uploaded to its upload
              target; an unknown `attachment_id` is rejected with 422. Files are only
              materialized for the agent on the Oz harness; other harnesses receive a notice
              naming the files.

          message: The follow-up message to send to the run. May be empty when `attachments` is
              non-empty.

          mode: Optional query mode for the follow-up. Defaults to `normal` when omitted. The
              server does not infer mode from prompt prefixes such as `/plan`. The mode only
              takes effect when the follow-up is queued ahead of the run starting or starts a
              new execution; a follow-up injected into a live session runs in the session's
              current mode.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return await self._post(
            path_template("/agent/conversations/{conversation_id}/followups", conversation_id=conversation_id),
            body=await async_maybe_transform(
                {
                    "attachments": attachments,
                    "message": message,
                    "mode": mode,
                },
                conversation_submit_followup_params.ConversationSubmitFollowupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationSubmitFollowupResponse,
        )


class ConversationsResourceWithRawResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self._conversations = conversations

        self.retrieve = to_raw_response_wrapper(
            conversations.retrieve,
        )
        self.check_redirect = to_raw_response_wrapper(
            conversations.check_redirect,
        )
        self.download_screenshot = to_custom_raw_response_wrapper(
            conversations.download_screenshot,
            BinaryAPIResponse,
        )
        self.get_transcript = to_custom_raw_response_wrapper(
            conversations.get_transcript,
            BinaryAPIResponse,
        )
        self.interrupt = to_raw_response_wrapper(
            conversations.interrupt,
        )
        self.submit_followup = to_raw_response_wrapper(
            conversations.submit_followup,
        )


class AsyncConversationsResourceWithRawResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

        self.retrieve = async_to_raw_response_wrapper(
            conversations.retrieve,
        )
        self.check_redirect = async_to_raw_response_wrapper(
            conversations.check_redirect,
        )
        self.download_screenshot = async_to_custom_raw_response_wrapper(
            conversations.download_screenshot,
            AsyncBinaryAPIResponse,
        )
        self.get_transcript = async_to_custom_raw_response_wrapper(
            conversations.get_transcript,
            AsyncBinaryAPIResponse,
        )
        self.interrupt = async_to_raw_response_wrapper(
            conversations.interrupt,
        )
        self.submit_followup = async_to_raw_response_wrapper(
            conversations.submit_followup,
        )


class ConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self._conversations = conversations

        self.retrieve = to_streamed_response_wrapper(
            conversations.retrieve,
        )
        self.check_redirect = to_streamed_response_wrapper(
            conversations.check_redirect,
        )
        self.download_screenshot = to_custom_streamed_response_wrapper(
            conversations.download_screenshot,
            StreamedBinaryAPIResponse,
        )
        self.get_transcript = to_custom_streamed_response_wrapper(
            conversations.get_transcript,
            StreamedBinaryAPIResponse,
        )
        self.interrupt = to_streamed_response_wrapper(
            conversations.interrupt,
        )
        self.submit_followup = to_streamed_response_wrapper(
            conversations.submit_followup,
        )


class AsyncConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

        self.retrieve = async_to_streamed_response_wrapper(
            conversations.retrieve,
        )
        self.check_redirect = async_to_streamed_response_wrapper(
            conversations.check_redirect,
        )
        self.download_screenshot = async_to_custom_streamed_response_wrapper(
            conversations.download_screenshot,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get_transcript = async_to_custom_streamed_response_wrapper(
            conversations.get_transcript,
            AsyncStreamedBinaryAPIResponse,
        )
        self.interrupt = async_to_streamed_response_wrapper(
            conversations.interrupt,
        )
        self.submit_followup = async_to_streamed_response_wrapper(
            conversations.submit_followup,
        )
