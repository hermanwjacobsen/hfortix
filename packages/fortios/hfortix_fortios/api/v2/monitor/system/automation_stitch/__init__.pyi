"""Type stubs for AUTOMATION_STITCH category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .stats import Stats
    from .test import Test
    from .webhook import Webhook

__all__ = [
    "Stats",
    "Test",
    "Webhook",
    "AutomationStitch",
]


class AutomationStitch:
    """AUTOMATION_STITCH API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    stats: Stats
    test: Test
    webhook: Webhook

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize automation_stitch category with HTTP client."""
        ...
