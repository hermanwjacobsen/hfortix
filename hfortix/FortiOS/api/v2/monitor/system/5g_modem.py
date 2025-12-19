"""
FortiOS MONITOR - Monitor System 5g Modem

Monitoring endpoint for monitor system 5g modem data.

API Endpoints:
    GET    /monitor/system/5g_modem

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>> 
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.5g_modem.get()
    >>> 
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.5g_modem.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Status:
    """
    Status Operations.
    
    Provides read-only access for FortiOS status data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)
    
    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Status endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        modem: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve the 5G modem status.
        
        Args:
            modem: Modem to query status [all|1|2]. Defaults to all modems if not provided. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.system.5g_modem.status.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if modem is not None:
            params['modem'] = modem
        params.update(kwargs)
        return self._client.get("monitor", "/system/5g-modem/status", params=params)


class 5gModem:
    """5gModem operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize 5gModem endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.status = Status(client)
