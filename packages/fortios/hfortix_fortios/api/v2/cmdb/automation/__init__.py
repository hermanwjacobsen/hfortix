"""FortiOS CMDB - Automation category"""

from .setting import Setting

__all__ = ["Setting"]


class Automation:
    """
    Automation category wrapper.

    This class provides access to all automation CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize Automation with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.setting = Setting(client)
