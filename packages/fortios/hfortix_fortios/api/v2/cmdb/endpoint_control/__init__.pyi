"""Type stubs for ENDPOINT_CONTROL category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .fctems import Fctems
    from .fctems_override import FctemsOverride
    from .settings import Settings

__all__ = [
    "Fctems",
    "FctemsOverride",
    "Settings",
    "EndpointControl",
]


class EndpointControl:
    """ENDPOINT_CONTROL API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    fctems: Fctems
    fctems_override: FctemsOverride
    settings: Settings

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize endpoint_control category with HTTP client."""
        ...
