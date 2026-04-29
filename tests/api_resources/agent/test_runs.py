# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from oz_agent_sdk import OzAPI, AsyncOzAPI
from oz_agent_sdk._utils import parse_datetime
from oz_agent_sdk.pagination import SyncRunsCursorPage, AsyncRunsCursorPage
from oz_agent_sdk.types.agent import (
    RunItem,
    RunListHandoffAttachmentsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: OzAPI) -> None:
        run = client.agent.runs.retrieve(
            "runId",
        )
        assert_matches_type(RunItem, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: OzAPI) -> None:
        response = client.agent.runs.with_raw_response.retrieve(
            "runId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunItem, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: OzAPI) -> None:
        with client.agent.runs.with_streaming_response.retrieve(
            "runId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunItem, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: OzAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.agent.runs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: OzAPI) -> None:
        run = client.agent.runs.list()
        assert_matches_type(SyncRunsCursorPage[RunItem], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: OzAPI) -> None:
        run = client.agent.runs.list(
            ancestor_run_id="ancestor_run_id",
            artifact_type="PLAN",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            creator="creator",
            cursor="cursor",
            environment_id="environment_id",
            execution_location="LOCAL",
            limit=1,
            model_id="model_id",
            name="name",
            q="q",
            schedule_id="schedule_id",
            skill="skill",
            skill_spec="skill_spec",
            sort_by="updated_at",
            sort_order="asc",
            source="LINEAR",
            state=["QUEUED"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncRunsCursorPage[RunItem], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OzAPI) -> None:
        response = client.agent.runs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(SyncRunsCursorPage[RunItem], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OzAPI) -> None:
        with client.agent.runs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(SyncRunsCursorPage[RunItem], run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel(self, client: OzAPI) -> None:
        run = client.agent.runs.cancel(
            "runId",
        )
        assert_matches_type(str, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: OzAPI) -> None:
        response = client.agent.runs.with_raw_response.cancel(
            "runId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(str, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: OzAPI) -> None:
        with client.agent.runs.with_streaming_response.cancel(
            "runId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(str, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: OzAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.agent.runs.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_handoff_attachments(self, client: OzAPI) -> None:
        run = client.agent.runs.list_handoff_attachments(
            "runId",
        )
        assert_matches_type(RunListHandoffAttachmentsResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_handoff_attachments(self, client: OzAPI) -> None:
        response = client.agent.runs.with_raw_response.list_handoff_attachments(
            "runId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunListHandoffAttachmentsResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_handoff_attachments(self, client: OzAPI) -> None:
        with client.agent.runs.with_streaming_response.list_handoff_attachments(
            "runId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunListHandoffAttachmentsResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_handoff_attachments(self, client: OzAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.agent.runs.with_raw_response.list_handoff_attachments(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_followup(self, client: OzAPI) -> None:
        run = client.agent.runs.submit_followup(
            run_id="runId",
            message="message",
        )
        assert_matches_type(object, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit_followup(self, client: OzAPI) -> None:
        response = client.agent.runs.with_raw_response.submit_followup(
            run_id="runId",
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(object, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit_followup(self, client: OzAPI) -> None:
        with client.agent.runs.with_streaming_response.submit_followup(
            run_id="runId",
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(object, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_submit_followup(self, client: OzAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.agent.runs.with_raw_response.submit_followup(
                run_id="",
                message="message",
            )


class TestAsyncRuns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOzAPI) -> None:
        run = await async_client.agent.runs.retrieve(
            "runId",
        )
        assert_matches_type(RunItem, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOzAPI) -> None:
        response = await async_client.agent.runs.with_raw_response.retrieve(
            "runId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunItem, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOzAPI) -> None:
        async with async_client.agent.runs.with_streaming_response.retrieve(
            "runId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunItem, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOzAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.agent.runs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOzAPI) -> None:
        run = await async_client.agent.runs.list()
        assert_matches_type(AsyncRunsCursorPage[RunItem], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOzAPI) -> None:
        run = await async_client.agent.runs.list(
            ancestor_run_id="ancestor_run_id",
            artifact_type="PLAN",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            creator="creator",
            cursor="cursor",
            environment_id="environment_id",
            execution_location="LOCAL",
            limit=1,
            model_id="model_id",
            name="name",
            q="q",
            schedule_id="schedule_id",
            skill="skill",
            skill_spec="skill_spec",
            sort_by="updated_at",
            sort_order="asc",
            source="LINEAR",
            state=["QUEUED"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncRunsCursorPage[RunItem], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOzAPI) -> None:
        response = await async_client.agent.runs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(AsyncRunsCursorPage[RunItem], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOzAPI) -> None:
        async with async_client.agent.runs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(AsyncRunsCursorPage[RunItem], run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncOzAPI) -> None:
        run = await async_client.agent.runs.cancel(
            "runId",
        )
        assert_matches_type(str, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncOzAPI) -> None:
        response = await async_client.agent.runs.with_raw_response.cancel(
            "runId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(str, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncOzAPI) -> None:
        async with async_client.agent.runs.with_streaming_response.cancel(
            "runId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(str, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncOzAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.agent.runs.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_handoff_attachments(self, async_client: AsyncOzAPI) -> None:
        run = await async_client.agent.runs.list_handoff_attachments(
            "runId",
        )
        assert_matches_type(RunListHandoffAttachmentsResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_handoff_attachments(self, async_client: AsyncOzAPI) -> None:
        response = await async_client.agent.runs.with_raw_response.list_handoff_attachments(
            "runId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunListHandoffAttachmentsResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_handoff_attachments(self, async_client: AsyncOzAPI) -> None:
        async with async_client.agent.runs.with_streaming_response.list_handoff_attachments(
            "runId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunListHandoffAttachmentsResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_handoff_attachments(self, async_client: AsyncOzAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.agent.runs.with_raw_response.list_handoff_attachments(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_followup(self, async_client: AsyncOzAPI) -> None:
        run = await async_client.agent.runs.submit_followup(
            run_id="runId",
            message="message",
        )
        assert_matches_type(object, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit_followup(self, async_client: AsyncOzAPI) -> None:
        response = await async_client.agent.runs.with_raw_response.submit_followup(
            run_id="runId",
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(object, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit_followup(self, async_client: AsyncOzAPI) -> None:
        async with async_client.agent.runs.with_streaming_response.submit_followup(
            run_id="runId",
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(object, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_submit_followup(self, async_client: AsyncOzAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.agent.runs.with_raw_response.submit_followup(
                run_id="",
                message="message",
            )
