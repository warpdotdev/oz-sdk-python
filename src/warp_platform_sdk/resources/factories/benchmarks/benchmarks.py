# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .runs import (
    RunsResource,
    AsyncRunsResource,
    RunsResourceWithRawResponse,
    AsyncRunsResourceWithRawResponse,
    RunsResourceWithStreamingResponse,
    AsyncRunsResourceWithStreamingResponse,
)
from .suites import (
    SuitesResource,
    AsyncSuitesResource,
    SuitesResourceWithRawResponse,
    AsyncSuitesResourceWithRawResponse,
    SuitesResourceWithStreamingResponse,
    AsyncSuitesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["BenchmarksResource", "AsyncBenchmarksResource"]


class BenchmarksResource(SyncAPIResource):
    @cached_property
    def suites(self) -> SuitesResource:
        """Operations for creating and managing factories"""
        return SuitesResource(self._client)

    @cached_property
    def runs(self) -> RunsResource:
        """Operations for creating and managing factories"""
        return RunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> BenchmarksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#accessing-raw-response-data-eg-headers
        """
        return BenchmarksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BenchmarksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#with_streaming_response
        """
        return BenchmarksResourceWithStreamingResponse(self)


class AsyncBenchmarksResource(AsyncAPIResource):
    @cached_property
    def suites(self) -> AsyncSuitesResource:
        """Operations for creating and managing factories"""
        return AsyncSuitesResource(self._client)

    @cached_property
    def runs(self) -> AsyncRunsResource:
        """Operations for creating and managing factories"""
        return AsyncRunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBenchmarksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBenchmarksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBenchmarksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/warpdotdev/oz-sdk-python#with_streaming_response
        """
        return AsyncBenchmarksResourceWithStreamingResponse(self)


class BenchmarksResourceWithRawResponse:
    def __init__(self, benchmarks: BenchmarksResource) -> None:
        self._benchmarks = benchmarks

    @cached_property
    def suites(self) -> SuitesResourceWithRawResponse:
        """Operations for creating and managing factories"""
        return SuitesResourceWithRawResponse(self._benchmarks.suites)

    @cached_property
    def runs(self) -> RunsResourceWithRawResponse:
        """Operations for creating and managing factories"""
        return RunsResourceWithRawResponse(self._benchmarks.runs)


class AsyncBenchmarksResourceWithRawResponse:
    def __init__(self, benchmarks: AsyncBenchmarksResource) -> None:
        self._benchmarks = benchmarks

    @cached_property
    def suites(self) -> AsyncSuitesResourceWithRawResponse:
        """Operations for creating and managing factories"""
        return AsyncSuitesResourceWithRawResponse(self._benchmarks.suites)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithRawResponse:
        """Operations for creating and managing factories"""
        return AsyncRunsResourceWithRawResponse(self._benchmarks.runs)


class BenchmarksResourceWithStreamingResponse:
    def __init__(self, benchmarks: BenchmarksResource) -> None:
        self._benchmarks = benchmarks

    @cached_property
    def suites(self) -> SuitesResourceWithStreamingResponse:
        """Operations for creating and managing factories"""
        return SuitesResourceWithStreamingResponse(self._benchmarks.suites)

    @cached_property
    def runs(self) -> RunsResourceWithStreamingResponse:
        """Operations for creating and managing factories"""
        return RunsResourceWithStreamingResponse(self._benchmarks.runs)


class AsyncBenchmarksResourceWithStreamingResponse:
    def __init__(self, benchmarks: AsyncBenchmarksResource) -> None:
        self._benchmarks = benchmarks

    @cached_property
    def suites(self) -> AsyncSuitesResourceWithStreamingResponse:
        """Operations for creating and managing factories"""
        return AsyncSuitesResourceWithStreamingResponse(self._benchmarks.suites)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithStreamingResponse:
        """Operations for creating and managing factories"""
        return AsyncRunsResourceWithStreamingResponse(self._benchmarks.runs)
