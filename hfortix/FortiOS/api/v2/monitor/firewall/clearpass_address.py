"""Monitor API - ClearpassAddress operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Add:
    """Add operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Add endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        endpoint_ip: list | None = None,
        spt: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Add ClearPass address with SPT (System Posture Token) value.
        
        Args:
            endpoint_ip: Endpoint IPv4 address. (optional)
            spt: SPT value [healthy|checkup|transient|quarantine|infected|unknown*]. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.firewall.clearpass_address.add.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if endpoint_ip is not None:
            data['endpoint_ip'] = endpoint_ip
        if spt is not None:
            data['spt'] = spt
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/clearpass-address/add", data=data)


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
        endpoint_ip: list | None = None,
        spt: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Delete ClearPass address with SPT (System Posture Token) value.
        
        Args:
            endpoint_ip: Endpoint IPv4 address. (optional)
            spt: SPT value [healthy|checkup|transient|quarantine|infected|unknown*]. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.firewall.clearpass_address.delete.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if endpoint_ip is not None:
            data['endpoint_ip'] = endpoint_ip
        if spt is not None:
            data['spt'] = spt
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/clearpass-address/delete", data=data)


class ClearpassAddress:
    """ClearpassAddress operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize ClearpassAddress endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.add = Add(client)
        self.delete = Delete(client)
