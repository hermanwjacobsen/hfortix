"""FortiOS CMDB - Waf category"""

from .main_class import MainClass
from .profile import Profile
from .signature import Signature

__all__ = ["MainClass", "Profile", "Signature"]


class Waf:
    """
    Waf category wrapper.

    This class provides access to all waf CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize Waf with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.main_class = MainClass(client)
        self.profile = Profile(client)
        self.signature = Signature(client)
