"""Monitor API - ProxyPolicy operations."""

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
        Reset traffic statistics for one or more explicit proxy policies by policy ID.
        
        Args:
            policy: Single policy ID to reset. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.firewall.proxy_policy.clear_counters.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if policy is not None:
            data['policy'] = policy
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/proxy-policy/clear_counters", data=data)


class ProxyPolicy:
    """ProxyPolicy operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize ProxyPolicy endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.clear_counters = ClearCounters(client)

    def get(
        self,
        policyid: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        List traffic statistics for all explicit proxy policies.
        
        Args:
            policyid: Filter: Policy ID. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.firewall.proxy_policy.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if policyid is not None:
            params['policyid'] = policyid
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/proxy-policy", params=params)
