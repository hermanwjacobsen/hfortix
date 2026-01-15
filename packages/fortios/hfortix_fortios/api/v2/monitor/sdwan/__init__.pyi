"""Type stubs for SDWAN category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .link_monitor_metrics import LinkMonitorMetrics

__all__ = [
    "Sdwan",
]


class Sdwan:
    """SDWAN API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    link_monitor_metrics: LinkMonitorMetrics

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize sdwan category with HTTP client."""
        ...
