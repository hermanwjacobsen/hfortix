"""Type stubs for GUEST category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .email import Email
    from .sms import Sms

__all__ = [
    "Email",
    "Sms",
    "Guest",
]


class Guest:
    """GUEST API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    email: Email
    sms: Sms

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize guest category with HTTP client."""
        ...
