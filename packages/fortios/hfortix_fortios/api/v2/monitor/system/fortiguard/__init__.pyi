"""Type stubs for FORTIGUARD category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .clear_statistics import ClearStatistics
    from .manual_update import ManualUpdate
    from .server_info import ServerInfo
    from .test_availability import TestAvailability
    from .update import Update

__all__ = [
    "ClearStatistics",
    "ManualUpdate",
    "ServerInfo",
    "TestAvailability",
    "Update",
    "Fortiguard",
]


class Fortiguard:
    """FORTIGUARD API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    clear_statistics: ClearStatistics
    manual_update: ManualUpdate
    server_info: ServerInfo
    test_availability: TestAvailability
    update: Update

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize fortiguard category with HTTP client."""
        ...
