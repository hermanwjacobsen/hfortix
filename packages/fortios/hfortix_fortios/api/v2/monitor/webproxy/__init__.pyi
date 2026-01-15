"""Type stubs for WEBPROXY category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .pacfile import Pacfile

__all__ = [
    "Webproxy",
]


class Webproxy:
    """WEBPROXY API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    pacfile: Pacfile

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize webproxy category with HTTP client."""
        ...
