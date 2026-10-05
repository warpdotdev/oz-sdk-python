# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from warp_platform_sdk import WarpClient, AsyncWarpClient
from warp_platform_sdk.types import Factory
from warp_platform_sdk.pagination import SyncFactoriesCursorPage, AsyncFactoriesCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFactories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: WarpClient) -> None:
        factory = client.factories.list()
        assert_matches_type(SyncFactoriesCursorPage[Factory], factory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: WarpClient) -> None:
        factory = client.factories.list(
            cursor="cursor",
            limit=1,
            search="search",
            query_team_uid="team_uid",
            team_uid="X-Warp-Team-Uid",
        )
        assert_matches_type(SyncFactoriesCursorPage[Factory], factory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: WarpClient) -> None:
        response = client.factories.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        factory = response.parse()
        assert_matches_type(SyncFactoriesCursorPage[Factory], factory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: WarpClient) -> None:
        with client.factories.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            factory = response.parse()
            assert_matches_type(SyncFactoriesCursorPage[Factory], factory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: WarpClient) -> None:
        factory = client.factories.get(
            "uid",
        )
        assert_matches_type(Factory, factory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: WarpClient) -> None:
        response = client.factories.with_raw_response.get(
            "uid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        factory = response.parse()
        assert_matches_type(Factory, factory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: WarpClient) -> None:
        with client.factories.with_streaming_response.get(
            "uid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            factory = response.parse()
            assert_matches_type(Factory, factory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: WarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uid` but received ''"):
            client.factories.with_raw_response.get(
                "",
            )


class TestAsyncFactories:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWarpClient) -> None:
        factory = await async_client.factories.list()
        assert_matches_type(AsyncFactoriesCursorPage[Factory], factory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWarpClient) -> None:
        factory = await async_client.factories.list(
            cursor="cursor",
            limit=1,
            search="search",
            query_team_uid="team_uid",
            team_uid="X-Warp-Team-Uid",
        )
        assert_matches_type(AsyncFactoriesCursorPage[Factory], factory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.factories.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        factory = await response.parse()
        assert_matches_type(AsyncFactoriesCursorPage[Factory], factory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWarpClient) -> None:
        async with async_client.factories.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            factory = await response.parse()
            assert_matches_type(AsyncFactoriesCursorPage[Factory], factory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncWarpClient) -> None:
        factory = await async_client.factories.get(
            "uid",
        )
        assert_matches_type(Factory, factory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.factories.with_raw_response.get(
            "uid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        factory = await response.parse()
        assert_matches_type(Factory, factory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncWarpClient) -> None:
        async with async_client.factories.with_streaming_response.get(
            "uid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            factory = await response.parse()
            assert_matches_type(Factory, factory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncWarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uid` but received ''"):
            await async_client.factories.with_raw_response.get(
                "",
            )
