"""Type stubs for IKE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .clear import Clear

__all__ = [
    "Clear",
    "Ike",
]


class Ike:
    """IKE API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    clear: Clear

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize ike category with HTTP client."""
        ...
