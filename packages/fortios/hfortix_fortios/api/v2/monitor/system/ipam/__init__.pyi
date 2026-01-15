"""Type stubs for IPAM category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .list import List
    from .status import Status
    from .utilization import Utilization

__all__ = [
    "List",
    "Status",
    "Utilization",
    "Ipam",
]


class Ipam:
    """IPAM API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    list: List
    status: Status
    utilization: Utilization

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize ipam category with HTTP client."""
        ...
