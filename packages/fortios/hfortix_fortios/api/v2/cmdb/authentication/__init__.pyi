"""Type stubs for AUTHENTICATION category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .rule import Rule
    from .scheme import Scheme
    from .setting import Setting

__all__ = [
    "Rule",
    "Scheme",
    "Setting",
    "Authentication",
]


class Authentication:
    """AUTHENTICATION API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    rule: Rule
    scheme: Scheme
    setting: Setting

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize authentication category with HTTP client."""
        ...
