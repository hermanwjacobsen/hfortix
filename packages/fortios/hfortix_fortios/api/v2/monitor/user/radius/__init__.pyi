"""Type stubs for RADIUS category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .get_test_connect import GetTestConnect
    from .test_connect import TestConnect

__all__ = [
    "GetTestConnect",
    "TestConnect",
    "Radius",
]


class Radius:
    """RADIUS API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    get_test_connect: GetTestConnect
    test_connect: TestConnect

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize radius category with HTTP client."""
        ...
