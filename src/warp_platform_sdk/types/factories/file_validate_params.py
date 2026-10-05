# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["FileValidateParams", "File"]


class FileValidateParams(TypedDict, total=False):
    files: Required[Iterable[File]]
    """The Factory tree's resource files.

    Send factory.yaml and the candidate Agent, Automation, Runner, and Scorer paths;
    skill files are not parser inputs. Symlinks must not be followed.
    """


class File(TypedDict, total=False):
    content: Required[str]
    """UTF-8 file content, at most 2 MiB."""

    path: Required[str]
    """Repository-relative path, for example agents/triage/agent.md."""
