"""Monitor API - LookupPolicy operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class LookupPolicy:
    """LookupPolicy operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize LookupPolicy endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        destination: str,
        ipv6: bool | None = None,
        source: str | None = None,
        destination_port: int | None = None,
        source_port: int | None = None,
        interface_name: str | None = None,
        protocol_number: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Performs a route lookup by querying the policy routing table.
        
        Args:
            destination: Destination IP/FQDN. (required)
            ipv6: Perform an IPv6 lookup. (optional)
            source: Source IP/FQDN. (optional)
            destination_port: Destination Port. (optional)
            source_port: Source Port. (optional)
            interface_name: Incoming Interface. (optional)
            protocol_number: IP Protocol Number. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.router.lookup_policy.get(destination='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params['destination'] = destination
        if ipv6 is not None:
            params['ipv6'] = ipv6
        if source is not None:
            params['source'] = source
        if destination_port is not None:
            params['destination_port'] = destination_port
        if source_port is not None:
            params['source_port'] = source_port
        if interface_name is not None:
            params['interface_name'] = interface_name
        if protocol_number is not None:
            params['protocol_number'] = protocol_number
        params.update(kwargs)
        return self._client.get("monitor", "/router/lookup-policy", params=params)
