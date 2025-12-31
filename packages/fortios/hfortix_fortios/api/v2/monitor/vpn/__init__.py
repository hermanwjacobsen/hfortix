"""
FortiOS Monitor - Vpn
VPN monitoring (IPsec/SSL)
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient

__all__ = ["Vpn"]

from .ike import Ike
from .ipsec import Ipsec
from .ssl import Ssl


class Vpn:
    """Vpn Monitor category class"""

    def __init__(self, client: "IHTTPClient") -> None:
        """
        Initialize Vpn Monitor category

        Args:
            client: HTTP client implementing IHTTPClient protocol
        """
        self._client = client

        # Initialize endpoints
        self.ike = Ike(client)
        self.ipsec = Ipsec(client)
        self.ssl = Ssl(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return ["ike", "ipsec", "ssl"]
