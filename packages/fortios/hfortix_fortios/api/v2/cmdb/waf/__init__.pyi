"""Type stubs for WAF category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .main_class import MainClass
    from .profile import Profile
    from .signature import Signature

__all__ = [
    "MainClass",
    "Profile",
    "Signature",
    "Waf",
]


class Waf:
    """WAF API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    main_class: MainClass
    profile: Profile
    signature: Signature

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize waf category with HTTP client."""
        ...
