# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from warp_platform_sdk import WarpClient, AsyncWarpClient
from warp_platform_sdk.pagination import SyncRunsCursorPage, AsyncRunsCursorPage
from warp_platform_sdk.types.factories.benchmarks import (
    RunGetResponse,
    RunListResponse,
    RunGetResultsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: WarpClient) -> None:
        run = client.factories.benchmarks.runs.list(
            uid="uid",
        )
        assert_matches_type(SyncRunsCursorPage[RunListResponse], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: WarpClient) -> None:
        run = client.factories.benchmarks.runs.list(
            uid="uid",
            cursor="cursor",
            limit=1,
            state=["pending"],
            suite_uid="suite_uid",
        )
        assert_matches_type(SyncRunsCursorPage[RunListResponse], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: WarpClient) -> None:
        response = client.factories.benchmarks.runs.with_raw_response.list(
            uid="uid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(SyncRunsCursorPage[RunListResponse], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: WarpClient) -> None:
        with client.factories.benchmarks.runs.with_streaming_response.list(
            uid="uid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(SyncRunsCursorPage[RunListResponse], run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: WarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uid` but received ''"):
            client.factories.benchmarks.runs.with_raw_response.list(
                uid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: WarpClient) -> None:
        run = client.factories.benchmarks.runs.get(
            run_uid="run_uid",
            uid="uid",
        )
        assert_matches_type(RunGetResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: WarpClient) -> None:
        response = client.factories.benchmarks.runs.with_raw_response.get(
            run_uid="run_uid",
            uid="uid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunGetResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: WarpClient) -> None:
        with client.factories.benchmarks.runs.with_streaming_response.get(
            run_uid="run_uid",
            uid="uid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunGetResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: WarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uid` but received ''"):
            client.factories.benchmarks.runs.with_raw_response.get(
                run_uid="run_uid",
                uid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_uid` but received ''"):
            client.factories.benchmarks.runs.with_raw_response.get(
                run_uid="",
                uid="uid",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_results(self, client: WarpClient) -> None:
        run = client.factories.benchmarks.runs.get_results(
            run_uid="run_uid",
            uid="uid",
        )
        assert_matches_type(RunGetResultsResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_results(self, client: WarpClient) -> None:
        response = client.factories.benchmarks.runs.with_raw_response.get_results(
            run_uid="run_uid",
            uid="uid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunGetResultsResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_results(self, client: WarpClient) -> None:
        with client.factories.benchmarks.runs.with_streaming_response.get_results(
            run_uid="run_uid",
            uid="uid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunGetResultsResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_results(self, client: WarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uid` but received ''"):
            client.factories.benchmarks.runs.with_raw_response.get_results(
                run_uid="run_uid",
                uid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_uid` but received ''"):
            client.factories.benchmarks.runs.with_raw_response.get_results(
                run_uid="",
                uid="uid",
            )


class TestAsyncRuns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWarpClient) -> None:
        run = await async_client.factories.benchmarks.runs.list(
            uid="uid",
        )
        assert_matches_type(AsyncRunsCursorPage[RunListResponse], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWarpClient) -> None:
        run = await async_client.factories.benchmarks.runs.list(
            uid="uid",
            cursor="cursor",
            limit=1,
            state=["pending"],
            suite_uid="suite_uid",
        )
        assert_matches_type(AsyncRunsCursorPage[RunListResponse], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.factories.benchmarks.runs.with_raw_response.list(
            uid="uid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(AsyncRunsCursorPage[RunListResponse], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWarpClient) -> None:
        async with async_client.factories.benchmarks.runs.with_streaming_response.list(
            uid="uid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(AsyncRunsCursorPage[RunListResponse], run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncWarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uid` but received ''"):
            await async_client.factories.benchmarks.runs.with_raw_response.list(
                uid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncWarpClient) -> None:
        run = await async_client.factories.benchmarks.runs.get(
            run_uid="run_uid",
            uid="uid",
        )
        assert_matches_type(RunGetResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.factories.benchmarks.runs.with_raw_response.get(
            run_uid="run_uid",
            uid="uid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunGetResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncWarpClient) -> None:
        async with async_client.factories.benchmarks.runs.with_streaming_response.get(
            run_uid="run_uid",
            uid="uid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunGetResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncWarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uid` but received ''"):
            await async_client.factories.benchmarks.runs.with_raw_response.get(
                run_uid="run_uid",
                uid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_uid` but received ''"):
            await async_client.factories.benchmarks.runs.with_raw_response.get(
                run_uid="",
                uid="uid",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_results(self, async_client: AsyncWarpClient) -> None:
        run = await async_client.factories.benchmarks.runs.get_results(
            run_uid="run_uid",
            uid="uid",
        )
        assert_matches_type(RunGetResultsResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_results(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.factories.benchmarks.runs.with_raw_response.get_results(
            run_uid="run_uid",
            uid="uid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunGetResultsResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_results(self, async_client: AsyncWarpClient) -> None:
        async with async_client.factories.benchmarks.runs.with_streaming_response.get_results(
            run_uid="run_uid",
            uid="uid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunGetResultsResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_results(self, async_client: AsyncWarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uid` but received ''"):
            await async_client.factories.benchmarks.runs.with_raw_response.get_results(
                run_uid="run_uid",
                uid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_uid` but received ''"):
            await async_client.factories.benchmarks.runs.with_raw_response.get_results(
                run_uid="",
                uid="uid",
            )
