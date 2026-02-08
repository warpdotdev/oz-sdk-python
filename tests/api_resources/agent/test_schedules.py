# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from oz_agent_sdk import OzAPI, AsyncOzAPI
from oz_agent_sdk.types.agent import (
    ScheduledAgentItem,
    ScheduleListResponse,
    ScheduleDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSchedules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: OzAPI) -> None:
        schedule = client.agent.schedules.create(
            cron_schedule="0 9 * * *",
            name="Daily Code Review",
            prompt="Review open pull requests and provide feedback",
        )
        assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: OzAPI) -> None:
        schedule = client.agent.schedules.create(
            cron_schedule="0 9 * * *",
            name="Daily Code Review",
            prompt="Review open pull requests and provide feedback",
            agent_config={
                "base_prompt": "base_prompt",
                "computer_use_enabled": True,
                "environment_id": "environment_id",
                "mcp_servers": {
                    "foo": {
                        "args": ["string"],
                        "command": "command",
                        "env": {"foo": "string"},
                        "headers": {"foo": "string"},
                        "url": "https://example.com",
                        "warp_id": "warp_id",
                    }
                },
                "model_id": "model_id",
                "name": "name",
                "skill_spec": "skill_spec",
                "worker_host": "worker_host",
            },
            enabled=True,
            team=True,
        )
        assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: OzAPI) -> None:
        response = client.agent.schedules.with_raw_response.create(
            cron_schedule="0 9 * * *",
            name="Daily Code Review",
            prompt="Review open pull requests and provide feedback",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: OzAPI) -> None:
        with client.agent.schedules.with_streaming_response.create(
            cron_schedule="0 9 * * *",
            name="Daily Code Review",
            prompt="Review open pull requests and provide feedback",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: OzAPI) -> None:
        schedule = client.agent.schedules.retrieve(
            "scheduleId",
        )
        assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: OzAPI) -> None:
        response = client.agent.schedules.with_raw_response.retrieve(
            "scheduleId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: OzAPI) -> None:
        with client.agent.schedules.with_streaming_response.retrieve(
            "scheduleId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: OzAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            client.agent.schedules.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: OzAPI) -> None:
        schedule = client.agent.schedules.update(
            schedule_id="scheduleId",
            cron_schedule="cron_schedule",
            enabled=True,
            name="name",
            prompt="prompt",
        )
        assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: OzAPI) -> None:
        schedule = client.agent.schedules.update(
            schedule_id="scheduleId",
            cron_schedule="cron_schedule",
            enabled=True,
            name="name",
            prompt="prompt",
            agent_config={
                "base_prompt": "base_prompt",
                "computer_use_enabled": True,
                "environment_id": "environment_id",
                "mcp_servers": {
                    "foo": {
                        "args": ["string"],
                        "command": "command",
                        "env": {"foo": "string"},
                        "headers": {"foo": "string"},
                        "url": "https://example.com",
                        "warp_id": "warp_id",
                    }
                },
                "model_id": "model_id",
                "name": "name",
                "skill_spec": "skill_spec",
                "worker_host": "worker_host",
            },
        )
        assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: OzAPI) -> None:
        response = client.agent.schedules.with_raw_response.update(
            schedule_id="scheduleId",
            cron_schedule="cron_schedule",
            enabled=True,
            name="name",
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: OzAPI) -> None:
        with client.agent.schedules.with_streaming_response.update(
            schedule_id="scheduleId",
            cron_schedule="cron_schedule",
            enabled=True,
            name="name",
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: OzAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            client.agent.schedules.with_raw_response.update(
                schedule_id="",
                cron_schedule="cron_schedule",
                enabled=True,
                name="name",
                prompt="prompt",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: OzAPI) -> None:
        schedule = client.agent.schedules.list()
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OzAPI) -> None:
        response = client.agent.schedules.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OzAPI) -> None:
        with client.agent.schedules.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleListResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: OzAPI) -> None:
        schedule = client.agent.schedules.delete(
            "scheduleId",
        )
        assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: OzAPI) -> None:
        response = client.agent.schedules.with_raw_response.delete(
            "scheduleId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: OzAPI) -> None:
        with client.agent.schedules.with_streaming_response.delete(
            "scheduleId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: OzAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            client.agent.schedules.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_pause(self, client: OzAPI) -> None:
        schedule = client.agent.schedules.pause(
            "scheduleId",
        )
        assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_pause(self, client: OzAPI) -> None:
        response = client.agent.schedules.with_raw_response.pause(
            "scheduleId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_pause(self, client: OzAPI) -> None:
        with client.agent.schedules.with_streaming_response.pause(
            "scheduleId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_pause(self, client: OzAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            client.agent.schedules.with_raw_response.pause(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_resume(self, client: OzAPI) -> None:
        schedule = client.agent.schedules.resume(
            "scheduleId",
        )
        assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_resume(self, client: OzAPI) -> None:
        response = client.agent.schedules.with_raw_response.resume(
            "scheduleId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_resume(self, client: OzAPI) -> None:
        with client.agent.schedules.with_streaming_response.resume(
            "scheduleId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_resume(self, client: OzAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            client.agent.schedules.with_raw_response.resume(
                "",
            )


class TestAsyncSchedules:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncOzAPI) -> None:
        schedule = await async_client.agent.schedules.create(
            cron_schedule="0 9 * * *",
            name="Daily Code Review",
            prompt="Review open pull requests and provide feedback",
        )
        assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOzAPI) -> None:
        schedule = await async_client.agent.schedules.create(
            cron_schedule="0 9 * * *",
            name="Daily Code Review",
            prompt="Review open pull requests and provide feedback",
            agent_config={
                "base_prompt": "base_prompt",
                "computer_use_enabled": True,
                "environment_id": "environment_id",
                "mcp_servers": {
                    "foo": {
                        "args": ["string"],
                        "command": "command",
                        "env": {"foo": "string"},
                        "headers": {"foo": "string"},
                        "url": "https://example.com",
                        "warp_id": "warp_id",
                    }
                },
                "model_id": "model_id",
                "name": "name",
                "skill_spec": "skill_spec",
                "worker_host": "worker_host",
            },
            enabled=True,
            team=True,
        )
        assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOzAPI) -> None:
        response = await async_client.agent.schedules.with_raw_response.create(
            cron_schedule="0 9 * * *",
            name="Daily Code Review",
            prompt="Review open pull requests and provide feedback",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOzAPI) -> None:
        async with async_client.agent.schedules.with_streaming_response.create(
            cron_schedule="0 9 * * *",
            name="Daily Code Review",
            prompt="Review open pull requests and provide feedback",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOzAPI) -> None:
        schedule = await async_client.agent.schedules.retrieve(
            "scheduleId",
        )
        assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOzAPI) -> None:
        response = await async_client.agent.schedules.with_raw_response.retrieve(
            "scheduleId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOzAPI) -> None:
        async with async_client.agent.schedules.with_streaming_response.retrieve(
            "scheduleId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOzAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            await async_client.agent.schedules.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncOzAPI) -> None:
        schedule = await async_client.agent.schedules.update(
            schedule_id="scheduleId",
            cron_schedule="cron_schedule",
            enabled=True,
            name="name",
            prompt="prompt",
        )
        assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOzAPI) -> None:
        schedule = await async_client.agent.schedules.update(
            schedule_id="scheduleId",
            cron_schedule="cron_schedule",
            enabled=True,
            name="name",
            prompt="prompt",
            agent_config={
                "base_prompt": "base_prompt",
                "computer_use_enabled": True,
                "environment_id": "environment_id",
                "mcp_servers": {
                    "foo": {
                        "args": ["string"],
                        "command": "command",
                        "env": {"foo": "string"},
                        "headers": {"foo": "string"},
                        "url": "https://example.com",
                        "warp_id": "warp_id",
                    }
                },
                "model_id": "model_id",
                "name": "name",
                "skill_spec": "skill_spec",
                "worker_host": "worker_host",
            },
        )
        assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOzAPI) -> None:
        response = await async_client.agent.schedules.with_raw_response.update(
            schedule_id="scheduleId",
            cron_schedule="cron_schedule",
            enabled=True,
            name="name",
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOzAPI) -> None:
        async with async_client.agent.schedules.with_streaming_response.update(
            schedule_id="scheduleId",
            cron_schedule="cron_schedule",
            enabled=True,
            name="name",
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncOzAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            await async_client.agent.schedules.with_raw_response.update(
                schedule_id="",
                cron_schedule="cron_schedule",
                enabled=True,
                name="name",
                prompt="prompt",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOzAPI) -> None:
        schedule = await async_client.agent.schedules.list()
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOzAPI) -> None:
        response = await async_client.agent.schedules.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOzAPI) -> None:
        async with async_client.agent.schedules.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleListResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncOzAPI) -> None:
        schedule = await async_client.agent.schedules.delete(
            "scheduleId",
        )
        assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOzAPI) -> None:
        response = await async_client.agent.schedules.with_raw_response.delete(
            "scheduleId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOzAPI) -> None:
        async with async_client.agent.schedules.with_streaming_response.delete(
            "scheduleId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOzAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            await async_client.agent.schedules.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_pause(self, async_client: AsyncOzAPI) -> None:
        schedule = await async_client.agent.schedules.pause(
            "scheduleId",
        )
        assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_pause(self, async_client: AsyncOzAPI) -> None:
        response = await async_client.agent.schedules.with_raw_response.pause(
            "scheduleId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_pause(self, async_client: AsyncOzAPI) -> None:
        async with async_client.agent.schedules.with_streaming_response.pause(
            "scheduleId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_pause(self, async_client: AsyncOzAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            await async_client.agent.schedules.with_raw_response.pause(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_resume(self, async_client: AsyncOzAPI) -> None:
        schedule = await async_client.agent.schedules.resume(
            "scheduleId",
        )
        assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_resume(self, async_client: AsyncOzAPI) -> None:
        response = await async_client.agent.schedules.with_raw_response.resume(
            "scheduleId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_resume(self, async_client: AsyncOzAPI) -> None:
        async with async_client.agent.schedules.with_streaming_response.resume(
            "scheduleId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduledAgentItem, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_resume(self, async_client: AsyncOzAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            await async_client.agent.schedules.with_raw_response.resume(
                "",
            )
