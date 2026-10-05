# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ScorerListResultsResponse",
    "ScoringRunUsage",
    "ScoringRunUsageModelTokenUsage",
    "ScoringRunUsageUsageByCategory",
    "ScoringRunUsageUsageByCategoryByokInferenceUsage",
    "ScoringRunUsageUsageByCategoryByokInferenceUsageCostInCents",
    "ScoringRunUsageUsageByCategoryByokInferenceUsageTokenCount",
    "ScoringRunUsageUsageByCategoryCustomEndpointInferenceUsage",
    "ScoringRunUsageUsageByCategoryCustomEndpointInferenceUsageCostInCents",
    "ScoringRunUsageUsageByCategoryCustomEndpointInferenceUsageTokenCount",
    "ScoringRunUsageUsageByCategoryDirectAPIInferenceUsage",
    "ScoringRunUsageUsageByCategoryDirectAPIInferenceUsageCostInCents",
    "ScoringRunUsageUsageByCategoryDirectAPIInferenceUsageTokenCount",
]


class ScoringRunUsageModelTokenUsage(BaseModel):
    """Tokens consumed by a single model over a run."""

    api_model_id: str = FieldInfo(alias="model_id")
    """Identifier of the model that served the inference.

    For `warp` and `byok` usage this is a model id drawn from the same set as
    `agent_config.model_id`. For `custom_endpoint` usage this is the caller's own
    configuration key for the endpoint.
    """

    total_tokens: int
    """Total tokens this model consumed, across every usage category."""

    usage_type: Literal["warp", "byok", "custom_endpoint"]
    """How a model's inference was accessed:

    - warp: through Warp-provided model access
    - byok: through the caller's own provider API key
    - custom_endpoint: through a caller-configured model endpoint
    """

    tokens_by_category: Optional[Dict[str, int]] = None
    """
    total_tokens split by the kind of work the tokens were spent on, keyed by usage
    category (e.g., primary_agent, tool_summarization, etc).
    """


class ScoringRunUsageUsageByCategoryByokInferenceUsageCostInCents(BaseModel):
    """
    Charged cost of LLM inference in US cents, split by token type.
    Omitted when the data is not available.
    """

    input_cache_read_cost_in_cents: float
    """Cost of cache-read input tokens, in US cents."""

    input_cache_write_cost_in_cents: float
    """Cost of cache-write input tokens, in US cents."""

    input_cost_in_cents: float
    """Cost of non-cached input tokens, in US cents."""

    output_cost_in_cents: float
    """Cost of output tokens, in US cents."""


class ScoringRunUsageUsageByCategoryByokInferenceUsageTokenCount(BaseModel):
    """A per-token-type token count."""

    input: int
    """Count of non-cached input tokens."""

    input_cache_read: int
    """Count of cache-read input tokens."""

    input_cache_write: int
    """Count of cache-write input tokens."""

    output: int
    """Count of output tokens."""


class ScoringRunUsageUsageByCategoryByokInferenceUsage(BaseModel):
    """
    Full token count and charged-cost detail for inference usage.
    The counts and cost describe the same usage (e.g. token_count.input
    tokens cost cost_in_cents.input_cost_in_cents in total).
    """

    cost_in_cents: ScoringRunUsageUsageByCategoryByokInferenceUsageCostInCents
    """
    Charged cost of LLM inference in US cents, split by token type. Omitted when the
    data is not available.
    """

    token_count: ScoringRunUsageUsageByCategoryByokInferenceUsageTokenCount
    """A per-token-type token count."""

    web_search_cost_in_cents: float
    """Total cost of those web searches, in US cents."""

    web_search_count: int
    """Number of web searches performed by this model."""


class ScoringRunUsageUsageByCategoryCustomEndpointInferenceUsageCostInCents(BaseModel):
    """
    Charged cost of LLM inference in US cents, split by token type.
    Omitted when the data is not available.
    """

    input_cache_read_cost_in_cents: float
    """Cost of cache-read input tokens, in US cents."""

    input_cache_write_cost_in_cents: float
    """Cost of cache-write input tokens, in US cents."""

    input_cost_in_cents: float
    """Cost of non-cached input tokens, in US cents."""

    output_cost_in_cents: float
    """Cost of output tokens, in US cents."""


