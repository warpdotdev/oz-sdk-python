# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AwsInferenceProviderConfigParam"]


class AwsInferenceProviderConfigParam(TypedDict, total=False):
    """
    Configures AWS Bedrock as the LLM inference provider for this
    agent or run.
    """

    disabled: bool
    """If true, opt out of Bedrock at this layer."""

    region: str
    """AWS region used for STS when assuming the Bedrock inference role."""

    role_arn: str
    """IAM role ARN to assume when calling Bedrock."""
