"""Type stubs for TACACS_PLUS category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .test import Test

__all__ = [
    "Test",
    "TacacsPlus",
]


class TacacsPlus:
    """TACACS_PLUS API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    test: Test

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize tacacs_plus category with HTTP client."""
        ...
