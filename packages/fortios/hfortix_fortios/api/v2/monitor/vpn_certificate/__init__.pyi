"""Type stubs for VPN_CERTIFICATE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .cert_name_available import CertNameAvailable
    from .ca import Ca
    from .crl import Crl
    from .csr import Csr
    from .local import Local
    from .remote import Remote

__all__ = [
    "CertNameAvailable",
    "VpnCertificate",
]


class VpnCertificate:
    """VPN_CERTIFICATE API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    ca: Ca
    crl: Crl
    csr: Csr
    local: Local
    remote: Remote
    cert_name_available: CertNameAvailable

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize vpn_certificate category with HTTP client."""
        ...
