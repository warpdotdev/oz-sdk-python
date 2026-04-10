# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from oz_agent_sdk import OzAPI, AsyncOzAPI
from oz_agent_sdk.types import (
    AgentRunResponse,
    AgentListResponse,
    AgentGetArtifactResponse,
    AgentListEnvironmentsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: OzAPI) -> None:
        agent = client.agent.list()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: OzAPI) -> None:
        agent = client.agent.list(
            include_malformed_skills=True,
            refresh=True,
            repo="repo",
            sort_by="name",
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OzAPI) -> None:
        response = client.agent.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OzAPI) -> None:
        with client.agent.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_artifact(self, client: OzAPI) -> None:
        agent = client.agent.get_artifact(
            "artifactUid",
        )
        assert_matches_type(AgentGetArtifactResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_artifact(self, client: OzAPI) -> None:
        response = client.agent.with_raw_response.get_artifact(
            "artifactUid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentGetArtifactResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_artifact(self, client: OzAPI) -> None:
        with client.agent.with_streaming_response.get_artifact(
            "artifactUid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentGetArtifactResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_artifact(self, client: OzAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_uid` but received ''"):
            client.agent.with_raw_response.get_artifact(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_environments(self, client: OzAPI) -> None:
        agent = client.agent.list_environments()
        assert_matches_type(AgentListEnvironmentsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_environments_with_all_params(self, client: OzAPI) -> None:
        agent = client.agent.list_environments(
            sort_by="name",
        )
        assert_matches_type(AgentListEnvironmentsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_environments(self, client: OzAPI) -> None:
        response = client.agent.with_raw_response.list_environments()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentListEnvironmentsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_environments(self, client: OzAPI) -> None:
        with client.agent.with_streaming_response.list_environments() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentListEnvironmentsResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run(self, client: OzAPI) -> None:
        agent = client.agent.run()
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: OzAPI) -> None:
        agent = client.agent.run(
            agent_identity_uid="agent_identity_uid",
            attachments=[
                {
                    "data": "U3RhaW5sZXNzIHJvY2tz",
                    "file_name": "file_name",
                    "mime_type": "mime_type",
                }
            ],
            config={
                "base_prompt": "base_prompt",
                "computer_use_enabled": True,
                "environment_id": "environment_id",
                "harness": {
                    "auth_secret_name": "auth_secret_name",
                    "type": "oz",
                },
                "idle_timeout_minutes": 1,
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
                "skill_spec": "skill_spec",
                "worker_host": "worker_host",
            },
            conversation_id="conversation_id",
            interactive=True,
            parent_run_id="parent_run_id",
            prompt="prompt",
            skill="skill",
            team=True,
            title="title",
        )
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: OzAPI) -> None:
        response = client.agent.with_raw_response.run()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: OzAPI) -> None:
        with client.agent.with_streaming_response.run() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentRunResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAgent:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOzAPI) -> None:
        agent = await async_client.agent.list()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOzAPI) -> None:
        agent = await async_client.agent.list(
            include_malformed_skills=True,
            refresh=True,
            repo="repo",
            sort_by="name",
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOzAPI) -> None:
        response = await async_client.agent.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOzAPI) -> None:
        async with async_client.agent.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_artifact(self, async_client: AsyncOzAPI) -> None:
        agent = await async_client.agent.get_artifact(
            "artifactUid",
        )
        assert_matches_type(AgentGetArtifactResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_artifact(self, async_client: AsyncOzAPI) -> None:
        response = await async_client.agent.with_raw_response.get_artifact(
            "artifactUid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentGetArtifactResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_artifact(self, async_client: AsyncOzAPI) -> None:
        async with async_client.agent.with_streaming_response.get_artifact(
            "artifactUid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentGetArtifactResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_artifact(self, async_client: AsyncOzAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_uid` but received ''"):
            await async_client.agent.with_raw_response.get_artifact(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_environments(self, async_client: AsyncOzAPI) -> None:
        agent = await async_client.agent.list_environments()
        assert_matches_type(AgentListEnvironmentsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_environments_with_all_params(self, async_client: AsyncOzAPI) -> None:
        agent = await async_client.agent.list_environments(
            sort_by="name",
        )
        assert_matches_type(AgentListEnvironmentsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_environments(self, async_client: AsyncOzAPI) -> None:
        response = await async_client.agent.with_raw_response.list_environments()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentListEnvironmentsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_environments(self, async_client: AsyncOzAPI) -> None:
        async with async_client.agent.with_streaming_response.list_environments() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentListEnvironmentsResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncOzAPI) -> None:
        agent = await async_client.agent.run()
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncOzAPI) -> None:
        agent = await async_client.agent.run(
            agent_identity_uid="agent_identity_uid",
            attachments=[
                {
                    "data": "U3RhaW5sZXNzIHJvY2tz",
                    "file_name": "file_name",
                    "mime_type": "mime_type",
                }
            ],
            config={
                "base_prompt": "base_prompt",
                "computer_use_enabled": True,
                "environment_id": "environment_id",
                "harness": {
                    "auth_secret_name": "auth_secret_name",
                    "type": "oz",
                },
                "idle_timeout_minutes": 1,
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
                "skill_spec": "skill_spec",
                "worker_host": "worker_host",
            },
            conversation_id="conversation_id",
            interactive=True,
            parent_run_id="parent_run_id",
            prompt="prompt",
            skill="skill",
            team=True,
            title="title",
        )
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncOzAPI) -> None:
        response = await async_client.agent.with_raw_response.run()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncOzAPI) -> None:
        async with async_client.agent.with_streaming_response.run() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentRunResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True
