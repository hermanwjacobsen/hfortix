"""Monitor API - PerIpShaper operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


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
        Reset statistics for all configured firewall per-IP traffic shapers.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.firewall.per_ip_shaper.reset.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/per-ip-shaper/reset", data=data)


class PerIpShaper:
    """PerIpShaper operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize PerIpShaper endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.reset = Reset(client)

    def get(
        self,
        shaper_name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        List of statistics for configured firewall per-IP traffic shapers.
        
        Args:
            shaper_name: Filter the results by per-IP shaper name. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.firewall.per_ip_shaper.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if shaper_name is not None:
            params['shaper_name'] = shaper_name
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/per-ip-shaper", params=params)
