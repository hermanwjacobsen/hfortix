"""Monitor API - Network operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Connect:
    """Connect operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Connect endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        ssid: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        When FortiWiFi is in client mode, connect to the specified network, if configured in the 'wifi' interface.
        
        Args:
            ssid: SSID of network to connect to. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.wifi.network.connect.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if ssid is not None:
            data['ssid'] = ssid
        data.update(kwargs)
        return self._client.post("monitor", "/wifi/network/connect", data=data)


class List:
    """List operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize List endpoint.

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
        When FortiWiFi is in client mode, retrieve list of local WiFi networks.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.wifi.network.list.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/wifi/network/list", params=params)


class Scan:
    """Scan operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Scan endpoint.

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
        When FortiWiFi is in client mode, start a scan for local WiFi networks.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.wifi.network.scan.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        data.update(kwargs)
        return self._client.post("monitor", "/wifi/network/scan", data=data)


class Status:
    """Status operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Status endpoint.

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
        When FortiWiFi is in client mode, retrieve status of currently connected WiFi network, if any.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.wifi.network.status.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/wifi/network/status", params=params)


class Network:
    """Network operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Network endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.connect = Connect(client)
        self.list = List(client)
        self.scan = Scan(client)
        self.status = Status(client)