class ScoringRunUsageUsageByCategoryCustomEndpointInferenceUsageTokenCount(BaseModel):
    """A per-token-type token count."""

    input: int
    """Count of non-cached input tokens."""

    input_cache_read: int
    """Count of cache-read input tokens."""

    input_cache_write: int
    """Count of cache-write input tokens."""

    output: int
    """Count of output tokens."""


class ScoringRunUsageUsageByCategoryCustomEndpointInferenceUsage(BaseModel):
    """
    Full token count and charged-cost detail for inference usage.
    The counts and cost describe the same usage (e.g. token_count.input
    tokens cost cost_in_cents.input_cost_in_cents in total).
    """

    cost_in_cents: ScoringRunUsageUsageByCategoryCustomEndpointInferenceUsageCostInCents
    """
    Charged cost of LLM inference in US cents, split by token type. Omitted when the
    data is not available.
    """

    token_count: ScoringRunUsageUsageByCategoryCustomEndpointInferenceUsageTokenCount
    """A per-token-type token count."""

    web_search_cost_in_cents: float
    """Total cost of those web searches, in US cents."""

    web_search_count: int
    """Number of web searches performed by this model."""


class ScoringRunUsageUsageByCategoryDirectAPIInferenceUsageCostInCents(BaseModel):
    """
    Charged cost of LLM inference in US cents, split by token type.
    Omitted when the data is not available.
    """

    input_cache_read_cost_in_cents: float
    """Cost of cache-read input tokens, in US cents."""

    input_cache_write_cost_in_cents: float
    """Cost of cache-write input tokens, in US cents."""

    input_cost_in_cents: float
    """Cost of non-cached input tokens, in US cents."""

    output_cost_in_cents: float
    """Cost of output tokens, in US cents."""


class ScoringRunUsageUsageByCategoryDirectAPIInferenceUsageTokenCount(BaseModel):
    """A per-token-type token count."""

    input: int
    """Count of non-cached input tokens."""

    input_cache_read: int
    """Count of cache-read input tokens."""

    input_cache_write: int
    """Count of cache-write input tokens."""

    output: int
    """Count of output tokens."""


class ScoringRunUsageUsageByCategoryDirectAPIInferenceUsage(BaseModel):
    """
    Full token count and charged-cost detail for inference usage.
    The counts and cost describe the same usage (e.g. token_count.input
    tokens cost cost_in_cents.input_cost_in_cents in total).
    """

    cost_in_cents: ScoringRunUsageUsageByCategoryDirectAPIInferenceUsageCostInCents
    """
    Charged cost of LLM inference in US cents, split by token type. Omitted when the
    data is not available.
    """

    token_count: ScoringRunUsageUsageByCategoryDirectAPIInferenceUsageTokenCount
    """A per-token-type token count."""

    web_search_cost_in_cents: float
    """Total cost of those web searches, in US cents."""

    web_search_count: int
    """Number of web searches performed by this model."""


class ScoringRunUsageUsageByCategory(BaseModel):
    """
    Usage charged for a single usage category, broken down by usage type
    (direct API/BYOK/custom endpoint) and, within each, by model ID.
    """

    platform_usage_in_cents: float
    """Platform usage charged for this category, in US cents."""

    byok_inference_usage: Optional[Dict[str, ScoringRunUsageUsageByCategoryByokInferenceUsage]] = None
    """Inference usage charged using a user's own API key, keyed by model ID."""

    custom_endpoint_inference_usage: Optional[Dict[str, ScoringRunUsageUsageByCategoryCustomEndpointInferenceUsage]] = (
        None
    )
    """
    Inference usage charged using a custom endpoint, keyed by the custom model's
    config key.
    """

    direct_api_inference_usage: Optional[Dict[str, ScoringRunUsageUsageByCategoryDirectAPIInferenceUsage]] = None
    """Inference usage incurred through Warp-provided model access, keyed by model ID."""


