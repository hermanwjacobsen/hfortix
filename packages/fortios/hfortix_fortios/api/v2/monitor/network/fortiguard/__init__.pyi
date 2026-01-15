"""Type stubs for FORTIGUARD category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .live_services_latency import LiveServicesLatency

__all__ = [
    "LiveServicesLatency",
    "Fortiguard",
]


class Fortiguard:
    """FORTIGUARD API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    live_services_latency: LiveServicesLatency

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize fortiguard category with HTTP client."""
        ...
