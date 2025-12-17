"""ZTNA firewall policy statistics operations."""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class ZTNAFirewallPolicy:
    """ZTNA firewall policy statistics."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize ZTNAFirewallPolicy endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def clear_counters(
        self, data_dict: Optional[Dict[str, Any]] = None, policy_ids: Optional[str] = None, **kwargs
    ) -> Dict[str, Any]:
        """
        Reset traffic statistics for one or more ZTNA firewall policies by policy ID.

        Args:
            data_dict: Optional dictionary of parameters
            policy_ids: Comma-separated list of policy IDs
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing operation result

        Example:
            >>> fgt.api.monitor.firewall.ztna_firewall_policy.clear_counters(policy_ids='1,2,3')
        """
        data = data_dict.copy() if data_dict else {}
        if policy_ids is not None:
            data["policy_ids"] = policy_ids
        data.update(kwargs)
        return self._client.post(
            "monitor", "/firewall/ztna-firewall-policy/clear-counters", data=data
        )
