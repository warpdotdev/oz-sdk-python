# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from tests.utils import assert_matches_type
from warp_platform_sdk import WarpClient, AsyncWarpClient
from warp_platform_sdk._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from warp_platform_sdk.types.agent import (
    ConversationRetrieveResponse,
    ConversationInterruptResponse,
    ConversationCheckRedirectResponse,
    ConversationSubmitFollowupResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConversations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: WarpClient) -> None:
        conversation = client.agent.conversations.retrieve(
            "conversation_id",
        )
        assert_matches_type(ConversationRetrieveResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: WarpClient) -> None:
        response = client.agent.conversations.with_raw_response.retrieve(
            "conversation_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(ConversationRetrieveResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: WarpClient) -> None:
        with client.agent.conversations.with_streaming_response.retrieve(
            "conversation_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(ConversationRetrieveResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: WarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            client.agent.conversations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check_redirect(self, client: WarpClient) -> None:
        conversation = client.agent.conversations.check_redirect(
            "conversationId",
        )
        assert_matches_type(ConversationCheckRedirectResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_check_redirect(self, client: WarpClient) -> None:
        response = client.agent.conversations.with_raw_response.check_redirect(
            "conversationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(ConversationCheckRedirectResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_check_redirect(self, client: WarpClient) -> None:
        with client.agent.conversations.with_streaming_response.check_redirect(
            "conversationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(ConversationCheckRedirectResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_check_redirect(self, client: WarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            client.agent.conversations.with_raw_response.check_redirect(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download_screenshot(self, client: WarpClient, respx_mock: MockRouter) -> None:
        respx_mock.get("/agent/conversations/conversation_id/screenshots/screenshot_uid/download").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        conversation = client.agent.conversations.download_screenshot(
            screenshot_uid="screenshot_uid",
            conversation_id="conversation_id",
        )
        assert conversation.is_closed
        assert conversation.json() == {"foo": "bar"}
        assert cast(Any, conversation.is_closed) is True
        assert isinstance(conversation, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download_screenshot(self, client: WarpClient, respx_mock: MockRouter) -> None:
        respx_mock.get("/agent/conversations/conversation_id/screenshots/screenshot_uid/download").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        conversation = client.agent.conversations.with_raw_response.download_screenshot(
            screenshot_uid="screenshot_uid",
            conversation_id="conversation_id",
        )

        assert conversation.is_closed is True
        assert conversation.http_request.headers.get("X-Stainless-Lang") == "python"
        assert conversation.json() == {"foo": "bar"}
        assert isinstance(conversation, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download_screenshot(self, client: WarpClient, respx_mock: MockRouter) -> None:
        respx_mock.get("/agent/conversations/conversation_id/screenshots/screenshot_uid/download").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.agent.conversations.with_streaming_response.download_screenshot(
            screenshot_uid="screenshot_uid",
            conversation_id="conversation_id",
        ) as conversation:
            assert not conversation.is_closed
            assert conversation.http_request.headers.get("X-Stainless-Lang") == "python"

            assert conversation.json() == {"foo": "bar"}
            assert cast(Any, conversation.is_closed) is True
            assert isinstance(conversation, StreamedBinaryAPIResponse)

        assert cast(Any, conversation.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download_screenshot(self, client: WarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            client.agent.conversations.with_raw_response.download_screenshot(
                screenshot_uid="screenshot_uid",
                conversation_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `screenshot_uid` but received ''"):
            client.agent.conversations.with_raw_response.download_screenshot(
                screenshot_uid="",
                conversation_id="conversation_id",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_transcript(self, client: WarpClient, respx_mock: MockRouter) -> None:
        respx_mock.get("/agent/conversations/conversation_id/transcript").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        conversation = client.agent.conversations.get_transcript(
            "conversation_id",
        )
        assert conversation.is_closed
        assert conversation.json() == {"foo": "bar"}
        assert cast(Any, conversation.is_closed) is True
        assert isinstance(conversation, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_transcript(self, client: WarpClient, respx_mock: MockRouter) -> None:
        respx_mock.get("/agent/conversations/conversation_id/transcript").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        conversation = client.agent.conversations.with_raw_response.get_transcript(
            "conversation_id",
        )

        assert conversation.is_closed is True
        assert conversation.http_request.headers.get("X-Stainless-Lang") == "python"
        assert conversation.json() == {"foo": "bar"}
        assert isinstance(conversation, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_transcript(self, client: WarpClient, respx_mock: MockRouter) -> None:
        respx_mock.get("/agent/conversations/conversation_id/transcript").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.agent.conversations.with_streaming_response.get_transcript(
            "conversation_id",
        ) as conversation:
            assert not conversation.is_closed
            assert conversation.http_request.headers.get("X-Stainless-Lang") == "python"

            assert conversation.json() == {"foo": "bar"}
            assert cast(Any, conversation.is_closed) is True
            assert isinstance(conversation, StreamedBinaryAPIResponse)

        assert cast(Any, conversation.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get_transcript(self, client: WarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            client.agent.conversations.with_raw_response.get_transcript(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_interrupt(self, client: WarpClient) -> None:
        conversation = client.agent.conversations.interrupt(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConversationInterruptResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_interrupt(self, client: WarpClient) -> None:
        response = client.agent.conversations.with_raw_response.interrupt(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(ConversationInterruptResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_interrupt(self, client: WarpClient) -> None:
        with client.agent.conversations.with_streaming_response.interrupt(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(ConversationInterruptResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_interrupt(self, client: WarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            client.agent.conversations.with_raw_response.interrupt(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_followup(self, client: WarpClient) -> None:
        conversation = client.agent.conversations.submit_followup(
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConversationSubmitFollowupResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_followup_with_all_params(self, client: WarpClient) -> None:
        conversation = client.agent.conversations.submit_followup(
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            attachments=[
                {
                    "attachment_id": "attachment_id",
                    "file_name": "file_name",
                }
            ],
            message="message",
            mode="normal",
        )
        assert_matches_type(ConversationSubmitFollowupResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit_followup(self, client: WarpClient) -> None:
        response = client.agent.conversations.with_raw_response.submit_followup(
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(ConversationSubmitFollowupResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit_followup(self, client: WarpClient) -> None:
        with client.agent.conversations.with_streaming_response.submit_followup(
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(ConversationSubmitFollowupResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_submit_followup(self, client: WarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            client.agent.conversations.with_raw_response.submit_followup(
                conversation_id="",
            )


class TestAsyncConversations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWarpClient) -> None:
        conversation = await async_client.agent.conversations.retrieve(
            "conversation_id",
        )
        assert_matches_type(ConversationRetrieveResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.agent.conversations.with_raw_response.retrieve(
            "conversation_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(ConversationRetrieveResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWarpClient) -> None:
        async with async_client.agent.conversations.with_streaming_response.retrieve(
            "conversation_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(ConversationRetrieveResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            await async_client.agent.conversations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check_redirect(self, async_client: AsyncWarpClient) -> None:
        conversation = await async_client.agent.conversations.check_redirect(
            "conversationId",
        )
        assert_matches_type(ConversationCheckRedirectResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_check_redirect(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.agent.conversations.with_raw_response.check_redirect(
            "conversationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(ConversationCheckRedirectResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_check_redirect(self, async_client: AsyncWarpClient) -> None:
        async with async_client.agent.conversations.with_streaming_response.check_redirect(
            "conversationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(ConversationCheckRedirectResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_check_redirect(self, async_client: AsyncWarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            await async_client.agent.conversations.with_raw_response.check_redirect(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download_screenshot(self, async_client: AsyncWarpClient, respx_mock: MockRouter) -> None:
        respx_mock.get("/agent/conversations/conversation_id/screenshots/screenshot_uid/download").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        conversation = await async_client.agent.conversations.download_screenshot(
            screenshot_uid="screenshot_uid",
            conversation_id="conversation_id",
        )
        assert conversation.is_closed
        assert await conversation.json() == {"foo": "bar"}
        assert cast(Any, conversation.is_closed) is True
        assert isinstance(conversation, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download_screenshot(
        self, async_client: AsyncWarpClient, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/agent/conversations/conversation_id/screenshots/screenshot_uid/download").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        conversation = await async_client.agent.conversations.with_raw_response.download_screenshot(
            screenshot_uid="screenshot_uid",
            conversation_id="conversation_id",
        )

        assert conversation.is_closed is True
        assert conversation.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await conversation.json() == {"foo": "bar"}
        assert isinstance(conversation, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download_screenshot(
        self, async_client: AsyncWarpClient, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/agent/conversations/conversation_id/screenshots/screenshot_uid/download").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.agent.conversations.with_streaming_response.download_screenshot(
            screenshot_uid="screenshot_uid",
            conversation_id="conversation_id",
        ) as conversation:
            assert not conversation.is_closed
            assert conversation.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await conversation.json() == {"foo": "bar"}
            assert cast(Any, conversation.is_closed) is True
            assert isinstance(conversation, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, conversation.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download_screenshot(self, async_client: AsyncWarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            await async_client.agent.conversations.with_raw_response.download_screenshot(
                screenshot_uid="screenshot_uid",
                conversation_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `screenshot_uid` but received ''"):
            await async_client.agent.conversations.with_raw_response.download_screenshot(
                screenshot_uid="",
                conversation_id="conversation_id",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_transcript(self, async_client: AsyncWarpClient, respx_mock: MockRouter) -> None:
        respx_mock.get("/agent/conversations/conversation_id/transcript").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        conversation = await async_client.agent.conversations.get_transcript(
            "conversation_id",
        )
        assert conversation.is_closed
        assert await conversation.json() == {"foo": "bar"}
        assert cast(Any, conversation.is_closed) is True
        assert isinstance(conversation, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_transcript(self, async_client: AsyncWarpClient, respx_mock: MockRouter) -> None:
        respx_mock.get("/agent/conversations/conversation_id/transcript").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        conversation = await async_client.agent.conversations.with_raw_response.get_transcript(
            "conversation_id",
        )

        assert conversation.is_closed is True
        assert conversation.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await conversation.json() == {"foo": "bar"}
        assert isinstance(conversation, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_transcript(
        self, async_client: AsyncWarpClient, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/agent/conversations/conversation_id/transcript").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.agent.conversations.with_streaming_response.get_transcript(
            "conversation_id",
        ) as conversation:
            assert not conversation.is_closed
            assert conversation.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await conversation.json() == {"foo": "bar"}
            assert cast(Any, conversation.is_closed) is True
            assert isinstance(conversation, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, conversation.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get_transcript(self, async_client: AsyncWarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            await async_client.agent.conversations.with_raw_response.get_transcript(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_interrupt(self, async_client: AsyncWarpClient) -> None:
        conversation = await async_client.agent.conversations.interrupt(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConversationInterruptResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_interrupt(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.agent.conversations.with_raw_response.interrupt(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(ConversationInterruptResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_interrupt(self, async_client: AsyncWarpClient) -> None:
        async with async_client.agent.conversations.with_streaming_response.interrupt(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(ConversationInterruptResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_interrupt(self, async_client: AsyncWarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            await async_client.agent.conversations.with_raw_response.interrupt(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_followup(self, async_client: AsyncWarpClient) -> None:
        conversation = await async_client.agent.conversations.submit_followup(
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConversationSubmitFollowupResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_followup_with_all_params(self, async_client: AsyncWarpClient) -> None:
        conversation = await async_client.agent.conversations.submit_followup(
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            attachments=[
                {
                    "attachment_id": "attachment_id",
                    "file_name": "file_name",
                }
            ],
            message="message",
            mode="normal",
        )
        assert_matches_type(ConversationSubmitFollowupResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit_followup(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.agent.conversations.with_raw_response.submit_followup(
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(ConversationSubmitFollowupResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit_followup(self, async_client: AsyncWarpClient) -> None:
        async with async_client.agent.conversations.with_streaming_response.submit_followup(
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(ConversationSubmitFollowupResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_submit_followup(self, async_client: AsyncWarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            await async_client.agent.conversations.with_raw_response.submit_followup(
                conversation_id="",
            )
