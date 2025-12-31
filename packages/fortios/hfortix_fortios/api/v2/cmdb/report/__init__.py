"""FortiOS CMDB - Report category"""

from .layout import Layout
from .setting import Setting

__all__ = ["Layout", "Setting"]


class Report:
    """
    Report category wrapper.

    This class provides access to all report CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize Report with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.layout = Layout(client)
        self.setting = Setting(client)
