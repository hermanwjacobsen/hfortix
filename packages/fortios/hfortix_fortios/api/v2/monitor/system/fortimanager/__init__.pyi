"""Type stubs for FORTIMANAGER category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .backup_action import BackupAction
    from .backup_details import BackupDetails
    from .backup_summary import BackupSummary

__all__ = [
    "BackupAction",
    "BackupDetails",
    "BackupSummary",
    "Fortimanager",
]


class Fortimanager:
    """FORTIMANAGER API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    backup_action: BackupAction
    backup_details: BackupDetails
    backup_summary: BackupSummary

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize fortimanager category with HTTP client."""
        ...
