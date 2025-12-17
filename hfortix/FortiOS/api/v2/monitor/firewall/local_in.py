"""IPv4 local-in firewall policy operations."""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class LocalIn:
    """Implicit and explicit local-in firewall policies."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize LocalIn endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def list(
        self, data_dict: Optional[Dict[str, Any]] = None, policyid: Optional[int] = None, **kwargs
    ) -> Dict[str, Any]:
        """
        List all implicit and explicit local-in firewall policies.

        Args:
            data_dict: Optional dictionary of parameters
            policyid: Filter by policy ID
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing local-in policies

        Example:
            >>> fgt.api.monitor.firewall.local_in.list()
        """
        params = data_dict.copy() if data_dict else {}
        if policyid is not None:
            params["policyid"] = policyid
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/local-in", params=params)

    def get(
        self, data_dict: Optional[Dict[str, Any]] = None, policyid: Optional[int] = None, **kwargs
    ) -> Dict[str, Any]:
        """
        Get a specific local-in firewall policy.

        Args:
            data_dict: Optional dictionary of parameters
            policyid: Policy ID to retrieve
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing policy information

        Example:
            >>> fgt.api.monitor.firewall.local_in.get(policyid=1)
        """
        params = data_dict.copy() if data_dict else {}
        if policyid is not None:
            params["policyid"] = policyid
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/local-in", params=params)
