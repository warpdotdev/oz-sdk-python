# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from tests.utils import assert_matches_type
from warp_platform_sdk import WarpClient, AsyncWarpClient
from warp_platform_sdk.types import (
    AgentRunResponse,
    AgentListResponse,
    AgentListModelsResponse,
    AgentGetArtifactResponse,
    AgentListEnvironmentsResponse,
    AgentGetRunByExternalReferenceResponse,
)
from warp_platform_sdk._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: WarpClient) -> None:
        with pytest.warns(DeprecationWarning):
            agent = client.agent.list()

        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: WarpClient) -> None:
        with pytest.warns(DeprecationWarning):
            agent = client.agent.list(
                include_malformed_skills=True,
                refresh=True,
                repo="repo",
                sort_by="name",
                team_uid="X-Warp-Team-Uid",
            )

        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: WarpClient) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.agent.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: WarpClient) -> None:
        with pytest.warns(DeprecationWarning):
            with client.agent.with_streaming_response.list() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                agent = response.parse()
                assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download_artifact(self, client: WarpClient, respx_mock: MockRouter) -> None:
        respx_mock.get("/agent/artifacts/artifactUid/download").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        agent = client.agent.download_artifact(
            "artifactUid",
        )
        assert agent.is_closed
        assert agent.json() == {"foo": "bar"}
        assert cast(Any, agent.is_closed) is True
        assert isinstance(agent, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download_artifact(self, client: WarpClient, respx_mock: MockRouter) -> None:
        respx_mock.get("/agent/artifacts/artifactUid/download").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        agent = client.agent.with_raw_response.download_artifact(
            "artifactUid",
        )

        assert agent.is_closed is True
        assert agent.http_request.headers.get("X-Stainless-Lang") == "python"
        assert agent.json() == {"foo": "bar"}
        assert isinstance(agent, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download_artifact(self, client: WarpClient, respx_mock: MockRouter) -> None:
        respx_mock.get("/agent/artifacts/artifactUid/download").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.agent.with_streaming_response.download_artifact(
            "artifactUid",
        ) as agent:
            assert not agent.is_closed
            assert agent.http_request.headers.get("X-Stainless-Lang") == "python"

            assert agent.json() == {"foo": "bar"}
            assert cast(Any, agent.is_closed) is True
            assert isinstance(agent, StreamedBinaryAPIResponse)

        assert cast(Any, agent.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download_artifact(self, client: WarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_uid` but received ''"):
            client.agent.with_raw_response.download_artifact(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_artifact(self, client: WarpClient) -> None:
        agent = client.agent.get_artifact(
            "artifactUid",
        )
        assert_matches_type(AgentGetArtifactResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_artifact(self, client: WarpClient) -> None:
        response = client.agent.with_raw_response.get_artifact(
            "artifactUid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentGetArtifactResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_artifact(self, client: WarpClient) -> None:
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
    def test_path_params_get_artifact(self, client: WarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_uid` but received ''"):
            client.agent.with_raw_response.get_artifact(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_run_by_external_reference(self, client: WarpClient) -> None:
        agent = client.agent.get_run_by_external_reference(
            url="url",
        )
        assert_matches_type(AgentGetRunByExternalReferenceResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_run_by_external_reference(self, client: WarpClient) -> None:
        response = client.agent.with_raw_response.get_run_by_external_reference(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentGetRunByExternalReferenceResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_run_by_external_reference(self, client: WarpClient) -> None:
        with client.agent.with_streaming_response.get_run_by_external_reference(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentGetRunByExternalReferenceResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_environments(self, client: WarpClient) -> None:
        agent = client.agent.list_environments()
        assert_matches_type(AgentListEnvironmentsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_environments_with_all_params(self, client: WarpClient) -> None:
        agent = client.agent.list_environments(
            sort_by="name",
            team_uid="X-Warp-Team-Uid",
        )
        assert_matches_type(AgentListEnvironmentsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_environments(self, client: WarpClient) -> None:
        response = client.agent.with_raw_response.list_environments()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentListEnvironmentsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_environments(self, client: WarpClient) -> None:
        with client.agent.with_streaming_response.list_environments() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentListEnvironmentsResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_models(self, client: WarpClient) -> None:
        agent = client.agent.list_models()
        assert_matches_type(AgentListModelsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_models(self, client: WarpClient) -> None:
        response = client.agent.with_raw_response.list_models()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentListModelsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_models(self, client: WarpClient) -> None:
        with client.agent.with_streaming_response.list_models() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentListModelsResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run(self, client: WarpClient) -> None:
        agent = client.agent.run()
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: WarpClient) -> None:
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
                "computer_use_model_id": "computer_use_model_id",
                "credential_strategy": "CREATOR",
                "environment_id": "environment_id",
                "harness": {
                    "model_id": "model_id",
                    "reasoning_level": "reasoning_level",
                    "type": "oz",
                },
                "harness_auth_secrets": {
                    "claude_auth_secret_name": "claude_auth_secret_name",
                    "codex_auth_secret_name": "codex_auth_secret_name",
                },
                "idle_timeout_minutes": 0,
                "inference_providers": {
                    "aws": {
                        "disabled": True,
                        "region": "region",
                        "role_arn": "role_arn",
                    }
                },
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
                "memory_stores": [
                    {
                        "access": "read_write",
                        "instructions": "instructions",
                        "uid": "uid",
                    }
                ],
                "model_id": "model_id",
                "name": "name",
                "runner_id": "runner_id",
                "secrets": [{"name": "name"}],
                "session_sharing": {"public_access": "VIEWER"},
                "skill_spec": "skill_spec",
                "skills": ["string"],
                "worker_host": "worker_host",
            },
            conversation_id="conversation_id",
            interactive=True,
            metadata={"foo": "string"},
            mode="normal",
            on_behalf_of="on_behalf_of",
            parent_run_id="parent_run_id",
            prompt="prompt",
            skill="skill",
            team=True,
            title="title",
            team_uid="X-Warp-Team-Uid",
        )
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: WarpClient) -> None:
        response = client.agent.with_raw_response.run()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: WarpClient) -> None:
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
    async def test_method_list(self, async_client: AsyncWarpClient) -> None:
        with pytest.warns(DeprecationWarning):
            agent = await async_client.agent.list()

        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWarpClient) -> None:
        with pytest.warns(DeprecationWarning):
            agent = await async_client.agent.list(
                include_malformed_skills=True,
                refresh=True,
                repo="repo",
                sort_by="name",
                team_uid="X-Warp-Team-Uid",
            )

        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWarpClient) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.agent.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWarpClient) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.agent.with_streaming_response.list() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                agent = await response.parse()
                assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download_artifact(self, async_client: AsyncWarpClient, respx_mock: MockRouter) -> None:
        respx_mock.get("/agent/artifacts/artifactUid/download").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        agent = await async_client.agent.download_artifact(
            "artifactUid",
        )
        assert agent.is_closed
        assert await agent.json() == {"foo": "bar"}
        assert cast(Any, agent.is_closed) is True
        assert isinstance(agent, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download_artifact(self, async_client: AsyncWarpClient, respx_mock: MockRouter) -> None:
        respx_mock.get("/agent/artifacts/artifactUid/download").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        agent = await async_client.agent.with_raw_response.download_artifact(
            "artifactUid",
        )

        assert agent.is_closed is True
        assert agent.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await agent.json() == {"foo": "bar"}
        assert isinstance(agent, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download_artifact(
        self, async_client: AsyncWarpClient, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/agent/artifacts/artifactUid/download").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.agent.with_streaming_response.download_artifact(
            "artifactUid",
        ) as agent:
            assert not agent.is_closed
            assert agent.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await agent.json() == {"foo": "bar"}
            assert cast(Any, agent.is_closed) is True
            assert isinstance(agent, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, agent.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download_artifact(self, async_client: AsyncWarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_uid` but received ''"):
            await async_client.agent.with_raw_response.download_artifact(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_artifact(self, async_client: AsyncWarpClient) -> None:
        agent = await async_client.agent.get_artifact(
            "artifactUid",
        )
        assert_matches_type(AgentGetArtifactResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_artifact(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.agent.with_raw_response.get_artifact(
            "artifactUid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentGetArtifactResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_artifact(self, async_client: AsyncWarpClient) -> None:
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
    async def test_path_params_get_artifact(self, async_client: AsyncWarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_uid` but received ''"):
            await async_client.agent.with_raw_response.get_artifact(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_run_by_external_reference(self, async_client: AsyncWarpClient) -> None:
        agent = await async_client.agent.get_run_by_external_reference(
            url="url",
        )
        assert_matches_type(AgentGetRunByExternalReferenceResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_run_by_external_reference(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.agent.with_raw_response.get_run_by_external_reference(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentGetRunByExternalReferenceResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_run_by_external_reference(self, async_client: AsyncWarpClient) -> None:
        async with async_client.agent.with_streaming_response.get_run_by_external_reference(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentGetRunByExternalReferenceResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_environments(self, async_client: AsyncWarpClient) -> None:
        agent = await async_client.agent.list_environments()
        assert_matches_type(AgentListEnvironmentsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_environments_with_all_params(self, async_client: AsyncWarpClient) -> None:
        agent = await async_client.agent.list_environments(
            sort_by="name",
            team_uid="X-Warp-Team-Uid",
        )
        assert_matches_type(AgentListEnvironmentsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_environments(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.agent.with_raw_response.list_environments()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentListEnvironmentsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_environments(self, async_client: AsyncWarpClient) -> None:
        async with async_client.agent.with_streaming_response.list_environments() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentListEnvironmentsResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_models(self, async_client: AsyncWarpClient) -> None:
        agent = await async_client.agent.list_models()
        assert_matches_type(AgentListModelsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_models(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.agent.with_raw_response.list_models()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentListModelsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_models(self, async_client: AsyncWarpClient) -> None:
        async with async_client.agent.with_streaming_response.list_models() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentListModelsResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncWarpClient) -> None:
        agent = await async_client.agent.run()
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncWarpClient) -> None:
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
                "computer_use_model_id": "computer_use_model_id",
                "credential_strategy": "CREATOR",
                "environment_id": "environment_id",
                "harness": {
                    "model_id": "model_id",
                    "reasoning_level": "reasoning_level",
                    "type": "oz",
                },
                "harness_auth_secrets": {
                    "claude_auth_secret_name": "claude_auth_secret_name",
                    "codex_auth_secret_name": "codex_auth_secret_name",
                },
                "idle_timeout_minutes": 0,
                "inference_providers": {
                    "aws": {
                        "disabled": True,
                        "region": "region",
                        "role_arn": "role_arn",
                    }
                },
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
                "memory_stores": [
                    {
                        "access": "read_write",
                        "instructions": "instructions",
                        "uid": "uid",
                    }
                ],
                "model_id": "model_id",
                "name": "name",
                "runner_id": "runner_id",
                "secrets": [{"name": "name"}],
                "session_sharing": {"public_access": "VIEWER"},
                "skill_spec": "skill_spec",
                "skills": ["string"],
                "worker_host": "worker_host",
            },
            conversation_id="conversation_id",
            interactive=True,
            metadata={"foo": "string"},
            mode="normal",
            on_behalf_of="on_behalf_of",
            parent_run_id="parent_run_id",
            prompt="prompt",
            skill="skill",
            team=True,
            title="title",
            team_uid="X-Warp-Team-Uid",
        )
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.agent.with_raw_response.run()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncWarpClient) -> None:
        async with async_client.agent.with_streaming_response.run() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentRunResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True
