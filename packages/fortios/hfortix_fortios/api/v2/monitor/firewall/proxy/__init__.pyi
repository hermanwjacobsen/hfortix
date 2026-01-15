"""Type stubs for PROXY category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .sessions import Sessions

__all__ = [
    "Sessions",
    "Proxy",
]


class Proxy:
    """PROXY API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    sessions: Sessions

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize proxy category with HTTP client."""
        ...
