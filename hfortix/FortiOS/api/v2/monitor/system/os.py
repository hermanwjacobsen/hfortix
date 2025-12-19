"""Monitor API - Os operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Reboot:
    """Reboot operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Reboot endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        event_log_message: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Immediately reboot this device.
        
        Args:
            event_log_message: Message to be logged in event log. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.system.os.reboot.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if event_log_message is not None:
            data['event_log_message'] = event_log_message
        data.update(kwargs)
        return self._client.post("monitor", "/system/os/reboot", data=data)


class Shutdown:
    """Shutdown operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Shutdown endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        event_log_message: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Immediately shutdown this device.
        
        Args:
            event_log_message: Message to be logged in event log. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.system.os.shutdown.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if event_log_message is not None:
            data['event_log_message'] = event_log_message
        data.update(kwargs)
        return self._client.post("monitor", "/system/os/shutdown", data=data)


class Os:
    """Os operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Os endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.reboot = Reboot(client)
        self.shutdown = Shutdown(client)
