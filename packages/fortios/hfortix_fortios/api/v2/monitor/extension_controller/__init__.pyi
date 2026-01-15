"""Type stubs for EXTENSION_CONTROLLER category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .fortigate import Fortigate
    from .lan_extension_vdom_status import LanExtensionVdomStatus

__all__ = [
    "Fortigate",
    "LanExtensionVdomStatus",
    "ExtensionController",
]


class ExtensionController:
    """EXTENSION_CONTROLLER API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    fortigate: Fortigate
    lan_extension_vdom_status: LanExtensionVdomStatus

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize extension_controller category with HTTP client."""
        ...
