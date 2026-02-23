# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["AgentGetArtifactResponse", "Data"]


class Data(BaseModel):
    """Response data for a screenshot artifact, including a signed download URL."""

    content_type: str
    """MIME type of the screenshot (e.g., image/png)"""

    download_url: str
    """Time-limited signed URL to download the screenshot"""

    expires_at: datetime
    """Timestamp when the download URL expires (RFC3339)"""

    description: Optional[str] = None
    """Optional description of the screenshot"""


class AgentGetArtifactResponse(BaseModel):
    """Response for artifact retrieval. Currently supports screenshot artifacts."""

    artifact_type: str
    """Type of the artifact (e.g., SCREENSHOT)"""

    artifact_uid: str
    """Unique identifier (UUID) for the artifact"""

    created_at: datetime
    """Timestamp when the artifact was created (RFC3339)"""

    data: Data
    """Response data for a screenshot artifact, including a signed download URL."""
