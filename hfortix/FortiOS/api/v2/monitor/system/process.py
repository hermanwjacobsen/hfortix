"""Monitor API - Process operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Kill:
    """Kill operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Kill endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        pid: int | None = None,
        signal: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Kill a running process.
        
        Args:
            pid: The process ID. (optional)
            signal: Signal to use when killing the process [9 (SIGKILL) | 11 (SIGSEGV) | 15 (SIGTERM)]. Defaults to 15. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.system.process.kill.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if pid is not None:
            data['pid'] = pid
        if signal is not None:
            data['signal'] = signal
        data.update(kwargs)
        return self._client.post("monitor", "/system/process/kill", data=data)


class Process:
    """Process operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Process endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.kill = Kill(client)
