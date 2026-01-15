"""Type stubs for SDWAN category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .routes import Routes
    from .routes6 import Routes6
    from .routes_statistics import RoutesStatistics

__all__ = [
    "Routes",
    "Routes6",
    "RoutesStatistics",
    "Sdwan",
]


class Sdwan:
    """SDWAN API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    routes: Routes
    routes6: Routes6
    routes_statistics: RoutesStatistics

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize sdwan category with HTTP client."""
        ...
