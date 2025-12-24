"""FortiOS CMDB - Diameter-filter category"""

from .profile import Profile

__all__ = ["Profile"]


class DiameterFilter:
    """
    DiameterFilter category wrapper.

    This class provides access to all diameter-filter CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize DiameterFilter with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.profile = Profile(client)
