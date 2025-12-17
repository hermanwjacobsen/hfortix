"""
FTP Proxy API endpoints.

This module provides access to FTP proxy configuration endpoints.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class FtpProxy:
    """FTP proxy configuration endpoints."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize FTP Proxy API.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    @property
    def explicit(self) -> "FtpProxyExplicit":
        """
        Access FTP proxy explicit endpoint.

        Returns:
            FtpProxyExplicit: Explicit FTP proxy configuration endpoint

        Example:
            >>> fgt.api.cmdb.ftp_proxy.explicit.get()
        """
        from .explicit import FtpProxyExplicit

        return FtpProxyExplicit(self._client)