class ScoringRunUsage(BaseModel):
    """Resource usage information for the run"""

    compute_cost: Optional[float] = None
    """Credits consumed by compute resources for the run"""

    compute_cost_usd: Optional[float] = None
    """What the run's hosted compute was billed at, in US dollars.

    Runs that predate billed-amount tracking fall back to an estimated cost.
    """

    inference_cost: Optional[float] = None
    """Credits consumed by LLM inference for the run"""

    inference_cost_usd: Optional[float] = None
    """What the run's LLM inference was billed at, in US dollars.

    Runs that predate billed-amount tracking fall back to an estimated cost.
    """

    api_model_token_usage: Optional[List[ScoringRunUsageModelTokenUsage]] = FieldInfo(
        alias="model_token_usage", default=None
    )
    """
    The models that actually served inference for the run, with the tokens each
    consumed. Used to discover what an auto-routing model resolves to. If a run is
    terminated before inference is complete, output a zero-token entry for that
    model. Omits runs that use a third-party harness, whose per-model usage is not
    tracked by Warp.
    """

    platform_cost: Optional[float] = None
    """Credits consumed by platform usage for the run"""

    platform_cost_usd: Optional[float] = None
    """What the run's platform usage was billed at, in US dollars.

    Runs that predate billed-amount tracking fall back to an estimated cost.
    """

    total_tokens: Optional[int] = None
    """
    Total LLM token count (summed across every usage category and model) for the
    run's conversation. Omitted when the data is not available.
    """

    usage_by_category: Optional[Dict[str, ScoringRunUsageUsageByCategory]] = None
    """
    Full-granularity token and charged-cost breakdown for the run's conversation,
    keyed by usage category (for example, primary_agent or conversation_compaction)
    and model id. Omitted when the data is not available.
    """


class ScorerListResultsResponse(BaseModel):
    attempted_at: datetime
    """When the scorer last attempted this run"""

    is_in_flight: bool
    """
    True when a non-terminal judge run currently holds this pair. Independent of
    status/classification: a previous live classification stays visible while a
    replacement judge runs.
    """

    run_id: str
    """The selected agent run that anchors the scoring attempt"""

    status: str
    """
    Outcome of a scoring attempt: "scored", "failed", or "in_flight" (no live score
    yet and a judge is currently running). A failed or in_flight attempt has no
    classification. A scored attempt whose is_in_flight is also true has a live
    classification while a replacement judge runs.
    """

    classification: Optional[str] = None
    """The chosen classification; absent when the attempt failed"""

    conversation_id: Optional[str] = None
    """Conversation whose transcript was judged"""

    conversation_title: Optional[str] = None
    """Title of the judged conversation"""

    outcome: Optional[Literal["pass", "fail"]] = None
    """
    Pass/fail verdict of a recorded score, derived at read time against the
    evaluation's current threshold rather than frozen at scoring time — editing the
    threshold retroactively changes the outcome of already-scored runs. Today this
    is "pass" or "fail"; clients should tolerate additional values so future
    non-scoreable verdicts (for example, excluded from scoring) do not break them.
    Do not use result_count as a pass-rate denominator: only pass and fail count.
    """

    score: Optional[float] = None
    """
    Numeric score of the classified label, resolved from the attempt's config
    snapshot at scoring time. Absent when the attempt failed.
    """

    scored_at: Optional[datetime] = None
    """When the live score was recorded; absent for failed attempts"""

    scoring_run_id: Optional[str] = None
    """
    The Warp run that performed the judging; absent when scoring was never
    dispatched for this attempt
    """

    scoring_run_time: Optional[str] = None
    """Total runtime of the scoring run as an ISO 8601 duration.

    Absent when there is no scoring run or its execution duration is not yet
    available.
    """

    scoring_run_usage: Optional[ScoringRunUsage] = None
    """Resource usage information for the run"""
