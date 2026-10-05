# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["RunSourceType"]

RunSourceType: TypeAlias = Literal[
    "LINEAR",
    "API",
    "MCP",
    "SLACK",
    "TEAMS",
    "LOCAL",
    "SCHEDULED_AGENT",
    "WEB_APP",
    "GITHUB_ACTION",
    "CLOUD_MODE",
    "CLI",
    "JIRA",
    "SELF_IMPROVEMENT",
    "GITHUB_WEBHOOK",
    "GITLAB_WEBHOOK",
    "AZURE_DEVOPS_WEBHOOK",
    "AUTOFIX",
    "RUN_SCORER",
    "ORCHESTRATION",
    "BENCHMARK_TRIAL",
    "CREATE_BENCHMARK_TASK",
    "CUSTOM_WEBHOOK",
]
