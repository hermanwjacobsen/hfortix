"""Monitor API - Policy operations."""

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
        Reset traffic statistics for one or more firewall policies by policy ID.
        
        Args:
            policy: Single policy ID to reset. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.firewall.policy.clear_counters.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if policy is not None:
            data['policy'] = policy
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/policy/clear_counters", data=data)


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
        Reset traffic statistics for all firewall policies.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.firewall.policy.reset.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/policy/reset", data=data)


class UpdateGlobalLabel:
    """UpdateGlobalLabel operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize UpdateGlobalLabel endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        policyid: str | None = None,
        current_label: str | None = None,
        new_label: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update the global-label of group starting with the provided leading policy ID.
        
        Args:
            policyid: Leading policy ID of the group to update. (optional)
            current_label: The current global-label of the group. If not provided, will assume the current group's label is empty string. (optional)
            new_label: The new global-label of the group. If not provided, the current group's label will be deleted (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.firewall.policy.update_global_label.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if policyid is not None:
            data['policyid'] = policyid
        if current_label is not None:
            data['current-label'] = current_label
        if new_label is not None:
            data['new-label'] = new_label
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/policy/update-global-label", data=data)


class Policy:
    """Policy operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Policy endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.clear_counters = ClearCounters(client)
        self.reset = Reset(client)
        self.update_global_label = UpdateGlobalLabel(client)

    def get(
        self,
        policyid: Any | None = None,
        ip_version: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        List traffic statistics for firewall policies.
        
        Args:
            policyid: Filter: Policy ID. (optional)
            ip_version: Filter: Traffic IP Version. [ ipv4 | ipv6 ], if left empty, will retrieve data for both ipv4 and ipv6. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.firewall.policy.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if policyid is not None:
            params['policyid'] = policyid
        if ip_version is not None:
            params['ip_version'] = ip_version
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/policy", params=params)
