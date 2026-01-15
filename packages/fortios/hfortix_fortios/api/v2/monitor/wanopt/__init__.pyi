"""Type stubs for WANOPT category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .history import History
    from .peer_stats import PeerStats
    from .webcache import Webcache

__all__ = [
    "Wanopt",
]


class Wanopt:
    """WANOPT API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    history: History
    peer_stats: PeerStats
    webcache: Webcache

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize wanopt category with HTTP client."""
        ...
