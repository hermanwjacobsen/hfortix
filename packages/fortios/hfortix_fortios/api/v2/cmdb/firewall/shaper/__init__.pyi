"""Type stubs for SHAPER category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .per_ip_shaper import PerIpShaper
    from .traffic_shaper import TrafficShaper

__all__ = [
    "PerIpShaper",
    "TrafficShaper",
    "Shaper",
]


class Shaper:
    """SHAPER API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    per_ip_shaper: PerIpShaper
    traffic_shaper: TrafficShaper

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize shaper category with HTTP client."""
        ...
