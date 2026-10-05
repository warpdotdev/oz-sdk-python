# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["RunListHandoffAttachmentsResponse", "Attachment"]


class Attachment(BaseModel):
    """A handoff snapshot attachment exposed for download."""

    attachment_id: str
    """Identifier for the snapshot attachment within the run."""

    download_url: str
    """Time-limited signed URL to download the snapshot attachment."""

    filename: str
    """Original filename of the snapshot attachment."""

    mime_type: Optional[str] = None
    """MIME type of the snapshot attachment, if known."""


class RunListHandoffAttachmentsResponse(BaseModel):
    """Response body for listing handoff snapshot attachments."""

    attachments: List[Attachment]
    """
    Handoff snapshot attachments exposed by the latest ended execution. Empty when
    no ended execution exists or no files were uploaded.
    """
