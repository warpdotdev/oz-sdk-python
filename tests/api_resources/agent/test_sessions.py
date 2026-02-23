# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from oz_agent_sdk import OzAPI, AsyncOzAPI
from oz_agent_sdk.types.agent import SessionCheckRedirectResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check_redirect(self, client: OzAPI) -> None:
        session = client.agent.sessions.check_redirect(
            "sessionUuid",
        )
        assert_matches_type(SessionCheckRedirectResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_check_redirect(self, client: OzAPI) -> None:
        response = client.agent.sessions.with_raw_response.check_redirect(
            "sessionUuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionCheckRedirectResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_check_redirect(self, client: OzAPI) -> None:
        with client.agent.sessions.with_streaming_response.check_redirect(
            "sessionUuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionCheckRedirectResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_check_redirect(self, client: OzAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_uuid` but received ''"):
            client.agent.sessions.with_raw_response.check_redirect(
                "",
            )


class TestAsyncSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check_redirect(self, async_client: AsyncOzAPI) -> None:
        session = await async_client.agent.sessions.check_redirect(
            "sessionUuid",
        )
        assert_matches_type(SessionCheckRedirectResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_check_redirect(self, async_client: AsyncOzAPI) -> None:
        response = await async_client.agent.sessions.with_raw_response.check_redirect(
            "sessionUuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionCheckRedirectResponse, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_check_redirect(self, async_client: AsyncOzAPI) -> None:
        async with async_client.agent.sessions.with_streaming_response.check_redirect(
            "sessionUuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionCheckRedirectResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_check_redirect(self, async_client: AsyncOzAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_uuid` but received ''"):
            await async_client.agent.sessions.with_raw_response.check_redirect(
                "",
            )
