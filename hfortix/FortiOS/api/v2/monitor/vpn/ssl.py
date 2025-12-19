"""Monitor API - Ssl operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class ClearTunnel:
    """ClearTunnel operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize ClearTunnel endpoint.

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
        Remove all active tunnel sessions in current virtual domain.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.vpn.ssl.clear_tunnel.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        data.update(kwargs)
        return self._client.post("monitor", "/vpn/ssl/clear_tunnel", data=data)


class Delete:
    """Delete operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Delete endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        type: str | None = None,
        index: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Terminate the provided Agentless VPN session.
        
        Args:
            type: The session type [websession|subsession]. (optional)
            index: The session index. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.vpn.ssl.delete.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if type is not None:
            data['type'] = type
        if index is not None:
            data['index'] = index
        data.update(kwargs)
        return self._client.post("monitor", "/vpn/ssl/delete", data=data)


class Stats:
    """Stats operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Stats endpoint.

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
        Return statistics about the Agentless VPN.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.vpn.ssl.stats.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/vpn/ssl/stats", params=params)


class Ssl:
    """Ssl operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Ssl endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.clear_tunnel = ClearTunnel(client)
        self.delete = Delete(client)
        self.stats = Stats(client)

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve a list of all Agentless VPN sessions and sub-sessions.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.vpn.ssl.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/vpn/ssl", params=params)
