"""Virtual IP overlap detection operations."""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class VipOverlap:
    """Overlapping Virtual IP detection."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize VipOverlap endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def list(self, data_dict: Optional[Dict[str, Any]] = None, **kwargs) -> Dict[str, Any]:
        """
        List any Virtual IPs that overlap with another Virtual IP.

        Args:
            data_dict: Optional dictionary of parameters
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing overlapping VIPs

        Example:
            >>> fgt.api.monitor.firewall.vip_overlap.list()
        """
        params = data_dict.copy() if data_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/vip-overlap", params=params)
