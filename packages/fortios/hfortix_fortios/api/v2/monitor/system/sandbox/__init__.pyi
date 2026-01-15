"""Type stubs for SANDBOX category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .cloud_regions import CloudRegions
    from .connection import Connection
    from .detect import Detect
    from .stats import Stats
    from .status import Status

__all__ = [
    "CloudRegions",
    "Connection",
    "Detect",
    "Stats",
    "Status",
    "Sandbox",
]


class Sandbox:
    """SANDBOX API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    cloud_regions: CloudRegions
    connection: Connection
    detect: Detect
    stats: Stats
    status: Status

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize sandbox category with HTTP client."""
        ...
