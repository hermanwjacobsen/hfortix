"""Type stubs for VPN category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .kmip_server import KmipServer
    from .l2tp import L2tp
    from .pptp import Pptp
    from .qkd import Qkd
    from .certificate import Certificate
    from .ipsec import Ipsec

__all__ = [
    "KmipServer",
    "L2tp",
    "Pptp",
    "Qkd",
    "Vpn",
]


class Vpn:
    """VPN API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    certificate: Certificate
    ipsec: Ipsec
    kmip_server: KmipServer
    l2tp: L2tp
    pptp: Pptp
    qkd: Qkd

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize vpn category with HTTP client."""
        ...
