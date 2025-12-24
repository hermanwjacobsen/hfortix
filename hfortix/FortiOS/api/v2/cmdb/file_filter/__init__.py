"""FortiOS CMDB - File-filter category"""

from .profile import Profile

__all__ = ["Profile"]


class FileFilter:
    """
    FileFilter category wrapper.

    This class provides access to all file-filter CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize FileFilter with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.profile = Profile(client)
