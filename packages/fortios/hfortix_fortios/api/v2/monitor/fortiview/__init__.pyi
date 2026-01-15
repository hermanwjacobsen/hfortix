"""Type stubs for FORTIVIEW category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .historical_statistics import HistoricalStatistics
    from .realtime_proxy_statistics import RealtimeProxyStatistics
    from .realtime_statistics import RealtimeStatistics
    from .session import Session

__all__ = [
    "HistoricalStatistics",
    "RealtimeProxyStatistics",
    "RealtimeStatistics",
    "Fortiview",
]


class Fortiview:
    """FORTIVIEW API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    session: Session
    historical_statistics: HistoricalStatistics
    realtime_proxy_statistics: RealtimeProxyStatistics
    realtime_statistics: RealtimeStatistics

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize fortiview category with HTTP client."""
        ...
