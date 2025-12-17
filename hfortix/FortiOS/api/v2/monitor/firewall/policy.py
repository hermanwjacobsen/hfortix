"""Firewall policy statistics and operations."""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Policy:
    """Firewall policy statistics and operations."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize Policy endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def list(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        policyid: Optional[int] = None,
        ip_version: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        List traffic statistics for all firewall policies.

        Args:
            data_dict: Optional dictionary of parameters
            policyid: Filter by policy ID
            ip_version: Filter by IP version ('ipv4' or 'ipv6')
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing policy statistics

        Example:
            >>> # List all policies
            >>> fgt.api.monitor.firewall.policy.list()
            >>> # Filter by IP version
            >>> fgt.api.monitor.firewall.policy.list(ip_version='ipv4')
        """
        params = data_dict.copy() if data_dict else {}
        if policyid is not None:
            params["policyid"] = policyid
        if ip_version is not None:
            params["ip_version"] = ip_version
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/policy", params=params)

    def get(
        self, data_dict: Optional[Dict[str, Any]] = None, policyid: Optional[int] = None, **kwargs
    ) -> Dict[str, Any]:
        """
        Get traffic statistics for a specific firewall policy.

        Args:
            data_dict: Optional dictionary of parameters
            policyid: Policy ID to retrieve
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing policy statistics

        Example:
            >>> fgt.api.monitor.firewall.policy.get(policyid=1)
        """
        params = data_dict.copy() if data_dict else {}
        if policyid is not None:
            params["policyid"] = policyid
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/policy", params=params)

    def reset(self, data_dict: Optional[Dict[str, Any]] = None, **kwargs) -> Dict[str, Any]:
        """
        Reset traffic statistics for all firewall policies.

        Args:
            data_dict: Optional dictionary of parameters
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing operation result

        Example:
            >>> fgt.api.monitor.firewall.policy.reset()
        """
        data = data_dict.copy() if data_dict else {}
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/policy/reset", data=data)

    def clear_counters(
        self, data_dict: Optional[Dict[str, Any]] = None, policy_ids: Optional[str] = None, **kwargs
    ) -> Dict[str, Any]:
        """
        Reset traffic statistics for one or more firewall policies by policy ID.

        Args:
            data_dict: Optional dictionary of parameters
            policy_ids: Comma-separated list of policy IDs
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing operation result

        Example:
            >>> fgt.api.monitor.firewall.policy.clear_counters(policy_ids='1,2,3')
        """
        data = data_dict.copy() if data_dict else {}
        if policy_ids is not None:
            data["policy_ids"] = policy_ids
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/policy/clear_counters", data=data)

    def update_global_label(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        id: Optional[int] = None,
        global_label: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Update the global-label of group starting with the provided leading policy ID.

        Args:
            data_dict: Optional dictionary of parameters
            id: Leading policy ID
            global_label: New global label value
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing operation result

        Example:
            >>> fgt.api.monitor.firewall.policy.update_global_label(id=1, global_label='DMZ_Policies')
        """
        data = data_dict.copy() if data_dict else {}
        if id is not None:
            data["id"] = id
        if global_label is not None:
            data["global_label"] = global_label
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/policy/update-global-label", data=data)
