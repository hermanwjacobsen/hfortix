"""Monitor API - Device operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class State:
    """State operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize State endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        scope: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve information on state of log devices.
        
        Args:
            scope: Scope from which to retrieve log device state [vdom*|global]. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.log.device.state.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if scope is not None:
            params['scope'] = scope
        params.update(kwargs)
        return self._client.get("monitor", "/log/device/state", params=params)


class Device:
    """Device operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Device endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.state = State(client)
