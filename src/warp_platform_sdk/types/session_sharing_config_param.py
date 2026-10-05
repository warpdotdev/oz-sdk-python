# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SessionSharingConfigParam"]


class SessionSharingConfigParam(TypedDict, total=False):
    """
    Configures sharing behavior for the run's shared session; when set,
    the worker emits `--share public:<level>` and the bundled Warp
    client applies an anyone-with-link ACL to the shared session once it
    has bootstrapped. The same ACL is mirrored onto the backing
    conversation so link viewers can read it without being on the run's
    team, subject to the workspace-level anyone-with-link sharing
    setting.
    """

    public_access: Literal["VIEWER", "EDITOR"]
    """
    Grants anyone-with-link access at the specified level to the run's shared
    session and backing conversation; link viewers must still be authenticated Warp
    users (anonymous reads are not supported in this release).

    - VIEWER: link viewers can read the session and conversation.
    - EDITOR: link viewers can also interact with the session.
    """
