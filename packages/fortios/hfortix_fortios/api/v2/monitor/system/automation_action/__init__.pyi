"""Type stubs for AUTOMATION_ACTION category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .stats import Stats

__all__ = [
    "Stats",
    "AutomationAction",
]


class AutomationAction:
    """AUTOMATION_ACTION API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    stats: Stats

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize automation_action category with HTTP client."""
        ...
