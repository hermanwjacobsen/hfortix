"""Type stubs for LOGDISK category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .format import Format

__all__ = [
    "Format",
    "Logdisk",
]


class Logdisk:
    """LOGDISK API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    format: Format

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize logdisk category with HTTP client."""
        ...
