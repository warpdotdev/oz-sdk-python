# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .agent.task_state import TaskState

__all__ = ["AgentRunResponse"]


class AgentRunResponse(BaseModel):
    state: TaskState
    """Current state of the task:

    - QUEUED: Task is waiting to be picked up
    - PENDING: Task is being prepared
    - CLAIMED: Task has been claimed by a worker
    - INPROGRESS: Task is actively being executed
    - SUCCEEDED: Task completed successfully
    - FAILED: Task failed
    """

    task_id: str
    """Unique identifier for the created task"""
