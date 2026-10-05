# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FileValidateResponse", "DeferredResolution", "Diagnostic", "ValidationScope"]


class DeferredResolution(BaseModel):
    """One authored value the validator did not resolve."""

    field: str
    """The authored field, for example triggers[0].filter.teams."""

    kind: str
    """The resolution that was skipped, for example linear_name_alias."""

    path: str


class Diagnostic(BaseModel):
    """A source-located validation problem."""

    code: str
    """Stable diagnostic code, for example FF_UNKNOWN_FIELD."""

    column: int
    """1-based column. A problem with no source position uses 1."""

    line: int
    """1-based line. A problem with no source position uses 1."""

    message: str

    path: str
    """Repository-relative path of the file the problem is in."""


class ValidationScope(BaseModel):
    """What each validation tier did for this request."""

    parser: Literal["checked", "not_run"]

    state_dependent: Literal["not_checked"]

    state_independent: Literal["checked", "not_run"]


class FileValidateResponse(BaseModel):
    """The outcome of validating a Factory tree.

    `valid` covers the parser and
    the state-independent checks only.
    """

    deferred_resolutions: List[DeferredResolution]
    """Authored values whose existence was deliberately not proven.

    A deferred value is not invalid.
    """

    diagnostics: List[Diagnostic]

    schema_version: str
    """
    The version factory.yaml declares, or the parser's default when the field is
    omitted.
    """

    state_dependent_checks_not_run: List[str]
    """
    The checks this endpoint never performs, listed even when the tree is clean, so
    a caller cannot read a pass as an apply guarantee.
    """

    valid: bool
    """True when no parser or state-independent diagnostic was found.

    It does not mean the tree will apply.
    """

    validation_scope: ValidationScope
    """What each validation tier did for this request."""
