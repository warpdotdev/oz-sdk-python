# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from warp_platform_sdk import WarpClient, AsyncWarpClient
from warp_platform_sdk.types import NetworkingGetEgressRangesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNetworking:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_egress_ranges(self, client: WarpClient) -> None:
        networking = client.networking.get_egress_ranges()
        assert_matches_type(NetworkingGetEgressRangesResponse, networking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_egress_ranges_with_all_params(self, client: WarpClient) -> None:
        networking = client.networking.get_egress_ranges(
            team_uid="X-Warp-Team-Uid",
        )
        assert_matches_type(NetworkingGetEgressRangesResponse, networking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_egress_ranges(self, client: WarpClient) -> None:
        response = client.networking.with_raw_response.get_egress_ranges()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        networking = response.parse()
        assert_matches_type(NetworkingGetEgressRangesResponse, networking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_egress_ranges(self, client: WarpClient) -> None:
        with client.networking.with_streaming_response.get_egress_ranges() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            networking = response.parse()
            assert_matches_type(NetworkingGetEgressRangesResponse, networking, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNetworking:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_egress_ranges(self, async_client: AsyncWarpClient) -> None:
        networking = await async_client.networking.get_egress_ranges()
        assert_matches_type(NetworkingGetEgressRangesResponse, networking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_egress_ranges_with_all_params(self, async_client: AsyncWarpClient) -> None:
        networking = await async_client.networking.get_egress_ranges(
            team_uid="X-Warp-Team-Uid",
        )
        assert_matches_type(NetworkingGetEgressRangesResponse, networking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_egress_ranges(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.networking.with_raw_response.get_egress_ranges()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        networking = await response.parse()
        assert_matches_type(NetworkingGetEgressRangesResponse, networking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_egress_ranges(self, async_client: AsyncWarpClient) -> None:
        async with async_client.networking.with_streaming_response.get_egress_ranges() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            networking = await response.parse()
            assert_matches_type(NetworkingGetEgressRangesResponse, networking, path=["response"])

        assert cast(Any, response.is_closed) is True
