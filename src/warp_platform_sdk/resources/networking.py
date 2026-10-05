# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import strip_not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.networking_get_egress_ranges_response import NetworkingGetEgressRangesResponse

__all__ = ["NetworkingResource", "AsyncNetworkingResource"]


class NetworkingResource(SyncAPIResource):
    """Networking information for Warp-hosted agents"""

    @cached_property
    def with_raw_response(self) -> NetworkingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#accessing-raw-response-data-eg-headers
        """
        return NetworkingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NetworkingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#with_streaming_response
        """
        return NetworkingResourceWithStreamingResponse(self)

    def get_egress_ranges(
        self,
        *,
        team_uid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NetworkingGetEgressRangesResponse:
        """
        Return the canonical IP network ranges used by outbound requests from
        Warp-hosted agents.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Warp-Team-Uid": team_uid}), **(extra_headers or {})}
        return self._get(
            "/networking/egress-ranges",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkingGetEgressRangesResponse,
        )


class AsyncNetworkingResource(AsyncAPIResource):
    """Networking information for Warp-hosted agents"""

    @cached_property
    def with_raw_response(self) -> AsyncNetworkingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNetworkingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNetworkingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#with_streaming_response
        """
        return AsyncNetworkingResourceWithStreamingResponse(self)

    async def get_egress_ranges(
        self,
        *,
        team_uid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NetworkingGetEgressRangesResponse:
        """
        Return the canonical IP network ranges used by outbound requests from
        Warp-hosted agents.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Warp-Team-Uid": team_uid}), **(extra_headers or {})}
        return await self._get(
            "/networking/egress-ranges",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkingGetEgressRangesResponse,
        )


class NetworkingResourceWithRawResponse:
    def __init__(self, networking: NetworkingResource) -> None:
        self._networking = networking

        self.get_egress_ranges = to_raw_response_wrapper(
            networking.get_egress_ranges,
        )


class AsyncNetworkingResourceWithRawResponse:
    def __init__(self, networking: AsyncNetworkingResource) -> None:
        self._networking = networking

        self.get_egress_ranges = async_to_raw_response_wrapper(
            networking.get_egress_ranges,
        )


class NetworkingResourceWithStreamingResponse:
    def __init__(self, networking: NetworkingResource) -> None:
        self._networking = networking

        self.get_egress_ranges = to_streamed_response_wrapper(
            networking.get_egress_ranges,
        )


class AsyncNetworkingResourceWithStreamingResponse:
    def __init__(self, networking: AsyncNetworkingResource) -> None:
        self._networking = networking

        self.get_egress_ranges = async_to_streamed_response_wrapper(
            networking.get_egress_ranges,
        )
