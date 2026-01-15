"""Type stubs for FIRMWARE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .extension_device import ExtensionDevice

__all__ = [
    "ExtensionDevice",
    "Firmware",
]


class Firmware:
    """FIRMWARE API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    extension_device: ExtensionDevice

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize firmware category with HTTP client."""
        ...
