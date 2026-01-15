"""Type stubs for VDOM category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .add_license import AddLicense

__all__ = [
    "AddLicense",
    "Vdom",
]


class Vdom:
    """VDOM API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    add_license: AddLicense

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize vdom category with HTTP client."""
        ...
