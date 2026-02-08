# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from .runs import (
    RunsResource,
    AsyncRunsResource,
    RunsResourceWithRawResponse,
    AsyncRunsResourceWithRawResponse,
    RunsResourceWithStreamingResponse,
    AsyncRunsResourceWithStreamingResponse,
)
from ...types import agent_run_params, agent_list_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .schedules import (
    SchedulesResource,
    AsyncSchedulesResource,
    SchedulesResourceWithRawResponse,
    AsyncSchedulesResourceWithRawResponse,
    SchedulesResourceWithStreamingResponse,
    AsyncSchedulesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.agent_run_response import AgentRunResponse
from ...types.agent_list_response import AgentListResponse
from ...types.ambient_agent_config_param import AmbientAgentConfigParam

__all__ = ["AgentResource", "AsyncAgentResource"]


class AgentResource(SyncAPIResource):
    @cached_property
    def runs(self) -> RunsResource:
        return RunsResource(self._client)

    @cached_property
    def schedules(self) -> SchedulesResource:
        return SchedulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#with_streaming_response
        """
        return AgentResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        refresh: bool | Omit = omit,
        repo: str | Omit = omit,
        sort_by: Literal["name", "last_run"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentListResponse:
        """
        Retrieve a list of available agents (skills) that can be used to run tasks.
        Agents are discovered from environments or a specific repository.

        Args:
          refresh: When true, clears the agent list cache before fetching. Use this to force a
              refresh of the available agents.

          repo: Optional repository specification to list agents from (format: "owner/repo"). If
              not provided, lists agents from all accessible environments.

          sort_by: Sort order for the returned agents.

              - "name": Sort alphabetically by name (default)
              - "last_run": Sort by most recently used

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/agent",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "refresh": refresh,
                        "repo": repo,
                        "sort_by": sort_by,
                    },
                    agent_list_params.AgentListParams,
                ),
            ),
            cast_to=AgentListResponse,
        )

    def run(
        self,
        *,
        config: AmbientAgentConfigParam | Omit = omit,
        conversation_id: str | Omit = omit,
        images: Iterable[agent_run_params.Image] | Omit = omit,
        prompt: str | Omit = omit,
        skill: str | Omit = omit,
        team: bool | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRunResponse:
        """Spawn an cloud agent with a prompt and optional configuration.

        The agent will be
        queued for execution and assigned a unique run ID.

        Args:
          config: Configuration for an cloud agent run

          conversation_id: Optional conversation ID to continue an existing conversation. If provided, the
              agent will continue from where the previous run left off.

          images: Optional images to include with the prompt (max 5). Images are uploaded to cloud
              storage and made available to the agent.

          prompt: The prompt/instruction for the agent to execute. Required unless a skill is
              specified via the skill field or config.skill_spec.

          skill:
              Skill specification to use as the base prompt for the agent. Supported formats:

              - "repo:skill_name" - Simple name in specific repo
              - "repo:skill_path" - Full path in specific repo
              - "org/repo:skill_name" - Simple name with org and repo
              - "org/repo:skill_path" - Full path with org and repo When provided, this takes
                precedence over config.skill_spec.

          team: Whether to create a team-owned run. Defaults to true for users on a single team.

          title: Custom title for the run (auto-generated if not provided)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/agent/run",
            body=maybe_transform(
                {
                    "config": config,
                    "conversation_id": conversation_id,
                    "images": images,
                    "prompt": prompt,
                    "skill": skill,
                    "team": team,
                    "title": title,
                },
                agent_run_params.AgentRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRunResponse,
        )


class AsyncAgentResource(AsyncAPIResource):
    @cached_property
    def runs(self) -> AsyncRunsResource:
        return AsyncRunsResource(self._client)

    @cached_property
    def schedules(self) -> AsyncSchedulesResource:
        return AsyncSchedulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#with_streaming_response
        """
        return AsyncAgentResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        refresh: bool | Omit = omit,
        repo: str | Omit = omit,
        sort_by: Literal["name", "last_run"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentListResponse:
        """
        Retrieve a list of available agents (skills) that can be used to run tasks.
        Agents are discovered from environments or a specific repository.

        Args:
          refresh: When true, clears the agent list cache before fetching. Use this to force a
              refresh of the available agents.

          repo: Optional repository specification to list agents from (format: "owner/repo"). If
              not provided, lists agents from all accessible environments.

          sort_by: Sort order for the returned agents.

              - "name": Sort alphabetically by name (default)
              - "last_run": Sort by most recently used

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/agent",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "refresh": refresh,
                        "repo": repo,
                        "sort_by": sort_by,
                    },
                    agent_list_params.AgentListParams,
                ),
            ),
            cast_to=AgentListResponse,
        )

    async def run(
        self,
        *,
        config: AmbientAgentConfigParam | Omit = omit,
        conversation_id: str | Omit = omit,
        images: Iterable[agent_run_params.Image] | Omit = omit,
        prompt: str | Omit = omit,
        skill: str | Omit = omit,
        team: bool | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRunResponse:
        """Spawn an cloud agent with a prompt and optional configuration.

        The agent will be
        queued for execution and assigned a unique run ID.

        Args:
          config: Configuration for an cloud agent run

          conversation_id: Optional conversation ID to continue an existing conversation. If provided, the
              agent will continue from where the previous run left off.

          images: Optional images to include with the prompt (max 5). Images are uploaded to cloud
              storage and made available to the agent.

          prompt: The prompt/instruction for the agent to execute. Required unless a skill is
              specified via the skill field or config.skill_spec.

          skill:
              Skill specification to use as the base prompt for the agent. Supported formats:

              - "repo:skill_name" - Simple name in specific repo
              - "repo:skill_path" - Full path in specific repo
              - "org/repo:skill_name" - Simple name with org and repo
              - "org/repo:skill_path" - Full path with org and repo When provided, this takes
                precedence over config.skill_spec.

          team: Whether to create a team-owned run. Defaults to true for users on a single team.

          title: Custom title for the run (auto-generated if not provided)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/agent/run",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "conversation_id": conversation_id,
                    "images": images,
                    "prompt": prompt,
                    "skill": skill,
                    "team": team,
                    "title": title,
                },
                agent_run_params.AgentRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRunResponse,
        )


