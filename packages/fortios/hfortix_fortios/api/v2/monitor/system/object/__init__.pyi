"""Type stubs for OBJECT category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .usage import Usage

__all__ = [
    "Usage",
    "Object",
]


class Object:
    """OBJECT API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    usage: Usage

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize object category with HTTP client."""
        ...
