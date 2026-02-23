# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "ArtifactItem",
    "PlanArtifact",
    "PlanArtifactData",
    "PullRequestArtifact",
    "PullRequestArtifactData",
    "ScreenshotArtifact",
    "ScreenshotArtifactData",
]


class PlanArtifactData(BaseModel):
    document_uid: str
    """Unique identifier for the plan document"""

    notebook_uid: Optional[str] = None
    """Unique identifier for the associated notebook"""

    title: Optional[str] = None
    """Title of the plan"""


class PlanArtifact(BaseModel):
    artifact_type: Literal["PLAN"]
    """Type of the artifact"""

    created_at: datetime
    """Timestamp when the artifact was created (RFC3339)"""

    data: PlanArtifactData


class PullRequestArtifactData(BaseModel):
    branch: str
    """Branch name for the pull request"""

    url: str
    """URL of the pull request"""


class PullRequestArtifact(BaseModel):
    artifact_type: Literal["PULL_REQUEST"]
    """Type of the artifact"""

    created_at: datetime
    """Timestamp when the artifact was created (RFC3339)"""

    data: PullRequestArtifactData


class ScreenshotArtifactData(BaseModel):
    artifact_uid: str
    """Unique identifier for the screenshot artifact"""

    mime_type: str
    """MIME type of the screenshot image"""

    description: Optional[str] = None
    """Optional description of the screenshot"""


class ScreenshotArtifact(BaseModel):
    artifact_type: Literal["SCREENSHOT"]
    """Type of the artifact"""

    created_at: datetime
    """Timestamp when the artifact was created (RFC3339)"""

    data: ScreenshotArtifactData


ArtifactItem: TypeAlias = Annotated[
    Union[PlanArtifact, PullRequestArtifact, ScreenshotArtifact], PropertyInfo(discriminator="artifact_type")
]
