"""
FortiOS MONITOR - Monitor Webfilter Malicious Urls

Monitoring endpoint for monitor webfilter malicious urls data.

API Endpoints:
    GET    /monitor/webfilter/malicious_urls

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>> 
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.webfilter.malicious_urls.get()
    >>> 
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.webfilter.malicious_urls.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Stat:
    """
    Stat Operations.
    
    Provides read-only access for FortiOS stat data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)
    
    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Stat endpoint.

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
        Retrieve statistics for the FortiSandbox malicious URL database.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.webfilter.malicious_urls.stat.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/webfilter/malicious-urls/stat", params=params)


class MaliciousUrls:
    """MaliciousUrls operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize MaliciousUrls endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.stat = Stat(client)

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        List all URLs in FortiSandbox malicious URL database.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.webfilter.malicious_urls.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/webfilter/malicious-urls", params=params)
