"""Type stubs for CONFIG category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .backup import Backup
    from .restore import Restore
    from .restore_status import RestoreStatus
    from .usb_filelist import UsbFilelist

__all__ = [
    "Backup",
    "Restore",
    "RestoreStatus",
    "UsbFilelist",
    "Config",
]


class Config:
    """CONFIG API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    backup: Backup
    restore: Restore
    restore_status: RestoreStatus
    usb_filelist: UsbFilelist

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize config category with HTTP client."""
        ...
