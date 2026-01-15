"""Type stubs for ZTNA category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .reverse_connector import ReverseConnector
    from .traffic_forward_proxy import TrafficForwardProxy
    from .web_portal import WebPortal
    from .web_portal_bookmark import WebPortalBookmark
    from .web_proxy import WebProxy

__all__ = [
    "ReverseConnector",
    "TrafficForwardProxy",
    "WebPortal",
    "WebPortalBookmark",
    "WebProxy",
    "Ztna",
]


class Ztna:
    """ZTNA API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    reverse_connector: ReverseConnector
    traffic_forward_proxy: TrafficForwardProxy
    web_portal: WebPortal
    web_portal_bookmark: WebPortalBookmark
    web_proxy: WebProxy

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize ztna category with HTTP client."""
        ...
