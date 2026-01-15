"""Type stubs for SYSTEM category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .fabric_admin_lockout_exists_on_firmware_update import FabricAdminLockoutExistsOnFirmwareUpdate
    from .fabric_time_in_sync import FabricTimeInSync
    from .psirt_vulnerabilities import PsirtVulnerabilities

__all__ = [
    "FabricAdminLockoutExistsOnFirmwareUpdate",
    "FabricTimeInSync",
    "PsirtVulnerabilities",
    "System",
]


class System:
    """SYSTEM API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    fabric_admin_lockout_exists_on_firmware_update: FabricAdminLockoutExistsOnFirmwareUpdate
    fabric_time_in_sync: FabricTimeInSync
    psirt_vulnerabilities: PsirtVulnerabilities

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize system category with HTTP client."""
        ...
