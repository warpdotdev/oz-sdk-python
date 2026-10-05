# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["SchemaListResponse", "Version"]


class Version(BaseModel):
    schema_url: str
    """Root-relative path of this version's schema bundle."""

    schema_version: str


class SchemaListResponse(BaseModel):
    """The Factory file schema versions a server can describe."""

    current_version: str
    """The version a new Factory tree should declare."""

    versions: List[Version]
    """Every supported version, sorted by schema version."""
