from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `warp_agent_sdk.resources` module.

    This is used so that we can lazily import `warp_agent_sdk.resources` only when
    needed *and* so that users can just import `warp_agent_sdk` and reference `warp_agent_sdk.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("warp_agent_sdk.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
