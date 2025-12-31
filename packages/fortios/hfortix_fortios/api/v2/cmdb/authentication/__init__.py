"""FortiOS CMDB - Authentication category"""

from .rule import Rule
from .scheme import Scheme
from .setting import Setting

__all__ = ["Rule", "Scheme", "Setting"]


class Authentication:
    """
    Authentication category wrapper.

    This class provides access to all authentication CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize Authentication with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.rule = Rule(client)
        self.scheme = Scheme(client)
        self.setting = Setting(client)
