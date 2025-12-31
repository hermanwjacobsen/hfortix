"""FortiOS CMDB - Dnsfilter category"""

from .domain_filter import DomainFilter
from .profile import Profile

__all__ = ["DomainFilter", "Profile"]


class Dnsfilter:
    """
    Dnsfilter category wrapper.

    This class provides access to all dnsfilter CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize Dnsfilter with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.domain_filter = DomainFilter(client)
        self.profile = Profile(client)
