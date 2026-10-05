# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from warp_platform_sdk import WarpClient, AsyncWarpClient
from warp_platform_sdk.pagination import SyncBenchmarkSuitesCursorPage, AsyncBenchmarkSuitesCursorPage
from warp_platform_sdk.types.factories.benchmarks import (
    SuiteGetResponse,
    SuiteListResponse,
    SuiteCreateResponse,
    SuiteLaunchRunResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSuites:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: WarpClient) -> None:
        suite = client.factories.benchmarks.suites.create(
            uid="uid",
            agent_uid="agent_uid",
            factory_agent_type="factory_agent_type",
            name="name",
            suite_uid="uid",
        )
        assert_matches_type(SuiteCreateResponse, suite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: WarpClient) -> None:
        suite = client.factories.benchmarks.suites.create(
            uid="uid",
            agent_uid="agent_uid",
            factory_agent_type="factory_agent_type",
            name="name",
            suite_uid="uid",
            description="description",
            tasks=[
                {
                    "prompt": "prompt",
                    "success_criteria": "success_criteria",
                    "title": "title",
                    "labels": {"foo": "string"},
                    "source_run_id": "source_run_id",
                    "starting_repo_refs": [
                        {
                            "code_forge": "code_forge",
                            "owner": "owner",
                            "repo": "repo",
                            "ref": "ref",
                        }
                    ],
                    "tags": ["string"],
                    "uid": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        )
        assert_matches_type(SuiteCreateResponse, suite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: WarpClient) -> None:
        response = client.factories.benchmarks.suites.with_raw_response.create(
            uid="uid",
            agent_uid="agent_uid",
            factory_agent_type="factory_agent_type",
            name="name",
            suite_uid="uid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suite = response.parse()
        assert_matches_type(SuiteCreateResponse, suite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: WarpClient) -> None:
        with client.factories.benchmarks.suites.with_streaming_response.create(
            uid="uid",
            agent_uid="agent_uid",
            factory_agent_type="factory_agent_type",
            name="name",
            suite_uid="uid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suite = response.parse()
            assert_matches_type(SuiteCreateResponse, suite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: WarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uid` but received ''"):
            client.factories.benchmarks.suites.with_raw_response.create(
                uid="",
                agent_uid="agent_uid",
                factory_agent_type="factory_agent_type",
                name="name",
                suite_uid="uid",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: WarpClient) -> None:
        suite = client.factories.benchmarks.suites.list(
            uid="uid",
        )
        assert_matches_type(SyncBenchmarkSuitesCursorPage[SuiteListResponse], suite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: WarpClient) -> None:
        suite = client.factories.benchmarks.suites.list(
            uid="uid",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(SyncBenchmarkSuitesCursorPage[SuiteListResponse], suite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: WarpClient) -> None:
        response = client.factories.benchmarks.suites.with_raw_response.list(
            uid="uid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suite = response.parse()
        assert_matches_type(SyncBenchmarkSuitesCursorPage[SuiteListResponse], suite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: WarpClient) -> None:
        with client.factories.benchmarks.suites.with_streaming_response.list(
            uid="uid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suite = response.parse()
            assert_matches_type(SyncBenchmarkSuitesCursorPage[SuiteListResponse], suite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: WarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uid` but received ''"):
            client.factories.benchmarks.suites.with_raw_response.list(
                uid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: WarpClient) -> None:
        suite = client.factories.benchmarks.suites.get(
            suite_uid="suite_uid",
            uid="uid",
        )
        assert_matches_type(SuiteGetResponse, suite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: WarpClient) -> None:
        response = client.factories.benchmarks.suites.with_raw_response.get(
            suite_uid="suite_uid",
            uid="uid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suite = response.parse()
        assert_matches_type(SuiteGetResponse, suite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: WarpClient) -> None:
        with client.factories.benchmarks.suites.with_streaming_response.get(
            suite_uid="suite_uid",
            uid="uid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suite = response.parse()
            assert_matches_type(SuiteGetResponse, suite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: WarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uid` but received ''"):
            client.factories.benchmarks.suites.with_raw_response.get(
                suite_uid="suite_uid",
                uid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `suite_uid` but received ''"):
            client.factories.benchmarks.suites.with_raw_response.get(
                suite_uid="",
                uid="uid",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_launch_run(self, client: WarpClient) -> None:
        suite = client.factories.benchmarks.suites.launch_run(
            suite_uid="suite_uid",
            uid="uid",
            repetition_count=1,
        )
        assert_matches_type(SuiteLaunchRunResponse, suite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_launch_run_with_all_params(self, client: WarpClient) -> None:
        suite = client.factories.benchmarks.suites.launch_run(
            suite_uid="suite_uid",
            uid="uid",
            repetition_count=1,
            configurations=[
                {
                    "role": "baseline",
                    "agent_configs": [
                        {
                            "agent_uid": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "harness": "harness",
                            "model": "model",
                            "agent_name": "agent_name",
                            "harness_auth_secret_name": "harness_auth_secret_name",
                        }
                    ],
                    "display_name": "display_name",
                    "harness": "harness",
                    "harness_auth_secret_name": "harness_auth_secret_name",
                    "model": "model",
                    "runner_id": "runner_id",
                }
            ],
            historical_replay_run_uid="historical_replay_run_uid",
            scorer_selection=[0],
            tasks=["7d69fb52-71c5-4e27-914e-8764ee9c5246", "ad8ff7dc-a7d1-4ed6-9f50-650010bb39aa"],
        )
        assert_matches_type(SuiteLaunchRunResponse, suite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_launch_run(self, client: WarpClient) -> None:
        response = client.factories.benchmarks.suites.with_raw_response.launch_run(
            suite_uid="suite_uid",
            uid="uid",
            repetition_count=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suite = response.parse()
        assert_matches_type(SuiteLaunchRunResponse, suite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_launch_run(self, client: WarpClient) -> None:
        with client.factories.benchmarks.suites.with_streaming_response.launch_run(
            suite_uid="suite_uid",
            uid="uid",
            repetition_count=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suite = response.parse()
            assert_matches_type(SuiteLaunchRunResponse, suite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_launch_run(self, client: WarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uid` but received ''"):
            client.factories.benchmarks.suites.with_raw_response.launch_run(
                suite_uid="suite_uid",
                uid="",
                repetition_count=1,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `suite_uid` but received ''"):
            client.factories.benchmarks.suites.with_raw_response.launch_run(
                suite_uid="",
                uid="uid",
                repetition_count=1,
            )


class TestAsyncSuites:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWarpClient) -> None:
        suite = await async_client.factories.benchmarks.suites.create(
            uid="uid",
            agent_uid="agent_uid",
            factory_agent_type="factory_agent_type",
            name="name",
            suite_uid="uid",
        )
        assert_matches_type(SuiteCreateResponse, suite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWarpClient) -> None:
        suite = await async_client.factories.benchmarks.suites.create(
            uid="uid",
            agent_uid="agent_uid",
            factory_agent_type="factory_agent_type",
            name="name",
            suite_uid="uid",
            description="description",
            tasks=[
                {
                    "prompt": "prompt",
                    "success_criteria": "success_criteria",
                    "title": "title",
                    "labels": {"foo": "string"},
                    "source_run_id": "source_run_id",
                    "starting_repo_refs": [
                        {
                            "code_forge": "code_forge",
                            "owner": "owner",
                            "repo": "repo",
                            "ref": "ref",
                        }
                    ],
                    "tags": ["string"],
                    "uid": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        )
        assert_matches_type(SuiteCreateResponse, suite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.factories.benchmarks.suites.with_raw_response.create(
            uid="uid",
            agent_uid="agent_uid",
            factory_agent_type="factory_agent_type",
            name="name",
            suite_uid="uid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suite = await response.parse()
        assert_matches_type(SuiteCreateResponse, suite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWarpClient) -> None:
        async with async_client.factories.benchmarks.suites.with_streaming_response.create(
            uid="uid",
            agent_uid="agent_uid",
            factory_agent_type="factory_agent_type",
            name="name",
            suite_uid="uid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suite = await response.parse()
            assert_matches_type(SuiteCreateResponse, suite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncWarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uid` but received ''"):
            await async_client.factories.benchmarks.suites.with_raw_response.create(
                uid="",
                agent_uid="agent_uid",
                factory_agent_type="factory_agent_type",
                name="name",
                suite_uid="uid",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWarpClient) -> None:
        suite = await async_client.factories.benchmarks.suites.list(
            uid="uid",
        )
        assert_matches_type(AsyncBenchmarkSuitesCursorPage[SuiteListResponse], suite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWarpClient) -> None:
        suite = await async_client.factories.benchmarks.suites.list(
            uid="uid",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(AsyncBenchmarkSuitesCursorPage[SuiteListResponse], suite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.factories.benchmarks.suites.with_raw_response.list(
            uid="uid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suite = await response.parse()
        assert_matches_type(AsyncBenchmarkSuitesCursorPage[SuiteListResponse], suite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWarpClient) -> None:
        async with async_client.factories.benchmarks.suites.with_streaming_response.list(
            uid="uid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suite = await response.parse()
            assert_matches_type(AsyncBenchmarkSuitesCursorPage[SuiteListResponse], suite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncWarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uid` but received ''"):
            await async_client.factories.benchmarks.suites.with_raw_response.list(
                uid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncWarpClient) -> None:
        suite = await async_client.factories.benchmarks.suites.get(
            suite_uid="suite_uid",
            uid="uid",
        )
        assert_matches_type(SuiteGetResponse, suite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.factories.benchmarks.suites.with_raw_response.get(
            suite_uid="suite_uid",
            uid="uid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suite = await response.parse()
        assert_matches_type(SuiteGetResponse, suite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncWarpClient) -> None:
        async with async_client.factories.benchmarks.suites.with_streaming_response.get(
            suite_uid="suite_uid",
            uid="uid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suite = await response.parse()
            assert_matches_type(SuiteGetResponse, suite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncWarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uid` but received ''"):
            await async_client.factories.benchmarks.suites.with_raw_response.get(
                suite_uid="suite_uid",
                uid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `suite_uid` but received ''"):
            await async_client.factories.benchmarks.suites.with_raw_response.get(
                suite_uid="",
                uid="uid",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_launch_run(self, async_client: AsyncWarpClient) -> None:
        suite = await async_client.factories.benchmarks.suites.launch_run(
            suite_uid="suite_uid",
            uid="uid",
            repetition_count=1,
        )
        assert_matches_type(SuiteLaunchRunResponse, suite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_launch_run_with_all_params(self, async_client: AsyncWarpClient) -> None:
        suite = await async_client.factories.benchmarks.suites.launch_run(
            suite_uid="suite_uid",
            uid="uid",
            repetition_count=1,
            configurations=[
                {
                    "role": "baseline",
                    "agent_configs": [
                        {
                            "agent_uid": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "harness": "harness",
                            "model": "model",
                            "agent_name": "agent_name",
                            "harness_auth_secret_name": "harness_auth_secret_name",
                        }
                    ],
                    "display_name": "display_name",
                    "harness": "harness",
                    "harness_auth_secret_name": "harness_auth_secret_name",
                    "model": "model",
                    "runner_id": "runner_id",
                }
            ],
            historical_replay_run_uid="historical_replay_run_uid",
            scorer_selection=[0],
            tasks=["7d69fb52-71c5-4e27-914e-8764ee9c5246", "ad8ff7dc-a7d1-4ed6-9f50-650010bb39aa"],
        )
        assert_matches_type(SuiteLaunchRunResponse, suite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_launch_run(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.factories.benchmarks.suites.with_raw_response.launch_run(
            suite_uid="suite_uid",
            uid="uid",
            repetition_count=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suite = await response.parse()
        assert_matches_type(SuiteLaunchRunResponse, suite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_launch_run(self, async_client: AsyncWarpClient) -> None:
        async with async_client.factories.benchmarks.suites.with_streaming_response.launch_run(
            suite_uid="suite_uid",
            uid="uid",
            repetition_count=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suite = await response.parse()
            assert_matches_type(SuiteLaunchRunResponse, suite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_launch_run(self, async_client: AsyncWarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uid` but received ''"):
            await async_client.factories.benchmarks.suites.with_raw_response.launch_run(
                suite_uid="suite_uid",
                uid="",
                repetition_count=1,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `suite_uid` but received ''"):
            await async_client.factories.benchmarks.suites.with_raw_response.launch_run(
                suite_uid="",
                uid="uid",
                repetition_count=1,
            )
