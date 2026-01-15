"""Type stubs for USB_DEVICE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .eject import Eject

__all__ = [
    "Eject",
    "UsbDevice",
]


class UsbDevice:
    """USB_DEVICE API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    eject: Eject

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize usb_device category with HTTP client."""
        ...
