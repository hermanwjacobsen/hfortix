"""Type stubs for EXTENSION_CONTROLLER category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .dataplan import Dataplan
    from .extender import Extender
    from .extender_profile import ExtenderProfile
    from .extender_vap import ExtenderVap
    from .fortigate import Fortigate
    from .fortigate_profile import FortigateProfile

__all__ = [
    "Dataplan",
    "Extender",
    "ExtenderProfile",
    "ExtenderVap",
    "Fortigate",
    "FortigateProfile",
    "ExtensionController",
]


class ExtensionController:
    """EXTENSION_CONTROLLER API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    dataplan: Dataplan
    extender: Extender
    extender_profile: ExtenderProfile
    extender_vap: ExtenderVap
    fortigate: Fortigate
    fortigate_profile: FortigateProfile

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize extension_controller category with HTTP client."""
        ...