class AgentResourceWithRawResponse:
    def __init__(self, agent: AgentResource) -> None:
        self._agent = agent

        self.list = to_raw_response_wrapper(
            agent.list,
        )
        self.run = to_raw_response_wrapper(
            agent.run,
        )

    @cached_property
    def runs(self) -> RunsResourceWithRawResponse:
        return RunsResourceWithRawResponse(self._agent.runs)

    @cached_property
    def schedules(self) -> SchedulesResourceWithRawResponse:
        return SchedulesResourceWithRawResponse(self._agent.schedules)


class AsyncAgentResourceWithRawResponse:
    def __init__(self, agent: AsyncAgentResource) -> None:
        self._agent = agent

        self.list = async_to_raw_response_wrapper(
            agent.list,
        )
        self.run = async_to_raw_response_wrapper(
            agent.run,
        )

    @cached_property
    def runs(self) -> AsyncRunsResourceWithRawResponse:
        return AsyncRunsResourceWithRawResponse(self._agent.runs)

    @cached_property
    def schedules(self) -> AsyncSchedulesResourceWithRawResponse:
        return AsyncSchedulesResourceWithRawResponse(self._agent.schedules)


class AgentResourceWithStreamingResponse:
    def __init__(self, agent: AgentResource) -> None:
        self._agent = agent

        self.list = to_streamed_response_wrapper(
            agent.list,
        )
        self.run = to_streamed_response_wrapper(
            agent.run,
        )

    @cached_property
    def runs(self) -> RunsResourceWithStreamingResponse:
        return RunsResourceWithStreamingResponse(self._agent.runs)

    @cached_property
    def schedules(self) -> SchedulesResourceWithStreamingResponse:
        return SchedulesResourceWithStreamingResponse(self._agent.schedules)


class AsyncAgentResourceWithStreamingResponse:
    def __init__(self, agent: AsyncAgentResource) -> None:
        self._agent = agent

        self.list = async_to_streamed_response_wrapper(
            agent.list,
        )
        self.run = async_to_streamed_response_wrapper(
            agent.run,
        )

    @cached_property
    def runs(self) -> AsyncRunsResourceWithStreamingResponse:
        return AsyncRunsResourceWithStreamingResponse(self._agent.runs)

    @cached_property
    def schedules(self) -> AsyncSchedulesResourceWithStreamingResponse:
        return AsyncSchedulesResourceWithStreamingResponse(self._agent.schedules)
