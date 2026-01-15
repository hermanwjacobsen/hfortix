"""Type stubs for CUSTOM_LANGUAGE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .create import Create
    from .download import Download
    from .update import Update

__all__ = [
    "Create",
    "Download",
    "Update",
    "CustomLanguage",
]


class CustomLanguage:
    """CUSTOM_LANGUAGE API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    create: Create
    download: Download
    update: Update

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize custom_language category with HTTP client."""
        ...
