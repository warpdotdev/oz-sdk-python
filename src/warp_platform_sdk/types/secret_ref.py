# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SecretRef"]


class SecretRef(BaseModel):
    """Reference to a managed secret by name."""

    name: str
    """Name of the managed secret."""
