"""Type stubs for GEOIP category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .geoip_query import GeoipQuery

__all__ = [
    "Geoip",
]


class Geoip:
    """GEOIP API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    geoip_query: GeoipQuery

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize geoip category with HTTP client."""
        ...
