"""FortiOS CMDB - Ethernet-oam category"""

from .cfm import Cfm

__all__ = ["Cfm"]


class EthernetOam:
    """
    EthernetOam category wrapper.

    This class provides access to all ethernet-oam CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize EthernetOam with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.cfm = Cfm(client)
