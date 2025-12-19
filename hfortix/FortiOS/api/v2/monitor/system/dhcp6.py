"""Monitor API - Dhcp6 operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Revoke:
    """Revoke operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Revoke endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        ip: list | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Revoke IPv6 DHCP leases.
        
        Args:
            ip: Optional list of addresses to revoke. Defaults to all addresses if not provided. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.system.dhcp6.revoke.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if ip is not None:
            data['ip'] = ip
        data.update(kwargs)
        return self._client.post("monitor", "/system/dhcp6/revoke", data=data)


class Dhcp6:
    """Dhcp6 operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Dhcp6 endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.revoke = Revoke(client)
