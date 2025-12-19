"""
FortiOS MONITOR - Monitor Firewall Load Balance

Monitoring endpoint for monitor firewall load balance data.

API Endpoints:
    GET    /monitor/firewall/load_balance

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>> 
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.firewall.load_balance.get()
    >>> 
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.firewall.load_balance.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class LoadBalance:
    """
    Loadbalance Operations.
    
    Provides read-only access for FortiOS loadbalance data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)
    
    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize LoadBalance endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        count: int,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        List all firewall load balance servers.
        
        Args:
            count: Maximum number of entries to return. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.firewall.load_balance.get(count=1)
        """
        params = payload_dict.copy() if payload_dict else {}
        params['count'] = count
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/load-balance", params=params)
