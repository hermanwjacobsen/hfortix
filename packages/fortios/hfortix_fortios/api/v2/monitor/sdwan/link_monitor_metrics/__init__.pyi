"""Type stubs for LINK_MONITOR_METRICS category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .report import Report

__all__ = [
    "Report",
    "LinkMonitorMetrics",
]


class LinkMonitorMetrics:
    """LINK_MONITOR_METRICS API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    report: Report

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize link_monitor_metrics category with HTTP client."""
        ...
