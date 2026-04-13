# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "AgentGetArtifactResponse",
    "ScreenshotArtifactResponse",
    "ScreenshotArtifactResponseData",
    "FileArtifactResponse",
    "FileArtifactResponseData",
]


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
    Union[ScreenshotArtifactResponse, FileArtifactResponse], PropertyInfo(discriminator="artifact_type")
]
