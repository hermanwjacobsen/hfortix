"""Type stubs for WEB_PROXY category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .debug_url import DebugUrl
    from .explicit import Explicit
    from .fast_fallback import FastFallback
    from .forward_server import ForwardServer
    from .forward_server_group import ForwardServerGroup
    from .global_ import Global
    from .isolator_server import IsolatorServer
    from .profile import Profile
    from .url_match import UrlMatch
    from .wisp import Wisp

__all__ = [
    "DebugUrl",
    "Explicit",
    "FastFallback",
    "ForwardServer",
    "ForwardServerGroup",
    "Global",
    "IsolatorServer",
    "Profile",
    "UrlMatch",
    "Wisp",
    "WebProxy",
]


class WebProxy:
    """WEB_PROXY API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    debug_url: DebugUrl
    explicit: Explicit
    fast_fallback: FastFallback
    forward_server: ForwardServer
    forward_server_group: ForwardServerGroup
    global_: Global
    isolator_server: IsolatorServer
    profile: Profile
    url_match: UrlMatch
    wisp: Wisp

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize web_proxy category with HTTP client."""
        ...
