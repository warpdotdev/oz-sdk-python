# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from tests.utils import assert_matches_type
from warp_platform_sdk import WarpClient, AsyncWarpClient
from warp_platform_sdk._utils import parse_datetime
from warp_platform_sdk._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from warp_platform_sdk.pagination import SyncRunsCursorPage, AsyncRunsCursorPage
from warp_platform_sdk.types.agent import (
    RunItem,
    RunGetTimelineResponse,
    RunSubmitFollowupResponse,
    RunGetConversationResponse,
    RunGetHarnessUsageResponse,
    RunListHandoffAttachmentsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: WarpClient) -> None:
        run = client.agent.runs.retrieve(
            "runId",
        )
        assert_matches_type(RunItem, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: WarpClient) -> None:
        response = client.agent.runs.with_raw_response.retrieve(
            "runId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunItem, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: WarpClient) -> None:
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
    def test_path_params_retrieve(self, client: WarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.agent.runs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: WarpClient) -> None:
        run = client.agent.runs.list()
        assert_matches_type(SyncRunsCursorPage[RunItem], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: WarpClient) -> None:
        run = client.agent.runs.list(
            ancestor_run_id="ancestor_run_id",
            artifact_type="PLAN",
            automation_id="automation_id",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            creator="creator",
            cursor="cursor",
            environment_id="environment_id",
            execution_location="LOCAL",
            executor="executor",
            factory_only=True,
            factory_uid="string",
            limit=1,
            metadata={"foo": "string"},
            model_id="model_id",
            name="name",
            q="q",
            schedule_id="schedule_id",
            skill="skill",
            skill_spec="skill_spec",
            sort_by="updated_at",
            sort_order="asc",
            source=["LINEAR"],
            state=["QUEUED"],
            task_status=["running"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            team_uid="X-Warp-Team-Uid",
        )
        assert_matches_type(SyncRunsCursorPage[RunItem], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: WarpClient) -> None:
        response = client.agent.runs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(SyncRunsCursorPage[RunItem], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: WarpClient) -> None:
        with client.agent.runs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(SyncRunsCursorPage[RunItem], run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel(self, client: WarpClient) -> None:
        run = client.agent.runs.cancel(
            "runId",
        )
        assert_matches_type(str, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: WarpClient) -> None:
        response = client.agent.runs.with_raw_response.cancel(
            "runId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(str, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: WarpClient) -> None:
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
    def test_path_params_cancel(self, client: WarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.agent.runs.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_conversation(self, client: WarpClient) -> None:
        run = client.agent.runs.get_conversation(
            "runId",
        )
        assert_matches_type(RunGetConversationResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_conversation(self, client: WarpClient) -> None:
        response = client.agent.runs.with_raw_response.get_conversation(
            "runId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunGetConversationResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_conversation(self, client: WarpClient) -> None:
        with client.agent.runs.with_streaming_response.get_conversation(
            "runId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunGetConversationResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_conversation(self, client: WarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.agent.runs.with_raw_response.get_conversation(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_harness_usage(self, client: WarpClient) -> None:
        run = client.agent.runs.get_harness_usage(
            "runId",
        )
        assert_matches_type(RunGetHarnessUsageResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_harness_usage(self, client: WarpClient) -> None:
        response = client.agent.runs.with_raw_response.get_harness_usage(
            "runId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunGetHarnessUsageResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_harness_usage(self, client: WarpClient) -> None:
        with client.agent.runs.with_streaming_response.get_harness_usage(
            "runId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunGetHarnessUsageResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_harness_usage(self, client: WarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.agent.runs.with_raw_response.get_harness_usage(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_timeline(self, client: WarpClient) -> None:
        run = client.agent.runs.get_timeline(
            "runId",
        )
        assert_matches_type(RunGetTimelineResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_timeline(self, client: WarpClient) -> None:
        response = client.agent.runs.with_raw_response.get_timeline(
            "runId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunGetTimelineResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_timeline(self, client: WarpClient) -> None:
        with client.agent.runs.with_streaming_response.get_timeline(
            "runId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunGetTimelineResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_timeline(self, client: WarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.agent.runs.with_raw_response.get_timeline(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_transcript(self, client: WarpClient, respx_mock: MockRouter) -> None:
        respx_mock.get("/agent/runs/runId/transcript").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        run = client.agent.runs.get_transcript(
            "runId",
        )
        assert run.is_closed
        assert run.json() == {"foo": "bar"}
        assert cast(Any, run.is_closed) is True
        assert isinstance(run, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_transcript(self, client: WarpClient, respx_mock: MockRouter) -> None:
        respx_mock.get("/agent/runs/runId/transcript").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        run = client.agent.runs.with_raw_response.get_transcript(
            "runId",
        )

        assert run.is_closed is True
        assert run.http_request.headers.get("X-Stainless-Lang") == "python"
        assert run.json() == {"foo": "bar"}
        assert isinstance(run, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_transcript(self, client: WarpClient, respx_mock: MockRouter) -> None:
        respx_mock.get("/agent/runs/runId/transcript").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.agent.runs.with_streaming_response.get_transcript(
            "runId",
        ) as run:
            assert not run.is_closed
            assert run.http_request.headers.get("X-Stainless-Lang") == "python"

            assert run.json() == {"foo": "bar"}
            assert cast(Any, run.is_closed) is True
            assert isinstance(run, StreamedBinaryAPIResponse)

        assert cast(Any, run.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get_transcript(self, client: WarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.agent.runs.with_raw_response.get_transcript(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_interrupt(self, client: WarpClient) -> None:
        run = client.agent.runs.interrupt(
            "runId",
        )
        assert_matches_type(object, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_interrupt(self, client: WarpClient) -> None:
        response = client.agent.runs.with_raw_response.interrupt(
            "runId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(object, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_interrupt(self, client: WarpClient) -> None:
        with client.agent.runs.with_streaming_response.interrupt(
            "runId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(object, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_interrupt(self, client: WarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.agent.runs.with_raw_response.interrupt(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_handoff_attachments(self, client: WarpClient) -> None:
        run = client.agent.runs.list_handoff_attachments(
            "runId",
        )
        assert_matches_type(RunListHandoffAttachmentsResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_handoff_attachments(self, client: WarpClient) -> None:
        response = client.agent.runs.with_raw_response.list_handoff_attachments(
            "runId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunListHandoffAttachmentsResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_handoff_attachments(self, client: WarpClient) -> None:
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
    def test_path_params_list_handoff_attachments(self, client: WarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.agent.runs.with_raw_response.list_handoff_attachments(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_followup(self, client: WarpClient) -> None:
        run = client.agent.runs.submit_followup(
            run_id="runId",
        )
        assert_matches_type(RunSubmitFollowupResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_followup_with_all_params(self, client: WarpClient) -> None:
        run = client.agent.runs.submit_followup(
            run_id="runId",
            attachments=[
                {
                    "attachment_id": "attachment_id",
                    "file_name": "file_name",
                }
            ],
            message="message",
            mode="normal",
        )
        assert_matches_type(RunSubmitFollowupResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit_followup(self, client: WarpClient) -> None:
        response = client.agent.runs.with_raw_response.submit_followup(
            run_id="runId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunSubmitFollowupResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit_followup(self, client: WarpClient) -> None:
        with client.agent.runs.with_streaming_response.submit_followup(
            run_id="runId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunSubmitFollowupResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_submit_followup(self, client: WarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.agent.runs.with_raw_response.submit_followup(
                run_id="",
            )


class TestAsyncRuns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWarpClient) -> None:
        run = await async_client.agent.runs.retrieve(
            "runId",
        )
        assert_matches_type(RunItem, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.agent.runs.with_raw_response.retrieve(
            "runId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunItem, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWarpClient) -> None:
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
    async def test_path_params_retrieve(self, async_client: AsyncWarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.agent.runs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWarpClient) -> None:
        run = await async_client.agent.runs.list()
        assert_matches_type(AsyncRunsCursorPage[RunItem], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWarpClient) -> None:
        run = await async_client.agent.runs.list(
            ancestor_run_id="ancestor_run_id",
            artifact_type="PLAN",
            automation_id="automation_id",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            creator="creator",
            cursor="cursor",
            environment_id="environment_id",
            execution_location="LOCAL",
            executor="executor",
            factory_only=True,
            factory_uid="string",
            limit=1,
            metadata={"foo": "string"},
            model_id="model_id",
            name="name",
            q="q",
            schedule_id="schedule_id",
            skill="skill",
            skill_spec="skill_spec",
            sort_by="updated_at",
            sort_order="asc",
            source=["LINEAR"],
            state=["QUEUED"],
            task_status=["running"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            team_uid="X-Warp-Team-Uid",
        )
        assert_matches_type(AsyncRunsCursorPage[RunItem], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.agent.runs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(AsyncRunsCursorPage[RunItem], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWarpClient) -> None:
        async with async_client.agent.runs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(AsyncRunsCursorPage[RunItem], run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncWarpClient) -> None:
        run = await async_client.agent.runs.cancel(
            "runId",
        )
        assert_matches_type(str, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.agent.runs.with_raw_response.cancel(
            "runId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(str, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncWarpClient) -> None:
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
    async def test_path_params_cancel(self, async_client: AsyncWarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.agent.runs.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_conversation(self, async_client: AsyncWarpClient) -> None:
        run = await async_client.agent.runs.get_conversation(
            "runId",
        )
        assert_matches_type(RunGetConversationResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_conversation(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.agent.runs.with_raw_response.get_conversation(
            "runId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunGetConversationResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_conversation(self, async_client: AsyncWarpClient) -> None:
        async with async_client.agent.runs.with_streaming_response.get_conversation(
            "runId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunGetConversationResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_conversation(self, async_client: AsyncWarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.agent.runs.with_raw_response.get_conversation(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_harness_usage(self, async_client: AsyncWarpClient) -> None:
        run = await async_client.agent.runs.get_harness_usage(
            "runId",
        )
        assert_matches_type(RunGetHarnessUsageResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_harness_usage(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.agent.runs.with_raw_response.get_harness_usage(
            "runId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunGetHarnessUsageResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_harness_usage(self, async_client: AsyncWarpClient) -> None:
        async with async_client.agent.runs.with_streaming_response.get_harness_usage(
            "runId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunGetHarnessUsageResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_harness_usage(self, async_client: AsyncWarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.agent.runs.with_raw_response.get_harness_usage(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_timeline(self, async_client: AsyncWarpClient) -> None:
        run = await async_client.agent.runs.get_timeline(
            "runId",
        )
        assert_matches_type(RunGetTimelineResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_timeline(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.agent.runs.with_raw_response.get_timeline(
            "runId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunGetTimelineResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_timeline(self, async_client: AsyncWarpClient) -> None:
        async with async_client.agent.runs.with_streaming_response.get_timeline(
            "runId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunGetTimelineResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_timeline(self, async_client: AsyncWarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.agent.runs.with_raw_response.get_timeline(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_transcript(self, async_client: AsyncWarpClient, respx_mock: MockRouter) -> None:
        respx_mock.get("/agent/runs/runId/transcript").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        run = await async_client.agent.runs.get_transcript(
            "runId",
        )
        assert run.is_closed
        assert await run.json() == {"foo": "bar"}
        assert cast(Any, run.is_closed) is True
        assert isinstance(run, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_transcript(self, async_client: AsyncWarpClient, respx_mock: MockRouter) -> None:
        respx_mock.get("/agent/runs/runId/transcript").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        run = await async_client.agent.runs.with_raw_response.get_transcript(
            "runId",
        )

        assert run.is_closed is True
        assert run.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await run.json() == {"foo": "bar"}
        assert isinstance(run, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_transcript(
        self, async_client: AsyncWarpClient, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/agent/runs/runId/transcript").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.agent.runs.with_streaming_response.get_transcript(
            "runId",
        ) as run:
            assert not run.is_closed
            assert run.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await run.json() == {"foo": "bar"}
            assert cast(Any, run.is_closed) is True
            assert isinstance(run, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, run.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get_transcript(self, async_client: AsyncWarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.agent.runs.with_raw_response.get_transcript(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_interrupt(self, async_client: AsyncWarpClient) -> None:
        run = await async_client.agent.runs.interrupt(
            "runId",
        )
        assert_matches_type(object, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_interrupt(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.agent.runs.with_raw_response.interrupt(
            "runId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(object, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_interrupt(self, async_client: AsyncWarpClient) -> None:
        async with async_client.agent.runs.with_streaming_response.interrupt(
            "runId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(object, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_interrupt(self, async_client: AsyncWarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.agent.runs.with_raw_response.interrupt(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_handoff_attachments(self, async_client: AsyncWarpClient) -> None:
        run = await async_client.agent.runs.list_handoff_attachments(
            "runId",
        )
        assert_matches_type(RunListHandoffAttachmentsResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_handoff_attachments(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.agent.runs.with_raw_response.list_handoff_attachments(
            "runId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunListHandoffAttachmentsResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_handoff_attachments(self, async_client: AsyncWarpClient) -> None:
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
    async def test_path_params_list_handoff_attachments(self, async_client: AsyncWarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.agent.runs.with_raw_response.list_handoff_attachments(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_followup(self, async_client: AsyncWarpClient) -> None:
        run = await async_client.agent.runs.submit_followup(
            run_id="runId",
        )
        assert_matches_type(RunSubmitFollowupResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_followup_with_all_params(self, async_client: AsyncWarpClient) -> None:
        run = await async_client.agent.runs.submit_followup(
            run_id="runId",
            attachments=[
                {
                    "attachment_id": "attachment_id",
                    "file_name": "file_name",
                }
            ],
            message="message",
            mode="normal",
        )
        assert_matches_type(RunSubmitFollowupResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit_followup(self, async_client: AsyncWarpClient) -> None:
        response = await async_client.agent.runs.with_raw_response.submit_followup(
            run_id="runId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunSubmitFollowupResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit_followup(self, async_client: AsyncWarpClient) -> None:
        async with async_client.agent.runs.with_streaming_response.submit_followup(
            run_id="runId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunSubmitFollowupResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_submit_followup(self, async_client: AsyncWarpClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.agent.runs.with_raw_response.submit_followup(
                run_id="",
            )
