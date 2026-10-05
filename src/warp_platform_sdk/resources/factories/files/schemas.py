# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, strip_not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.factories.files.schema_list_response import SchemaListResponse
from ....types.factories.files.schema_retrieve_response import SchemaRetrieveResponse
from ....types.factories.files.schema_get_document_response import SchemaGetDocumentResponse

__all__ = ["SchemasResource", "AsyncSchemasResource"]


class SchemasResource(SyncAPIResource):
    """Operations for creating and managing factories"""

    @cached_property
    def with_raw_response(self) -> SchemasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SchemasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SchemasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#with_streaming_response
        """
        return SchemasResourceWithStreamingResponse(self)

    def retrieve(
        self,
        schema_version: str,
        *,
        if_none_match: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaRetrieveResponse:
        """
        Returns every JSON Schema 2020-12 document describing one Factory file schema
        version, as a single bundle so the relative `$id` and `$ref` identities between
        the documents keep resolving.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schema_version:
            raise ValueError(f"Expected a non-empty value for `schema_version` but received {schema_version!r}")
        extra_headers = {**strip_not_given({"If-None-Match": if_none_match}), **(extra_headers or {})}
        return self._get(
            path_template("/factory-files/schemas/{schema_version}", schema_version=schema_version),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=SchemaRetrieveResponse,
        )

    def list(
        self,
        *,
        if_none_match: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaListResponse:
        """
        Returns every Factory file schema version this server can describe, with a link
        to each version's schema bundle.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"If-None-Match": if_none_match}), **(extra_headers or {})}
        return self._get(
            "/factory-files/schemas",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=SchemaListResponse,
        )

    def get_document(
        self,
        document: str,
        *,
        schema_version: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaGetDocumentResponse:
        """
        Returns a single generated JSON Schema document on its own, rather than inside
        the bundle envelope, so it can be used directly as a schema reference. A
        document served here resolves its relative `$ref`s against its siblings at this
        same path, which is what each document's `$id` assumes, making the URL usable
        directly from an editor or YAML language server, for example:

        ```yaml
        # yaml-language-server: $schema=/api/v1/factory-files/schemas/v1alpha1/factory.schema.json
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schema_version:
            raise ValueError(f"Expected a non-empty value for `schema_version` but received {schema_version!r}")
        if not document:
            raise ValueError(f"Expected a non-empty value for `document` but received {document!r}")
        return self._get(
            path_template(
                "/factory-files/schemas/{schema_version}/{document}", schema_version=schema_version, document=document
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=SchemaGetDocumentResponse,
        )


class AsyncSchemasResource(AsyncAPIResource):
    """Operations for creating and managing factories"""

    @cached_property
    def with_raw_response(self) -> AsyncSchemasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSchemasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSchemasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#with_streaming_response
        """
        return AsyncSchemasResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        schema_version: str,
        *,
        if_none_match: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaRetrieveResponse:
        """
        Returns every JSON Schema 2020-12 document describing one Factory file schema
        version, as a single bundle so the relative `$id` and `$ref` identities between
        the documents keep resolving.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schema_version:
            raise ValueError(f"Expected a non-empty value for `schema_version` but received {schema_version!r}")
        extra_headers = {**strip_not_given({"If-None-Match": if_none_match}), **(extra_headers or {})}
        return await self._get(
            path_template("/factory-files/schemas/{schema_version}", schema_version=schema_version),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=SchemaRetrieveResponse,
        )

    async def list(
        self,
        *,
        if_none_match: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaListResponse:
        """
        Returns every Factory file schema version this server can describe, with a link
        to each version's schema bundle.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"If-None-Match": if_none_match}), **(extra_headers or {})}
        return await self._get(
            "/factory-files/schemas",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=SchemaListResponse,
        )

    async def get_document(
        self,
        document: str,
        *,
        schema_version: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaGetDocumentResponse:
        """
        Returns a single generated JSON Schema document on its own, rather than inside
        the bundle envelope, so it can be used directly as a schema reference. A
        document served here resolves its relative `$ref`s against its siblings at this
        same path, which is what each document's `$id` assumes, making the URL usable
        directly from an editor or YAML language server, for example:

        ```yaml
        # yaml-language-server: $schema=/api/v1/factory-files/schemas/v1alpha1/factory.schema.json
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schema_version:
            raise ValueError(f"Expected a non-empty value for `schema_version` but received {schema_version!r}")
        if not document:
            raise ValueError(f"Expected a non-empty value for `document` but received {document!r}")
        return await self._get(
            path_template(
                "/factory-files/schemas/{schema_version}/{document}", schema_version=schema_version, document=document
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=SchemaGetDocumentResponse,
        )


class SchemasResourceWithRawResponse:
    def __init__(self, schemas: SchemasResource) -> None:
        self._schemas = schemas

        self.retrieve = to_raw_response_wrapper(
            schemas.retrieve,
        )
        self.list = to_raw_response_wrapper(
            schemas.list,
        )
        self.get_document = to_raw_response_wrapper(
            schemas.get_document,
        )


class AsyncSchemasResourceWithRawResponse:
    def __init__(self, schemas: AsyncSchemasResource) -> None:
        self._schemas = schemas

        self.retrieve = async_to_raw_response_wrapper(
            schemas.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            schemas.list,
        )
        self.get_document = async_to_raw_response_wrapper(
            schemas.get_document,
        )


class SchemasResourceWithStreamingResponse:
    def __init__(self, schemas: SchemasResource) -> None:
        self._schemas = schemas

        self.retrieve = to_streamed_response_wrapper(
            schemas.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            schemas.list,
        )
        self.get_document = to_streamed_response_wrapper(
            schemas.get_document,
        )


class AsyncSchemasResourceWithStreamingResponse:
    def __init__(self, schemas: AsyncSchemasResource) -> None:
        self._schemas = schemas

        self.retrieve = async_to_streamed_response_wrapper(
            schemas.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            schemas.list,
        )
        self.get_document = async_to_streamed_response_wrapper(
            schemas.get_document,
        )
