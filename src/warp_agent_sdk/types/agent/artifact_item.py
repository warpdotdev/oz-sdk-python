# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = ["ArtifactItem", "PlanArtifact", "PlanArtifactPlan", "PullRequestArtifact", "PullRequestArtifactPullRequest"]


class PlanArtifactPlan(BaseModel):
    document_uid: str
    """Unique identifier for the plan document"""

    notebook_uid: Optional[str] = None
    """Unique identifier for the associated notebook"""

    title: Optional[str] = None
    """Title of the plan"""


class PlanArtifact(BaseModel):
    artifact_type: Literal["plan"]
    """Type of the artifact"""

    created_at: datetime
    """Timestamp when the artifact was created (RFC3339)"""

    plan: PlanArtifactPlan


class PullRequestArtifactPullRequest(BaseModel):
    branch: str
    """Branch name for the pull request"""

    url: str
    """URL of the pull request"""


class PullRequestArtifact(BaseModel):
    artifact_type: Literal["pull_request"]
    """Type of the artifact"""

    created_at: datetime
    """Timestamp when the artifact was created (RFC3339)"""

    pull_request: PullRequestArtifactPullRequest


ArtifactItem: TypeAlias = Annotated[
    Union[PlanArtifact, PullRequestArtifact], PropertyInfo(discriminator="artifact_type")
]
