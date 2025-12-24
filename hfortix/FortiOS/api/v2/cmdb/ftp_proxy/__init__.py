"""FortiOS CMDB - Ftp-proxy category"""

from .explicit import Explicit

__all__ = ["Explicit"]


class FtpProxy:
    """
    FtpProxy category wrapper.

    This class provides access to all ftp-proxy CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize FtpProxy with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.explicit = Explicit(client)
