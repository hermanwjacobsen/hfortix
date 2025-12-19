"""Monitor API - ZtnaFirewallPolicy operations."""

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
        Reset traffic statistics for one or more ZTNA firewall policies by policy ID.
        
        Args:
            policy: Single ZTNA firewall policy ID to reset. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.firewall.ztna_firewall_policy.clear_counters.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if policy is not None:
            data['policy'] = policy
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/ztna-firewall-policy/clear-counters", data=data)


class ZtnaFirewallPolicy:
    """ZtnaFirewallPolicy operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize ZtnaFirewallPolicy endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.clear_counters = ClearCounters(client)
