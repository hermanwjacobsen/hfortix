"""FortiOS CMDB - Voip category"""

from .profile import Profile

__all__ = ["Profile"]


class Voip:
    """
    Voip category wrapper.

    This class provides access to all voip CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize Voip with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.profile = Profile(client)
