# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .aws_inference_provider_config_param import AwsInferenceProviderConfigParam

__all__ = ["InferenceProvidersConfigParam"]


class InferenceProvidersConfigParam(TypedDict, total=False):
    """Inference provider settings used for LLM calls."""

    aws: AwsInferenceProviderConfigParam
    """Configures AWS Bedrock as the LLM inference provider for this agent or run."""
