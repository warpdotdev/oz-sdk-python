# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.agent import agent_list_params, agent_create_params, agent_update_params
from ..._base_client import make_request_options
from ...types.agent.agent_response import AgentResponse
from ...types.mcp_server_config_param import McpServerConfigParam
from ...types.agent.list_agent_identities_response import ListAgentIdentitiesResponse

__all__ = ["AgentResource", "AsyncAgentResource"]


class AgentResource(SyncAPIResource):
    """Operations for running and managing cloud agents"""

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

    def create(
        self,
        *,
        name: str,
        agent_type: Optional[Literal["FOREMAN", "TRIAGE", "SPEC", "IMPLEMENT", "REVIEW", "VERIFY", "CUSTOM"]]
        | Omit = omit,
        base_harness: Optional[str] | Omit = omit,
        base_model: Optional[str] | Omit = omit,
        default_runner_uid: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        environment_id: Optional[str] | Omit = omit,
        factory_uid: Optional[str] | Omit = omit,
        harness_auth_secrets: agent_create_params.HarnessAuthSecrets | Omit = omit,
        inference_providers: agent_create_params.InferenceProviders | Omit = omit,
        mcp_servers: Dict[str, McpServerConfigParam] | Omit = omit,
        memory: agent_create_params.Memory | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        secrets: Iterable[agent_create_params.Secret] | Omit = omit,
        skills: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
        """Create a new agent for the caller's team.

        Agents can be used as the execution
        principal for team-owned runs.

        Args:
          name: A name for the agent

          agent_type: The well-known type of a named agent. The built-in factory agents use FOREMAN,
              TRIAGE, SPEC, IMPLEMENT, REVIEW, or VERIFY; every other agent is CUSTOM.

          base_harness: Optional default harness for runs executed by this agent.

          base_model: Optional base model for runs executed by this agent.

          default_runner_uid: Optional default runner UID for runs executed by this agent. When set, it
              overrides the selected environment's default runner for runs that do not specify
              their own `runner_id`. The editor must have View permission on the referenced
              runner.

          description: Optional description of the agent

          environment_id: Optional default cloud environment ID for runs executed by this agent. The
              environment must be owned by the same team as the agent.

          factory_uid: Optional UID of the Factory to link this agent to. When omitted, the agent is
              not linked to any factory.

          harness_auth_secrets: Authentication secrets for third-party harnesses. Only the secret for the
              harness specified gets injected into the environment.

          inference_providers: Inference provider settings used for LLM calls.

          mcp_servers: Optional map of MCP server configurations by name to attach to runs executed by
              this agent. Run-level MCP config takes precedence over this agent-level default.

          memory: Memory settings for creating an agent.

          prompt: Optional base prompt for this agent

          secrets: Optional list of secrets associated with the agent. Duplicate names within a
              single request are rejected. Each entry is unioned into the run-time secret
              scope when the agent executes.

          skills:
              Optional list of skill specs to associate with the agent. Format:
              "{owner}/{repo}:{skill_path}" (e.g.,
              "warpdotdev/warp-server:.claude/skills/deploy/SKILL.md"). Each spec is validated
              and normalized at attach time using the team's GitHub credentials; inaccessible
              or malformed specs are rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/agent/identities",
            body=maybe_transform(
                {
                    "name": name,
                    "agent_type": agent_type,
                    "base_harness": base_harness,
                    "base_model": base_model,
                    "default_runner_uid": default_runner_uid,
                    "description": description,
                    "environment_id": environment_id,
                    "factory_uid": factory_uid,
                    "harness_auth_secrets": harness_auth_secrets,
                    "inference_providers": inference_providers,
                    "mcp_servers": mcp_servers,
                    "memory": memory,
                    "prompt": prompt,
                    "secrets": secrets,
                    "skills": skills,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )

    def update(
        self,
        uid: str,
        *,
        agent_type: Optional[Literal["FOREMAN", "TRIAGE", "SPEC", "IMPLEMENT", "REVIEW", "VERIFY", "CUSTOM"]]
        | Omit = omit,
        base_harness: Optional[str] | Omit = omit,
        base_model: Optional[str] | Omit = omit,
        default_runner_uid: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        environment_id: Optional[str] | Omit = omit,
        harness_auth_secrets: Optional[agent_update_params.HarnessAuthSecrets] | Omit = omit,
        inference_providers: Optional[agent_update_params.InferenceProviders] | Omit = omit,
        mcp_servers: Dict[str, McpServerConfigParam] | Omit = omit,
        memory: Optional[agent_update_params.Memory] | Omit = omit,
        name: str | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        secrets: Optional[Iterable[agent_update_params.Secret]] | Omit = omit,
        skills: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
        """
        Update an existing agent.

        Args:
          agent_type: The well-known type of a named agent. The built-in factory agents use FOREMAN,
              TRIAGE, SPEC, IMPLEMENT, REVIEW, or VERIFY; every other agent is CUSTOM.

          base_harness: Replacement default harness. Omit or pass `null` to leave unchanged, or pass an
              empty string to clear.

          base_model: Replacement base model. Omit or pass `null` to leave unchanged, or pass an empty
              string to clear.

          default_runner_uid: Replacement default runner UID. Omit or pass `null` to leave unchanged, or pass
              an empty string to clear. A non-empty value must reference a runner the editor
              can View.

          description: Replacement description. Omit or pass `null` to leave unchanged, or use an empty
              value to clear.

          environment_id: Replacement default cloud environment ID. Omit or pass `null` to leave
              unchanged, or pass an empty string to clear.

          harness_auth_secrets: Authentication secrets for third-party harnesses. Only the secret for the
              harness specified gets injected into the environment.

          inference_providers: Inference provider settings used for LLM calls.

          mcp_servers: Replacement map of MCP server configurations by name. Omit to leave unchanged,
              pass an empty object to clear, or pass a non-empty object to replace. Run-level
              MCP config takes precedence over this agent-level default.

          memory: Memory settings for updating an agent.

          name: The new name for the agent

          prompt: Replacement prompt. Omit or pass `null` to leave unchanged, or use an empty
              value to clear.

          secrets: Replacement list of secrets. Omit to leave unchanged, pass an empty array to
              clear, or pass a non-empty array to replace. Duplicate names are rejected.

          skills: Replacement list of skill specs. Omit to leave unchanged, pass an empty array to
              clear, or pass a non-empty array to replace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return self._put(
            path_template("/agent/identities/{uid}", uid=uid),
            body=maybe_transform(
                {
                    "agent_type": agent_type,
                    "base_harness": base_harness,
                    "base_model": base_model,
                    "default_runner_uid": default_runner_uid,
                    "description": description,
                    "environment_id": environment_id,
                    "harness_auth_secrets": harness_auth_secrets,
                    "inference_providers": inference_providers,
                    "mcp_servers": mcp_servers,
                    "memory": memory,
                    "name": name,
                    "prompt": prompt,
                    "secrets": secrets,
                    "skills": skills,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )

    def list(
        self,
        *,
        factory_uid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListAgentIdentitiesResponse:
        """List all agents for the caller's team.

        Each agent includes an `available` flag
        indicating whether it is within the team's plan limit and may be used for runs.

        Args:
          factory_uid: Optional UID of a Factory to filter by. When provided, only agents linked to
              that factory (and owned by the caller's team) are returned. Ignored unless the
              factory API is enabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/agent/identities",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"factory_uid": factory_uid}, agent_list_params.AgentListParams),
            ),
            cast_to=ListAgentIdentitiesResponse,
        )

    def delete(
        self,
        uid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete an agent.

        All API keys associated with the agent are deleted atomically.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/agent/identities/{uid}", uid=uid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        uid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
        """Retrieve a single agent by its unique identifier.

        The response includes an
        `available` flag indicating whether the agent is within the team's plan limit
        and may be used for runs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return self._get(
            path_template("/agent/identities/{uid}", uid=uid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )


class AsyncAgentResource(AsyncAPIResource):
    """Operations for running and managing cloud agents"""

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

    async def create(
        self,
        *,
        name: str,
        agent_type: Optional[Literal["FOREMAN", "TRIAGE", "SPEC", "IMPLEMENT", "REVIEW", "VERIFY", "CUSTOM"]]
        | Omit = omit,
        base_harness: Optional[str] | Omit = omit,
        base_model: Optional[str] | Omit = omit,
        default_runner_uid: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        environment_id: Optional[str] | Omit = omit,
        factory_uid: Optional[str] | Omit = omit,
        harness_auth_secrets: agent_create_params.HarnessAuthSecrets | Omit = omit,
        inference_providers: agent_create_params.InferenceProviders | Omit = omit,
        mcp_servers: Dict[str, McpServerConfigParam] | Omit = omit,
        memory: agent_create_params.Memory | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        secrets: Iterable[agent_create_params.Secret] | Omit = omit,
        skills: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
        """Create a new agent for the caller's team.

        Agents can be used as the execution
        principal for team-owned runs.

        Args:
          name: A name for the agent

          agent_type: The well-known type of a named agent. The built-in factory agents use FOREMAN,
              TRIAGE, SPEC, IMPLEMENT, REVIEW, or VERIFY; every other agent is CUSTOM.

          base_harness: Optional default harness for runs executed by this agent.

          base_model: Optional base model for runs executed by this agent.

          default_runner_uid: Optional default runner UID for runs executed by this agent. When set, it
              overrides the selected environment's default runner for runs that do not specify
              their own `runner_id`. The editor must have View permission on the referenced
              runner.

          description: Optional description of the agent

          environment_id: Optional default cloud environment ID for runs executed by this agent. The
              environment must be owned by the same team as the agent.

          factory_uid: Optional UID of the Factory to link this agent to. When omitted, the agent is
              not linked to any factory.

          harness_auth_secrets: Authentication secrets for third-party harnesses. Only the secret for the
              harness specified gets injected into the environment.

          inference_providers: Inference provider settings used for LLM calls.

          mcp_servers: Optional map of MCP server configurations by name to attach to runs executed by
              this agent. Run-level MCP config takes precedence over this agent-level default.

          memory: Memory settings for creating an agent.

          prompt: Optional base prompt for this agent

          secrets: Optional list of secrets associated with the agent. Duplicate names within a
              single request are rejected. Each entry is unioned into the run-time secret
              scope when the agent executes.

          skills:
              Optional list of skill specs to associate with the agent. Format:
              "{owner}/{repo}:{skill_path}" (e.g.,
              "warpdotdev/warp-server:.claude/skills/deploy/SKILL.md"). Each spec is validated
              and normalized at attach time using the team's GitHub credentials; inaccessible
              or malformed specs are rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/agent/identities",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "agent_type": agent_type,
                    "base_harness": base_harness,
                    "base_model": base_model,
                    "default_runner_uid": default_runner_uid,
                    "description": description,
                    "environment_id": environment_id,
                    "factory_uid": factory_uid,
                    "harness_auth_secrets": harness_auth_secrets,
                    "inference_providers": inference_providers,
                    "mcp_servers": mcp_servers,
                    "memory": memory,
                    "prompt": prompt,
                    "secrets": secrets,
                    "skills": skills,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )

    async def update(
        self,
        uid: str,
        *,
        agent_type: Optional[Literal["FOREMAN", "TRIAGE", "SPEC", "IMPLEMENT", "REVIEW", "VERIFY", "CUSTOM"]]
        | Omit = omit,
        base_harness: Optional[str] | Omit = omit,
        base_model: Optional[str] | Omit = omit,
        default_runner_uid: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        environment_id: Optional[str] | Omit = omit,
        harness_auth_secrets: Optional[agent_update_params.HarnessAuthSecrets] | Omit = omit,
        inference_providers: Optional[agent_update_params.InferenceProviders] | Omit = omit,
        mcp_servers: Dict[str, McpServerConfigParam] | Omit = omit,
        memory: Optional[agent_update_params.Memory] | Omit = omit,
        name: str | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        secrets: Optional[Iterable[agent_update_params.Secret]] | Omit = omit,
        skills: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
        """
        Update an existing agent.

        Args:
          agent_type: The well-known type of a named agent. The built-in factory agents use FOREMAN,
              TRIAGE, SPEC, IMPLEMENT, REVIEW, or VERIFY; every other agent is CUSTOM.

          base_harness: Replacement default harness. Omit or pass `null` to leave unchanged, or pass an
              empty string to clear.

          base_model: Replacement base model. Omit or pass `null` to leave unchanged, or pass an empty
              string to clear.

          default_runner_uid: Replacement default runner UID. Omit or pass `null` to leave unchanged, or pass
              an empty string to clear. A non-empty value must reference a runner the editor
              can View.

          description: Replacement description. Omit or pass `null` to leave unchanged, or use an empty
              value to clear.

          environment_id: Replacement default cloud environment ID. Omit or pass `null` to leave
              unchanged, or pass an empty string to clear.

          harness_auth_secrets: Authentication secrets for third-party harnesses. Only the secret for the
              harness specified gets injected into the environment.

          inference_providers: Inference provider settings used for LLM calls.

          mcp_servers: Replacement map of MCP server configurations by name. Omit to leave unchanged,
              pass an empty object to clear, or pass a non-empty object to replace. Run-level
              MCP config takes precedence over this agent-level default.

          memory: Memory settings for updating an agent.

          name: The new name for the agent

          prompt: Replacement prompt. Omit or pass `null` to leave unchanged, or use an empty
              value to clear.

          secrets: Replacement list of secrets. Omit to leave unchanged, pass an empty array to
              clear, or pass a non-empty array to replace. Duplicate names are rejected.

          skills: Replacement list of skill specs. Omit to leave unchanged, pass an empty array to
              clear, or pass a non-empty array to replace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return await self._put(
            path_template("/agent/identities/{uid}", uid=uid),
            body=await async_maybe_transform(
                {
                    "agent_type": agent_type,
                    "base_harness": base_harness,
                    "base_model": base_model,
                    "default_runner_uid": default_runner_uid,
                    "description": description,
                    "environment_id": environment_id,
                    "harness_auth_secrets": harness_auth_secrets,
                    "inference_providers": inference_providers,
                    "mcp_servers": mcp_servers,
                    "memory": memory,
                    "name": name,
                    "prompt": prompt,
                    "secrets": secrets,
                    "skills": skills,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )

    async def list(
        self,
        *,
        factory_uid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListAgentIdentitiesResponse:
        """List all agents for the caller's team.

        Each agent includes an `available` flag
        indicating whether it is within the team's plan limit and may be used for runs.

        Args:
          factory_uid: Optional UID of a Factory to filter by. When provided, only agents linked to
              that factory (and owned by the caller's team) are returned. Ignored unless the
              factory API is enabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/agent/identities",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"factory_uid": factory_uid}, agent_list_params.AgentListParams),
            ),
            cast_to=ListAgentIdentitiesResponse,
        )

    async def delete(
        self,
        uid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete an agent.

        All API keys associated with the agent are deleted atomically.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/agent/identities/{uid}", uid=uid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        uid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
        """Retrieve a single agent by its unique identifier.

        The response includes an
        `available` flag indicating whether the agent is within the team's plan limit
        and may be used for runs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return await self._get(
            path_template("/agent/identities/{uid}", uid=uid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )


class AgentResourceWithRawResponse:
    def __init__(self, agent: AgentResource) -> None:
        self._agent = agent

        self.create = to_raw_response_wrapper(
            agent.create,
        )
        self.update = to_raw_response_wrapper(
            agent.update,
        )
        self.list = to_raw_response_wrapper(
            agent.list,
        )
        self.delete = to_raw_response_wrapper(
            agent.delete,
        )
        self.get = to_raw_response_wrapper(
            agent.get,
        )


class AsyncAgentResourceWithRawResponse:
    def __init__(self, agent: AsyncAgentResource) -> None:
        self._agent = agent

        self.create = async_to_raw_response_wrapper(
            agent.create,
        )
        self.update = async_to_raw_response_wrapper(
            agent.update,
        )
        self.list = async_to_raw_response_wrapper(
            agent.list,
        )
        self.delete = async_to_raw_response_wrapper(
            agent.delete,
        )
        self.get = async_to_raw_response_wrapper(
            agent.get,
        )


class AgentResourceWithStreamingResponse:
    def __init__(self, agent: AgentResource) -> None:
        self._agent = agent

        self.create = to_streamed_response_wrapper(
            agent.create,
        )
        self.update = to_streamed_response_wrapper(
            agent.update,
        )
        self.list = to_streamed_response_wrapper(
            agent.list,
        )
        self.delete = to_streamed_response_wrapper(
            agent.delete,
        )
        self.get = to_streamed_response_wrapper(
            agent.get,
        )


class AsyncAgentResourceWithStreamingResponse:
    def __init__(self, agent: AsyncAgentResource) -> None:
        self._agent = agent

        self.create = async_to_streamed_response_wrapper(
            agent.create,
        )
        self.update = async_to_streamed_response_wrapper(
            agent.update,
        )
        self.list = async_to_streamed_response_wrapper(
            agent.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            agent.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            agent.get,
        )
