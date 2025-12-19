"""Monitor API - InterfaceLog operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class InterfaceLog:
    """InterfaceLog operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize InterfaceLog endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        interface: str | None = None,
        since: int | None = None,
        seconds: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve log of SD-WAN interface quality information.
        
        Args:
            interface: Filter: Interface name. (optional)
            since: Filter: Only return SLA logs generated since this Unix timestamp. (optional)
            seconds: Filter: Only return SLA logs generated in the last N seconds. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.virtual_wan.interface_log.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if interface is not None:
            params['interface'] = interface
        if since is not None:
            params['since'] = since
        if seconds is not None:
            params['seconds'] = seconds
        params.update(kwargs)
        return self._client.get("monitor", "/virtual-wan/interface-log", params=params)
