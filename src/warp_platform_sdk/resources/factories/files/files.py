# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from .schemas import (
    SchemasResource,
    AsyncSchemasResource,
    SchemasResourceWithRawResponse,
    AsyncSchemasResourceWithRawResponse,
    SchemasResourceWithStreamingResponse,
    AsyncSchemasResourceWithStreamingResponse,
)
from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.factories import file_validate_params
from ....types.factories.file_validate_response import FileValidateResponse

__all__ = ["FilesResource", "AsyncFilesResource"]


class FilesResource(SyncAPIResource):
    """Operations for creating and managing factories"""

    @cached_property
    def schemas(self) -> SchemasResource:
        """Operations for creating and managing factories"""
        return SchemasResource(self._client)

    @cached_property
    def with_raw_response(self) -> FilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#with_streaming_response
        """
        return FilesResourceWithStreamingResponse(self)

    def validate(
        self,
        *,
        files: Iterable[file_validate_params.File],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileValidateResponse:
        """
        Parses a Factory tree supplied as paths and content, then applies the checks the
        apply path performs without consulting tenant state; nothing is persisted, no
        Factory is loaded, and no repository is read. Validation is unauthenticated,
        like the schema endpoints beside it, since it reads no tenant state and local
        authoring agents reach the server from a shell with no access to the client's
        session.

        Args:
          files: The Factory tree's resource files. Send factory.yaml and the candidate Agent,
              Automation, Runner, and Scorer paths; skill files are not parser inputs.
              Symlinks must not be followed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/factory-files/validate",
            body=maybe_transform({"files": files}, file_validate_params.FileValidateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=FileValidateResponse,
        )


class AsyncFilesResource(AsyncAPIResource):
    """Operations for creating and managing factories"""

    @cached_property
    def schemas(self) -> AsyncSchemasResource:
        """Operations for creating and managing factories"""
        return AsyncSchemasResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#with_streaming_response
        """
        return AsyncFilesResourceWithStreamingResponse(self)

    async def validate(
        self,
        *,
        files: Iterable[file_validate_params.File],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileValidateResponse:
        """
        Parses a Factory tree supplied as paths and content, then applies the checks the
        apply path performs without consulting tenant state; nothing is persisted, no
        Factory is loaded, and no repository is read. Validation is unauthenticated,
        like the schema endpoints beside it, since it reads no tenant state and local
        authoring agents reach the server from a shell with no access to the client's
        session.

        Args:
          files: The Factory tree's resource files. Send factory.yaml and the candidate Agent,
              Automation, Runner, and Scorer paths; skill files are not parser inputs.
              Symlinks must not be followed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/factory-files/validate",
            body=await async_maybe_transform({"files": files}, file_validate_params.FileValidateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=FileValidateResponse,
        )


class FilesResourceWithRawResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.validate = to_raw_response_wrapper(
            files.validate,
        )

    @cached_property
    def schemas(self) -> SchemasResourceWithRawResponse:
        """Operations for creating and managing factories"""
        return SchemasResourceWithRawResponse(self._files.schemas)


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.validate = async_to_raw_response_wrapper(
            files.validate,
        )

    @cached_property
    def schemas(self) -> AsyncSchemasResourceWithRawResponse:
        """Operations for creating and managing factories"""
        return AsyncSchemasResourceWithRawResponse(self._files.schemas)


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.validate = to_streamed_response_wrapper(
            files.validate,
        )

    @cached_property
    def schemas(self) -> SchemasResourceWithStreamingResponse:
        """Operations for creating and managing factories"""
        return SchemasResourceWithStreamingResponse(self._files.schemas)


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.validate = async_to_streamed_response_wrapper(
            files.validate,
        )

    @cached_property
    def schemas(self) -> AsyncSchemasResourceWithStreamingResponse:
        """Operations for creating and managing factories"""
        return AsyncSchemasResourceWithStreamingResponse(self._files.schemas)
