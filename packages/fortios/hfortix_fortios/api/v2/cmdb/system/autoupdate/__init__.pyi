"""Type stubs for AUTOUPDATE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .schedule import Schedule

__all__ = [
    "Schedule",
    "Autoupdate",
]


class Autoupdate:
    """AUTOUPDATE API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    schedule: Schedule

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize autoupdate category with HTTP client."""
        ...
