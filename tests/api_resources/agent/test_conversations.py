# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from oz_agent_sdk import OzAPI, AsyncOzAPI

from oz_agent_sdk.types.agent import ConversationCheckRedirectResponse

from typing import cast, Any

import os
import pytest
import httpx
from typing_extensions import get_args
from respx import MockRouter
from oz_agent_sdk import OzAPI, AsyncOzAPI
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestConversations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check_redirect(self, client: OzAPI) -> None:
        conversation = client.agent.conversations.check_redirect(
            "conversationId",
        )
        assert_matches_type(ConversationCheckRedirectResponse, conversation, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_check_redirect(self, client: OzAPI) -> None:

        response = client.agent.conversations.with_raw_response.check_redirect(
            "conversationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        conversation = response.parse()
        assert_matches_type(ConversationCheckRedirectResponse, conversation, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_check_redirect(self, client: OzAPI) -> None:
        with client.agent.conversations.with_streaming_response.check_redirect(
            "conversationId",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            conversation = response.parse()
            assert_matches_type(ConversationCheckRedirectResponse, conversation, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_check_redirect(self, client: OzAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
          client.agent.conversations.with_raw_response.check_redirect(
              "",
          )
class TestAsyncConversations:
    parametrize = pytest.mark.parametrize("async_client", [False, True, {'http_client': 'aiohttp'}], indirect=True, ids=['loose', 'strict', 'aiohttp'])


    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check_redirect(self, async_client: AsyncOzAPI) -> None:
        conversation = await async_client.agent.conversations.check_redirect(
            "conversationId",
        )
        assert_matches_type(ConversationCheckRedirectResponse, conversation, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_check_redirect(self, async_client: AsyncOzAPI) -> None:

        response = await async_client.agent.conversations.with_raw_response.check_redirect(
            "conversationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        conversation = await response.parse()
        assert_matches_type(ConversationCheckRedirectResponse, conversation, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_check_redirect(self, async_client: AsyncOzAPI) -> None:
        async with async_client.agent.conversations.with_streaming_response.check_redirect(
            "conversationId",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            conversation = await response.parse()
            assert_matches_type(ConversationCheckRedirectResponse, conversation, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_check_redirect(self, async_client: AsyncOzAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
          await async_client.agent.conversations.with_raw_response.check_redirect(
              "",
          )