"""Type stubs for ISL_LOCKDOWN category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .status import Status
    from .update import Update

__all__ = [
    "Status",
    "Update",
    "IslLockdown",
]


class IslLockdown:
    """ISL_LOCKDOWN API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    status: Status
    update: Update

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize isl_lockdown category with HTTP client."""
        ...
