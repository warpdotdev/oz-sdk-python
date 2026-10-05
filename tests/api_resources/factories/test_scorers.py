# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from warp_platform_sdk import WarpClient, AsyncWarpClient
from warp_platform_sdk._utils import parse_datetime
from warp_platform_sdk.pagination import SyncScorerResultsCursorPage, AsyncScorerResultsCursorPage
from warp_platform_sdk.types.factories import (
    ScorerListResponse,
    ScorerCreateResponse,
    ScorerListResultsResponse,
    ScorerListResultReasonsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScorers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: WarpClient) -> None:
        scorer = client.factories.scorers.create(
            allowed_classifications=[
                {
                    "score": 0,
                    "value": "x",
                }
            ],
            factory_uid="x",
            model_id="x",
            name="x",
            scope_mode="all_agents",
            scoring_prompt="x",
            threshold=0,
        )
        assert_matches_type(ScorerCreateResponse, scorer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: WarpClient) -> None:
        scorer = client.factories.scorers.create(
            allowed_classifications=[
                {
                    "score": 0,
                    "value": "x",
                    "description": "description",
                }
            ],
            factory_uid="x",
            model_id="x",
            name="x",
            scope_mode="all_agents",
            scoring_prompt="x",
            threshold=0,
            agent_config={
                "default_runner_uid": "default_runner_uid",
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
                "secrets": [{"name": "name"}],
            },
            agent_uids=["string"],
            agents=[
                {
                    "uid": "uid",
                    "include_descendants": True,
                }
            ],
            description="description",
            sampling_rate=0,
            self_improvement_enabled=True,
        )
        assert_matches_type(ScorerCreateResponse, scorer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: WarpClient) -> None:
        response = client.factories.scorers.with_raw_response.create(
            allowed_classifications=[
                {
                    "score": 0,
                    "value": "x",
                }
            ],
            factory_uid="x",
            model_id="x",
            name="x",
            scope_mode="all_agents",
            scoring_prompt="x",
            threshold=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scorer = response.parse()
        assert_matches_type(ScorerCreateResponse, scorer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: WarpClient) -> None:
        with client.factories.scorers.with_streaming_response.create(
            allowed_classifications=[
                {
                    "score": 0,
                    "value": "x",
                }
            ],
            factory_uid="x",
            model_id="x",
            name="x",
            scope_mode="all_agents",
            scoring_prompt="x",
            threshold=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scorer = response.parse()
            assert_matches_type(ScorerCreateResponse, scorer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: WarpClient) -> None:
        scorer = client.factories.scorers.list()
        assert_matches_type(ScorerListResponse, scorer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: WarpClient) -> None:
        scorer = client.factories.scorers.list(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            factory_uid="factory_uid",
            include_managed=True,
            recent_outcomes_limit=0,
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            team_uid="X-Warp-Team-Uid",
        )
        assert_matches_type(ScorerListResponse, scorer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: WarpClient) -> None:
        response = client.factories.scorers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scorer = response.parse()
        assert_matches_type(ScorerListResponse, scorer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: WarpClient) -> None:
        with client.factories.scorers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scorer = response.parse()
            assert_matches_type(ScorerListResponse, scorer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_result_reasons(self, client: WarpClient) -> None:
        scorer = client.factories.scorers.list_result_reasons(
            scorer_id=0,
            run_id=["string"],
        )
        assert_matches_type(ScorerListResultReasonsResponse, scorer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_result_reasons_with_all_params(self, client: WarpClient) -> None:
        scorer = client.factories.scorers.list_result_reasons(
            scorer_id=0,
            run_id=["string"],
            team_uid="X-Warp-Team-Uid",
        )
        assert_matches_type(ScorerListResultReasonsResponse, scorer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_result_reasons(self, client: WarpClient) -> None:
        response = client.factories.scorers.with_raw_response.list_result_reasons(
            scorer_id=0,
            run_id=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scorer = response.parse()
        assert_matches_type(ScorerListResultReasonsResponse, scorer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_result_reasons(self, client: WarpClient) -> None:
        with client.factories.scorers.with_streaming_response.list_result_reasons(
            scorer_id=0,
            run_id=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scorer = response.parse()
            assert_matches_type(ScorerListResultReasonsResponse, scorer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_results(self, client: WarpClient) -> None:
        scorer = client.factories.scorers.list_results(
            scorer_id=0,
        )
        assert_matches_type(SyncScorerResultsCursorPage[ScorerListResultsResponse], scorer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_results_with_all_params(self, client: WarpClient) -> None:
        scorer = client.factories.scorers.list_results(
            scorer_id=0,
            cursor="cursor",
            limit=1,
            team_uid="X-Warp-Team-Uid",
        )
        assert_matches_type(SyncScorerResultsCursorPage[ScorerListResultsResponse], scorer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_results(self, client: WarpClient) -> None:
        response = client.factories.scorers.with_raw_response.list_results(
            scorer_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scorer = response.parse()
        assert_matches_type(SyncScorerResultsCursorPage[ScorerListResultsResponse], scorer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_results(self, client: WarpClient) -> None:
        with client.factories.scorers.with_streaming_response.list_results(
            scorer_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scorer = response.parse()
            assert_matches_type(SyncScorerResultsCursorPage[ScorerListResultsResponse], scorer, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncScorers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWarpClient) -> None:
        scorer = await async_client.factories.scorers.create(
            allowed_classifications=[
                {
                    "score": 0,
                    "value": "x",
                }
            ],
            factory_uid="x",
            model_id="x",
            name="x",
            scope_mode="all_agents",
            scoring_prompt="x",
            threshold=0,
        )
        assert_matches_type(ScorerCreateResponse, scorer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWarpClient) -> None:
        scorer = await async_client.factories.scorers.create(
            allowed_classifications=[
                {
                    "score": 0,
                    "value": "x",
                    "description": "description",
                }
            ],
            factory_uid="x",
            model_id="x",
            name="x",
            scope_mode="all_agents",
            scoring_prompt="x",
            threshold=0,
            agent_config={
                "default_runner_uid": "default_runner_uid",
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
                "secrets": [{"name": "name"}],
            },
            agent_uids=["string"],
            agents=[
                {
                    "uid": "uid",
                    "include_descendants": True,
                }
            ],
            description="description",
            sampling_rate=0,
            self_improvement_enabled=True,
        )
        assert_matches_type(ScorerCreateResponse, scorer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.factories.scorers.with_raw_response.create(
            allowed_classifications=[
                {
                    "score": 0,
                    "value": "x",
                }
            ],
            factory_uid="x",
            model_id="x",
            name="x",
            scope_mode="all_agents",
            scoring_prompt="x",
            threshold=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scorer = await response.parse()
        assert_matches_type(ScorerCreateResponse, scorer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWarpClient) -> None:
        async with async_client.factories.scorers.with_streaming_response.create(
            allowed_classifications=[
                {
                    "score": 0,
                    "value": "x",
                }
            ],
            factory_uid="x",
            model_id="x",
            name="x",
            scope_mode="all_agents",
            scoring_prompt="x",
            threshold=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scorer = await response.parse()
            assert_matches_type(ScorerCreateResponse, scorer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWarpClient) -> None:
        scorer = await async_client.factories.scorers.list()
        assert_matches_type(ScorerListResponse, scorer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWarpClient) -> None:
        scorer = await async_client.factories.scorers.list(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            factory_uid="factory_uid",
            include_managed=True,
            recent_outcomes_limit=0,
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            team_uid="X-Warp-Team-Uid",
        )
        assert_matches_type(ScorerListResponse, scorer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.factories.scorers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scorer = await response.parse()
        assert_matches_type(ScorerListResponse, scorer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWarpClient) -> None:
        async with async_client.factories.scorers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scorer = await response.parse()
            assert_matches_type(ScorerListResponse, scorer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_result_reasons(self, async_client: AsyncWarpClient) -> None:
        scorer = await async_client.factories.scorers.list_result_reasons(
            scorer_id=0,
            run_id=["string"],
        )
        assert_matches_type(ScorerListResultReasonsResponse, scorer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_result_reasons_with_all_params(self, async_client: AsyncWarpClient) -> None:
        scorer = await async_client.factories.scorers.list_result_reasons(
            scorer_id=0,
            run_id=["string"],
            team_uid="X-Warp-Team-Uid",
        )
        assert_matches_type(ScorerListResultReasonsResponse, scorer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_result_reasons(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.factories.scorers.with_raw_response.list_result_reasons(
            scorer_id=0,
            run_id=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scorer = await response.parse()
        assert_matches_type(ScorerListResultReasonsResponse, scorer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_result_reasons(self, async_client: AsyncWarpClient) -> None:
        async with async_client.factories.scorers.with_streaming_response.list_result_reasons(
            scorer_id=0,
            run_id=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scorer = await response.parse()
            assert_matches_type(ScorerListResultReasonsResponse, scorer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_results(self, async_client: AsyncWarpClient) -> None:
        scorer = await async_client.factories.scorers.list_results(
            scorer_id=0,
        )
        assert_matches_type(AsyncScorerResultsCursorPage[ScorerListResultsResponse], scorer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_results_with_all_params(self, async_client: AsyncWarpClient) -> None:
        scorer = await async_client.factories.scorers.list_results(
            scorer_id=0,
            cursor="cursor",
            limit=1,
            team_uid="X-Warp-Team-Uid",
        )
        assert_matches_type(AsyncScorerResultsCursorPage[ScorerListResultsResponse], scorer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_results(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.factories.scorers.with_raw_response.list_results(
            scorer_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scorer = await response.parse()
        assert_matches_type(AsyncScorerResultsCursorPage[ScorerListResultsResponse], scorer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_results(self, async_client: AsyncWarpClient) -> None:
        async with async_client.factories.scorers.with_streaming_response.list_results(
            scorer_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scorer = await response.parse()
            assert_matches_type(AsyncScorerResultsCursorPage[ScorerListResultsResponse], scorer, path=["response"])

        assert cast(Any, response.is_closed) is True
