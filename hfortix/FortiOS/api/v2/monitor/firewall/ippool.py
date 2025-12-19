"""Monitor API - Ippool operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Mapping:
    """Mapping operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Mapping endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        mkey: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get the list of IPv4 mappings for the specified IP pool.
        
        Args:
            mkey: The IP pool name. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.firewall.ippool.mapping.get(mkey='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params['mkey'] = mkey
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/ippool/mapping", params=params)


class Ippool:
    """Ippool operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Ippool endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.mapping = Mapping(client)

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        List IPv4 pool statistics.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.firewall.ippool.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/ippool", params=params)
