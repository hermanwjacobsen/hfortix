"""Type stubs for TRAFFIC_HISTORY category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .enable_app_bandwidth_tracking import EnableAppBandwidthTracking
    from .interface import Interface
    from .top_applications import TopApplications

__all__ = [
    "EnableAppBandwidthTracking",
    "Interface",
    "TopApplications",
    "TrafficHistory",
]


class TrafficHistory:
    """TRAFFIC_HISTORY API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    enable_app_bandwidth_tracking: EnableAppBandwidthTracking
    interface: Interface
    top_applications: TopApplications

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize traffic_history category with HTTP client."""
        ...
