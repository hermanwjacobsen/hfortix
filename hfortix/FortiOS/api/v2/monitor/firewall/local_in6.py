"""IPv6 local-in firewall policy operations."""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class LocalIn6:
    """Implicit and explicit IPv6 local-in firewall policies."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize LocalIn6 endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def list(self, data_dict: Optional[Dict[str, Any]] = None, **kwargs) -> Dict[str, Any]:
        """
        List implicit and explicit IPv6 local-in firewall policies.

        Args:
            data_dict: Optional dictionary of parameters
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing IPv6 local-in policies

        Example:
            >>> fgt.api.monitor.firewall.local_in6.list()
        """
        params = data_dict.copy() if data_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/local-in6", params=params)
