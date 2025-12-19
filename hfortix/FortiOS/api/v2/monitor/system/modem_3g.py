"""
FortiOS MONITOR - Monitor System Modem 3g

Monitoring endpoint for monitor system modem 3g data.

API Endpoints:
    GET    /monitor/system/modem_3g

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>> 
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.modem_3g.get()
    >>> 
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.modem_3g.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Modem3g:
    """
    Modem3G Operations.
    
    Provides read-only access for FortiOS modem3g data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)
    
    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize 3gModem endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        List all 3G modems available via FortiGuard.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.system.3g_modem.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/system/3g-modem", params=params)
