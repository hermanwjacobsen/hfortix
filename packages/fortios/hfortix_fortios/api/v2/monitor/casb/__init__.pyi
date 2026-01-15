"""Type stubs for CASB category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .saas_application import SaasApplication

__all__ = [
    "Casb",
]


class Casb:
    """CASB API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    saas_application: SaasApplication

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize casb category with HTTP client."""
        ...
