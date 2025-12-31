"""FortiOS CMDB - Certificate category"""

from .ca import Ca
from .crl import Crl
from .hsm_local import HsmLocal
from .local import Local
from .remote import Remote

__all__ = ["Ca", "Crl", "HsmLocal", "Local", "Remote"]


class Certificate:
    """
    Certificate category wrapper.

    This class provides access to all certificate CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize Certificate with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.ca = Ca(client)
        self.crl = Crl(client)
        self.hsm_local = HsmLocal(client)
        self.local = Local(client)
        self.remote = Remote(client)
