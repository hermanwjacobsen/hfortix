"""FortiOS CMDB - Sctp-filter category"""

from .profile import Profile

__all__ = ["Profile"]


class SctpFilter:
    """
    SctpFilter category wrapper.

    This class provides access to all sctp-filter CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize SctpFilter with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.profile = Profile(client)
