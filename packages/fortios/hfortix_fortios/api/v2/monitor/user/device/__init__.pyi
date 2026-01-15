"""Type stubs for DEVICE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .iot_query import IotQuery
    from .purdue_level import PurdueLevel
    from .query import Query
    from .stats import Stats

__all__ = [
    "IotQuery",
    "PurdueLevel",
    "Query",
    "Stats",
    "Device",
]


class Device:
    """DEVICE API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    iot_query: IotQuery
    purdue_level: PurdueLevel
    query: Query
    stats: Stats

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize device category with HTTP client."""
        ...
