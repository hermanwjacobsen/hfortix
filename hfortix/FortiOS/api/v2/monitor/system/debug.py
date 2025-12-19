"""
FortiOS MONITOR - Monitor System Debug

Monitoring endpoint for monitor system debug data.

API Endpoints:
    GET    /monitor/system/debug

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>> 
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.debug.get()
    >>> 
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.debug.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Download:
    """
    Download Operations.
    
    Provides read-only access for FortiOS download data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)
    
    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Download endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Download debug report for technical support.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.system.debug.download.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/system/debug/download", params=params)


class Debug:
    """Debug operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Debug endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.download = Download(client)
