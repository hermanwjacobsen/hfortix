"""
FortiOS MONITOR - Monitor System Resolve Fqdn

Monitoring endpoint for monitor system resolve fqdn data.

API Endpoints:
    GET    /monitor/system/resolve_fqdn

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>> 
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.resolve_fqdn.get()
    >>> 
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.resolve_fqdn.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class ResolveFqdn:
    """
    Resolvefqdn Operations.
    
    Provides read-only access for FortiOS resolvefqdn data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)
    
    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize ResolveFqdn endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        fqdn: Any,
        ipv6: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Resolves the provided FQDNs to FQDN -> IP mappings.
        
        Args:
            fqdn: FQDN (required)
            ipv6: Resolve for the AAAA record? (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.system.resolve_fqdn.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params['fqdn'] = fqdn
        if ipv6 is not None:
            params['ipv6'] = ipv6
        params.update(kwargs)
        return self._client.get("monitor", "/system/resolve-fqdn", params=params)
