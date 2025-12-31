"""FortiOS CMDB - Alertemail category"""

from .setting import Setting

__all__ = ["Setting"]


class Alertemail:
    """
    Alertemail category wrapper.

    This class provides access to all alertemail CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize Alertemail with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.setting = Setting(client)
