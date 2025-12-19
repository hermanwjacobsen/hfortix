"""
FortiOS MONITOR - Monitor System Monitor Sensor

Monitoring endpoint for monitor system monitor sensor data.

API Endpoints:
    GET    /monitor/system/monitor_sensor

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>> 
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.monitor_sensor.get()
    >>> 
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.monitor_sensor.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class MonitorSensor:
    """
    Monitorsensor Operations.
    
    Provides read-only access for FortiOS monitorsensor data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)
    
    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize MonitorSensor endpoint.

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
        Retrieve monitor sensor status.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.system.monitor_sensor.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/system/monitor-sensor", params=params)
