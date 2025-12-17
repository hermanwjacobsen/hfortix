"""IPv6 multicast policy statistics operations."""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class MulticastPolicy6:
    """IPv6 multicast policy statistics."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize MulticastPolicy6 endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def list(
        self, data_dict: Optional[Dict[str, Any]] = None, policyid: Optional[int] = None, **kwargs
    ) -> Dict[str, Any]:
        """
        List traffic statistics for all IPv6 firewall multicast policies.

        Args:
            data_dict: Optional dictionary of parameters
            policyid: Filter by policy ID
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing multicast policy statistics

        Example:
            >>> fgt.api.monitor.firewall.multicast_policy6.list()
        """
        params = data_dict.copy() if data_dict else {}
        if policyid is not None:
            params["policyid"] = policyid
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/multicast-policy6", params=params)

    def get(
        self, data_dict: Optional[Dict[str, Any]] = None, policyid: Optional[int] = None, **kwargs
    ) -> Dict[str, Any]:
        """
        Get traffic statistics for a specific IPv6 multicast policy.

        Args:
            data_dict: Optional dictionary of parameters
            policyid: Policy ID to retrieve
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing multicast policy statistics

        Example:
            >>> fgt.api.monitor.firewall.multicast_policy6.get(policyid=1)
        """
        params = data_dict.copy() if data_dict else {}
        if policyid is not None:
            params["policyid"] = policyid
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/multicast-policy6", params=params)

    def reset(self, data_dict: Optional[Dict[str, Any]] = None, **kwargs) -> Dict[str, Any]:
        """
        Reset traffic statistics for all IPv6 firewall multicast policies.

        Args:
            data_dict: Optional dictionary of parameters
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing operation result

        Example:
            >>> fgt.api.monitor.firewall.multicast_policy6.reset()
        """
        data = data_dict.copy() if data_dict else {}
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/multicast-policy6/reset", data=data)

    def clear_counters(
        self, data_dict: Optional[Dict[str, Any]] = None, policy_ids: Optional[str] = None, **kwargs
    ) -> Dict[str, Any]:
        """
        Reset traffic statistics for one or more firewall IPv6 multicast policies by policy ID.

        Args:
            data_dict: Optional dictionary of parameters
            policy_ids: Comma-separated list of policy IDs
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing operation result

        Example:
            >>> fgt.api.monitor.firewall.multicast_policy6.clear_counters(policy_ids='1,2,3')
        """
        data = data_dict.copy() if data_dict else {}
        if policy_ids is not None:
            data["policy_ids"] = policy_ids
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/multicast-policy6/clear_counters", data=data)
