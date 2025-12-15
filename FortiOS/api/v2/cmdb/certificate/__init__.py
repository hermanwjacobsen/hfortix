"""
FortiOS CMDB - Certificate Category

Manage certificates on FortiGate.

Available Endpoints:
    - ca: View CA certificates (read-only)
    - crl: View Certificate Revocation Lists (read-only)
    - hsm_local: Manage HSM (Hardware Security Module) certificates (full CRUD)
    - local: View local certificates (read-only)
    - remote: View remote certificates (read-only)
"""
from typing import TYPE_CHECKING

from .ca import Ca
from .crl import Crl
from .hsm_local import HsmLocal
from .local import Local
from .remote import Remote

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ['Certificate']


class Certificate:
    """Certificate management category"""

    def __init__(self, client: 'HTTPClient') -> None:
        """
        Initialize Certificate category

        Args:
            client: HTTPClient instance
        """
        self.ca = Ca(client)
        self.crl = Crl(client)
        self.hsm_local = HsmLocal(client)
        self.local = Local(client)
        self.remote = Remote(client)
    
    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return ['ca', 'crl', 'hsm_local', 'local', 'remote']
