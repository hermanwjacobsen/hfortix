"""Monitor API - Sdwan operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Routes:
    """Routes operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Routes endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        List all discovered IPv4 SD-WAN routes.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.router.sdwan.routes.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/router/sdwan/routes", params=params)


class RoutesStatistics:
    """RoutesStatistics operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize RoutesStatistics endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        ip_version: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve SD-WAN routes statistics, including number of IPv4 or IPv6 SD-WAN routes.
        
        Args:
            ip_version: IP version [*ipv4 | ipv6 | ipboth]. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.router.sdwan.routes_statistics.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if ip_version is not None:
            params['ip_version'] = ip_version
        params.update(kwargs)
        return self._client.get("monitor", "/router/sdwan/routes-statistics", params=params)


class Routes6:
    """Routes6 operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Routes6 endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        List all discovered IPv6 SD-WAN routes.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.router.sdwan.routes6.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/router/sdwan/routes6", params=params)


class Sdwan:
    """Sdwan operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Sdwan endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.routes = Routes(client)
        self.routes_statistics = RoutesStatistics(client)
        self.routes6 = Routes6(client)
