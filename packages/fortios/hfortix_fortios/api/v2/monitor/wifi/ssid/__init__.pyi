"""Type stubs for SSID category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .generate_keys import GenerateKeys

__all__ = [
    "GenerateKeys",
    "Ssid",
]


class Ssid:
    """SSID API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    generate_keys: GenerateKeys

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize ssid category with HTTP client."""
        ...
