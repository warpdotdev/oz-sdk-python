# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["SuiteCreateParams", "Task", "TaskStartingRepoRef"]


class SuiteCreateParams(TypedDict, total=False):
    agent_uid: Required[str]

    factory_agent_type: Required[str]

    name: Required[str]

    suite_uid: Required[Annotated[str, PropertyInfo(alias="uid")]]

    description: str

    tasks: Iterable[Task]


class TaskStartingRepoRef(TypedDict, total=False):
    """A repository location and optional starting ref for a suite task."""

    code_forge: Required[str]

    owner: Required[str]

    repo: Required[str]

    ref: str


class Task(TypedDict, total=False):
    prompt: Required[str]

    success_criteria: Required[str]
    """
    Plain-text criteria the built-in Correctness scorer grades each trial against,
    as the authoritative requirements. The task prompt provides context only.
    """

    title: Required[str]

    labels: Dict[str, str]

    source_run_id: Optional[str]

    starting_repo_refs: Iterable[TaskStartingRepoRef]

    tags: SequenceNotStr[str]

    uid: str
    """Existing task UID. Accepted only when editing its current suite."""
