"""Type stubs for WEB_UI category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .custom_language import CustomLanguage
    from .language import Language

__all__ = [
    "WebUi",
]


class WebUi:
    """WEB_UI API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    custom_language: CustomLanguage
    language: Language

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize web_ui category with HTTP client."""
        ...
