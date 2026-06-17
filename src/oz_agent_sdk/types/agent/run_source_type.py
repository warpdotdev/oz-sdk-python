# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["RunSourceType"]

RunSourceType: TypeAlias = Literal[
    "LINEAR", "API", "SLACK", "LOCAL", "SCHEDULED_AGENT", "WEB_APP", "GITHUB_ACTION", "CLOUD_MODE", "CLI"
]
