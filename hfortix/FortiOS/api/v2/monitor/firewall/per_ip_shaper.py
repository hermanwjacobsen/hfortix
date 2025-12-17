"""Per-IP traffic shaper statistics operations."""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class PerIpShaper:
    """Per-IP traffic shaper statistics."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize PerIpShaper endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def list(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        shaper_name: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        List of statistics for all configured firewall per-IP traffic shapers.

        Args:
            data_dict: Optional dictionary of parameters
            shaper_name: Filter by shaper name
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing per-IP shaper statistics

        Example:
            >>> fgt.api.monitor.firewall.per_ip_shaper.list()
            >>> fgt.api.monitor.firewall.per_ip_shaper.list(shaper_name='per_ip_shaper1')
        """
        params = data_dict.copy() if data_dict else {}
        if shaper_name is not None:
            params["shaper_name"] = shaper_name
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/per-ip-shaper", params=params)

    def get(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        shaper_name: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Get statistics for a specific per-IP traffic shaper.

        Args:
            data_dict: Optional dictionary of parameters
            shaper_name: Shaper name to retrieve
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing per-IP shaper statistics

        Example:
            >>> fgt.api.monitor.firewall.per_ip_shaper.get(shaper_name='per_ip_shaper1')
        """
        params = data_dict.copy() if data_dict else {}
        if shaper_name is not None:
            params["shaper_name"] = shaper_name
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/per-ip-shaper", params=params)

    def reset(self, data_dict: Optional[Dict[str, Any]] = None, **kwargs) -> Dict[str, Any]:
        """
        Reset statistics for all configured firewall per-IP traffic shapers.

        Args:
            data_dict: Optional dictionary of parameters
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing operation result

        Example:
            >>> fgt.api.monitor.firewall.per_ip_shaper.reset()
        """
        data = data_dict.copy() if data_dict else {}
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/per-ip-shaper/reset", data=data)
