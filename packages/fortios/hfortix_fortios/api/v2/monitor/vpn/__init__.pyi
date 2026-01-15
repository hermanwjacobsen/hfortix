"""Type stubs for VPN category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .ike import Ike
    from .ipsec import Ipsec
    from .ssl import Ssl

__all__ = [
    "Vpn",
]


class Vpn:
    """VPN API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    ike: Ike
    ipsec: Ipsec
    ssl: Ssl

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize vpn category with HTTP client."""
        ...
