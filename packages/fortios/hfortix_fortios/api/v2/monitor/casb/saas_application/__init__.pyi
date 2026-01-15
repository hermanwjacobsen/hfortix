"""Type stubs for SAAS_APPLICATION category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .details import Details

__all__ = [
    "Details",
    "SaasApplication",
]


class SaasApplication:
    """SAAS_APPLICATION API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    details: Details

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize saas_application category with HTTP client."""
        ...
