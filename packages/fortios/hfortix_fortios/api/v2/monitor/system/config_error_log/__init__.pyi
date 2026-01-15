"""Type stubs for CONFIG_ERROR_LOG category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .download import Download

__all__ = [
    "Download",
    "ConfigErrorLog",
]


class ConfigErrorLog:
    """CONFIG_ERROR_LOG API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    download: Download

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize config_error_log category with HTTP client."""
        ...
