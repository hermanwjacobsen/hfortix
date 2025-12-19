"""
FortiOS MONITOR - Monitor System Usb Device

Monitoring endpoint for monitor system usb device data.

API Endpoints:
    GET    /monitor/system/usb_device

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>> 
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.usb_device.get()
    >>> 
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.usb_device.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Eject:
    """
    Eject Operations.
    
    Provides read-only access for FortiOS eject data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)
    
    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Eject endpoint.

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
        Eject USB drives for safe removal.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.system.usb_device.eject.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        data.update(kwargs)
        return self._client.post("monitor", "/system/usb-device/eject", data=data)


class UsbDevice:
    """UsbDevice operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize UsbDevice endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.eject = Eject(client)
