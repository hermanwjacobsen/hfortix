"""FortiOS CMDB - Endpoint-control category"""

from .fctems import Fctems
from .fctems_override import FctemsOverride
from .settings import Settings

__all__ = ["Fctems", "FctemsOverride", "Settings"]


class EndpointControl:
    """
    EndpointControl category wrapper.

    This class provides access to all endpoint-control CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize EndpointControl with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.fctems = Fctems(client)
        self.fctems_override = FctemsOverride(client)
        self.settings = Settings(client)
