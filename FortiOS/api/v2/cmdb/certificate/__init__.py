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

from .ca import Ca
from .crl import Crl
from .hsm_local import HsmLocal
from .local import Local
from .remote import Remote


class Certificate:
    """Certificate management category"""
    
    def __init__(self, client):
        """
        Initialize Certificate category
        
        Args:
            client: FortiOS client instance
        """
        self.ca = Ca(client)
        self.crl = Crl(client)
        self.hsm_local = HsmLocal(client)
        self.local = Local(client)
        self.remote = Remote(client)
