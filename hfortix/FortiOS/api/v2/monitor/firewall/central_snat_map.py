"""Monitor API - CentralSnatMap operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class ClearCounters:
    """ClearCounters operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize ClearCounters endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        policy: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Reset traffic statistics for one or more firewall central SNAT policy by policy ID.
        
        Args:
            policy: Single policy ID to reset. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.firewall.central_snat_map.clear_counters.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if policy is not None:
            data['policy'] = policy
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/central-snat-map/clear-counters", data=data)


class Reset:
    """Reset operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Reset endpoint.

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
        Reset traffic statistics for all firewall central SNAT policies.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.firewall.central_snat_map.reset.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/central-snat-map/reset", data=data)


class CentralSnatMap:
    """CentralSnatMap operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize CentralSnatMap endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.clear_counters = ClearCounters(client)
        self.reset = Reset(client)

    def get(
        self,
        policyid: int | None = None,
        ip_version: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        List traffic statistics for firewall central SNAT policies.
        
        Args:
            policyid: Filter: Policy ID. (optional)
            ip_version: Filter: Traffic IP Version. [ ipv4 | ipv6 ], if left empty, will retrieve data for both IPv4 and IPv6. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.firewall.central_snat_map.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if policyid is not None:
            params['policyid'] = policyid
        if ip_version is not None:
            params['ip_version'] = ip_version
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/central-snat-map", params=params)
