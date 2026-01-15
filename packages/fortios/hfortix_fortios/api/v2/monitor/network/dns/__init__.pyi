"""Type stubs for DNS category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .latency import Latency

__all__ = [
    "Latency",
    "Dns",
]


class Dns:
    """DNS API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    latency: Latency

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize dns category with HTTP client."""
        ...
