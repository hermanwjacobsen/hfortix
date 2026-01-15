"""Type stubs for MODEM3G category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .custom import Custom

__all__ = [
    "Custom",
    "Modem3g",
]


class Modem3g:
    """MODEM3G API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    custom: Custom

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize modem3g category with HTTP client."""
        ...
