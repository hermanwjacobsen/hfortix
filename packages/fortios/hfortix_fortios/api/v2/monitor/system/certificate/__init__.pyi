"""Type stubs for CERTIFICATE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .download import Download
    from .read_info import ReadInfo

__all__ = [
    "Download",
    "ReadInfo",
    "Certificate",
]


class Certificate:
    """CERTIFICATE API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    download: Download
    read_info: ReadInfo

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize certificate category with HTTP client."""
        ...
