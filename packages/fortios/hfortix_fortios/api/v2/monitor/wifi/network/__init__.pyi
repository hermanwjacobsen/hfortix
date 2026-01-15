"""Type stubs for NETWORK category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .connect import Connect
    from .list import List
    from .scan import Scan
    from .status import Status

__all__ = [
    "Connect",
    "List",
    "Scan",
    "Status",
    "Network",
]


class Network:
    """NETWORK API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    connect: Connect
    list: List
    scan: Scan
    status: Status

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize network category with HTTP client."""
        ...
