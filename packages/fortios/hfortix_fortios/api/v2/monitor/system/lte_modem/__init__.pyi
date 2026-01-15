"""Type stubs for LTE_MODEM category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .status import Status
    from .upgrade import Upgrade
    from .upload import Upload

__all__ = [
    "Status",
    "Upgrade",
    "Upload",
    "LteModem",
]


class LteModem:
    """LTE_MODEM API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    status: Status
    upgrade: Upgrade
    upload: Upload

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize lte_modem category with HTTP client."""
        ...
