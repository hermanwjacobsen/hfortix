"""Type stubs for AZURE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .application_list import ApplicationList

__all__ = [
    "Azure",
]


class Azure:
    """AZURE API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    application_list: ApplicationList

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize azure category with HTTP client."""
        ...
