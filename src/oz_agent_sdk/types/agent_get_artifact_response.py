# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "AgentGetArtifactResponse",
    "PlanArtifactResponse",
    "PlanArtifactResponseData",
    "ScreenshotArtifactResponse",
    "ScreenshotArtifactResponseData",
    "FileArtifactResponse",
    "FileArtifactResponseData",
]


class PlanArtifactResponseData(BaseModel):
    """Response data for a plan artifact, including current markdown content."""

    content: str
    """Current markdown content of the plan"""

    content_type: str
    """MIME type of the returned plan content"""

    document_uid: str
    """Unique identifier for the plan document"""

    notebook_uid: str
    """Unique identifier for the associated notebook"""

    title: Optional[str] = None
    """Current title of the plan"""

    url: Optional[str] = None
    """URL to open the plan in Warp Drive"""


class PlanArtifactResponse(BaseModel):
    """Response for retrieving a plan artifact."""

    artifact_type: Literal["PLAN"]
    """Type of the artifact"""

    artifact_uid: str
    """Unique identifier (UUID) for the artifact"""

    created_at: datetime
    """Timestamp when the artifact was created (RFC3339)"""

    data: PlanArtifactResponseData
    """Response data for a plan artifact, including current markdown content."""


class ScreenshotArtifactResponseData(BaseModel):
    """Response data for a screenshot artifact, including a signed download URL."""

    content_type: str
    """MIME type of the screenshot (e.g., image/png)"""

    download_url: str
    """Time-limited signed URL to download the screenshot"""

    expires_at: datetime
    """Timestamp when the download URL expires (RFC3339)"""

    description: Optional[str] = None
    """Optional description of the screenshot"""


class ScreenshotArtifactResponse(BaseModel):
    """Response for retrieving a screenshot artifact."""

    artifact_type: Literal["SCREENSHOT"]
    """Type of the artifact"""

    artifact_uid: str
    """Unique identifier (UUID) for the artifact"""

    created_at: datetime
    """Timestamp when the artifact was created (RFC3339)"""

    data: ScreenshotArtifactResponseData
    """Response data for a screenshot artifact, including a signed download URL."""


class FileArtifactResponseData(BaseModel):
    """Response data for a file artifact, including a signed download URL."""

    content_type: str
    """MIME type of the uploaded file"""

    download_url: str
    """Time-limited signed URL to download the file"""

    expires_at: datetime
    """Timestamp when the download URL expires (RFC3339)"""

    filename: str
    """Last path component of filepath"""

    filepath: str
    """Conversation-relative filepath for the uploaded file"""

    description: Optional[str] = None
    """Optional description of the file"""

    size_bytes: Optional[int] = None
    """Size of the uploaded file in bytes"""


class FileArtifactResponse(BaseModel):
    """Response for retrieving a file artifact."""

    artifact_type: Literal["FILE"]
    """Type of the artifact"""

    artifact_uid: str
    """Unique identifier (UUID) for the artifact"""

    created_at: datetime
    """Timestamp when the artifact was created (RFC3339)"""

    data: FileArtifactResponseData
    """Response data for a file artifact, including a signed download URL."""


AgentGetArtifactResponse: TypeAlias = Annotated[
    Union[PlanArtifactResponse, ScreenshotArtifactResponse, FileArtifactResponse],
    PropertyInfo(discriminator="artifact_type"),
]
