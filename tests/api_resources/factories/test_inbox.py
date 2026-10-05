# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from warp_platform_sdk import WarpClient, AsyncWarpClient
from warp_platform_sdk.pagination import SyncFactoryInboxCursorPage, AsyncFactoryInboxCursorPage
from warp_platform_sdk.types.factories import (
    InboxItem,
    InboxMarkReadResponse,
    InboxMarkUnreadResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInbox:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: WarpClient) -> None:
        inbox = client.factories.inbox.list()
        assert_matches_type(SyncFactoryInboxCursorPage[InboxItem], inbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: WarpClient) -> None:
        inbox = client.factories.inbox.list(
            cursor="cursor",
            factory_uid="factory_uid",
            limit=1,
            recipient_uid="recipient_uid",
            scope="mine",
            team_uid="X-Warp-Team-Uid",
        )
        assert_matches_type(SyncFactoryInboxCursorPage[InboxItem], inbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: WarpClient) -> None:
        response = client.factories.inbox.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = response.parse()
        assert_matches_type(SyncFactoryInboxCursorPage[InboxItem], inbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: WarpClient) -> None:
        with client.factories.inbox.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = response.parse()
            assert_matches_type(SyncFactoryInboxCursorPage[InboxItem], inbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_mark_read(self, client: WarpClient) -> None:
        inbox = client.factories.inbox.mark_read(
            notification_uids=["string"],
        )
        assert_matches_type(InboxMarkReadResponse, inbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_mark_read(self, client: WarpClient) -> None:
        response = client.factories.inbox.with_raw_response.mark_read(
            notification_uids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = response.parse()
        assert_matches_type(InboxMarkReadResponse, inbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_mark_read(self, client: WarpClient) -> None:
        with client.factories.inbox.with_streaming_response.mark_read(
            notification_uids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = response.parse()
            assert_matches_type(InboxMarkReadResponse, inbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_mark_unread(self, client: WarpClient) -> None:
        inbox = client.factories.inbox.mark_unread(
            notification_uids=["string"],
        )
        assert_matches_type(InboxMarkUnreadResponse, inbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_mark_unread(self, client: WarpClient) -> None:
        response = client.factories.inbox.with_raw_response.mark_unread(
            notification_uids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = response.parse()
        assert_matches_type(InboxMarkUnreadResponse, inbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_mark_unread(self, client: WarpClient) -> None:
        with client.factories.inbox.with_streaming_response.mark_unread(
            notification_uids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = response.parse()
            assert_matches_type(InboxMarkUnreadResponse, inbox, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInbox:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWarpClient) -> None:
        inbox = await async_client.factories.inbox.list()
        assert_matches_type(AsyncFactoryInboxCursorPage[InboxItem], inbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWarpClient) -> None:
        inbox = await async_client.factories.inbox.list(
            cursor="cursor",
            factory_uid="factory_uid",
            limit=1,
            recipient_uid="recipient_uid",
            scope="mine",
            team_uid="X-Warp-Team-Uid",
        )
        assert_matches_type(AsyncFactoryInboxCursorPage[InboxItem], inbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.factories.inbox.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = await response.parse()
        assert_matches_type(AsyncFactoryInboxCursorPage[InboxItem], inbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWarpClient) -> None:
        async with async_client.factories.inbox.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = await response.parse()
            assert_matches_type(AsyncFactoryInboxCursorPage[InboxItem], inbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_mark_read(self, async_client: AsyncWarpClient) -> None:
        inbox = await async_client.factories.inbox.mark_read(
            notification_uids=["string"],
        )
        assert_matches_type(InboxMarkReadResponse, inbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_mark_read(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.factories.inbox.with_raw_response.mark_read(
            notification_uids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = await response.parse()
        assert_matches_type(InboxMarkReadResponse, inbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_mark_read(self, async_client: AsyncWarpClient) -> None:
        async with async_client.factories.inbox.with_streaming_response.mark_read(
            notification_uids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = await response.parse()
            assert_matches_type(InboxMarkReadResponse, inbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_mark_unread(self, async_client: AsyncWarpClient) -> None:
        inbox = await async_client.factories.inbox.mark_unread(
            notification_uids=["string"],
        )
        assert_matches_type(InboxMarkUnreadResponse, inbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_mark_unread(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.factories.inbox.with_raw_response.mark_unread(
            notification_uids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = await response.parse()
        assert_matches_type(InboxMarkUnreadResponse, inbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_mark_unread(self, async_client: AsyncWarpClient) -> None:
        async with async_client.factories.inbox.with_streaming_response.mark_unread(
            notification_uids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = await response.parse()
            assert_matches_type(InboxMarkUnreadResponse, inbox, path=["response"])

        assert cast(Any, response.is_closed) is True
