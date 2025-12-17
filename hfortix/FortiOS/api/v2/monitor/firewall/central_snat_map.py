"""Central SNAT policy statistics operations."""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class CentralSnatMap:
    """Central SNAT policy statistics."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize CentralSnatMap endpoint.

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
        List traffic statistics for all firewall central SNAT policies.

        Args:
            data_dict: Optional dictionary of parameters
            policyid: Filter by policy ID
            ip_version: Filter by IP version
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing SNAT policy statistics

        Example:
            >>> fgt.api.monitor.firewall.central_snat_map.list()
        """
        params = data_dict.copy() if data_dict else {}
        if policyid is not None:
            params["policyid"] = policyid
        if ip_version is not None:
            params["ip_version"] = ip_version
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/central-snat-map", params=params)

    def get(
        self, data_dict: Optional[Dict[str, Any]] = None, policyid: Optional[int] = None, **kwargs
    ) -> Dict[str, Any]:
        """
        Get traffic statistics for a specific central SNAT policy.

        Args:
            data_dict: Optional dictionary of parameters
            policyid: Policy ID to retrieve
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing policy statistics

        Example:
            >>> fgt.api.monitor.firewall.central_snat_map.get(policyid=1)
        """
        params = data_dict.copy() if data_dict else {}
        if policyid is not None:
            params["policyid"] = policyid
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/central-snat-map", params=params)

    def reset(self, data_dict: Optional[Dict[str, Any]] = None, **kwargs) -> Dict[str, Any]:
        """
        Reset traffic statistics for all firewall central SNAT policies.

        Args:
            data_dict: Optional dictionary of parameters
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing operation result

        Example:
            >>> fgt.api.monitor.firewall.central_snat_map.reset()
        """
        data = data_dict.copy() if data_dict else {}
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/central-snat-map/reset", data=data)

    def clear_counters(
        self, data_dict: Optional[Dict[str, Any]] = None, policy_ids: Optional[str] = None, **kwargs
    ) -> Dict[str, Any]:
        """
        Reset traffic statistics for one or more firewall central SNAT policy by policy ID.

        Args:
            data_dict: Optional dictionary of parameters
            policy_ids: Comma-separated list of policy IDs
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing operation result

        Example:
            >>> fgt.api.monitor.firewall.central_snat_map.clear_counters(policy_ids='1,2,3')
        """
        data = data_dict.copy() if data_dict else {}
        if policy_ids is not None:
            data["policy_ids"] = policy_ids
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/central-snat-map/clear-counters", data=data)
