"""
FortiOS MONITOR - Monitor System Logdisk

Monitoring endpoint for monitor system logdisk data.

API Endpoints:
    GET    /monitor/system/logdisk

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>> 
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.logdisk.get()
    >>> 
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.logdisk.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Format:
    """
    Format Operations.
    
    Provides read-only access for FortiOS format data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)
    
    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Format endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Format log disk.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.system.logdisk.format.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        data.update(kwargs)
        return self._client.post("monitor", "/system/logdisk/format", data=data)


class Logdisk:
    """Logdisk operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Logdisk endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.format = Format(client)
