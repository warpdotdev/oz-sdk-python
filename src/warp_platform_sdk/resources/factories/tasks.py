# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
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
from ...pagination import SyncFactoryTasksCursorPage, AsyncFactoryTasksCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.factories import (
    task_list_params,
    task_create_params,
    task_update_params,
    task_get_by_run_params,
    task_get_by_conversation_params,
)
from ...types.factories.task import Task

__all__ = ["TasksResource", "AsyncTasksResource"]


class TasksResource(SyncAPIResource):
    """Operations for creating and managing factories"""

    @cached_property
    def with_raw_response(self) -> TasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#with_streaming_response
        """
        return TasksResourceWithStreamingResponse(self)

    def create(
        self,
        uid: str,
        *,
        conversation_id: str,
        title: str,
        description: Optional[str] | Omit = omit,
        stage: Literal["TRIAGE", "SPEC", "IMPLEMENT", "REVIEW", "COMPLETE", "CANCELLED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Task:
        """Create a task in a factory, bound to an existing agent conversation.

        title and
        conversation_id are required. The stage defaults to TRIAGE. The conversation's
        most recent run must be owned by the factory's team, and a conversation may be
        bound to at most one live task across all factories.

        Args:
          conversation_id: UUID of the agent conversation to bind the task to. The conversation's most
              recent run must be owned by the factory's team, and the conversation must not
              already be bound to a live task.

          title: Human-readable title of the task. Required and non-empty.

          description: Optional description of the task.

          stage: Lifecycle stage of a factory task, mirroring the seeded factory agent roles plus
              the terminal COMPLETE and CANCELLED states. COMPLETE and CANCELLED are terminal
              in intent but not enforced: any stage may be written explicitly at any time.
              CANCELLED is set automatically when the task's current top-level run is
              cancelled, regardless of that run's agent type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return self._post(
            path_template("/factory/{uid}/tasks", uid=uid),
            body=maybe_transform(
                {
                    "conversation_id": conversation_id,
                    "title": title,
                    "description": description,
                    "stage": stage,
                },
                task_create_params.TaskCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Task,
        )

    def update(
        self,
        task_uid: str,
        *,
        uid: str,
        description: Optional[str] | Omit = omit,
        stage: Literal["TRIAGE", "SPEC", "IMPLEMENT", "REVIEW", "COMPLETE", "CANCELLED"] | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Task:
        """Partially update a task's title, description, and/or stage.

        Last write wins.
        Stage writes are unrestricted: any stage-to-stage transition is allowed,
        including moving backwards or to completion.

        Args:
          description: Updated description. null or an empty string clears the description.

          stage: Lifecycle stage of a factory task, mirroring the seeded factory agent roles plus
              the terminal COMPLETE and CANCELLED states. COMPLETE and CANCELLED are terminal
              in intent but not enforced: any stage may be written explicitly at any time.
              CANCELLED is set automatically when the task's current top-level run is
              cancelled, regardless of that run's agent type.

          title: Updated title. Must be non-empty when provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        if not task_uid:
            raise ValueError(f"Expected a non-empty value for `task_uid` but received {task_uid!r}")
        return self._patch(
            path_template("/factory/{uid}/tasks/{task_uid}", uid=uid, task_uid=task_uid),
            body=maybe_transform(
                {
                    "description": description,
                    "stage": stage,
                    "title": title,
                },
                task_update_params.TaskUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Task,
        )

    def list(
        self,
        uid: str,
        *,
        created_after: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        created_by: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
        full_list: bool | Omit = omit,
        include_current_run: bool | Omit = omit,
        limit: int | Omit = omit,
        q: str | Omit = omit,
        sort_by: Literal["created_at", "updated_at"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        stage: List[Literal["TRIAGE", "SPEC", "IMPLEMENT", "REVIEW", "COMPLETE", "CANCELLED"]] | Omit = omit,
        updated_after: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncFactoryTasksCursorPage[Task]:
        """List the factory's tasks with optional filtering and search.

        List responses are
        lean by default; set full_list=true to include canonical ticket metadata and
        derived outputs for the returned page.

        Args:
          created_after: Filter to tasks created after this timestamp (RFC3339 format).

          created_before: Filter to tasks created before this timestamp (RFC3339 format).

          created_by: Filter to tasks whose seed run was started by any of these teammates, each given
              as their email address. Can be specified multiple times to match any of the
              given teammates.

          cursor: Opaque cursor returned by a previous list response. Valid only for the
              sort_by/sort_order it was issued under; omit to restart the listing.

          full_list: Include canonical ticket_source and ticket_id metadata from each task's bound
              run, plus its derived outputs. Defaults to false.

          include_current_run: Include each task's current top-level run, resolved in one batch for the
              returned page. Defaults to false.

          limit: Maximum number of tasks to return (default 50, max 100).

          q: Case-insensitive substring search over the task title.

          sort_by: Sort field for results.

          sort_order: Sort direction.

          stage: Filter by task stage. Can be specified multiple times to match any of the given
              stages.

          updated_after: Filter to tasks updated after this timestamp (RFC3339 format).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return self._get_api_list(
            path_template("/factory/{uid}/tasks", uid=uid),
            page=SyncFactoryTasksCursorPage[Task],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_after": created_after,
                        "created_before": created_before,
                        "created_by": created_by,
                        "cursor": cursor,
                        "full_list": full_list,
                        "include_current_run": include_current_run,
                        "limit": limit,
                        "q": q,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "stage": stage,
                        "updated_after": updated_after,
                    },
                    task_list_params.TaskListParams,
                ),
            ),
            model=Task,
        )

    def delete(
        self,
        task_uid: str,
        *,
        uid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Soft-delete a task.

        The task disappears from list and get responses immediately,
        and its conversation may be bound to a new task. Deleting a task never deletes
        artifacts or the conversation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        if not task_uid:
            raise ValueError(f"Expected a non-empty value for `task_uid` but received {task_uid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/factory/{uid}/tasks/{task_uid}", uid=uid, task_uid=task_uid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def cancel(
        self,
        task_uid: str,
        *,
        uid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Task:
        """Cancel the task's current top-level run and move the task to CANCELLED.

        Every
        non-terminal descendant of the root run is cancelled as well.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        if not task_uid:
            raise ValueError(f"Expected a non-empty value for `task_uid` but received {task_uid!r}")
        return self._post(
            path_template("/factory/{uid}/tasks/{task_uid}/cancel", uid=uid, task_uid=task_uid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Task,
        )

    def get(
        self,
        task_uid: str,
        *,
        uid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Task:
        """
        Get a task with its derived outputs, newest-first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        if not task_uid:
            raise ValueError(f"Expected a non-empty value for `task_uid` but received {task_uid!r}")
        return self._get(
            path_template("/factory/{uid}/tasks/{task_uid}", uid=uid, task_uid=task_uid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Task,
        )

    def get_by_conversation(
        self,
        uid: str,
        *,
        conversation_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Task:
        """Get the factory task bound to an agent conversation.

        Conversation bindings are
        unique across factories, but the lookup is factory-scoped: a task owned by a
        different factory is 404.

        Args:
          conversation_id: The agent conversation ID the task is bound to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return self._get(
            path_template("/factory/{uid}/task-by-conversation", uid=uid),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"conversation_id": conversation_id}, task_get_by_conversation_params.TaskGetByConversationParams
                ),
            ),
            cast_to=Task,
        )

    def get_by_run(
        self,
        uid: str,
        *,
        run_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Task:
        """
        Get the factory task that owns a run: the task bound to the conversation of the
        run's root ancestor. The lookup is factory-scoped: a task owned by a different
        factory is 404.

        Args:
          run_id: Any run ID in the task's run tree.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return self._get(
            path_template("/factory/{uid}/task-by-run", uid=uid),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"run_id": run_id}, task_get_by_run_params.TaskGetByRunParams),
            ),
            cast_to=Task,
        )


class AsyncTasksResource(AsyncAPIResource):
    """Operations for creating and managing factories"""

    @cached_property
    def with_raw_response(self) -> AsyncTasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#with_streaming_response
        """
        return AsyncTasksResourceWithStreamingResponse(self)

    async def create(
        self,
        uid: str,
        *,
        conversation_id: str,
        title: str,
        description: Optional[str] | Omit = omit,
        stage: Literal["TRIAGE", "SPEC", "IMPLEMENT", "REVIEW", "COMPLETE", "CANCELLED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Task:
        """Create a task in a factory, bound to an existing agent conversation.

        title and
        conversation_id are required. The stage defaults to TRIAGE. The conversation's
        most recent run must be owned by the factory's team, and a conversation may be
        bound to at most one live task across all factories.

        Args:
          conversation_id: UUID of the agent conversation to bind the task to. The conversation's most
              recent run must be owned by the factory's team, and the conversation must not
              already be bound to a live task.

          title: Human-readable title of the task. Required and non-empty.

          description: Optional description of the task.

          stage: Lifecycle stage of a factory task, mirroring the seeded factory agent roles plus
              the terminal COMPLETE and CANCELLED states. COMPLETE and CANCELLED are terminal
              in intent but not enforced: any stage may be written explicitly at any time.
              CANCELLED is set automatically when the task's current top-level run is
              cancelled, regardless of that run's agent type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return await self._post(
            path_template("/factory/{uid}/tasks", uid=uid),
            body=await async_maybe_transform(
                {
                    "conversation_id": conversation_id,
                    "title": title,
                    "description": description,
                    "stage": stage,
                },
                task_create_params.TaskCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Task,
        )

    async def update(
        self,
        task_uid: str,
        *,
        uid: str,
        description: Optional[str] | Omit = omit,
        stage: Literal["TRIAGE", "SPEC", "IMPLEMENT", "REVIEW", "COMPLETE", "CANCELLED"] | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Task:
        """Partially update a task's title, description, and/or stage.

        Last write wins.
        Stage writes are unrestricted: any stage-to-stage transition is allowed,
        including moving backwards or to completion.

        Args:
          description: Updated description. null or an empty string clears the description.

          stage: Lifecycle stage of a factory task, mirroring the seeded factory agent roles plus
              the terminal COMPLETE and CANCELLED states. COMPLETE and CANCELLED are terminal
              in intent but not enforced: any stage may be written explicitly at any time.
              CANCELLED is set automatically when the task's current top-level run is
              cancelled, regardless of that run's agent type.

          title: Updated title. Must be non-empty when provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        if not task_uid:
            raise ValueError(f"Expected a non-empty value for `task_uid` but received {task_uid!r}")
        return await self._patch(
            path_template("/factory/{uid}/tasks/{task_uid}", uid=uid, task_uid=task_uid),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "stage": stage,
                    "title": title,
                },
                task_update_params.TaskUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Task,
        )

    def list(
        self,
        uid: str,
        *,
        created_after: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        created_by: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
        full_list: bool | Omit = omit,
        include_current_run: bool | Omit = omit,
        limit: int | Omit = omit,
        q: str | Omit = omit,
        sort_by: Literal["created_at", "updated_at"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        stage: List[Literal["TRIAGE", "SPEC", "IMPLEMENT", "REVIEW", "COMPLETE", "CANCELLED"]] | Omit = omit,
        updated_after: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Task, AsyncFactoryTasksCursorPage[Task]]:
        """List the factory's tasks with optional filtering and search.

        List responses are
        lean by default; set full_list=true to include canonical ticket metadata and
        derived outputs for the returned page.

        Args:
          created_after: Filter to tasks created after this timestamp (RFC3339 format).

          created_before: Filter to tasks created before this timestamp (RFC3339 format).

          created_by: Filter to tasks whose seed run was started by any of these teammates, each given
              as their email address. Can be specified multiple times to match any of the
              given teammates.

          cursor: Opaque cursor returned by a previous list response. Valid only for the
              sort_by/sort_order it was issued under; omit to restart the listing.

          full_list: Include canonical ticket_source and ticket_id metadata from each task's bound
              run, plus its derived outputs. Defaults to false.

          include_current_run: Include each task's current top-level run, resolved in one batch for the
              returned page. Defaults to false.

          limit: Maximum number of tasks to return (default 50, max 100).

          q: Case-insensitive substring search over the task title.

          sort_by: Sort field for results.

          sort_order: Sort direction.

          stage: Filter by task stage. Can be specified multiple times to match any of the given
              stages.

          updated_after: Filter to tasks updated after this timestamp (RFC3339 format).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return self._get_api_list(
            path_template("/factory/{uid}/tasks", uid=uid),
            page=AsyncFactoryTasksCursorPage[Task],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_after": created_after,
                        "created_before": created_before,
                        "created_by": created_by,
                        "cursor": cursor,
                        "full_list": full_list,
                        "include_current_run": include_current_run,
                        "limit": limit,
                        "q": q,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "stage": stage,
                        "updated_after": updated_after,
                    },
                    task_list_params.TaskListParams,
                ),
            ),
            model=Task,
        )

    async def delete(
        self,
        task_uid: str,
        *,
        uid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Soft-delete a task.

        The task disappears from list and get responses immediately,
        and its conversation may be bound to a new task. Deleting a task never deletes
        artifacts or the conversation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        if not task_uid:
            raise ValueError(f"Expected a non-empty value for `task_uid` but received {task_uid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/factory/{uid}/tasks/{task_uid}", uid=uid, task_uid=task_uid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def cancel(
        self,
        task_uid: str,
        *,
        uid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Task:
        """Cancel the task's current top-level run and move the task to CANCELLED.

        Every
        non-terminal descendant of the root run is cancelled as well.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        if not task_uid:
            raise ValueError(f"Expected a non-empty value for `task_uid` but received {task_uid!r}")
        return await self._post(
            path_template("/factory/{uid}/tasks/{task_uid}/cancel", uid=uid, task_uid=task_uid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Task,
        )

    async def get(
        self,
        task_uid: str,
        *,
        uid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Task:
        """
        Get a task with its derived outputs, newest-first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        if not task_uid:
            raise ValueError(f"Expected a non-empty value for `task_uid` but received {task_uid!r}")
        return await self._get(
            path_template("/factory/{uid}/tasks/{task_uid}", uid=uid, task_uid=task_uid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Task,
        )

    async def get_by_conversation(
        self,
        uid: str,
        *,
        conversation_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Task:
        """Get the factory task bound to an agent conversation.

        Conversation bindings are
        unique across factories, but the lookup is factory-scoped: a task owned by a
        different factory is 404.

        Args:
          conversation_id: The agent conversation ID the task is bound to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return await self._get(
            path_template("/factory/{uid}/task-by-conversation", uid=uid),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"conversation_id": conversation_id}, task_get_by_conversation_params.TaskGetByConversationParams
                ),
            ),
            cast_to=Task,
        )

    async def get_by_run(
        self,
        uid: str,
        *,
        run_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Task:
        """
        Get the factory task that owns a run: the task bound to the conversation of the
        run's root ancestor. The lookup is factory-scoped: a task owned by a different
        factory is 404.

        Args:
          run_id: Any run ID in the task's run tree.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return await self._get(
            path_template("/factory/{uid}/task-by-run", uid=uid),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"run_id": run_id}, task_get_by_run_params.TaskGetByRunParams),
            ),
            cast_to=Task,
        )


class TasksResourceWithRawResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.create = to_raw_response_wrapper(
            tasks.create,
        )
        self.update = to_raw_response_wrapper(
            tasks.update,
        )
        self.list = to_raw_response_wrapper(
            tasks.list,
        )
        self.delete = to_raw_response_wrapper(
            tasks.delete,
        )
        self.cancel = to_raw_response_wrapper(
            tasks.cancel,
        )
        self.get = to_raw_response_wrapper(
            tasks.get,
        )
        self.get_by_conversation = to_raw_response_wrapper(
            tasks.get_by_conversation,
        )
        self.get_by_run = to_raw_response_wrapper(
            tasks.get_by_run,
        )


class AsyncTasksResourceWithRawResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.create = async_to_raw_response_wrapper(
            tasks.create,
        )
        self.update = async_to_raw_response_wrapper(
            tasks.update,
        )
        self.list = async_to_raw_response_wrapper(
            tasks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tasks.delete,
        )
        self.cancel = async_to_raw_response_wrapper(
            tasks.cancel,
        )
        self.get = async_to_raw_response_wrapper(
            tasks.get,
        )
        self.get_by_conversation = async_to_raw_response_wrapper(
            tasks.get_by_conversation,
        )
        self.get_by_run = async_to_raw_response_wrapper(
            tasks.get_by_run,
        )


class TasksResourceWithStreamingResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.create = to_streamed_response_wrapper(
            tasks.create,
        )
        self.update = to_streamed_response_wrapper(
            tasks.update,
        )
        self.list = to_streamed_response_wrapper(
            tasks.list,
        )
        self.delete = to_streamed_response_wrapper(
            tasks.delete,
        )
        self.cancel = to_streamed_response_wrapper(
            tasks.cancel,
        )
        self.get = to_streamed_response_wrapper(
            tasks.get,
        )
        self.get_by_conversation = to_streamed_response_wrapper(
            tasks.get_by_conversation,
        )
        self.get_by_run = to_streamed_response_wrapper(
            tasks.get_by_run,
        )


class AsyncTasksResourceWithStreamingResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.create = async_to_streamed_response_wrapper(
            tasks.create,
        )
        self.update = async_to_streamed_response_wrapper(
            tasks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            tasks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tasks.delete,
        )
        self.cancel = async_to_streamed_response_wrapper(
            tasks.cancel,
        )
        self.get = async_to_streamed_response_wrapper(
            tasks.get,
        )
        self.get_by_conversation = async_to_streamed_response_wrapper(
            tasks.get_by_conversation,
        )
        self.get_by_run = async_to_streamed_response_wrapper(
            tasks.get_by_run,
        )
