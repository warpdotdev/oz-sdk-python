# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "RunsCursorPagePageInfo",
    "SyncRunsCursorPage",
    "AsyncRunsCursorPage",
    "FactoryTasksCursorPagePageInfo",
    "SyncFactoryTasksCursorPage",
    "AsyncFactoryTasksCursorPage",
    "ScorerResultsCursorPagePageInfo",
    "SyncScorerResultsCursorPage",
    "AsyncScorerResultsCursorPage",
    "BenchmarkSuitesCursorPagePageInfo",
    "SyncBenchmarkSuitesCursorPage",
    "AsyncBenchmarkSuitesCursorPage",
    "FactoriesCursorPagePageInfo",
    "SyncFactoriesCursorPage",
    "AsyncFactoriesCursorPage",
]

_T = TypeVar("_T")


class RunsCursorPagePageInfo(BaseModel):
    has_next_page: Optional[bool] = None

    next_cursor: Optional[str] = None


class SyncRunsCursorPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    runs: List[_T]
    page_info: Optional[RunsCursorPagePageInfo] = None

    @override
    def _get_page_items(self) -> List[_T]:
        runs = self.runs
        if not runs:
            return []
        return runs

    @override
    def has_next_page(self) -> bool:
        has_next_page = None
        if self.page_info is not None:
            if self.page_info.has_next_page is not None:
                has_next_page = self.page_info.has_next_page
        if has_next_page is not None and has_next_page is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = None
        if self.page_info is not None:
            if self.page_info.next_cursor is not None:
                next_cursor = self.page_info.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class AsyncRunsCursorPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    runs: List[_T]
    page_info: Optional[RunsCursorPagePageInfo] = None

    @override
    def _get_page_items(self) -> List[_T]:
        runs = self.runs
        if not runs:
            return []
        return runs

    @override
    def has_next_page(self) -> bool:
        has_next_page = None
        if self.page_info is not None:
            if self.page_info.has_next_page is not None:
                has_next_page = self.page_info.has_next_page
        if has_next_page is not None and has_next_page is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = None
        if self.page_info is not None:
            if self.page_info.next_cursor is not None:
                next_cursor = self.page_info.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class FactoryTasksCursorPagePageInfo(BaseModel):
    has_next_page: Optional[bool] = None

    next_cursor: Optional[str] = None


class SyncFactoryTasksCursorPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    tasks: List[_T]
    page_info: Optional[FactoryTasksCursorPagePageInfo] = None

    @override
    def _get_page_items(self) -> List[_T]:
        tasks = self.tasks
        if not tasks:
            return []
        return tasks

    @override
    def has_next_page(self) -> bool:
        has_next_page = None
        if self.page_info is not None:
            if self.page_info.has_next_page is not None:
                has_next_page = self.page_info.has_next_page
        if has_next_page is not None and has_next_page is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = None
        if self.page_info is not None:
            if self.page_info.next_cursor is not None:
                next_cursor = self.page_info.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class AsyncFactoryTasksCursorPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    tasks: List[_T]
    page_info: Optional[FactoryTasksCursorPagePageInfo] = None

    @override
    def _get_page_items(self) -> List[_T]:
        tasks = self.tasks
        if not tasks:
            return []
        return tasks

    @override
    def has_next_page(self) -> bool:
        has_next_page = None
        if self.page_info is not None:
            if self.page_info.has_next_page is not None:
                has_next_page = self.page_info.has_next_page
        if has_next_page is not None and has_next_page is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = None
        if self.page_info is not None:
            if self.page_info.next_cursor is not None:
                next_cursor = self.page_info.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class ScorerResultsCursorPagePageInfo(BaseModel):
    has_next_page: Optional[bool] = None

    next_cursor: Optional[str] = None


class SyncScorerResultsCursorPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    results: List[_T]
    page_info: Optional[ScorerResultsCursorPagePageInfo] = None

    @override
    def _get_page_items(self) -> List[_T]:
        results = self.results
        if not results:
            return []
        return results

    @override
    def has_next_page(self) -> bool:
        has_next_page = None
        if self.page_info is not None:
            if self.page_info.has_next_page is not None:
                has_next_page = self.page_info.has_next_page
        if has_next_page is not None and has_next_page is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = None
        if self.page_info is not None:
            if self.page_info.next_cursor is not None:
                next_cursor = self.page_info.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class AsyncScorerResultsCursorPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    results: List[_T]
    page_info: Optional[ScorerResultsCursorPagePageInfo] = None

    @override
    def _get_page_items(self) -> List[_T]:
        results = self.results
        if not results:
            return []
        return results

    @override
    def has_next_page(self) -> bool:
        has_next_page = None
        if self.page_info is not None:
            if self.page_info.has_next_page is not None:
                has_next_page = self.page_info.has_next_page
        if has_next_page is not None and has_next_page is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = None
        if self.page_info is not None:
            if self.page_info.next_cursor is not None:
                next_cursor = self.page_info.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class BenchmarkSuitesCursorPagePageInfo(BaseModel):
    has_next_page: Optional[bool] = None

    next_cursor: Optional[str] = None


class SyncBenchmarkSuitesCursorPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    suites: List[_T]
    page_info: Optional[BenchmarkSuitesCursorPagePageInfo] = None

    @override
    def _get_page_items(self) -> List[_T]:
        suites = self.suites
        if not suites:
            return []
        return suites

    @override
    def has_next_page(self) -> bool:
        has_next_page = None
        if self.page_info is not None:
            if self.page_info.has_next_page is not None:
                has_next_page = self.page_info.has_next_page
        if has_next_page is not None and has_next_page is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = None
        if self.page_info is not None:
            if self.page_info.next_cursor is not None:
                next_cursor = self.page_info.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class AsyncBenchmarkSuitesCursorPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    suites: List[_T]
    page_info: Optional[BenchmarkSuitesCursorPagePageInfo] = None

    @override
    def _get_page_items(self) -> List[_T]:
        suites = self.suites
        if not suites:
            return []
        return suites

    @override
    def has_next_page(self) -> bool:
        has_next_page = None
        if self.page_info is not None:
            if self.page_info.has_next_page is not None:
                has_next_page = self.page_info.has_next_page
        if has_next_page is not None and has_next_page is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = None
        if self.page_info is not None:
            if self.page_info.next_cursor is not None:
                next_cursor = self.page_info.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class FactoriesCursorPagePageInfo(BaseModel):
    has_next_page: Optional[bool] = None

    next_cursor: Optional[str] = None


class SyncFactoriesCursorPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    factories: List[_T]
    page_info: Optional[FactoriesCursorPagePageInfo] = None

    @override
    def _get_page_items(self) -> List[_T]:
        factories = self.factories
        if not factories:
            return []
        return factories

    @override
    def has_next_page(self) -> bool:
        has_next_page = None
        if self.page_info is not None:
            if self.page_info.has_next_page is not None:
                has_next_page = self.page_info.has_next_page
        if has_next_page is not None and has_next_page is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = None
        if self.page_info is not None:
            if self.page_info.next_cursor is not None:
                next_cursor = self.page_info.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class AsyncFactoriesCursorPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    factories: List[_T]
    page_info: Optional[FactoriesCursorPagePageInfo] = None

    @override
    def _get_page_items(self) -> List[_T]:
        factories = self.factories
        if not factories:
            return []
        return factories

    @override
    def has_next_page(self) -> bool:
        has_next_page = None
        if self.page_info is not None:
            if self.page_info.has_next_page is not None:
                has_next_page = self.page_info.has_next_page
        if has_next_page is not None and has_next_page is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = None
        if self.page_info is not None:
            if self.page_info.next_cursor is not None:
                next_cursor = self.page_info.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})
