"""Type stubs for EXTENDER_CONTROLLER category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .extender import Extender

__all__ = [
    "ExtenderController",
]


class ExtenderController:
    """EXTENDER_CONTROLLER API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    extender: Extender

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize extender_controller category with HTTP client."""
        ...
