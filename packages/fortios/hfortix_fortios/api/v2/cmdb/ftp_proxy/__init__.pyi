"""Type stubs for FTP_PROXY category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .explicit import Explicit

__all__ = [
    "Explicit",
    "FtpProxy",
]


class FtpProxy:
    """FTP_PROXY API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    explicit: Explicit

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize ftp_proxy category with HTTP client."""
        ...
