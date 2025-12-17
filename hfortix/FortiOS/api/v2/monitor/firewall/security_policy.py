"""Security policy IPS engine statistics operations."""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class SecurityPolicy:
    """Security policy IPS engine statistics."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize SecurityPolicy endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def list(
        self, data_dict: Optional[Dict[str, Any]] = None, policyid: Optional[int] = None, **kwargs
    ) -> Dict[str, Any]:
        """
        List IPS engine statistics for all security policies.

        Args:
            data_dict: Optional dictionary of parameters
            policyid: Filter by policy ID
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing security policy statistics

        Example:
            >>> fgt.api.monitor.firewall.security_policy.list()
        """
        params = data_dict.copy() if data_dict else {}
        if policyid is not None:
            params["policyid"] = policyid
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/security-policy", params=params)

    def get(
        self, data_dict: Optional[Dict[str, Any]] = None, policyid: Optional[int] = None, **kwargs
    ) -> Dict[str, Any]:
        """
        Get IPS engine statistics for a specific security policy.

        Args:
            data_dict: Optional dictionary of parameters
            policyid: Policy ID to retrieve
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing security policy statistics

        Example:
            >>> fgt.api.monitor.firewall.security_policy.get(policyid=1)
        """
        params = data_dict.copy() if data_dict else {}
        if policyid is not None:
            params["policyid"] = policyid
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/security-policy", params=params)

    def clear_counters(
        self, data_dict: Optional[Dict[str, Any]] = None, policy_ids: Optional[str] = None, **kwargs
    ) -> Dict[str, Any]:
        """
        Reset traffic statistics for one or more security policies by policy ID.

        Args:
            data_dict: Optional dictionary of parameters
            policy_ids: Comma-separated list of policy IDs
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing operation result

        Example:
            >>> fgt.api.monitor.firewall.security_policy.clear_counters(policy_ids='1,2,3')
        """
        data = data_dict.copy() if data_dict else {}
        if policy_ids is not None:
            data["policy_ids"] = policy_ids
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/security-policy/clear_counters", data=data)

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
            >>> fgt.api.monitor.firewall.security_policy.update_global_label(id=1, global_label='IPS_Policies')
        """
        data = data_dict.copy() if data_dict else {}
        if id is not None:
            data["id"] = id
        if global_label is not None:
            data["global_label"] = global_label
        data.update(kwargs)
        return self._client.post(
            "monitor", "/firewall/security-policy/update-global-label", data=data
        )
