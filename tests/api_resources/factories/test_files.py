# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from warp_platform_sdk import WarpClient, AsyncWarpClient
from warp_platform_sdk.types.factories import FileValidateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate(self, client: WarpClient) -> None:
        file = client.factories.files.validate(
            files=[
                {
                    "content": "content",
                    "path": "factory.yaml",
                }
            ],
        )
        assert_matches_type(FileValidateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_validate(self, client: WarpClient) -> None:
        response = client.factories.files.with_raw_response.validate(
            files=[
                {
                    "content": "content",
                    "path": "factory.yaml",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileValidateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_validate(self, client: WarpClient) -> None:
        with client.factories.files.with_streaming_response.validate(
            files=[
                {
                    "content": "content",
                    "path": "factory.yaml",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileValidateResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate(self, async_client: AsyncWarpClient) -> None:
        file = await async_client.factories.files.validate(
            files=[
                {
                    "content": "content",
                    "path": "factory.yaml",
                }
            ],
        )
        assert_matches_type(FileValidateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.factories.files.with_raw_response.validate(
            files=[
                {
                    "content": "content",
                    "path": "factory.yaml",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileValidateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncWarpClient) -> None:
        async with async_client.factories.files.with_streaming_response.validate(
            files=[
                {
                    "content": "content",
                    "path": "factory.yaml",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileValidateResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True
