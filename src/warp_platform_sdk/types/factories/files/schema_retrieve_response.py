# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from ...._models import BaseModel

__all__ = ["SchemaRetrieveResponse"]


class SchemaRetrieveResponse(BaseModel):
    """
    Every JSON Schema document describing one Factory file schema version.
    The envelope is plain JSON; each value in `documents` is a JSON Schema
    2020-12 document keyed by its `$id`.
    """

    documents: Dict[str, object]
    """Schema documents keyed by file name, which is also each document's $id."""

    schema_version: str
