# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from warp_agent_sdk import WarpAPI, AsyncWarpAPI
from warp_agent_sdk.types import AgentRunResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run(self, client: WarpAPI) -> None:
        agent = client.agent.run(
            prompt="Fix the bug in auth.go",
        )
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: WarpAPI) -> None:
        agent = client.agent.run(
            prompt="Fix the bug in auth.go",
            config={
                "base_prompt": "base_prompt",
                "environment_id": "environment_id",
                "mcp_servers": {
                    "foo": {
                        "args": ["string"],
                        "command": "command",
                        "env": {"foo": "string"},
                        "headers": {"foo": "string"},
                        "url": "https://example.com",
                        "warp_id": "warp_id",
                    }
                },
                "model_id": "model_id",
                "name": "name",
            },
            title="title",
        )
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: WarpAPI) -> None:
        response = client.agent.with_raw_response.run(
            prompt="Fix the bug in auth.go",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: WarpAPI) -> None:
        with client.agent.with_streaming_response.run(
            prompt="Fix the bug in auth.go",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentRunResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAgent:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncWarpAPI) -> None:
        agent = await async_client.agent.run(
            prompt="Fix the bug in auth.go",
        )
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncWarpAPI) -> None:
        agent = await async_client.agent.run(
            prompt="Fix the bug in auth.go",
            config={
                "base_prompt": "base_prompt",
                "environment_id": "environment_id",
                "mcp_servers": {
                    "foo": {
                        "args": ["string"],
                        "command": "command",
                        "env": {"foo": "string"},
                        "headers": {"foo": "string"},
                        "url": "https://example.com",
                        "warp_id": "warp_id",
                    }
                },
                "model_id": "model_id",
                "name": "name",
            },
            title="title",
        )
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncWarpAPI) -> None:
        response = await async_client.agent.with_raw_response.run(
            prompt="Fix the bug in auth.go",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncWarpAPI) -> None:
        async with async_client.agent.with_streaming_response.run(
            prompt="Fix the bug in auth.go",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentRunResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True
