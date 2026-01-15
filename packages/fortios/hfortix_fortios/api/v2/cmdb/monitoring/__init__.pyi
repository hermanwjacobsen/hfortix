"""Type stubs for MONITORING category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .npu_hpe import NpuHpe

__all__ = [
    "NpuHpe",
    "Monitoring",
]


class Monitoring:
    """MONITORING API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    npu_hpe: NpuHpe

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize monitoring category with HTTP client."""
        ...
