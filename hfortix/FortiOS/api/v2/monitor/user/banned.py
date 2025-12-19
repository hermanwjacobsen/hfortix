"""Monitor API - Banned operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class AddUsers:
    """AddUsers operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize AddUsers endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        ip_addresses: list | None = None,
        expiry: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Immediately add one or more users to the banned list.
        
        Args:
            ip_addresses: List of IP Addresses to ban. IPv4 and IPv6 addresses are allowed. (optional)
            expiry: Time until expiry in seconds. 0 for indefinite ban. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.user.banned.add_users.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if ip_addresses is not None:
            data['ip_addresses'] = ip_addresses
        if expiry is not None:
            data['expiry'] = expiry
        data.update(kwargs)
        return self._client.post("monitor", "/user/banned/add_users", data=data)


class Check:
    """Check operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Check endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        ip_address: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Check if an IPv4 or IPv6 address is banned administratively.
        
        Args:
            ip_address: IPv4 or IPv6 Address to check. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.user.banned.check.get(ip_address='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params['ip_address'] = ip_address
        params.update(kwargs)
        return self._client.get("monitor", "/user/banned/check", params=params)


class ClearAll:
    """ClearAll operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize ClearAll endpoint.

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
        Immediately clear all banned users.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.user.banned.clear_all.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        data.update(kwargs)
        return self._client.post("monitor", "/user/banned/clear_all", data=data)


class ClearUsers:
    """ClearUsers operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize ClearUsers endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        ip_addresses: list | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Immediately clear a list of specific banned users by IP.
        
        Args:
            ip_addresses: List of banned user IPs to clear. IPv4 and IPv6 addresses are allowed. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.user.banned.clear_users.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if ip_addresses is not None:
            data['ip_addresses'] = ip_addresses
        data.update(kwargs)
        return self._client.post("monitor", "/user/banned/clear_users", data=data)


class Banned:
    """Banned operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Banned endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.add_users = AddUsers(client)
        self.check = Check(client)
        self.clear_all = ClearAll(client)
        self.clear_users = ClearUsers(client)

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Return a list of all banned users by IP.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.user.banned.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/user/banned", params=params)
