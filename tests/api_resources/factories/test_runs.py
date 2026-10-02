# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from oz_agent_sdk import WarpClient, AsyncWarpClient
from oz_agent_sdk.types.factories import RunCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: WarpClient) -> None:
        run = client.factories.runs.create(
            uid="uid",
            prompt="prompt",
        )
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: WarpClient) -> None:
        run = client.factories.runs.create(
            uid="uid",
            prompt="prompt",
            ticket_ref="ticket_ref",
            ticket_url="ticket_url",
            title="title",
        )
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: WarpClient) -> None:
        response = client.factories.runs.with_raw_response.create(
            uid="uid",
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: WarpClient) -> None:
        with client.factories.runs.with_streaming_response.create(
            uid="uid",
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunCreateResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: WarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uid` but received ''"):
            client.factories.runs.with_raw_response.create(
                uid="",
                prompt="prompt",
            )


class TestAsyncRuns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWarpClient) -> None:
        run = await async_client.factories.runs.create(
            uid="uid",
            prompt="prompt",
        )
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWarpClient) -> None:
        run = await async_client.factories.runs.create(
            uid="uid",
            prompt="prompt",
            ticket_ref="ticket_ref",
            ticket_url="ticket_url",
            title="title",
        )
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.factories.runs.with_raw_response.create(
            uid="uid",
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWarpClient) -> None:
        async with async_client.factories.runs.with_streaming_response.create(
            uid="uid",
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunCreateResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncWarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uid` but received ''"):
            await async_client.factories.runs.with_raw_response.create(
                uid="",
                prompt="prompt",
            )
