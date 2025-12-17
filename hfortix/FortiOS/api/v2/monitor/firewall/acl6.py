"""IPv6 ACL counter operations."""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class ACL6:
    """IPv6 ACL counters and operations."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize ACL6 endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def list(self, data_dict: Optional[Dict[str, Any]] = None, **kwargs) -> Dict[str, Any]:
        """
        List counters for all IPv6 ACL.

        Args:
            data_dict: Optional dictionary of parameters
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing ACL counters

        Example:
            >>> fgt.api.monitor.firewall.acl6.list()
        """
        params = data_dict.copy() if data_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/acl6", params=params)

    def clear_counters(
        self, data_dict: Optional[Dict[str, Any]] = None, policy_ids: Optional[str] = None, **kwargs
    ) -> Dict[str, Any]:
        """
        Reset counters for one or more IPv6 ACLs by policy ID.

        Args:
            data_dict: Optional dictionary of parameters
            policy_ids: Comma-separated list of policy IDs
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing operation result

        Example:
            >>> fgt.api.monitor.firewall.acl6.clear_counters(policy_ids='1,2,3')
        """
        data = data_dict.copy() if data_dict else {}
        if policy_ids is not None:
            data["policy_ids"] = policy_ids
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/acl6/clear_counters", data=data)
