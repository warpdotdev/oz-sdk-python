# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AgentGetRunByExternalReferenceResponse"]


class AgentGetRunByExternalReferenceResponse(BaseModel):
    """Response for a run reverse-lookup by external reference URL."""

    run_id: str
    """The ID of the run that produced the external reference."""
