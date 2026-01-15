"""Type stubs for SECURITY_RATING category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .controls import Controls
    from .settings import Settings

__all__ = [
    "Controls",
    "Settings",
    "SecurityRating",
]


class SecurityRating:
    """SECURITY_RATING API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    controls: Controls
    settings: Settings

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize security_rating category with HTTP client."""
        ...
