# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..user_profile import UserProfile
from ..agent.run_state import RunState
from ..agent.artifact_item import ArtifactItem

__all__ = ["Task", "CurrentRun"]


class CurrentRun(BaseModel):
    """
    A factory task's current top-level run, resolved from the bound
    conversation at read time. This differs from FactoryTask.run_id,
    which is a creation-time provenance snapshot and is never updated.
    """

    is_run_type_cancellable: bool
    """Whether the current run's type is eligible for cancellation via the API.

    State-independent; clients should also gate on state.
    """

    run_id: str
    """ID of the task's current top-level (root) run."""

    state: RunState
    """Current state of the run:

    - QUEUED: Run is waiting to be picked up
    - PENDING: Run is being prepared
    - CLAIMED: Run has been claimed by a worker
    - INPROGRESS: Run is actively being executed
    - SUCCEEDED: Run completed successfully
    - FAILED: Run failed
    - BLOCKED: Run is blocked (e.g., awaiting user input or approval)
    - ERROR: Run encountered an error
    - CANCELLED: Run was cancelled by user
    """


class Task(BaseModel):
    """
    A factory task: the unit of work in a factory, bound to the agent
    conversation that owns it.
    """

    conversation_id: str
    """UUID of the agent conversation the task is bound to."""

    created_at: datetime
    """Time the task was created."""

    factory_uid: str
    """Public UID of the factory the task belongs to. Fixed at creation."""

    run_id: str
    """
    ID of the bound conversation's most recent run at task creation. This is a
    provenance snapshot and is not updated afterward; consumers needing the
    conversation's live latest run should resolve it via the conversation.
    """

    stage: Literal["TRIAGE", "SPEC", "IMPLEMENT", "REVIEW", "COMPLETE", "CANCELLED"]
    """
    Lifecycle stage of a factory task, mirroring the seeded factory agent roles plus
    the terminal COMPLETE and CANCELLED states. COMPLETE and CANCELLED are terminal
    in intent but not enforced: any stage may be written explicitly at any time.
    CANCELLED is set automatically when the task's current top-level run is
    cancelled, regardless of that run's agent type.
    """

    title: str
    """Human-readable title of the task."""

    uid: str
    """Public UID of the task."""

    updated_at: datetime
    """Time the task was last created, updated, or deleted.

    Artifact reporting does not bump this; new outputs appear on the next detail
    read.
    """

    author: Optional[UserProfile] = None
    """Creator of the run captured by run_id.

    Omitted when the creation run or its creator principal can no longer be
    resolved.
    """

    current_run: Optional[CurrentRun] = None
    """
    A factory task's current top-level run, resolved from the bound conversation at
    read time. This differs from FactoryTask.run_id, which is a creation-time
    provenance snapshot and is never updated.
    """

    description: Optional[str] = None
    """Optional description of the task."""

    outputs: Optional[List[ArtifactItem]] = None
    """
    Derived outputs, newest-first: PULL_REQUEST, EXTERNAL_REFERENCE, SCREENSHOT, and
    FILE artifacts (video recordings are FILE artifacts). Present on single-task
    reads (by uid, by conversation, and by run), where outputs are derived from the
    task's whole run tree (every run bound to the conversation plus the runs
    dispatched under them). On list responses with full_list=true, outputs are
    derived from the bound conversation only, not the wider run tree.
    """

    ticket_id: Optional[str] = None
    """Canonical ticket ID from the bound run.

    Present on list responses only when full_list=true and ticket metadata exists.
    """

    ticket_source: Optional[str] = None
    """Canonical ticket source from the bound run.

    Present on list responses only when full_list=true and ticket metadata exists.
    """
