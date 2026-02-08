# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.agent import schedule_create_params, schedule_update_params
from ..._base_client import make_request_options
from ...types.agent.scheduled_agent_item import ScheduledAgentItem
from ...types.ambient_agent_config_param import AmbientAgentConfigParam
from ...types.agent.schedule_list_response import ScheduleListResponse
from ...types.agent.schedule_delete_response import ScheduleDeleteResponse

__all__ = ["SchedulesResource", "AsyncSchedulesResource"]


class SchedulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SchedulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SchedulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SchedulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#with_streaming_response
        """
        return SchedulesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        cron_schedule: str,
        name: str,
        prompt: str,
        agent_config: AmbientAgentConfigParam | Omit = omit,
        enabled: bool | Omit = omit,
        team: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledAgentItem:
        """Create a new scheduled agent that runs on a cron schedule.

        The agent will be
        triggered automatically based on the cron expression.

        Args:
          cron_schedule: Cron expression defining when the agent runs (e.g., "0 9 \\** \\** \\**" for daily at
              9am UTC)

          name: Human-readable name for the schedule

          prompt: The prompt/instruction for the agent to execute

          agent_config: Configuration for an cloud agent run

          enabled: Whether the schedule should be active immediately

          team: Whether to create a team-owned schedule. Defaults to true for users on a single
              team.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/agent/schedules",
            body=maybe_transform(
                {
                    "cron_schedule": cron_schedule,
                    "name": name,
                    "prompt": prompt,
                    "agent_config": agent_config,
                    "enabled": enabled,
                    "team": team,
                },
                schedule_create_params.ScheduleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledAgentItem,
        )

    def retrieve(
        self,
        schedule_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledAgentItem:
        """
        Retrieve detailed information about a specific scheduled agent, including its
        configuration, history, and next scheduled run time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return self._get(
            f"/agent/schedules/{schedule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledAgentItem,
        )

    def update(
        self,
        schedule_id: str,
        *,
        cron_schedule: str,
        enabled: bool,
        name: str,
        prompt: str,
        agent_config: AmbientAgentConfigParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledAgentItem:
        """Update an existing scheduled agent's configuration.

        All fields except
        agent_config are required.

        Args:
          cron_schedule: Cron expression defining when the agent runs

          enabled: Whether the schedule should be active

          name: Human-readable name for the schedule

          prompt: The prompt/instruction for the agent to execute

          agent_config: Configuration for an cloud agent run

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return self._put(
            f"/agent/schedules/{schedule_id}",
            body=maybe_transform(
                {
                    "cron_schedule": cron_schedule,
                    "enabled": enabled,
                    "name": name,
                    "prompt": prompt,
                    "agent_config": agent_config,
                },
                schedule_update_params.ScheduleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledAgentItem,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleListResponse:
        """Retrieve all scheduled agents accessible to the authenticated user.

        Results are
        sorted alphabetically by name.
        """
        return self._get(
            "/agent/schedules",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleListResponse,
        )

    def delete(
        self,
        schedule_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleDeleteResponse:
        """Delete a scheduled agent.

        This will stop all future scheduled runs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return self._delete(
            f"/agent/schedules/{schedule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleDeleteResponse,
        )

    def pause(
        self,
        schedule_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledAgentItem:
        """Pause a scheduled agent.

        The agent will not run until resumed. This sets the
        enabled flag to false.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return self._post(
            f"/agent/schedules/{schedule_id}/pause",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledAgentItem,
        )

    def resume(
        self,
        schedule_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledAgentItem:
        """Resume a paused scheduled agent.

        The agent will start running according to its
        cron schedule. This sets the enabled flag to true.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return self._post(
            f"/agent/schedules/{schedule_id}/resume",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledAgentItem,
        )


class AsyncSchedulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSchedulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSchedulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSchedulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#with_streaming_response
        """
        return AsyncSchedulesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        cron_schedule: str,
        name: str,
        prompt: str,
        agent_config: AmbientAgentConfigParam | Omit = omit,
        enabled: bool | Omit = omit,
        team: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledAgentItem:
        """Create a new scheduled agent that runs on a cron schedule.

        The agent will be
        triggered automatically based on the cron expression.

        Args:
          cron_schedule: Cron expression defining when the agent runs (e.g., "0 9 \\** \\** \\**" for daily at
              9am UTC)

          name: Human-readable name for the schedule

          prompt: The prompt/instruction for the agent to execute

          agent_config: Configuration for an cloud agent run

          enabled: Whether the schedule should be active immediately

          team: Whether to create a team-owned schedule. Defaults to true for users on a single
              team.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/agent/schedules",
            body=await async_maybe_transform(
                {
                    "cron_schedule": cron_schedule,
                    "name": name,
                    "prompt": prompt,
                    "agent_config": agent_config,
                    "enabled": enabled,
                    "team": team,
                },
                schedule_create_params.ScheduleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledAgentItem,
        )

    async def retrieve(
        self,
        schedule_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledAgentItem:
        """
        Retrieve detailed information about a specific scheduled agent, including its
        configuration, history, and next scheduled run time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return await self._get(
            f"/agent/schedules/{schedule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledAgentItem,
        )

    async def update(
        self,
        schedule_id: str,
        *,
        cron_schedule: str,
        enabled: bool,
        name: str,
        prompt: str,
        agent_config: AmbientAgentConfigParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledAgentItem:
        """Update an existing scheduled agent's configuration.

        All fields except
        agent_config are required.

        Args:
          cron_schedule: Cron expression defining when the agent runs

          enabled: Whether the schedule should be active

          name: Human-readable name for the schedule

          prompt: The prompt/instruction for the agent to execute

          agent_config: Configuration for an cloud agent run

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return await self._put(
            f"/agent/schedules/{schedule_id}",
            body=await async_maybe_transform(
                {
                    "cron_schedule": cron_schedule,
                    "enabled": enabled,
                    "name": name,
                    "prompt": prompt,
                    "agent_config": agent_config,
                },
                schedule_update_params.ScheduleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledAgentItem,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleListResponse:
        """Retrieve all scheduled agents accessible to the authenticated user.

        Results are
        sorted alphabetically by name.
        """
        return await self._get(
            "/agent/schedules",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleListResponse,
        )

    async def delete(
        self,
        schedule_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleDeleteResponse:
        """Delete a scheduled agent.

        This will stop all future scheduled runs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return await self._delete(
            f"/agent/schedules/{schedule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleDeleteResponse,
        )

    async def pause(
        self,
        schedule_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledAgentItem:
        """Pause a scheduled agent.

        The agent will not run until resumed. This sets the
        enabled flag to false.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return await self._post(
            f"/agent/schedules/{schedule_id}/pause",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledAgentItem,
        )

    async def resume(
        self,
        schedule_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledAgentItem:
        """Resume a paused scheduled agent.

        The agent will start running according to its
        cron schedule. This sets the enabled flag to true.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return await self._post(
            f"/agent/schedules/{schedule_id}/resume",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledAgentItem,
        )


class SchedulesResourceWithRawResponse:
    def __init__(self, schedules: SchedulesResource) -> None:
        self._schedules = schedules

        self.create = to_raw_response_wrapper(
            schedules.create,
        )
        self.retrieve = to_raw_response_wrapper(
            schedules.retrieve,
        )
        self.update = to_raw_response_wrapper(
            schedules.update,
        )
        self.list = to_raw_response_wrapper(
            schedules.list,
        )
        self.delete = to_raw_response_wrapper(
            schedules.delete,
        )
        self.pause = to_raw_response_wrapper(
            schedules.pause,
        )
        self.resume = to_raw_response_wrapper(
            schedules.resume,
        )


class AsyncSchedulesResourceWithRawResponse:
    def __init__(self, schedules: AsyncSchedulesResource) -> None:
        self._schedules = schedules

        self.create = async_to_raw_response_wrapper(
            schedules.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            schedules.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            schedules.update,
        )
        self.list = async_to_raw_response_wrapper(
            schedules.list,
        )
        self.delete = async_to_raw_response_wrapper(
            schedules.delete,
        )
        self.pause = async_to_raw_response_wrapper(
            schedules.pause,
        )
        self.resume = async_to_raw_response_wrapper(
            schedules.resume,
        )


class SchedulesResourceWithStreamingResponse:
    def __init__(self, schedules: SchedulesResource) -> None:
        self._schedules = schedules

        self.create = to_streamed_response_wrapper(
            schedules.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            schedules.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            schedules.update,
        )
        self.list = to_streamed_response_wrapper(
            schedules.list,
        )
        self.delete = to_streamed_response_wrapper(
            schedules.delete,
        )
        self.pause = to_streamed_response_wrapper(
            schedules.pause,
        )
        self.resume = to_streamed_response_wrapper(
            schedules.resume,
        )


class AsyncSchedulesResourceWithStreamingResponse:
    def __init__(self, schedules: AsyncSchedulesResource) -> None:
        self._schedules = schedules

        self.create = async_to_streamed_response_wrapper(
            schedules.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            schedules.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            schedules.update,
        )
        self.list = async_to_streamed_response_wrapper(
            schedules.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            schedules.delete,
        )
        self.pause = async_to_streamed_response_wrapper(
            schedules.pause,
        )
        self.resume = async_to_streamed_response_wrapper(
            schedules.resume,
        )
