# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ErrorCode"]

ErrorCode: TypeAlias = Literal[
    "insufficient_credits",
    "feature_not_available",
    "external_authentication_required",
    "not_authorized",
    "invalid_request",
    "resource_not_found",
    "budget_exceeded",
    "integration_disabled",
    "integration_not_configured",
    "operation_not_supported",
    "environment_setup_failed",
    "content_policy_violation",
    "conflict",
    "authentication_required",
    "resource_unavailable",
    "internal_error",
]
