# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from warp_platform_sdk import WarpClient, AsyncWarpClient
from warp_platform_sdk.types.factories.files import (
    SchemaListResponse,
    SchemaRetrieveResponse,
    SchemaGetDocumentResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSchemas:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: WarpClient) -> None:
        schema = client.factories.files.schemas.retrieve(
            schema_version="schema_version",
        )
        assert_matches_type(SchemaRetrieveResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: WarpClient) -> None:
        schema = client.factories.files.schemas.retrieve(
            schema_version="schema_version",
            if_none_match="If-None-Match",
        )
        assert_matches_type(SchemaRetrieveResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: WarpClient) -> None:
        response = client.factories.files.schemas.with_raw_response.retrieve(
            schema_version="schema_version",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(SchemaRetrieveResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: WarpClient) -> None:
        with client.factories.files.schemas.with_streaming_response.retrieve(
            schema_version="schema_version",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(SchemaRetrieveResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: WarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_version` but received ''"):
            client.factories.files.schemas.with_raw_response.retrieve(
                schema_version="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: WarpClient) -> None:
        schema = client.factories.files.schemas.list()
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: WarpClient) -> None:
        schema = client.factories.files.schemas.list(
            if_none_match="If-None-Match",
        )
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: WarpClient) -> None:
        response = client.factories.files.schemas.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: WarpClient) -> None:
        with client.factories.files.schemas.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(SchemaListResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_document(self, client: WarpClient) -> None:
        schema = client.factories.files.schemas.get_document(
            document="document",
            schema_version="schema_version",
        )
        assert_matches_type(SchemaGetDocumentResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_document(self, client: WarpClient) -> None:
        response = client.factories.files.schemas.with_raw_response.get_document(
            document="document",
            schema_version="schema_version",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(SchemaGetDocumentResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_document(self, client: WarpClient) -> None:
        with client.factories.files.schemas.with_streaming_response.get_document(
            document="document",
            schema_version="schema_version",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(SchemaGetDocumentResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_document(self, client: WarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_version` but received ''"):
            client.factories.files.schemas.with_raw_response.get_document(
                document="document",
                schema_version="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document` but received ''"):
            client.factories.files.schemas.with_raw_response.get_document(
                document="",
                schema_version="schema_version",
            )


class TestAsyncSchemas:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWarpClient) -> None:
        schema = await async_client.factories.files.schemas.retrieve(
            schema_version="schema_version",
        )
        assert_matches_type(SchemaRetrieveResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncWarpClient) -> None:
        schema = await async_client.factories.files.schemas.retrieve(
            schema_version="schema_version",
            if_none_match="If-None-Match",
        )
        assert_matches_type(SchemaRetrieveResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.factories.files.schemas.with_raw_response.retrieve(
            schema_version="schema_version",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(SchemaRetrieveResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWarpClient) -> None:
        async with async_client.factories.files.schemas.with_streaming_response.retrieve(
            schema_version="schema_version",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(SchemaRetrieveResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_version` but received ''"):
            await async_client.factories.files.schemas.with_raw_response.retrieve(
                schema_version="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWarpClient) -> None:
        schema = await async_client.factories.files.schemas.list()
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWarpClient) -> None:
        schema = await async_client.factories.files.schemas.list(
            if_none_match="If-None-Match",
        )
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.factories.files.schemas.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWarpClient) -> None:
        async with async_client.factories.files.schemas.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(SchemaListResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_document(self, async_client: AsyncWarpClient) -> None:
        schema = await async_client.factories.files.schemas.get_document(
            document="document",
            schema_version="schema_version",
        )
        assert_matches_type(SchemaGetDocumentResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_document(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.factories.files.schemas.with_raw_response.get_document(
            document="document",
            schema_version="schema_version",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(SchemaGetDocumentResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_document(self, async_client: AsyncWarpClient) -> None:
        async with async_client.factories.files.schemas.with_streaming_response.get_document(
            document="document",
            schema_version="schema_version",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(SchemaGetDocumentResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_document(self, async_client: AsyncWarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_version` but received ''"):
            await async_client.factories.files.schemas.with_raw_response.get_document(
                document="document",
                schema_version="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document` but received ''"):
            await async_client.factories.files.schemas.with_raw_response.get_document(
                document="",
                schema_version="schema_version",
            )
