"""FortiOS CMDB - Icap category"""

from .profile import Profile
from .server import Server
from .server_group import ServerGroup

__all__ = ["Profile", "Server", "ServerGroup"]


class Icap:
    """
    Icap category wrapper.

    This class provides access to all icap CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize Icap with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.profile = Profile(client)
        self.server = Server(client)
        self.server_group = ServerGroup(client)
