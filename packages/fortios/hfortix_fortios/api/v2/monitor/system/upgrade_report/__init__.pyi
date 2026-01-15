"""Type stubs for UPGRADE_REPORT category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .current import Current
    from .exists import Exists
    from .saved import Saved

__all__ = [
    "Current",
    "Exists",
    "Saved",
    "UpgradeReport",
]


class UpgradeReport:
    """UPGRADE_REPORT API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    current: Current
    exists: Exists
    saved: Saved

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize upgrade_report category with HTTP client."""
        ...
