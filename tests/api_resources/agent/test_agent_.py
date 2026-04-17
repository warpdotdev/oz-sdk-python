# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from oz_agent_sdk import OzAPI, AsyncOzAPI
from oz_agent_sdk.types.agent import (
    AgentResponse,
    ListAgentIdentitiesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: OzAPI) -> None:
        agent = client.agent.agent.create(
            name="name",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: OzAPI) -> None:
        response = client.agent.agent.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: OzAPI) -> None:
        with client.agent.agent.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: OzAPI) -> None:
        agent = client.agent.agent.update(
            uid="uid",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: OzAPI) -> None:
        agent = client.agent.agent.update(
            uid="uid",
            name="name",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: OzAPI) -> None:
        response = client.agent.agent.with_raw_response.update(
            uid="uid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: OzAPI) -> None:
        with client.agent.agent.with_streaming_response.update(
            uid="uid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: OzAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uid` but received ''"):
            client.agent.agent.with_raw_response.update(
                uid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: OzAPI) -> None:
        agent = client.agent.agent.list()
        assert_matches_type(ListAgentIdentitiesResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OzAPI) -> None:
        response = client.agent.agent.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(ListAgentIdentitiesResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OzAPI) -> None:
        with client.agent.agent.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(ListAgentIdentitiesResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: OzAPI) -> None:
        agent = client.agent.agent.delete(
            "uid",
        )
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: OzAPI) -> None:
        response = client.agent.agent.with_raw_response.delete(
            "uid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: OzAPI) -> None:
        with client.agent.agent.with_streaming_response.delete(
            "uid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: OzAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uid` but received ''"):
            client.agent.agent.with_raw_response.delete(
                "",
            )


class TestAsyncAgent:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncOzAPI) -> None:
        agent = await async_client.agent.agent.create(
            name="name",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOzAPI) -> None:
        response = await async_client.agent.agent.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOzAPI) -> None:
        async with async_client.agent.agent.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncOzAPI) -> None:
        agent = await async_client.agent.agent.update(
            uid="uid",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOzAPI) -> None:
        agent = await async_client.agent.agent.update(
            uid="uid",
            name="name",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOzAPI) -> None:
        response = await async_client.agent.agent.with_raw_response.update(
            uid="uid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOzAPI) -> None:
        async with async_client.agent.agent.with_streaming_response.update(
            uid="uid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncOzAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uid` but received ''"):
            await async_client.agent.agent.with_raw_response.update(
                uid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOzAPI) -> None:
        agent = await async_client.agent.agent.list()
        assert_matches_type(ListAgentIdentitiesResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOzAPI) -> None:
        response = await async_client.agent.agent.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(ListAgentIdentitiesResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOzAPI) -> None:
        async with async_client.agent.agent.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(ListAgentIdentitiesResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncOzAPI) -> None:
        agent = await async_client.agent.agent.delete(
            "uid",
        )
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOzAPI) -> None:
        response = await async_client.agent.agent.with_raw_response.delete(
            "uid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOzAPI) -> None:
        async with async_client.agent.agent.with_streaming_response.delete(
            "uid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOzAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uid` but received ''"):
            await async_client.agent.agent.with_raw_response.delete(
                "",
            )
