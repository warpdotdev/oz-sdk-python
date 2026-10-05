# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["HarnessAuthSecretsParam"]


class HarnessAuthSecretsParam(TypedDict, total=False):
    """
    Authentication secrets for third-party harnesses.
    Only the secret for the harness specified gets injected into the environment.
    """

    claude_auth_secret_name: str
    """
    Name of a managed secret for Claude Code harness authentication. The secret must
    exist within the caller's personal or team scope. Only applicable when harness
    type is "claude".
    """

    codex_auth_secret_name: str
    """
    Name of a managed secret for Codex harness authentication. The secret must exist
    within the caller's personal or team scope. Only applicable when harness type is
    "codex".
    """
