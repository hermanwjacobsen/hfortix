"""FortiOS CMDB - Virtual-patch category"""

from .profile import Profile

__all__ = ["Profile"]


class VirtualPatch:
    """
    VirtualPatch category wrapper.

    This class provides access to all virtual-patch CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize VirtualPatch with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.profile = Profile(client)
