"""
FortiOS Monitor - Vpn Certificate
VPN certificate monitoring
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .....http_client_interface import IHTTPClient

__all__ = ["VpnCertificate"]

from .ca import Ca
from .cert_name_available import CertNameAvailable
from .crl import Crl
from .csr import Csr
from .local import Local
from .remote import Remote


class VpnCertificate:
    """VpnCertificate Monitor category class"""

    def __init__(self, client: "IHTTPClient") -> None:
        """
        Initialize VpnCertificate Monitor category

        Args:
            client: HTTP client implementing IHTTPClient protocol
        """
        self._client = client

        # Initialize endpoints
        self.ca = Ca(client)
        self.cert_name_available = CertNameAvailable(client)
        self.crl = Crl(client)
        self.csr = Csr(client)
        self.local = Local(client)
        self.remote = Remote(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return ["ca", "cert_name_available", "crl", "csr", "local", "remote"]
